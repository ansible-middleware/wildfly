wildfly utils role
==================

This roles regroups reusable content to manage the server, but also dealing with JBoss EAP specific
feature (such as apply cumulative patches).


Entrypoints
-----------

* download_from_rhn: download resources from the Red Hat Customer Portal via the JBossNetwork API
* apply_cp: download and patch EAP
* keycloak_adapter: download and install the keycloak adapter module
* jboss_cli: execute arbitrary cli commands of command files

<!--start argument_specs-->
Role Defaults
-------------

| Variable | Description | Default |
|:---------|:------------|:--------|
|`jboss_cli_controller_host`| Hostname for connecting to cli | `localhost` |
|`jboss_cli_controller_port`| Port for connecting to cli | `9990` |
|`wildfly_no_restart_after_patch`| When true, skip restarting after applying a cumulative patch | `False` |
|`wildfly_install_workdir`| Wildfly installation directory (where the server files are unzipped) | `/opt/wildfly/` |
|`wildfly_home`| Wildfly installation directory (WILDFLY_HOME) | `{{ wildfly_install_workdir }}wildfly-{{ wildfly_version }}/` |


Role Variables
--------------

| Variable | Description | Required |
|:---------|:------------|:---------|
|`jboss_cli_query`| The command to execute via jboss-cli; one of jboss_cli_query or jboss_cli_file is required exclusively | `False` |
|`jboss_cli_file`| The file to execute via jboss-cli; one of jboss_cli_query or jboss_cli_file is required exclusively | `False` |
|`jboss_cli_timeout`| Seconds to wait for jboss-cli connection to server | `False` |
<!--end argument_specs-->
