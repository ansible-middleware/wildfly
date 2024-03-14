wildfly prospero role
=====================

Integrate [Prospero](https://www.wildfly.org/news/2023/04/05/prospero/) as an alternative installation mechanism for Wildfly. This role integrates the tool inside the collection, so it can be used as part of a playbook or as alternative to the usual installation method (zipfile).

<!--start argument_specs-->
Role Defaults
-------------

| Variable | Description | Default |
|:---------|:------------|:--------|
|`wildfly_prospero_version`| Version of Prospero to use | `1.2.0.Final` |
|`wildfly_prospero_name`| TODO document argument | `prospero` |
|`wildfly_prospero_install_dir`| Path to the installation dir for Prospero | `/opt/prospero` |
|`wildfly_prospero_profile_name`| TODO document argument | `wildfly` |
|`wildfly_prospero_scenario_enable`| TODO document argument | `True` |
|`wildfly_prospero_archive_name`| TODO document argument | `{{ wildfly_prospero_name }}-{{ wildfly_prospero_version }}.zip` |
|`wildfly_prospero_home`| Home of the prospero tool | `{{ wildfly_prospero_install_dir }}/{{ wildfly_prospero_name }}-{{ wildfly_prospero_version }}` |
|`wildfly_install_manifest_dir`| TODO document argument | `{{ wildfly_install_workdir }}/manifest` |
|`wildfly_prospero_download_url`| URL to download Prospero | `https://github.com/wildfly-extras/prospero/releases/download/{{ wildfly_prospero_version }}/prospero-{{ wildfly_prospero_version }}.zip` |
|`wildfly_prospero_download_check_ssl`| TODO document argument | `False` |
<!--end argument_specs-->


Role Variables
--------------

| Variable | Description | Required |
|:---------|:------------|:--------|

| Variable | Description | Required |
|:---------|:------------|:---------|

Example Playbook
----------------

```
- name: Playbook to install Wildfly using Prospero
  hosts: all
  vars:
    wildfly_install_user: 'wildfly'
    wildfly_install_group: "{{ wildfly_install_user }}"
    wildfly_install_use_prospero: True
    wildfly_prospero_scenario_enable: True
  collections:
    - middleware_automation.wildfly
  tasks:
    - name: "Run Prospero scenario only upstream."
      block:
        - name: "Ensure required local user and group exists."
          ansible.builtin.include_role:
            name: wildfly_install
            tasks_from: user.yml

        - name: "Install server using Prospero"
          ansible.builtin.include_role:
            name: wildfly_install

        - name: "Run server with systemd"
          ansible.builtin.include_role:
            name: wildfly_systemd
      when:
        - wildfly_prospero_scenario_enable is defined and wildfly_prospero_scenario_enable

```

Author Information
------------------

* [Romain Pelisse](https://github.com/rpelisse)
* [Bartosz Spyrko-Smietanko](https://github.com/spyrkob)
