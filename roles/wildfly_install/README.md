# Wildfly Install role


## Requirements


## Role Variables

TODO

### Base Variables

| Variable | Description | Default |
| :------- | :---------- | :------ |
| wildfly_version | | '26.0.0.Final' |
| wildfly_download_baseurl | | 'https://github.com/wildfly/wildfly/releases/download' |
| wildfly_install_workdir | | '/opt/wildfly/' |
| wildfly_config_base | Base config file | 'standalone.xml' |
| wildfly_user | Service account user | 'wildfly' |
| wildfly_jvm_memory_min | | '64m' |
| wildfly_jvm_memory_max | | '512m' |
| wildfly_jvm_metaspace_size | | '96m' |
| wildfly_java_package_name | | 'java-1.8.0-openjdk' |
| wildfly_jboss_eap_version | | '7.4.0' |
| wildfly_jboss_eap_archive_filename | | 'jboss-eap-7.4.0.zip' |

### Derived Variables

| Variable | Description | Default |
| :------- | :---------- | :------ |
| wildfly_archive_filename | | 'wildfly-{{ wildfly_version }}.zip' |
| wildfly_home | | '{{ wildfly_install_workdir }}wildfly-{{ wildfly_version }}/' |
| wildfly_install_download_url | | '{{ wildfly_download_baseurl }}/{{ wildfly_version }}/{{ wildfly_archive_filename }}' |
| wildfly_archive_dir | | '{{ wildfly_install_workdir }}' |
| wildfly_group | | '{{ wildfly_user }}' |
| wildfly_offline_install | Whether to install from local archive | False |
| wildfly_jboss_eap_home | | |
| wildfly_jboss_eap_enable | Install jboss eap if rhn_username and rhn_password are defined | False |

## Dependencies

## Example Playbooks

### Default Install

Installs the default version of Wildfly to the default location with the default user.

```
---
- name: "Wildfly installation and configuration"
  hosts: "{{ hosts_group_name | default('localhost') }}"
  become: yes
  collections:
    - middleware_automation.wildfly
  roles:
    - wildfly_install
```

### Explicit Location and Version

Older Wildfly versions can be download from outside Github.

```
---
- name: "Wildfly installation and configuration"
  hosts: "{{ hosts_group_name | default('localhost') }}"
  become: yes
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
