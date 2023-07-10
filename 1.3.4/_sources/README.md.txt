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

### Roles

* [wildfly_install](https://github.com/ansible-middleware/wildfly/blob/main/roles/wildfly_install/README.md): download and install
* [wildfly_systemd](https://github.com/ansible-middleware/wildfly/blob/main/roles/wildfly_systemd/README.md): configure systemd unit
* [wildfly_driver](https://github.com/ansible-middleware/wildfly/blob/main/roles/wildfly_driver/README.md): install additional driver modules (ie. JDBC)
* [wildfly_utils](https://github.com/ansible-middleware/wildfly/blob/main/roles/wildfly_utils/README.md): utilities related to EAP
* [wildfly_validation](https://github.com/ansible-middleware/wildfly/blob/main/roles/wildfly_validation/README.md): validate deployed installation
* [wildfly_uninstall](https://github.com/ansible-middleware/wildfly/blob/main/roles/wildfly_uninstall/README.md): restore status pre wildfly_install


### Installing the collection

To install this Ansible collection:

    $ ansible-galaxy collection install middleware_automation.wildfly

or with a downloaded or built tarball, run the following command:

    $ ansible-galaxy collection install /path/to/middleware_automation.wildfly.tgz

or via the included requirements file:

    $ ansible-galaxy collection install -r requirements.yml


## Building the collection

    $ ansible-galaxy collection build .


### Dependencies

* [middleware_automation.common](https://github.com/ansible-middleware/common)
* [ansible-posix](https://docs.ansible.com/ansible/latest/collections/ansible/posix/index.html)


<!--start support -->
<!--end support -->


## License

[GNU General Public License v2.0](https://github.com/ansible-middleware/wildfly/blob/main/LICENSE)
