Wildfly Systemd role
====================

This role provides a playbook to easily install a JDBC driver within
the server modules directory tree. It comes a template for the main.xml
(that can be overriden).

Requirements
------------

A valid Java runtime environment must be available for execution of the jcliff utility

<!--start argument_specs-->
Role Defaults
-------------

* No defaults


Role Variables
--------------

| Variable | Description |
|:---------|:------------|
|`jdbc_driver_module_dir`| Path for module installation |
|`jdbc_driver_version`| Version of jdbc driver to download |
|`jdbc_driver_jar_filename`| Filename of jdbc driver to download |
|`jdbc_driver_jar_url`| URL for jdbc driver download |
|`jdbc_driver_jar_installation_path`| Path for jdbc driver installation |
|`jdbc_driver_module_name`| Name for the jdbc driver module |

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
