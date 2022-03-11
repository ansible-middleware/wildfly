Wildfly systemd role
=========

Using basic information on the JEE app server installation, this
role setup a systemd service to manager.

Note: default values are based on the one of the wildfly install
role.

Requirements
------------

A working systemd environnment is required on target's system.

<!--start argument_specs-->
Role Defaults
-------------

| Variable | Description | Default |
|:---------|:------------|:--------|
|`wildfly_user`| posix user account for wildfly service | `wildfly` |
|`wildfly_group`| posix group for wildfly service | `{{ wildfly_user }}` |
|`wildfly_home`| Wildfly installation directory | `/opt/wildfly/wildfly-26.0.0.Final/` |
|`wildfly_config_base`| Base standalone.xml config for instance | `standalone.xml` |
|`wildfly_port_range_offset`| Increment for `jboss.socket.binding.port-offset` | `100` |
|`wildfly_systemd_enabled`| Enable systemd unit | `True` |
|`wildfly_systemd_service_config_location`| Path for systemd unit file | `/usr/lib/systemd/system` |
|`wildfly_systemd_service_config_file_suffix`| Systemd unit file extension | `.service` |
|`wildfly_systemd_conf_file_suffix`| Suffix for systemd conf file | `.conf` |
|`wildfly_systemd_service_config_file_template`| Template for systemd unit | `templates/wfly.service.j2` |
|`wildfly_service_config_file_template`| Template for systemd config | `templates/wfly.conf.j2` |
|`wildfly_service_config_file_location`| Path for wildfly systemd unit file | `/etc/` |
|`wildfly_enable_yml_config`| Enable yaml file configuration feature (WFCORE5343) | `False` |
|`wildfly_yml_configs`| List of filenames for wildfly configuration bootstrap | `[]` |





Role Variables
--------------

<!--end argument_specs-->

Dependencies
------------

community.general.xml


Example Playbook
----------------

```
  tasks:

    - name: "Set up for WildFly instance {{ item }}"
      include_role:
        name: wildfly_systemd
      vars:
        wildfly_config_base: 'standalone-ha.xml'
        wildfly_basedir_prefix: "/opt/{{ inventory_hostname }}"
        wildfly_config_name: "{{ install_name }}"
        wildfly_port_range_offset: 100
        wildfly_instance_name: "{{ install_name }}"
        instance_id: "{{ item }}"
        service_systemd_env_file: "/etc/eap-{{ item }}.conf"
        service_systemd_conf_file: "/usr/lib/systemd/system/jboss-eap-{{ item }}.service"
      loop: "{{ range(0,3) | list }}"
```


License
-------

GPL2


Author Information
------------------

* [Romain Pelisse](https://github.com/rpelisse)
