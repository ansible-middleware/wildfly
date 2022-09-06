Wildfly Subs role
====================

This role is designed to help set up JBoss EAP (Red Hat product based on Wildfly) using RPM
delivered by Red Hat to its customer. The playbook provides handy reusable content to enable
or disable a repo and install EAP using the group install feature.

Requirements
------------

Requirements on the target system are ensured by the role.

<!--start argument_specs-->
Role Defaults
-------------

| Variable | Description | Default |
|:---------|:------------|:--------|
|`wildfly_subs_check_repo_enable`| Enable repo | `True` |
|`wildfly_subs_check_repo_disabled`| Disable repo | `"{{ wildfly_subs_check_repo_enable }}"` |
|`wildfly_subs_skip_remove`| Remove installed server | `False` |
|`wildfly_repos_state_file_homedir`| State file home directory | `/opt` |
|`wildfly_repos_state_file_prefix`| State filename prefix | `.eap` |
|`wildfly_repos_state_file_suffix`| State filename suffix | `.repo` |
|`wildfly_rpm_install_root_dir`| RPM install root dir | `/opt/rh/eap7/` |
|`eap_group_install_name`| EAP group install package name| `jboss-eap7-jdk11` |

Role Variables
--------------

* No required variables

<!--end argument_specs-->

## Dependencies

## Example Playbooks

### Enable repository


TODO

## License

GPL2

## Author Information

* [Romain Pelisse](https://github.com/rpelisse)
