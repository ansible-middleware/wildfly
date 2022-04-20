Wildfly Driver role
====================

This role provides a playbook to easily install a JDBC driver within
the server modules directory tree. It comes with a template for the main.xml
(that can be overriden).

Requirements
------------

A valid Java runtime environment must be available for execution of the jcliff utility

<!--start argument_specs-->
Role Defaults
-------------

| Variable | Description | Default |
|:---------|:------------|:--------|
|`wildfly_user`| posix user account for wildfly | `wildfly` |
|`wildfly_group`| posix group for wildfly | `wildfly` |
|`jdbc_driver_module_dir`| Path for module installation | `{{ jdbc_driver_jboss_home }}/modules/org/postgresql/main"` |
|`jdbc_driver_version`| Version of jdbc driver to download | `9.4.1212` |
|`jdbc_driver_jar_filename`| Filename of jdbc driver to download | `postgresql-{{ jdbc_driver_version }}.jar` |
|`jdbc_driver_jar_url`| URL for jdbc driver download | `https://repo.maven.apache.org/maven2/org/postgresql/postgresql/{{ jdbc_driver_version }}/postgresql-{{ jdbc_driver_version }}.jar` |
|`jdbc_driver_jar_installation_path`| Path for jdbc driver installation | `{{ jdbc_driver_module_dir }}/{{ jdbc_driver_jar_filename }}` |
|`jdbc_driver_module_name`| Name for the jdbc driver module | `org.postgresql` |
|`override_module_xml_template`| Override path of template used for module configuration | `None` |

Role Variables
--------------

| Variable | Description |
|:---------|:------------|
|`wildfly_home`| Home directory of jboss installation |
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
