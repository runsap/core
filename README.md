Ansible Collection - runsap.core
================================

![Ansible Lint](https://github.com/runsap/runsap.core/actions/workflows/lint.yml/badge.svg)
![Bandit security](https://github.com/runsap/runsap.core/actions/workflows/security-check.yml/badge.svg)

Runsap Introduction
-------------------
**Runsap** is a method of installing and managing SAP-focused landscapes, designed to handle both small and large SAP environments. This Ansible collection is an integral part of the **Runsap framework** and should ideally be used in conjunction with other Runsap collections for optimal usage and flexibility. It aims to streamline the deployment and management of SAP infrastructure, ensuring consistency, automation, and idempotence across multiple environments.

Collection introduction
-----------------------
This collection helps you in managing several runsap core activities.

**Roles**
- summary

**Modules**
- play_status

The play_status is used to store the status of an ansible play on the linux operating system. This way you can get an idempotent playbook while installing complex and dependent applications.

Within the runsap framework the `--check` mode is often used to indicate to the user what will be performed by the automation. The summary role is able to display these messages.

Testing and Quality
-------------------

We ensure the quality of the collection using:

- Ansible Lint: To enforce best practices in Ansible playbooks and roles.
- Bandit: A Python security tool that checks for common security issues in custom Ansible modules written in Python.

Both of these tools are integrated into our GitHub Actions workflows, ensuring that each change to the collection is validated for security and code quality before being merged.


Contributing
------------

Contributions are welcome! Please follow the guidelines for contributing, which include linting your Ansible playbooks with ansible-lint and running security checks with Bandit. You can submit pull requests, and we will review and merge them as appropriate.

To contribute:

1. Fork the repository.
2. Make your changes.
3. Run the tests:
   - ansible-lint for playbook validation.
   - bandit for security checks on Python code.
4. Submit a pull request.


License
-------

This collection is licensed under the MIT License. Please see the `LICENSE` file for more details.