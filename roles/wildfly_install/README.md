wildfly install role
====================

A role to automate the download and installation of the Wildfly JEE server.


Requirements
------------

Requirements on the target system are ensured by the role.

<!--start argument_specs-->
Role Defaults
-------------

| Variable | Description | Default |
|:---------|:------------|:--------|
|`wildfly_version`| Wildfly version to install | `35.0.0.Final` |
|`wildfly_archive_filename`| Wildfly download archive name | `wildfly-{{ wildfly_version }}.zip` |
|`wildfly_download_baseurl`| Base URL for wildfly download | `https://github.com/wildfly/wildfly/releases/download` |
|`wildfly_install_workdir`| Wildfly installation directory (where the server files are unzipped) | `/opt/wildfly/` |
|`wildfly_home`| Wildfly installation directory (WILDFLY_HOME) | `{{ wildfly_install_workdir }}wildfly-{{ wildfly_version }}/` |
|`wildfly_install_download_url`| Wildfly download URL | `{{ wildfly_download_baseurl }}/{{ wildfly_version }}/{{ wildfly_archive_filename }}` |
|`wildfly_archive_dir`| Target download directory | `{{ wildfly_install_workdir }}` |
|`wildfly_config_base`| Base standalone.xml config for instance | `standalone.xml` unless `wildfly_config_custom_file` is used |
|`wildfly_config_custom_file`| Custom standalone.xml config to be copied to target instance and used as base | `''` |
|`wildfly_user`| posix user account for wildfly | `wildfly` |
|`wildfly_group`| posix group for wildfly | `{{ wildfly_user }}` |
|`wildfly_java_package_name`| RHEL java rpm package | `java-11-openjdk-headless` |
|`wildfly_offline_install`| Whether to install from local archive | `False` |


Role Variables
--------------

* No required variables

<!--end argument_specs-->


## Example Playbooks

### Default Install

Installs the default version of Wildfly to the default location with the default user.

```
---
- name: "Installation and configuration"
  hosts: "{{ hosts_group_name | default('localhost') }}"
  collections:
    - middleware_automation.wildfly
  roles:
    - wildfly_install
```

### Explicit Location and Version

Older Wildfly versions can be download from outside Github.

```
---
- name: "Installation and configuration"
  hosts: "{{ hosts_group_name | default('localhost') }}"
  vars:
    wildfly_version: '24.0.1.Final'
    wildfly_download_baseurl: "https://download.jboss.org/wildfly"
  collections:
    - middleware_automation.wildfly
  roles:
    - wildfly_install
```

## License

GPL2

## Author Information

* [Romain Pelisse](https://github.com/rpelisse)
