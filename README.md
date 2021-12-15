# Ansible Collection - middleware_automation.jcliff

[![Build Status](https://github.com/ansible-middleware/ansible_collections_jcliff/workflows/CI/badge.svg?branch=master)](https://github.com/ansible-middleware/ansible_collections_jcliff/actions/workflows/ci.yml)

## About

This Ansible Collection wraps a tool called [JCliff](https://github.com/bserdar/jcliff), designed to integrate the [Wildfly](https://wildfly.org/) server (or its product counterpart  [JBoss Enterprise Application (EAP)](https://www.redhat.com/en/technologies/jboss-middleware/application-platform) ) into a configuration management tool such as Ansible.

## Install

### Installing the collection

To install this Ansible collection simply download the latest tarball and run the following command:

    $ ansible-galaxy collection install /path/to/middleware_automation.jcliff.tgz

Alternatively, you can simply build the tarball (to then install it):

    $ ansible-galaxy collection build

### Ensuring JCliff is available

The collection itself only provides the integration of JCliff into Ansible. JCliff itself needs to be installed and available on the system Ansible is running on.

For commodity purpose, the Collection comes with a role named 'jcliff:' that will take care of installing JCliff. However, currently, this role **only** supports Linux distribution using Yum (namely Fedora, RHEL and CentOS) and MacOSX using [Homebrew](https://brew.sh/).

    - hosts: ...
      collections:
        - middleware_automation.jcliff
      tasks:
        - name: Include Jcliff role
          include_role:
            name: jcliff

If you would like to use it on windows we have named the role "win-jcliff" that will install out jcliff collection on windows. We have created a separate role for windows environment.
    - hosts: ...
      collections:
        - middleware_automation.jcliff
      tasks:
        - name: Include Jcliff role for windows
          include_role:
            name: win-jcliff


Refers to [JCliff](https://github.com/bserdar/jcliff) for more information on how to install the tool manually. JCliff being a Java based application setting up is pretty simple, so do not let it deter you from using the collection.

## Using the JCliff collection within your playbook

Once the Collection has been installed and JCliff is available on the system, you can directly use the tool within your playbook to configure a EAP or Wildfly instance:

    ---
    - hosts: localhost
      gather_facts: false
      collections:
        - middleware_automation.jcliff

      tasks:

        - jcliff:
            wfly_home: /var/opt/jboss-eap-7.3
            subsystems:
              - system_properties:
                  - name: jcliff.enabled
                    value: 'enabled'
                  - name: jcliff.version
                    value: '1.0'
