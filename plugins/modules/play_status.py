#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2024, Sjoerd Lubbers <sjoerd.lubbers@salconsultancy.nl>
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: play_status

short_description: Manage play status in a status file

version_added: "1.0.0"

description:
    - This module will manage the status of plays in a status file.
    - It can create the file if it does not exist, read the status of a play, and update the status of a play.

options:
    path:
        description:
        - Path to the status file.
        required: true
        type: str
    play_name:
        description:
        - The name of the play to manage.
        required: true
        type: str
    set_status:
        description:
        - Status to set for the play. Choices are 'init', 'pending', 'done'.
        required: false
        type: str
        choices:
            - 'init'
            - 'pending'
            - 'done'

requirements:
    - None

author:
    - Sjoerd Lubbers

notes:
    - The module creates the status file if it does not exist.
    - When retrieving status, the module will return 'init' if the play is not found.

'''

EXAMPLES = r'''
- name: Get the current status of a play
  status_update:
    path: /var/automatesap/status_file
    play_name: "SAP Common Role Play"
  register: play_status

- name: Show the current status
  ansible.builtin.debug:
    msg: "Current status of '{{ play_status.status }}'"

- name: Update the status to pending
  status_update:
    path: /var/automatesap/status_file
    play_name: "SAP Common Role Play"
    set_status: "pending"

- name: Update the status to done
  status_update:
    path: /var/automatesap/status_file
    play_name: "SAP Common Role Play"
    set_status: "done"
'''

RETURN = r'''
status:
  description: The status of the play.
  type: str
  returned: always
  sample: 'pending'
msg:
  description: A small execution description.
  type: str
  returned: always
  sample: 'Status updated in file'
out:
  description: A complete description of the executed tasks. If this is available.
  type: dict
  returned: always
  sample: '{
        "status": "pending",
        "msg": "Status updated in file"
    }'
'''

from ansible.module_utils.basic import AnsibleModule
import traceback
import os
from datetime import datetime

def ensure_file_exists(path):
    """Ensure that the file exists, create it if it does not."""
    if not os.path.exists(path):
        try:
            with open(path, 'w') as file:
                file.write("# AUTOMATED INSTALLATION STATUS FILE\n")
            return True, "File created"
        except IOError as e:
            return False, str(e)
    return False, "File already exists"

def read_status_file(path, play_name):
    """Read the status of a given play from the file."""
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith(play_name + ":"):
                    parts = line.strip().split(':', 1)
                    if len(parts) > 1:
                        status_part = parts[1].split('(', 1)[0].strip()
                        if status_part in ['init', 'pending', 'done']:
                            return True, status_part
                        else:
                            return True, 'unknown'
            return True, 'init'
    except IOError as e:
        return False, f"Error reading file: {str(e)}"

def update_status_file(path, play_name, status):
    """Update the status of a given play in the file."""
    try:
        lines = []
        updated = False
        with open(path, 'r') as file:
            lines = file.readlines()

        with open(path, 'w') as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            updated = False
            for line in lines:
                if line.startswith(play_name + ":"):
                    file.write(f"{play_name}: {status} ({timestamp})\n")
                    updated = True
                else:
                    file.write(line)
            if not updated:
                file.write(f"{play_name}: {status} ({timestamp})\n")
        return True, "Status updated in file"
    except IOError as e:
        return False, f"Error writing to file: {str(e)}"

def main():
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='str', required=True),
            play_name=dict(type='str', required=True),
            set_status=dict(type='str', choices=['init', 'pending', 'done']),
        ),
        supports_check_mode=True
    )

    path = module.params['path']
    play_name = module.params['play_name']
    set_status = module.params.get('set_status')

    file_created, file_message = ensure_file_exists(path)
    if file_created:
        module.log(msg=file_message)

    if set_status:
        changed, message = update_status_file(path, play_name, set_status)
    else:
        changed, message = read_status_file(path, play_name)

    if changed:
        module.exit_json(changed=changed, status=message)
    else:
        module.fail_json(msg=message)

if __name__ == '__main__':
    main()
