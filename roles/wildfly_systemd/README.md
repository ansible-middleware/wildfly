Wildfly Systemd role
=========

Requirements
------------

A valid Java runtime environment must be available for execution of the jcliff utility

Role Variables
--------------

TODO

| Variable | Description |
| :------- | :---------- |
| wildfly_port_range_offset | Increment for `jboss.socket.binding.port-offset`. Default: 100 | 

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
