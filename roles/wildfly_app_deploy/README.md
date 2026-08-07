wildfly app deploy role
========================

Role to deploy applications (.war, .ear, .jar) to WildFly application server in standalone mode.

Requirements
------------

* WildFly server must be installed and running
* Management interface must be accessible
* The `wildfly_utils` role is required as a dependency

<!--start argument_specs-->
Role Defaults
-------------

| Variable | Description | Default |
|:---------|:------------|:--------|
|`wildfly_app_deploy_deployment_file`| Path to the application artifact (.war, .ear, .jar) on the Ansible controller | `/path/to/your/application.war` |
|`wildfly_app_deploy_name`| The name to use for the deployment in WildFly (e.g., app-v1.war) | `application.war` |
|`wildfly_app_deploy_home`| WildFly installation directory | Inherited |
|`wildfly_app_deploy_jboss_cli_controller_host`| Hostname for connecting to CLI | `localhost` |
|`wildfly_app_deploy_jboss_cli_controller_port`| Port for connecting to CLI | `9990` |
|`wildfly_app_deploy_port_range_offset`| Increment for `jboss.socket.binding.port-offset` | `0` |
|`wildfly_app_deploy_user`| POSIX user account for WildFly | `wildfly` |
|`wildfly_app_deploy_group`| POSIX group for WildFly | `{{ wildfly_app_deploy_user }}` |

Role Variables
--------------

| Variable | Description | Required |
|:---------|:------------|:---------|
|`wildfly_app_deploy_deployment_file`| Path to the application artifact on the Ansible controller | `Yes` |
<!--end argument_specs-->

## Example Playbooks

### Deploy Application to Standalone Server

Deploy a WAR file to a standalone WildFly instance.

```yaml
- name: Deploy application to WildFly
  hosts: wildfly_servers
  gather_facts: false
  roles:
    - role: middleware_automation.wildfly.wildfly_app_deploy
  vars:
    wildfly_app_deploy_deployment_file: "/path/to/myapp.war"
    wildfly_app_deploy_name: "myapp.war"
    wildfly_app_deploy_home: "/opt/wildfly/wildfly-40.0.0.Final/"
    wildfly_app_deploy_jboss_cli_controller_host: "localhost"
    wildfly_app_deploy_jboss_cli_controller_port: "9990"
```

### Deploy with Port Offset

Deploy to a WildFly instance using a port offset.

```yaml
- name: Deploy application with port offset
  hosts: wildfly_servers
  gather_facts: false
  roles:
    - role: middleware_automation.wildfly.wildfly_app_deploy
  vars:
    wildfly_app_deploy_deployment_file: "/path/to/myapp.war"
    wildfly_app_deploy_name: "myapp.war"
    wildfly_app_deploy_port_range_offset: 100
    wildfly_app_deploy_jboss_cli_controller_port: "9990"  # Port will be 9990 + 100 = 10090
```

## Dependencies

* `wildfly_utils` - Required for CLI operations

## License

Apache License 2.0

## Author Information

* [Harsha Cherukuri](https://github.com/hcherukuri)
