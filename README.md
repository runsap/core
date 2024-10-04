Ansible Collection - runsap.core
================================

![Ansible Lint](https://github.com/runsap/runsap.core/actions/workflows/lint.yml/badge.svg)

![Bandit security](https://github.com/runsap/runsap.core/actions/workflows/bandit-security.yml/badge.svg)

Runsap Introduction
-------------------
Runsap is a method of installing and managing large or small SAP focussed landschapes. This collection is part of, and should be used with, the other runsap collections for optimal usage.

Collection introduction
-----------------------
This collection helps you in managing several runsap core activities.

**Roles**
- summary

**Modules**
- play_status

The play_status is used to store the status of an ansible play on the linux operating system. This way you can get an idempotent playbook while installing complex and dependent applications.

Within the runsap framework the `--check` mode is often used to indicate to the user what will be performed by the automation. The summary role is able to display these messages.

Author
------
Sjoerd Lubbers