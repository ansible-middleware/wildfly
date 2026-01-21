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
|`wildfly_version`| WildFly version to install | `39.0.0.Final` |
|`wildfly_archive_filename`| WildFly download archive name | `wildfly-{{ wildfly_version }}.zip` |
|`wildfly_download_baseurl`| Base URL for wildfly download | `https://github.com/wildfly/wildfly/releases/download` |
|`wildfly_install_workdir`| WildFly installation directory (where the server files are unzipped) | `/opt/wildfly/` |
|`wildfly_home`| WildFly installation directory (WILDFLY_HOME) | `{{ wildfly_install_workdir }}wildfly-{{ wildfly_version }}/` |
|`wildfly_install_download_url`| WildFly download URL | `{{ wildfly_download_baseurl }}/{{ wildfly_version }}/{{ wildfly_archive_filename }}` |
|`wildfly_archive_dir`| Target download directory | `{{ wildfly_install_workdir }}` |
|`wildfly_config_base`| Base standalone.xml config for instance | `standalone.xml` unless `wildfly_config_custom_file` is used |
|`wildfly_config_custom_file`| Custom standalone.xml config to be copied to target instance and used as base | `''` |
|`wildfly_user`| POSIX user account for WildFly | `wildfly` |
|`wildfly_group`| POSIX group for WildFly | `{{ wildfly_user }}` |
|`wildfly_java_package_name`| RHEL/Fedora Java RPM package | `java-21-openjdk-headless` |
|`wildfly_offline_install`| Whether to install from local archive | `False` |


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
    wildfly_version: '39.0.0.Final'
    wildfly_download_baseurl: "https://github.com/wildfly/wildfly/releases/download"
  collections:
    - middleware_automation.wildfly
  roles:
    - wildfly_install
```

## License

GPL2

## Author Information

* [Romain Pelisse](https://github.com/rpelisse)
