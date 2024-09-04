summary
=========

This role will create a custom summary informing the end user in --check mode.

Requirements
------------
This summary is part of the runsap methology which means that all code must be idempotent. In check mode the code must always explain to the user what will be done.


Role Variables
--------------

During play or role execution you can set a variable:
```
- set_fact:
    custom_change_summary: "{{ custom_change_summary | default([]) + [ 'Lets execute some super stuff' ] }}"
```

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```
      - name: Running Summary Play
        hosts: localhost 
        tasks:
          - include_role: 
              name: community.runsap.summary
            when: ansible_check_mode
```

This will result in:

```
ok: [localhost] => 
  msg: |-
    --------------------------------------------------
    RUNSAP CHANGE SUMMARY
    --------------------------------------------------  
    -   hostname: saps4x1
        samenvatting:
        - AWS Backint Agent 2.0.3.755 needs to be installed
```

License
-------

MIT

Author Information
------------------

S. Lubbers
