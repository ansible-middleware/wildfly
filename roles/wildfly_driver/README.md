wildfly driver role
===================

This role provides a playbook to easily install a JDBC driver within
the server modules directory tree. It comes with a template for the main.xml
(that can be overriden).

<!--start argument_specs-->
Role Defaults
-------------

| Variable | Description | Default |
|:---------|:------------|:--------|
|`wildfly_driver_module_dir`| Path for module installation | `{{ wildfly_home }}/modules/{{ wildfly_driver.module_name | replace('.', '/') }}/main` |
|`wildfly_driver_jar_installation_path`| Path for JDBC driver installation | `{{ wildfly_driver_module_dir }}/{{ wildfly_driver.jar_filename }}` |
|`wildfly_version`| WildFly version to install | `39.0.0.Final` |
|`wildfly_home`| WildFly installation directory | `/opt/wildfly/wildfly-{{ wildfly_version }}/` |
|`wildfly_user`| POSIX user account for WildFly | `wildfly` |
|`wildfly_group`| POSIX group for WildFly | `{{ wildfly_user }}` |
<!--end argument_specs-->


Role Variables
--------------

| Variable | Description | Required |
|:---------|:------------|:--------|
|`wildfly_driver_version`| Version of JDBC driver to download | `yes` |
|`wildfly_driver_jar_filename`| Filename of JDBC driver to download | `yes` |
|`wildfly_driver_jar_url`| URL for JDBC driver download | `yes` |
|`wildfly_driver_module_name`| Name for the JDBC driver module | `yes` |


Example Playbook
----------------

```yaml
  tasks:
    - name: Install drivers with wildfly_driver role
      ansible.builtin.include_role:
        name: wildfly_driver
      vars:
        wildfly_driver_module_name: "{{ item.name }}"
        wildfly_driver_version: "{{ item.version }}"
        wildfly_driver_jar_filename: "{{ item.jar_file }}"
        wildfly_driver_jar_url: "{{ item.url }}"
      loop:
        - version: "{{ postgres_driver_version }}"
          name: 'org.postgresql'
          jar_file: "postgresql-{{ postgres_driver_version }}.jar"
          url: "https://repo.maven.apache.org/maven2/org/postgresql/postgresql/{{ postgres_driver_version }}/postgresql-{{ postgres_driver_version }}.jar"
        - version: "{{ mariadb_driver_version }}"
          name: 'org.mariadb'
          jar_file: "mariadb-java-client-{{ mariadb_driver_version }}.jar"
          url: "https://repo1.maven.org/maven2/org/mariadb/jdbc/mariadb-java-client/{{ mariadb_driver_version }}/mariadb-java-client-{{ mariadb_driver_version }}.jar"
```


Author Information
------------------

* [Romain Pelisse](https://github.com/rpelisse)
