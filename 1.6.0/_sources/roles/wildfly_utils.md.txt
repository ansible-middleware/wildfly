wildfly utils role
==================

This roles regroups reusable content to manage the server, but also dealing with JBoss EAP specific
feature (such as apply cumulative patches).


Entrypoints
-----------

* download_from_rhn: download resources from the Red Hat Customer Portal via the Unified Downloads API
* apply_cp: download and patch EAP
* keycloak_adapter: download and install the keycloak adapter module
* jboss_cli: execute arbitrary cli commands of command files
* prospero/history: retrieve the Prospero revision history for a server installation
* prospero/revert: revert a Prospero-managed server to a previous revision
* prospero/run_cli: run an arbitrary Prospero CLI command

Prospero Server Rollback
------------------------

For servers installed using Prospero (WildFly 32+ / EAP 8.1+), the collection provides tasks to view revision history and revert the server to a previous state. Every Prospero operation (install, update, channel change) automatically creates a revision entry. You can revert to any previous revision.

### View revision history

```yaml
- hosts: all
  tasks:
    - name: "Get revision history"
      ansible.builtin.include_role:
        name: middleware_automation.wildfly.wildfly_utils
        tasks_from: prospero/history.yml

    - name: "Show revisions"
      ansible.builtin.debug:
        msg: "{{ wildfly_utils_prospero_history }}"
```

Output looks like:

```
[a1b2c3d4] 2026-09-24T10:00:00Z - update
[e5f6g7h8] 2026-09-20T09:00:00Z - update
[i9j0k1l2] 2026-09-01T06:00:00Z - install
```

### Revert to a previous revision

The `prospero/revert.yml` task stops the service, reverts the server, fixes file ownership, and restarts the service.

```yaml
- hosts: all
  vars:
    wildfly_user: 'wildfly'
    wildfly_group: "{{ wildfly_user }}"
  tasks:
    - name: "Get revision history"
      ansible.builtin.include_role:
        name: middleware_automation.wildfly.wildfly_utils
        tasks_from: prospero/history.yml

    - name: "Revert to the previous revision (undo last update)"
      ansible.builtin.include_role:
        name: middleware_automation.wildfly.wildfly_utils
        tasks_from: prospero/revert.yml
      vars:
        wildfly_utils_prospero_revert_revision: "{{ wildfly_utils_prospero_revision_ids[1] }}"
```

### Bulk rollback across multiple servers

Revision IDs are unique per server, but you do not need to know them in advance. Ansible retrieves each server's history individually, so a single playbook works for all servers:

```yaml
- hosts: all_wildfly_servers
  vars:
    wildfly_user: 'wildfly'
    wildfly_group: "{{ wildfly_user }}"
  tasks:
    - name: "Get each server's revision history"
      ansible.builtin.include_role:
        name: middleware_automation.wildfly.wildfly_utils
        tasks_from: prospero/history.yml

    - name: "Revert all servers to the previous revision"
      ansible.builtin.include_role:
        name: middleware_automation.wildfly.wildfly_utils
        tasks_from: prospero/revert.yml
      vars:
        wildfly_utils_prospero_revert_revision: "{{ wildfly_utils_prospero_revision_ids[1] }}"
```

### Revision index reference

Prospero lists revisions most recent first. The parsed list follows the same order:

| Index | Meaning |
|:------|:--------|
| `[0]` | Most recent revision (current state) |
| `[1]` | Previous revision (undo last change) |
| `[2]` | Two changes ago |
| `[3]` | Three changes ago |

<!--start argument_specs-->
Role Defaults
-------------

| Variable | Description | Default |
|:---------|:------------|:--------|
|`wildfly_utils_jboss_cli_controller_host`| Hostname for connecting to CLI | `localhost` |
|`wildfly_utils_jboss_cli_controller_port`| Port for connecting to CLI | `9990` |
|`wildfly_utils_no_restart_after_patch`| When true, skip restarting after applying a cumulative patch | `False` |
|`wildfly_utils_install_workdir`| WildFly installation directory (where the server files are unzipped) | `/opt/wildfly/` |
|`wildfly_utils_home`| WildFly installation directory (WILDFLY_HOME) | `{{ wildfly_utils_install_workdir }}wildfly-{{ wildfly_utils_version }}/` |
|`wildfly_utils_prospero_version`| Version of Prospero to use | `''` |
|`wildfly_utils_prospero_name`| Constant for the name of the prospero tool | `prospero` |
|`wildfly_utils_prospero_install_dir`| Path to the installation dir for Prospero | `/opt/prospero` |
|`wildfly_utils_prospero_profile_name`| Name of the WildFly profile for the server to install | `wildfly` |
|`wildfly_utils_prospero_scenario_enable`| Specify to Molecule if it should run the Prospero scenario | `True` |
|`wildfly_utils_prospero_archive_name`| Name of the Prospero archive | `{{ wildfly_utils_prospero_name }}-{{ wildfly_utils_prospero_version }}.zip` |
|`wildfly_utils_prospero_download_check_ssl`| Should Ansible check SSL when downloading Prospero | `False` |
<!--end argument_specs-->




Role Variables
--------------

| Variable | Description | Required |
|:---------|:------------|:---------|
|`wildfly_utils_jboss_cli_query`| The command to execute via jboss-cli; one of wildfly_utils_jboss_cli_query or wildfly_utils_jboss_cli_file is required exclusively | `False` |
|`wildfly_utils_jboss_cli_file`| The file to execute via jboss-cli; one of wildfly_utils_jboss_cli_query or wildfly_utils_jboss_cli_file is required exclusively | `False` |
|`wildfly_utils_jboss_cli_timeout`| Seconds to wait for jboss-cli connection to server | `False` |
<!--end argument_specs-->

## Author Information

* [Ranabir Chakraborty](https://github.com/RanabirChakraborty)
