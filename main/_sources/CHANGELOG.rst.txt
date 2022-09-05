===========================================
middleware_automation.wildfly Release Notes
===========================================

.. contents:: Topics

This changelog describes changes after version 0.0.7.

v1.2.0
======

Major Changes
-------------

- Propagate wildfly_install defaults to driver, systemd and utils roles `#80 <https://github.com/ansible-middleware/wildfly/pull/80>`_
- Propagate wildfly_install defaults to driver, systemd and utils roles `#80 <https://github.com/ansible-middleware/wildfly/pull/80>`_

Bugfixes
--------

- Become in "Check local download archive path" `#74 <https://github.com/ansible-middleware/wildfly/pull/74>`_
- Become in "Check local download archive path" `#74 <https://github.com/ansible-middleware/wildfly/pull/74>`_
- wildfly_driver: added wildfly_user and wildfly_group to defaults `#77 <https://github.com/ansible-middleware/wildfly/pull/77>`_
- wildfly_driver: added wildfly_user and wildfly_group to defaults `#77 <https://github.com/ansible-middleware/wildfly/pull/77>`_

v1.1.0
======

Minor Changes
-------------

- Bump version to 1.1.0 to align with downstream (1.1.0 is identical to 1.0.6 upstream) `#67 <https://github.com/ansible-middleware/wildfly/pull/67>`_

v1.0.6
======

v1.0.5
======

Minor Changes
-------------

- Add ``wildfly_java_opts`` to set parameters for wfly JVM `#60 <https://github.com/ansible-middleware/wildfly/pull/60>`_
- Add ``wildfly_statistics_enabled`` var to enable statistics `#58 <https://github.com/ansible-middleware/wildfly/pull/58>`_
- Add variable ``wildfly_bind_addr_private`` to set private iface bind address `#55 <https://github.com/ansible-middleware/wildfly/pull/55>`_
- Add variable ``wildfly_multicast_addr`` to set tcp/udp mcast address `#56 <https://github.com/ansible-middleware/wildfly/pull/56>`_
- Added variable for setting management port bind address `#62 <https://github.com/ansible-middleware/wildfly/pull/62>`_

Bugfixes
--------

- Fix EAP patch apply when yaml configuration is enabled `#59 <https://github.com/ansible-middleware/wildfly/pull/59>`_

v1.0.4
======

Breaking Changes / Porting Guide
--------------------------------

- Rename variable ``instance_id`` to ``wildfly_instance_id`` and update docs `#52 <https://github.com/ansible-middleware/wildfly/pull/52>`_

Bugfixes
--------

- Add become parameter to tasks that require it `#53 <https://github.com/ansible-middleware/wildfly/pull/53>`_

v1.0.3
======

Minor Changes
-------------

- Rename validation role vars to follow proper convention `#48 <https://github.com/ansible-middleware/wildfly/pull/48>`_
- wildfly_driver: make variables as default `#39 <https://github.com/ansible-middleware/wildfly/pull/39>`_

Breaking Changes / Porting Guide
--------------------------------

- Rename jboss_eap role into wildfly_utils to be consistent with role naming convention `#45 <https://github.com/ansible-middleware/wildfly/pull/45>`_

Bugfixes
--------

- JAVA_HOME should be set according to requested JVM package, or overridden via ``wildfly_java_home`` `#46 <https://github.com/ansible-middleware/wildfly/pull/46>`_
- Update included role to new name in rhn installation `#51 <https://github.com/ansible-middleware/wildfly/pull/51>`_

v1.0.2
======

Release Summary
---------------

Minor enhancements, and documentation updates.


v1.0.1
======

Release Summary
---------------

Minor enhancements, and documentation updates.


v1.0.0
======

Release Summary
---------------

This is the first stable release of the ``middleware_automation.wildfly`` collection.

