wildfly install role
====================

A role to automate the download and installation of the WildFly JEE server.


Requirements
------------

Requirements on the target system are ensured by the role.

<!--start argument_specs-->
Role Defaults
-------------

| Variable | Description | Default |
|:---------|:------------|:--------|
|`wildfly_install_version`| WildFly version to install | `41.0.0.Final` |
|`wildfly_install_archive_filename`| WildFly download archive name | `wildfly-{{ wildfly_install_version }}.zip` |
|`wildfly_install_download_baseurl`| Base URL for wildfly download | `https://github.com/wildfly/wildfly/releases/download` |
|`wildfly_install_workdir`| WildFly installation directory (where the server files are unzipped) | `/opt/wildfly/` |
|`wildfly_install_home`| WildFly installation directory (WILDFLY_HOME) | `{{ wildfly_install_workdir }}wildfly-{{ wildfly_install_version }}/` |
|`wildfly_install_download_url`| WildFly download URL | `{{ wildfly_install_download_baseurl }}/{{ wildfly_install_version }}/{{ wildfly_install_archive_filename }}` |
|`wildfly_install_archive_dir`| Target download directory | `{{ wildfly_install_workdir }}` |
|`wildfly_install_config_base`| Base standalone.xml config for instance | `standalone.xml` unless `wildfly_install_config_custom_file` is used |
|`wildfly_install_config_custom_file`| Custom standalone.xml config to be copied to target instance and used as base | `''` |
|`wildfly_install_user`| POSIX user account for WildFly | `wildfly` |
|`wildfly_install_group`| POSIX group for WildFly | `{{ wildfly_install_user }}` |
|`wildfly_install_java_package_name`| RHEL/Fedora Java RPM package | `java-21-openjdk-headless` |
|`wildfly_install_offline_install`| Whether to install from local archive | `False` |

When `wildfly_config_custom_file` is set, WildFly/EAP may rewrite the active standalone XML while running. The role reapplies your template from the controller but sets `changed` to false on that task so repeated Ansible passes (including Molecule idempotence) stay green.

NOTE: for eap_version the micro version must be 0

Role Variables
--------------

* No required variables

<!--end argument_specs-->


## Example Playbooks

### Default Install

Installs the default version of WildFly to the default location with the default user.

```yaml

- name: "Installation and configuration"
  hosts: "{{ hosts_group_name | default('localhost') }}"
  collections:
    - middleware_automation.wildfly
  roles:
    - wildfly_install
```

### Explicit Location and Version

Older WildFly versions can be download from outside Github.

```yaml

- name: "Installation and configuration"
  hosts: "{{ hosts_group_name | default('localhost') }}"
  vars:
    wildfly_install_version: '41.0.0.Final'
    wildfly_install_download_baseurl: "https://github.com/wildfly/wildfly/releases/download"
  collections:
    - middleware_automation.wildfly
  roles:
    - wildfly_install
```

## License

GPL2

## Author Information

* [Romain Pelisse](https://github.com/rpelisse)
* [Ranabir Chakraborty](https://github.com/RanabirChakraborty)
