JBoss EAP role
==============

This roles regroups reusable content to manage the server, but also dealing with JBoss EAP specific
feature (such as apply cumulative patches).

<!--start argument_specs-->
Role Defaults
-------------

| Variable | Description | Default |
|:---------|:------------|:--------|
|`jboss_cli_controller_host`| Hostname for connecting to cli | `localhost` |
|`jboss_cli_controller_port`| Port for connecting to cli | `9990` |
|`wildfly_no_restart_after_patch`| When true, skip restarting after applying a cumulative patch | `False` |
|`wildfly_home`| Wildfly installation directory | `/opt/wildfly/wildfly-{{ wildfly_version }}/` |

Role Variables
--------------

| Variable | Description | Required |
|:---------|:------------|:---------|
|`query`| The command to sed to jboss-cli when tasks from jboss_cli.yml are used | `Yes` |
<!--end argument_specs-->
