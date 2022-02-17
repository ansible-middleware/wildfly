# Ansible Collection - middleware_automation.wildfly
# Wildfly Collection for Ansible

[![Build Status](https://github.com/ansible-middleware/wildfly_collection/workflows/CI/badge.svg?branch=master)](https://github.com/ansible-middleware/wildfly_collection/actions/workflows/ci.yml)
This Ansible Collection regroups several playbooks (packaged as role) to help install, setup and maintain Java JEE appserver Wildfly (and its product counterpart [JBoss Enterprise Application (EAP)](https://www.redhat.com/en/technologies/jboss-middleware/application-platform) ) within the configuration management tool Ansible.

## About
## Ansible version compatibility

This Ansible Collection regroups several playbooks (packaged as role) to help install, setup and maintain Java JEE appserver Wildfly (and its product counterpart  [JBoss Enterprise Application (EAP)](https://www.redhat.com/en/technologies/jboss-middleware/application-platform) ) within the configuration management tool Ansible.
This collection has been tested against following Ansible versions: **>=2.9.10**.

## Install
Plugins and modules within a collection may be tested with only specific Ansible versions. A collection may contain metadata that identifies these versions.
<!--end requires_ansible-->
## Included content

### Installing the collection
Click on the name of a plugin or module to view that content's documentation:

To install this Ansible collection simply download the latest tarball and run the following command:
### Collections

    $ ansible-galaxy collection install /path/to/middleware_automation.wildfly.tgz
- middleware_automation.redhat_csp_download
    - This collection is required to download resources from RedHat Customer Portal.
    - Documentation to collection can be found at <https://github.com/ansible-middleware/redhat-csp-download>

Alternatively, you can simply build the tarball (and then install it):
## Installation and Usage

    $ ansible-galaxy collection build
You can the playbook directly from this folder for demostration purpose, however, the proper way to install the collection is to build it and install it :

    $ ansible-galaxy collection build .
    $ ansible-galaxy collection install middleware_automation-wildfly-*.tar.gz

## Support

jws collection v1.0.0 is a Beta release and for [Technical Preview](https://access.redhat.com/support/offerings/techpreview). If you have any issues or questions related to collection, please don't hesitate to contact us on <Ansible-middleware-core@redhat.com> or open an issue on https://github.com/ansible-middleware/jws-ansible-playbook/issues

## License

Apache License v2.0 or later

See [LICENCE](LICENSE) to view the full text.
