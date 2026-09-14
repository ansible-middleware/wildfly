wildfly snapshot role
=====================

A role to manage WildFly configuration snapshots and provide automatic rollback on failure, using the JBoss CLI `:take-snapshot` operation for standalone mode.


Requirements
------------

A running WildFly or JBoss EAP instance managed via systemd, with the management interface accessible.


Entrypoints
-----------

* main / take_snapshot: take a configuration snapshot (auto-named or with a custom name)
* list_snapshots: list all available configuration snapshots
* delete_snapshot: delete a specific snapshot by name
* restore_snapshot: stop the service, restore a snapshot file as the active configuration, and restart
* apply_with_rollback: take a snapshot, apply CLI commands (or include a tasks file), and automatically restore on failure

<!--start argument_specs-->
Role Defaults
-------------

| Variable | Description | Default |
|:---------|:------------|:--------|
|`wildfly_snapshot_home`| WildFly installation directory | `{{ wildfly_snapshot_install_workdir }}wildfly-{{ wildfly_snapshot_version }}/` |
|`wildfly_snapshot_jboss_home`| WildFly installation directory used for CLI execution | `{{ wildfly_snapshot_home }}` |
|`wildfly_snapshot_user`| POSIX user account for WildFly | `wildfly` |
|`wildfly_snapshot_group`| POSIX group for WildFly | `{{ wildfly_snapshot_user }}` |
|`wildfly_snapshot_instance_name`| WildFly instance name | `wildfly` |
|`wildfly_snapshot_service_name`| WildFly systemd service name | `{{ wildfly_snapshot_instance_name }}` |
|`wildfly_snapshot_basedir_prefix`| Base directory prefix for standalone server | `{{ wildfly_snapshot_home }}` |
|`wildfly_snapshot_basedir`| Standalone server base directory | `{{ wildfly_snapshot_basedir_prefix }}/standalone` |
|`wildfly_snapshot_config_dir`| Configuration directory path | `{{ wildfly_snapshot_basedir }}/configuration` |
|`wildfly_snapshot_config_file`| Active configuration file name | `{{ wildfly_snapshot_instance_name }}.xml` |
|`wildfly_snapshot_jboss_cli_controller_host`| Hostname for connecting to JBoss CLI | `localhost` |
|`wildfly_snapshot_jboss_cli_controller_port`| Port for connecting to JBoss CLI | `9990` |
|`wildfly_snapshot_port_range_offset`| Increment for jboss.socket.binding.port-offset | `0` |
|`wildfly_snapshot_jboss_cli_timeout`| Seconds to wait for JBoss CLI connection | `5` |
|`wildfly_snapshot_name`| Optional name for the snapshot (auto-generated if empty) | `''` |
|`wildfly_snapshot_require_privilege_escalation`| Whether privilege escalation is required | `True` |
|`wildfly_snapshot_selinux_enabled`| Whether to deploy on a selinux enforcing target host | `False` |

Role Variables
--------------

| Variable | Description | Required |
|:---------|:------------|:---------|
|`wildfly_snapshot_delete_name`| Name of the snapshot file to delete (for delete_snapshot entrypoint) | Yes (delete_snapshot) |
|`wildfly_snapshot_restore_file`| Full path to the snapshot file to restore (for restore_snapshot entrypoint) | Yes (restore_snapshot) |
|`wildfly_snapshot_apply_cli_commands`| List of JBoss CLI commands to execute with automatic rollback on failure | Yes (apply_with_rollback) |
|`wildfly_snapshot_apply_tasks_file`| Path to an Ansible tasks file to include with automatic rollback on failure; mutually exclusive with wildfly_snapshot_apply_cli_commands | No |
<!--end argument_specs-->


## Example Playbooks

### Take a Snapshot

Takes a timestamped configuration snapshot of a running WildFly instance.

```yaml
- name: "Take a configuration snapshot"
  hosts: all
  collections:
    - middleware_automation.wildfly
  tasks:
    - name: "Snapshot current configuration"
      ansible.builtin.include_role:
        name: wildfly_snapshot
      vars:
        wildfly_snapshot_jboss_home: /opt/wildfly/wildfly-41.0.0.Final/
    # snapshot path is available in wildfly_snapshot_file_path
```

### Take a Named Snapshot

```yaml
- name: "Take a named snapshot"
  hosts: all
  collections:
    - middleware_automation.wildfly
  tasks:
    - name: "Snapshot before maintenance"
      ansible.builtin.include_role:
        name: wildfly_snapshot
        tasks_from: take_snapshot.yml
      vars:
        wildfly_snapshot_jboss_home: /opt/wildfly/wildfly-41.0.0.Final/
        wildfly_snapshot_name: "pre-maintenance"
```

### Apply Changes with Automatic Rollback

Applies a list of CLI commands with automatic rollback to the previous state if any command fails.

```yaml
- name: "Apply configuration with rollback protection"
  hosts: all
  collections:
    - middleware_automation.wildfly
  tasks:
    - name: "Configure datasource with rollback"
      ansible.builtin.include_role:
        name: wildfly_snapshot
        tasks_from: apply_with_rollback.yml
      vars:
        wildfly_snapshot_jboss_home: /opt/wildfly/wildfly-41.0.0.Final/
        wildfly_snapshot_apply_cli_commands:
          - "/subsystem=datasources/data-source=ExampleDS:write-attribute(name=max-pool-size,value=50)"
          - "/subsystem=logging/root-logger=ROOT:write-attribute(name=level,value=DEBUG)"
```

### Manually Restore from a Snapshot

Stops the WildFly service, replaces the active configuration with the snapshot, and restarts.

```yaml
- name: "Restore from snapshot"
  hosts: all
  collections:
    - middleware_automation.wildfly
  tasks:
    - name: "Restore previous configuration"
      ansible.builtin.include_role:
        name: wildfly_snapshot
        tasks_from: restore_snapshot.yml
      vars:
        wildfly_snapshot_jboss_home: /opt/wildfly/wildfly-41.0.0.Final/
        wildfly_snapshot_restore_file: /opt/wildfly/wildfly-41.0.0.Final/standalone/configuration/standalone_xml_history/snapshot/20240101-120000000standalone.xml
```

### List and Delete Snapshots

```yaml
- name: "Manage snapshots"
  hosts: all
  collections:
    - middleware_automation.wildfly
  tasks:
    - name: "List all snapshots"
      ansible.builtin.include_role:
        name: wildfly_snapshot
        tasks_from: list_snapshots.yml
      vars:
        wildfly_snapshot_jboss_home: /opt/wildfly/wildfly-41.0.0.Final/
    # available in wildfly_snapshot_list.names and wildfly_snapshot_list.directory

    - name: "Delete a snapshot"
      ansible.builtin.include_role:
        name: wildfly_snapshot
        tasks_from: delete_snapshot.yml
      vars:
        wildfly_snapshot_jboss_home: /opt/wildfly/wildfly-41.0.0.Final/
        wildfly_snapshot_delete_name: "my-old-snapshot.xml"
```

## YAML Configuration Extension

When the YAML configuration extension is enabled, `:take-snapshot` captures the effective XML configuration. YAML overlay files are applied at server boot time and are managed separately as templates by the `wildfly_systemd` role. If a rollback is needed due to YAML overlay issues, the overlay template files should be reverted independently.

## License

GPL2

## Author Information

* [Ranabir Chakraborty](https://github.com/RanabirChakraborty)
