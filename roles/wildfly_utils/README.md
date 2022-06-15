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


Role Variables
--------------

| Variable | Description | Required |
|:---------|:------------|:---------|
|`wildfly_home`| Wildfly home directory | `Yes` |
<!--end argument_specs-->
