wildfly uninstall role
======================

Role to uninstall Wildfly and clean the target nodes.

<!--start argument_specs-->
Role Defaults
-------------

| Variable | Description | Default |
|:---------|:------------|:--------|
|`wildfly_uninstall_require_privileges_escalation`| Specifiy if the uninstallation process requires privileges escalation | `True` |
|`wildfly_uninstall_service_name`| Instance name of the server to uninstall | `{{ instance_name | default('wildfly') }}` |
|`wildfly_uninstall_home`| Path to server home | `{{ wildfly_home }}` |
|`wildfly_uninstall_systemd_service_file`| Path to the systemd configuration file associated to the server | `/usr/lib/systemd/system/{{ wildfly_uninstall_service_name }}.service` |
|`wildfly_uninstall_systemd_service_conf_file`| Path to the env file used by the systemd service associated to the server | `/etc/{{ wildfly_uninstall_service_name }}.conf` |
|`wildfly_uninstall_delete_group`| Specify if uninstall procedure should remove server specific group | `True` |
|`wildfly_uninstall_delete_groupname`| Name of the server's group | `wildfly` |
|`wildfly_uninstall_delete_user`| Specify if uninstall procedure should remove server specific user | `True` |
|`wildfly_uninstall_delete_username`| Name of the server's group | `wildfly` |


* No defaults

Role Variables
--------------

* No required variables
<!--end argument_specs-->


## Example Playbooks

```yaml
---
- name: "Uninstall server from target"
  hosts: all
  gather_facts: false
  vars:
    wildfly_uninstall_service_name: wildfly
    wildfly_uninstall_home: /opt/wildfly/wildfly-37.0.0.Final
    wildfly_uninstall_path_to_archive: /opt/wildfly/wildfly-37.0.0.Final.zip
  roles:
    - name: wildfly_uninstall
```

## License

GPL2

## Author Information

* [Romain Pelisse](https://github.com/rpelisse)
