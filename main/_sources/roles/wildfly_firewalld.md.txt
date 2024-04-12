wildfly firewalld role
======================

Install and configure the firewalld service for wildfly application server or JBoss Enterprise Application (EAP)

Role Defaults
-------------

| Variable | Description | Default |
|:---------|:------------|:--------|
|`wildfly_firewalld_package_name`| Package name for firewalld on target hosts | `firewalld` |
|`wildfly_firewalld_enabled`| Specify whether or not firewalld should be used | `false` |
|`wildfly_firewalld_custom_ports`|Override to provided a custom set of ports of open for the server (number, protocol)|``|
|`wildfly_firewalld_listen_ports`|Default port set used by the standalone.xml|N/A|
|`wildfly_firewalld_listen_full_ports`|Default port set used by the standalone-full.xml"|N/A|
|`wildfly_firewalld_ha_listen_ports`|Default port set used by the standalone-ha.xml"|N/A|
|`wildfly_firewalld_full_ha_listen_ports`|Default port set used by the standalone-full-ha.xml"|N/A|
|`wildfly_firewalld_multicast_addr`|Multicast address used by JGroups for server clustering|230.0.0.4|
|`wildfly_firewalld_multicast_rules`|Firewalld rules added to allow multicast|N/A|
|`wildfly_cluster_enabled`|Specify whether or not the server's cluster is enabled|`false`|
