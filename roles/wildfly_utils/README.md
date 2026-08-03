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
|`wildfly_utils_prospero_scenario_enable`| Specificy to Molecule if it should run the Prospero scenario | `True` |
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
