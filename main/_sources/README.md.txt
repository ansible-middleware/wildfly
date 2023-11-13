# Wildfly Collection for Ansible - middleware_automation.wildfly

<!--start build_status -->
[![Build Status](https://github.com/ansible-middleware/wildfly/workflows/CI/badge.svg?branch=main)](https://github.com/ansible-middleware/wildfly/actions/workflows/ci.yml)
<!--end build_status -->

## About

This Ansible Collection provides several roles to help install, setup and maintain Java JEE appserver Wildfly within the configuration management tool Ansible.

### I know nothing about Ansible, but I want to install Wildfly, can I?

Yes, once Ansible is installed on your computer, you can simply run the following command (note that the inventory file needs to be populated with the name(s) of the machine(s) you wish to install Wildfly on):

    $ ansible-galaxy collection install middleware_automation.wildfly
    $ ansible-playbook -i inventory middleware_automation.wildfly.playbook

<!--start requires_ansible-->
## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.9.10**.


## Install

Plugins and modules within a collection may be tested with only specific Ansible versions. A collection may contain metadata that identifies these versions.
<!--end requires_ansible-->

## Included content
<!--start roles_paths -->
### Roles

* [wildfly_install](https://github.com/ansible-middleware/wildfly/blob/main/roles/wildfly_install/README.md): download and install
* [wildfly_systemd](https://github.com/ansible-middleware/wildfly/blob/main/roles/wildfly_systemd/README.md): configure systemd unit
* [wildfly_driver](https://github.com/ansible-middleware/wildfly/blob/main/roles/wildfly_driver/README.md): install additional driver modules (ie. JDBC)
* [wildfly_utils](https://github.com/ansible-middleware/wildfly/blob/main/roles/wildfly_utils/README.md): utilities related to EAP
* [wildfly_validation](https://github.com/ansible-middleware/wildfly/blob/main/roles/wildfly_validation/README.md): validate deployed installation
* [wildfly_uninstall](https://github.com/ansible-middleware/wildfly/blob/main/roles/wildfly_uninstall/README.md): restore status pre wildfly_install
<!--end roles_paths -->

### Installing the collection

To install this Ansible collection:

    $ ansible-galaxy collection install middleware_automation.wildfly

or with a downloaded or built tarball, run the following command:

    $ ansible-galaxy collection install /path/to/middleware_automation.wildfly.tgz

or via the included requirements file:

    $ ansible-galaxy collection install -r requirements.yml


## Building the collection

    $ ansible-galaxy collection build .


## Using the collection to install and run Wildfly on target hosts

The collection comes with a simple playbook that allows to directly install and run Wildfly:

    $ ansible-playbook -i inventory middleware_automation.wildfly.playbook

Note that depending on your use case, you might need to redefine some variables. In this case, you can simply import the playbook with the appropriate values:

    ---
    - ansible.builtin.import_playbook: middleware_automation.wildfly.playbook
      vars:
        wildfly_config_base: 'standalone-full.xml'

Overrideable variables are documented in the roles wildfly_install, wildfly_systemd, wildfly_drive

### Dependencies

* [middleware_automation.common](https://github.com/ansible-middleware/common)
* [ansible-posix](https://docs.ansible.com/ansible/latest/collections/ansible/posix/index.html)


<!--start support -->
<!--end support -->

## Using the collection to customize Wildfly configuration

Regarding the configuration of the Java app server itself, the Ansible collection has a specific strategy, designed to ensure idempotency of the resulting setup, but also ensure Ansible has the capacity to fine-tune, as much as needed, the server.

First, the collection will use a template configuration file as a base (by default, it's the standalone.xml provided with the server files). This file is first copy into wildfly.yml (can be renamed and relocated if needed to). Then, the server starts with this copy in read-only. So to apply any change to the configuration after this point, the user will need to use, either the YAML Config or the JBoss CLI. This ensures that the configuration can change can be performed by Ansible in an idempotent fashion.

Depending on the number of configuration changes and if the server is a new deployment, the user can decide to implement its configuration changes directly in the base template (for instance removing some subsystem from the standalone-full.xml and use this modified file as a base) or perform all the changes using the Yaml Config. The latter is generally the better approach, because it will also work with a running system, while the previous approach requires to deploy again the configuration file.

A last option is to use JBoss cli queries, within the Ansible, but it requires more work as the state has to be managed for Ansible. Which means, a first query will assess the current state of the server (is the configuration already correct?), then a second will be need to update, if needed, the configuration.

## A note on domain mode

This collection does not provides any support to use Wildfly's domain mode. The rationale behind this decision is that this Wildfly feature overlaps a lot with Ansible and it's **not recommended** and cumbersome to combine those. So, for simplicity sake, this collection focus only on standalone deployment of Wildfly JEE servers.

## License

[GNU General Public License v2.0](https://github.com/ansible-middleware/wildfly/blob/main/LICENSE)
