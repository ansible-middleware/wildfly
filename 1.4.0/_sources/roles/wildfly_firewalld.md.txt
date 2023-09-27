wildfly firewalld role
======================

Install and configure the firewalld service for wildfly application server or JBoss Enterprise Application (EAP)

Role Defaults
-------------

| Variable | Description | Default |
|:---------|:------------|:--------|
|`wildfly_firewalld_package_name`| Package name for firewalld on target hosts | `firewalld` |
|`wildfly_app_firewalld_enabled`| Indicate if firewalld should be used | `false` |
|`wildfly_listen_ports`| Indicate if firewalld should be used | `['8009', '8080', '8443', '8443', '4712', '4713']` |
