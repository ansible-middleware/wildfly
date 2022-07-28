# Testing

## Continuous integration

The collection is tested with a [molecule](https://github.com/ansible-community/molecule) setup covering the included roles and verifying correct installation and idempotency.
In order to run the molecule tests locally with python 3.9 available, after cloning the repository:

```
pip install yamllint 'molecule[docker]~=3.5.2' ansible-core flake8 ansible-lint voluptuous
molecule test --all
```


## Integration testing

Demo repositories which depend on the collection, and aggregate functionality with other middleware_automation collections, are automatically rebuilt
at every collection release to ensure non-breaking changes and consistent behaviour.

The repository are:

 - [Flange demo](https://github.com/ansible-middleware/flange-demo)
   A deployment of Wildfly cluster integrated with keycloak and infinispan.
 - [CrossDC keycloak demo](https://github.com/ansible-middleware/wildfly-cluster-demo)
   A clustered installation of EAP.


## Test playbooks

Sample playbooks are provided in the `playbooks/` directory; to run the playbooks locally (requires a rhel system with python 3.9+, ansible, and systemd) the steps are as follows:

```
# setup environment
pip install ansible-core
# clone the repository
git clone https://github.com/ansible-middleware/wildfly
cd wildfly
# install collection dependencies
ansible-galaxy collection install -r requirements.yml
# create inventory for localhost
cat << EOF > inventory
[wildfly]
localhost ansible_connection=local
EOF
# run the playbook
ansible-playbook -i inventory playbooks/playbook.yml
```
