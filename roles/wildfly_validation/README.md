wildfly validation role
=======================

Role to validate that the app server installed was successful
and the associated systemd service is currently running.

<!--start argument_specs-->
Role Defaults
-------------

| Variable | Description | Default |
|:---------|:------------|:--------|
|`wildfly_user`| posix user account for wildfly | `wildfly` |
|`wildfly_group`| posix group for wildfly | `{{ wildfly_user }}` |
|`wildfly_service_name`| Systemd service name for wildfly | `wildfly` |
|`wildfly_install_workdir`| WildFly installation directory (where the server files are unzipped) | `/opt/wildfly/` |
|`wildfly_home`| WildFly installation directory (WILDFLY_HOME) | `{{ wildfly_install_workdir }}wildfly-{{ wildfly_version }}/` |
|`wildfly_http_port`| Port to verify the WildFly server is listening to requests | 8080 |
|`wildfly_controller_port`| Port to use to verify CLI connection to the WildFly server | 9990 |


Role Variables
--------------

* No required variables
<!--end argument_specs-->

## Example playbook

### WildFly service using an offset port

Validate a WildFly service that was created using port offset of 100.

```
---
- name: Verify
  hosts: all
  gather_facts: false
  collections:
    - middleware_automation.wildfly
  roles:
    - wildfly_validation
  vars:
    wildfly_http_port: 8180
    wildfly_controller_port: 10090
```
