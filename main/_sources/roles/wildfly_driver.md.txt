wildfly driver role
====================

This role provides a playbook to easily install a JDBC driver within
the server modules directory tree. It comes with a template for the main.xml
(that can be overriden).

<!--start argument_specs-->
Role Defaults
-------------

| Variable | Description | Default |
|:---------|:------------|:--------|
|`wildfly_driver_module_dir`| Path for module installation | `{{ wildfly_home }}/modules/{{ wildfly_driver_module_name | replace('.', '/') }}/main` |
|`wildfly_driver_version`| Version of jdbc driver to download | `` |
|`wildfly_driver_jar_filename`| Filename of jdbc driver to download | `` |
|`wildfly_driver_jar_url`| URL for jdbc driver download | `` |
|`wildfly_driver_jar_installation_path`| Path for jdbc driver installation | `` |
|`wildfly_driver_module_name`| Name for the jdbc driver module | `` |
|`wildfly_version`| Wildfly version to install | `29.0.0.Final` |
|`wildfly_home`| Wildfly installation directory | `/opt/wildfly/wildfly-{{ wildfly_version }}/` |
|`wildfly_user`| posix user account for wildfly | `wildfly` |
|`wildfly_group`| posix group for wildfly | `{{ wildfly_user }}` |
<!--end argument_specs-->

Dependencies
------------


Example Playbook
----------------

License
-------

GPL2

Author Information
------------------

* [Romain Pelisse](https://github.com/rpelisse)
