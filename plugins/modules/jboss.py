#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

__metaclass__ = type

# Copyright (c) 2013, Jeroen Hoekx <jeroen.hoekx@dsquare.be>
# Copyright (c) 2024, Red Hat, Inc.
# GNU General Public License v3.0+ (see https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

DOCUMENTATION = r"""
module: jboss
short_description: Deploy applications to WildFly/JBoss using filesystem deployment scanner
description:
  - Deploy or undeploy applications to WildFly/JBoss standalone server using the filesystem deployment scanner.
  - This module works by copying application files (WAR, EAR, etc.) to the deployment directory and monitoring
    deployment marker files created by the deployment scanner.
  - The module waits for the deployment scanner to process the application, which depends on the scan-interval
    configured in C(standalone.xml).
version_added: "1.6.0"
attributes:
  check_mode:
    description: The module supports check mode.
    support: full
  diff_mode:
    description: The module does not support diff mode.
    support: none
options:
  deployment:
    description:
      - The name of the deployment file.
      - This should match the filename that will be created in the deployment directory.
    type: str
    required: true
  src:
    description:
      - The remote path of the application file (EAR, WAR, JAR, etc.) to deploy.
      - Required when O(state=present).
      - Ignored when O(state=absent).
    type: path
  deploy_path:
    description:
      - The location in the filesystem where the deployment scanner listens.
      - This should match the deployment-scanner path configured in C(standalone.xml).
      - If not specified, defaults to C(/var/lib/jbossas/standalone/deployments).
      - For typical WildFly installations, this is usually C({{ wildfly_home }}/standalone/deployments).
    type: path
    default: /var/lib/jbossas/standalone/deployments
  state:
    description:
      - Whether the application should be deployed or undeployed.
    type: str
    choices: [absent, present]
    default: present
  timeout:
    description:
      - Maximum time in seconds to wait for deployment or undeployment to complete.
      - The deployment scanner processes files based on its scan-interval setting.
      - If the timeout is reached before completion, the module will fail.
    type: int
    default: 300
notes:
  - The JBoss standalone deployment-scanner subsystem must be enabled in C(standalone.xml).
  - The module monitors deployment marker files (C(.deployed), C(.undeployed), C(.failed)) created by the deployment scanner.
  - The wait time depends on the scan-interval parameter configured in C(standalone.xml).
  - Ensure no identically named application is deployed through the JBoss CLI, as this can cause conflicts.
  - The module uses SHA1 checksums to detect changes in application files for idempotency.
seealso:
  - name: WildFly Deployment Scanner documentation
    description: Complete reference of the WildFly deployment scanner.
    link: https://docs.wildfly.org/
author:
  - Jeroen Hoekx (@jhoekx)
  - Red Hat, Inc. (@ansible-middleware)
"""

EXAMPLES = r"""
- name: Deploy a hello world application
  middleware_automation.wildfly.jboss:
    src: /tmp/hello-1.0-SNAPSHOT.war
    deployment: hello.war
    state: present

- name: Deploy application to custom WildFly deployment path
  middleware_automation.wildfly.jboss:
    src: /tmp/myapp-2.0.war
    deploy_path: "{{ wildfly_home }}/standalone/deployments"
    deployment: myapp.war
    state: present

- name: Update an existing deployment
  middleware_automation.wildfly.jboss:
    src: /tmp/hello-1.1-SNAPSHOT.war
    deployment: hello.war
    state: present

- name: Undeploy an application
  middleware_automation.wildfly.jboss:
    deployment: hello.war
    state: absent

- name: Deploy with custom timeout
  middleware_automation.wildfly.jboss:
    src: /tmp/large-app.war
    deployment: large-app.war
    timeout: 600
    state: present
"""

RETURN = r"""
changed:
  description: Whether the module made any changes.
  returned: always
  type: bool
  sample: true
deployment:
  description: The name of the deployment file.
  returned: always
  type: str
  sample: hello.war
deploy_path:
  description: The deployment directory path used.
  returned: always
  type: str
  sample: /opt/wildfly/standalone/deployments
deployed:
  description: Whether the application is currently deployed.
  returned: always
  type: bool
  sample: true
"""

import os
import time
from ansible.module_utils.basic import AnsibleModule


def is_deployed(deploy_path, deployment):
    """Check if deployment marker file exists indicating successful deployment."""
    return os.path.exists(os.path.join(deploy_path, "{0}.deployed".format(deployment)))


def is_undeployed(deploy_path, deployment):
    """Check if undeployment marker file exists."""
    return os.path.exists(os.path.join(deploy_path, "{0}.undeployed".format(deployment)))


def is_failed(deploy_path, deployment):
    """Check if deployment failed marker file exists."""
    return os.path.exists(os.path.join(deploy_path, "{0}.failed".format(deployment)))


def main():
    """Main module execution."""
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type="path"),
            deployment=dict(type="str", required=True),
            deploy_path=dict(type="path", default="/var/lib/jbossas/standalone/deployments"),
            state=dict(type="str", choices=["absent", "present"], default="present"),
            timeout=dict(type="int", default=300),
        ),
        required_if=[("state", "present", ("src",))],
        supports_check_mode=True,
    )

    result = dict(
        changed=False,
        deployment=module.params["deployment"],
        deploy_path=module.params["deploy_path"],
        deployed=False,
    )

    src = module.params["src"]
    deployment = module.params["deployment"]
    deploy_path = module.params["deploy_path"]
    state = module.params["state"]
    timeout = module.params.get("timeout", 300)

    deployed_file = os.path.join(deploy_path, deployment)

    if not os.path.exists(deploy_path):
        module.fail_json(msg="Deployment path '{0}' does not exist.".format(deploy_path))

    if not os.path.isdir(deploy_path):
        module.fail_json(msg="Deployment path '{0}' is not a directory.".format(deploy_path))

    if state == "absent" and src:
        module.warn("Parameter 'src' is ignored when state=absent")
    elif state == "present" and not os.path.exists(src):
        module.fail_json(msg="Source file '{0}' does not exist.".format(src))

    deployed = is_deployed(deploy_path, deployment)
    result["deployed"] = deployed

    if module.check_mode:
        if state == "present":
            result["changed"] = True
        elif state == "absent":
            result["changed"] = True

        module.exit_json(**result)

    if state == "present":
        if is_failed(deploy_path, deployment):
            os.remove(os.path.join(deploy_path, "{0}.failed".format(deployment)))

        if is_undeployed(deploy_path, deployment):
            os.remove(os.path.join(deploy_path, "{0}.undeployed".format(deployment)))

        if deployed:
            os.remove(os.path.join(deploy_path, "{0}.deployed".format(deployment)))

        module.preserved_copy(src, deployed_file)
        result["changed"] = True
        deployed = False
        start_time = time.time()
        while not deployed:
            deployed = is_deployed(deploy_path, deployment)
            if is_failed(deploy_path, deployment):
                module.fail_json(msg="Deploying {0} failed. Check server logs for details.".format(deployment))
            elapsed = time.time() - start_time
            if elapsed > timeout:
                module.fail_json(
                    msg="Timeout waiting for deploying {0} after {1} seconds".format(deployment, timeout)
                )
            time.sleep(1)
        result["deployed"] = True

    elif state == "absent":
        if deployed:
            os.remove(os.path.join(deploy_path, "{0}.deployed".format(deployment)))
            start_time = time.time()
            while deployed:
                deployed = not is_undeployed(deploy_path, deployment)
                if is_failed(deploy_path, deployment):
                    module.fail_json(msg="Undeploying {0} failed. Check server logs for details.".format(deployment))
                elapsed = time.time() - start_time
                if elapsed > timeout:
                    module.fail_json(
                        msg="Timeout waiting for undeploying {0} after {1} seconds".format(deployment, timeout)
                    )
                time.sleep(1)
        result["changed"] = True
        result["deployed"] = False

    module.exit_json(**result)


if __name__ == "__main__":
    main()
