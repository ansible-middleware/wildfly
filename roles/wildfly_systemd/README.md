wildfly systemd role
====================

Role setting up a systemd service to manage a Wildfly app server instance, using basic information on server installation.

Note: default values are based on the one of the wildfly_install role.

Requirements
------------

A working systemd environment is required on target's system.

<!--start argument_specs-->
Role Defaults
-------------

| Variable | Description | Default |
|:---------|:------------|:--------|
|`wildfly_user`| posix user account for wildfly service | `wildfly` |
|`wildfly_group`| posix group for wildfly service | `{{ wildfly_user }}` |
|`wildfly_version`| Wildfly version to install | `31.0.1.Final` |
|`wildfly_install_workdir`| Wildfly installation directory (where the server files are unzipped) | `/opt/wildfly/` |
|`wildfly_home`| Wildfly installation directory (WILDFLY_HOME) | `{{ wildfly_install_workdir }}wildfly-{{ wildfly_version }}/` |
|`wildfly_config_base`| Base standalone.xml config for instance | `standalone.xml` unless `wildfly_config_custom_file` is used |
|`wildfly_config_custom_file`| Custom standalone.xml config to be copied to target instance and used as base | `''` |
|`wildfly_port_range_offset`| Increment for `jboss.socket.binding.port-offset` | `100` |
|`wildfly_systemd_unit_enabled`| Enable systemd unit to autostart after reboot | `True` |
|`wildfly_systemd_service_config_location`| Path for systemd unit file | `/etc/systemd/system` |
|`wildfly_systemd_service_config_file_suffix`| Systemd unit file extension | `.service` |
|`wildfly_systemd_conf_file_suffix`| Suffix for systemd conf file | `.conf` |
|`wildfly_systemd_java_home`| JAVA_HOME of installed JRE, leave empty for using specified wildfly_java_package_name RPM path|``|
|`wildfly_systemd_service_config_file_template`| Template for systemd unit | `templates/wfly.service.j2` |
|`wildfly_service_config_file_template`| Template for systemd config | `templates/wfly.conf.j2` |
|`wildfly_service_config_file_location`| Path for wildfly systemd unit file | `/etc/sysconfig` |
|`wildfly_enable_yml_config`| Enable yaml file configuration feature (WFCORE5343) | `False` |
|`wildfly_yml_configs`| List of filenames for wildfly configuration bootstrap | `[]` |
|`wildfly_java_package_name`| RHEL java rpm package | `java-11-openjdk-headless` |
|`wildfly_java_opts`| Additional settings for the JVM running wildfly | `-Xmx1024M -Xms512M` |
|`wildfly_bind_addr`| Bind address for listening to public network | `0.0.0.0` |
|`wildfly_bind_addr_private`| Bind address for listening to private network |`127.0.0.1` |
|`wildfly_bind_addr_management`| Bind address for management console port |`127.0.0.1` |
|`wildfly_multicast_addr`| Multicast address for jgroup cluster discovery |`230.0.0.4` |
|`wildfly_statistics_enabled`| Whether to enable statistics | `False` |
|`wildfly_systemd_require_privilege_escalation`| Specify if Ansible needs to escalate privilege to interact with Systemd | `True` |
|`wildfly_service_name`| Systemd unit service name | `{{ wildfly_instance_name }}`|
|`wildfly_systemd_env_config_name`| Systemd unit service name | `{{ wildfly_instance_name }}`|
|`wildfly_instance_name`| When collocating services on the same host, EAP instance name | `wildfly` |
|`wildfly_node_id`| Name of the node to be passed as jboss.tx.node.id, must be unique in a cluster. Max length 23 characters | `{{ inventory_hostname_short }}` |

Role Variables
--------------

| Variable | Description | Required |
|:---------|:------------|:---------|
|`wildfly_java_home`| JAVA_HOME of installed JRE, leave empty for using specified wildfly_java_package_name RPM path | `No` |
|`wildfly_yml_configs_repository`| Path to the folder containing the YAML config files | `True` |
<!--end argument_specs-->


Example Playbook
----------------

```yaml
  tasks:

    - name: "Set up for WildFly instance {{ item }}"
      include_role:
        name: wildfly_systemd
      vars:
        wildfly_node_id: "wildfly-{{ item }}"
        wildfly_instance_name: "wildfly-{{ item }}"
        wildfly_service_name: "wildfly-{{ item }}-service"
        wildfly_config_base: standalone-ha.xml
        wildfly_install_workdir: "/opt/wildfly-{{ item }}"
        wildfly_home: "{{ wildfly_install_workdir }}/wildfly-{{ wildfly_version }}/"
        wildfly_port_range_offset: "{{ item * 100 }}"
        wildfly_node_id: "test-{{ item }}"
      loop: "{{ range(0,3) | list }}"
```

## License

GPL2


Author Information
------------------

* [Romain Pelisse](https://github.com/rpelisse)
