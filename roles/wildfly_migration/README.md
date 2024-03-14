wildfly migration role
======================

This role encapsulate the [Wildfly Migration Tool](https://docs.wildfly.org/28/Migration_Guide.html) to allow using it as part of a Playbook.

Requirements
------------

Requirements on the target system are ensured by the role.

<!--start argument_specs-->
Role Defaults
-------------

| Variable | Description | Default |
|:---------|:------------|:--------|
|`wildfly_migration_environment_props`| Template to configure the migration tool | `templates/environment.properties.j2` |


| Variable | Description | Required |
|:---------|:------------|:---------|


Role Variables
--------------

* No required variables

<!--end argument_specs-->

## Dependencies

None

## Example Playbooks



### Enable repository


TODO

## License

GPL2

## Author Information

* [Romain Pelisse](https://github.com/rpelisse)
