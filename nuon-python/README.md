# nuon

Developer-friendly & type-safe Python SDK specifically catered to leverage *nuon* API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=nuon&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


<br /><br />
> [!IMPORTANT]
> This SDK is not yet ready for production use. To complete setup please follow the steps outlined in your [workspace](https://app.speakeasy.com/org/nuon-test/nuon-python). Delete this section before > publishing to a package manager.

<!-- Start Summary [summary] -->
## Summary

Nuon: API for managing nuon apps, components, installs, and actions.
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [nuon](#nuon)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!TIP]
> To finish publishing your SDK to PyPI you must [run your first generation action](https://www.speakeasy.com/docs/github-setup#step-by-step-guide).


> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add git+<UNSET>.git
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install git+<UNSET>.git
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add git+<UNSET>.git
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from nuon python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "nuon",
# ]
# ///

from nuon import Nuon

sdk = Nuon(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from nuon import Nuon, models
import os


with Nuon() as n_client:

    res = n_client.actions.get_action_workflow_config(security=models.GetActionWorkflowConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), action_workflow_config_id="<id>")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from nuon import Nuon, models
import os

async def main():

    async with Nuon() as n_client:

        res = await n_client.actions.get_action_workflow_config_async(security=models.GetActionWorkflowConfigSecurity(
            api_key=os.getenv("NUON_API_KEY", ""),
        ), action_workflow_config_id="<id>")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name      | Type   | Scheme  | Environment Variable |
| --------- | ------ | ------- | -------------------- |
| `api_key` | apiKey | API key | `NUON_API_KEY`       |

To authenticate with the API the `api_key` parameter must be set when initializing the SDK client instance. For example:
```python
from nuon import Nuon
import os


with Nuon(
    api_key=os.getenv("NUON_API_KEY", ""),
) as n_client:

    res = n_client.general.get_cli_config()

    # Handle response
    print(res)

```

### Per-Operation Security Schemes

Some operations in this SDK require the security scheme to be specified at the request level. For example:
```python
from nuon import Nuon, models


with Nuon() as n_client:

    res = n_client.actions.get_action_workflow_config(security=models.GetActionWorkflowConfigSecurity(

    ), action_workflow_config_id="<id>")

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [actions](docs/sdks/actions/README.md)

* [get_action_workflow_config](docs/sdks/actions/README.md#get_action_workflow_config) - get an app action workflow config
* [delete_action_workflow](docs/sdks/actions/README.md#delete_action_workflow) - delete an app
* [get_action_workflow](docs/sdks/actions/README.md#get_action_workflow) - get an app action workflow
* [update_app_action_workflow](docs/sdks/actions/README.md#update_app_action_workflow) - patch an app
* [get_action_workflow_configs](docs/sdks/actions/README.md#get_action_workflow_configs) - get action workflow for an app
* [create_action_workflow_config](docs/sdks/actions/README.md#create_action_workflow_config) - create action workflow config
* [get_action_workflow_latest_config](docs/sdks/actions/README.md#get_action_workflow_latest_config) - get an app action workflow's latest config
* [get_action_workflows](docs/sdks/actions/README.md#get_action_workflows) - get action workflows for an app
* [create_app_action_workflow](docs/sdks/actions/README.md#create_app_action_workflow) - create an app
* [get_app_action_workflow](docs/sdks/actions/README.md#get_app_action_workflow) - get an app action workflow
* [get_install_action_workflows_latest_runs](docs/sdks/actions/README.md#get_install_action_workflows_latest_runs) - get latest runs for all action workflows by install id
* [get_install_action_workflow_runs](docs/sdks/actions/README.md#get_install_action_workflow_runs) - get action workflow runs by install id
* [create_install_action_workflow_run](docs/sdks/actions/README.md#create_install_action_workflow_run) - create an action workflow run for an install
* [get_install_action_workflow_run](docs/sdks/actions/README.md#get_install_action_workflow_run) - get action workflow runs by install id and run id
* [get_install_action_workflow_run_step](docs/sdks/actions/README.md#get_install_action_workflow_run_step) - get action workflow run step by install id and step id
* [get_install_action_workflow_recent_runs](docs/sdks/actions/README.md#get_install_action_workflow_recent_runs) - get recent runs for an action workflow by install id

### [actions_runner](docs/sdks/actionsrunner/README.md)

* [get_action_workflow_config](docs/sdks/actionsrunner/README.md#get_action_workflow_config) - get an app action workflow config
* [get_action_workflow_latest_config](docs/sdks/actionsrunner/README.md#get_action_workflow_latest_config) - get an app action workflow's latest config
* [get_install_action_workflow_run](docs/sdks/actionsrunner/README.md#get_install_action_workflow_run) - get action workflow runs by install id and run id

### [apps](docs/sdks/apps/README.md)

* [get_apps](docs/sdks/apps/README.md#get_apps) - get all apps for the current org
* [create_app](docs/sdks/apps/README.md#create_app) - create an app
* [delete_app](docs/sdks/apps/README.md#delete_app) - delete an app
* [get_app](docs/sdks/apps/README.md#get_app) - get an app
* [update_app](docs/sdks/apps/README.md#update_app) - update an app
* [get_app_branches](docs/sdks/apps/README.md#get_app_branches) - get app branches
* [create_app_branch](docs/sdks/apps/README.md#create_app_branch) - Cancel a runner job.

* [get_app_branch_app_configs](docs/sdks/apps/README.md#get_app_branch_app_configs) - get app branch app configs
* [create_app_break_glass_config](docs/sdks/apps/README.md#create_app_break_glass_config) - Create a break glass config for an app.

* [get_app_break_glass_config](docs/sdks/apps/README.md#get_app_break_glass_config) - get app break_glass config
* [create_app_config](docs/sdks/apps/README.md#create_app_config) - Create an app config, by pushing the contents of a config file.

The API will automatically configure the app according to the config file in the background.

* [get_app_config](docs/sdks/apps/README.md#get_app_config) - get an app config
* [update_app_config](docs/sdks/apps/README.md#update_app_config) - Update an app config, setting status and state.

* [get_app_config_graph](docs/sdks/apps/README.md#get_app_config_graph) - get an app config graph
* [update_app_config_installs](docs/sdks/apps/README.md#update_app_config_installs)
* [get_app_configs](docs/sdks/apps/README.md#get_app_configs) - get app configs
* [create_app_input_config](docs/sdks/apps/README.md#create_app_input_config) - App input configs allow you to declare the inputs for your application, and do things such as require customer inputs or 
expose configuration knobs in your application.

* [get_app_input_configs](docs/sdks/apps/README.md#get_app_input_configs) - get app input configs
* [get_app_input_config](docs/sdks/apps/README.md#get_app_input_config) - get app input config
* [get_app_input_latest_config](docs/sdks/apps/README.md#get_app_input_latest_config) - get latest app input config
* [get_latest_app_break_glass_config](docs/sdks/apps/README.md#get_latest_app_break_glass_config) - get latest app input config
* [get_latest_app_permissions_config](docs/sdks/apps/README.md#get_latest_app_permissions_config) - get latest app permissions config
* [get_latest_app_policies_config](docs/sdks/apps/README.md#get_latest_app_policies_config) - get latest app policies config
* [get_latest_app_secrets_config](docs/sdks/apps/README.md#get_latest_app_secrets_config) - get latest app secrets config
* [get_app_latest_config](docs/sdks/apps/README.md#get_app_latest_config) - get latest app config
* [create_app_permissions_config](docs/sdks/apps/README.md#create_app_permissions_config) - Create app permissions config.

* [get_app_permissions_config](docs/sdks/apps/README.md#get_app_permissions_config) - get app permissions config
* [create_app_policies_config](docs/sdks/apps/README.md#create_app_policies_config) - Create app policies config.

* [get_app_policies_config](docs/sdks/apps/README.md#get_app_policies_config) - get app policies config
* [get_app_runner_configs](docs/sdks/apps/README.md#get_app_runner_configs) - get app runner configs
* [create_app_runner_config](docs/sdks/apps/README.md#create_app_runner_config) - create an app runner config
* [get_app_runner_latest_config](docs/sdks/apps/README.md#get_app_runner_latest_config) - get latest app runner config
* [create_app_sandbox_config](docs/sdks/apps/README.md#create_app_sandbox_config) - create an app sandbox config
* [get_app_sandbox_configs](docs/sdks/apps/README.md#get_app_sandbox_configs) - get app sandbox configs
* [get_app_sandbox_latest_config](docs/sdks/apps/README.md#get_app_sandbox_latest_config) - get latest app sandbox config
* [create_app_secret](docs/sdks/apps/README.md#create_app_secret) - create an app secret
* [delete_app_secret](docs/sdks/apps/README.md#delete_app_secret) - delete an app secret
* [get_app_secrets](docs/sdks/apps/README.md#get_app_secrets) - get app secrets
* [create_app_secrets_config](docs/sdks/apps/README.md#create_app_secrets_config) - Create an app secrets config.

* [get_app_secrets_config](docs/sdks/apps/README.md#get_app_secrets_config) - get app secrets config
* [create_app_stack_config](docs/sdks/apps/README.md#create_app_stack_config) - create an app stack config
* [get_app_stack_config](docs/sdks/apps/README.md#get_app_stack_config) - get app stack config
* [get_app_config_template](docs/sdks/apps/README.md#get_app_config_template) - get an app config template

### [components](docs/sdks/components/README.md)

* [get_app_component](docs/sdks/components/README.md#get_app_component) - get a components for a specific app
* [get_app_components](docs/sdks/components/README.md#get_app_components) - get all components for an app
* [create_component](docs/sdks/components/README.md#create_component) - create a component
* [get_component_builds](docs/sdks/components/README.md#get_component_builds) - get builds for components
* [get_org_components](docs/sdks/components/README.md#get_org_components) - get all components for an org
* [get_build](docs/sdks/components/README.md#get_build) - get a build
* [delete_component](docs/sdks/components/README.md#delete_component) - delete a component
* [get_component](docs/sdks/components/README.md#get_component) - get a component
* [update_component](docs/sdks/components/README.md#update_component) - update a component
* [create_component_build](docs/sdks/components/README.md#create_component_build) - create component build
* [get_component_latest_build](docs/sdks/components/README.md#get_component_latest_build) - get latest build for a component
* [get_component_build](docs/sdks/components/README.md#get_component_build) - get a build for a component
* [get_component_configs](docs/sdks/components/README.md#get_component_configs) - get all configs for a component
* [create_docker_build_component_config](docs/sdks/components/README.md#create_docker_build_component_config) - create a docker build component config
* [create_external_image_component_config](docs/sdks/components/README.md#create_external_image_component_config) - create an external image component config
* [create_helm_component_config](docs/sdks/components/README.md#create_helm_component_config) - create a helm component config
* [create_job_component_config](docs/sdks/components/README.md#create_job_component_config) - create a job component config
* [create_kubernetes_manifest_component_config](docs/sdks/components/README.md#create_kubernetes_manifest_component_config) - create a kubernetes manifest component config
* [get_component_latest_config](docs/sdks/components/README.md#get_component_latest_config) - get latest config for a component
* [create_terraform_module_component_config](docs/sdks/components/README.md#create_terraform_module_component_config) - create a terraform component config
* [get_component_config](docs/sdks/components/README.md#get_component_config) - get all configs for a component
* [get_component_dependencies](docs/sdks/components/README.md#get_component_dependencies) - get a component's dependencies
* [get_component_dependents](docs/sdks/components/README.md#get_component_dependents) - get a component's children

### [general](docs/sdks/general/README.md)

* [get_cli_config](docs/sdks/general/README.md#get_cli_config) - Get config for cli
* [get_cloud_platform_regions](docs/sdks/general/README.md#get_cloud_platform_regions) - Get regions for a cloud platform
* [get_config_schema](docs/sdks/general/README.md#get_config_schema) - Get jsonschema for config file
* [get_current_user](docs/sdks/general/README.md#get_current_user) - Get current user
* [create_waitlist](docs/sdks/general/README.md#create_waitlist) - Allow user to be added to an org waitlist.

### [installers](docs/sdks/installers/README.md)

* [render_installer](docs/sdks/installers/README.md#render_installer) - render an installer
* [get_installers](docs/sdks/installers/README.md#get_installers) - get installers for current org
* [create_installer](docs/sdks/installers/README.md#create_installer) - create an installer
* [delete_installer](docs/sdks/installers/README.md#delete_installer) - delete an installer
* [get_installer](docs/sdks/installers/README.md#get_installer) - get an installer
* [update_installer](docs/sdks/installers/README.md#update_installer) - update an installer

### [installs](docs/sdks/installs/README.md)

* [get_app_installs](docs/sdks/installs/README.md#get_app_installs) - get all installs for an app
* [create_install](docs/sdks/installs/README.md#create_install) - create an app install
* [get_install_workflow](docs/sdks/installs/README.md#get_install_workflow) - get an install workflow
* [update_install_workflow](docs/sdks/installs/README.md#update_install_workflow) - update an install workflow
* [cancel_install_workflow](docs/sdks/installs/README.md#cancel_install_workflow) - cancel an ongoing install workflow
* [get_install_workflow_steps](docs/sdks/installs/README.md#get_install_workflow_steps) - get an install workflow step
* [get_install_workflow_step](docs/sdks/installs/README.md#get_install_workflow_step) - get an install workflow step
* [get_install_workflow_step_approval](docs/sdks/installs/README.md#get_install_workflow_step_approval) - get an install workflow step approval
* [create_install_workflow_step_approval_response](docs/sdks/installs/README.md#create_install_workflow_step_approval_response) - deploy a build to an install
* [get_org_installs](docs/sdks/installs/README.md#get_org_installs) - get all installs for an org
* [get_install_sandbox_run](docs/sdks/installs/README.md#get_install_sandbox_run) - get an install sandbox run
* [get_install_stack](docs/sdks/installs/README.md#get_install_stack) - get an install stack by stack ID
* [delete_install](docs/sdks/installs/README.md#delete_install) - delete an install
* [get_install](docs/sdks/installs/README.md#get_install) - get an install
* [update_install](docs/sdks/installs/README.md#update_install) - update an install
* [get_install_action_workflows](docs/sdks/installs/README.md#get_install_action_workflows) - get an installs action workflows
* [get_install_action_workflow](docs/sdks/installs/README.md#get_install_action_workflow) - get an install action workflow
* [get_install_audit_logs](docs/sdks/installs/README.md#get_install_audit_logs) - get install audit logs
* [get_install_components](docs/sdks/installs/README.md#get_install_components) - get an installs components
* [deploy_install_components](docs/sdks/installs/README.md#deploy_install_components) - deploy all components on an install
* [get_install_components_summary](docs/sdks/installs/README.md#get_install_components_summary) - get an installs components summary
* [teardown_install_components](docs/sdks/installs/README.md#teardown_install_components) - teardown an install's components
* [get_install_component](docs/sdks/installs/README.md#get_install_component) - get an install component
* [get_install_component_deploys](docs/sdks/installs/README.md#get_install_component_deploys) - get an install components deploys
* [get_install_component_latest_deploy](docs/sdks/installs/README.md#get_install_component_latest_deploy) - get the latest deploy for an install component
* [get_install_component_outputs](docs/sdks/installs/README.md#get_install_component_outputs) - get an install component outputs
* [teardown_install_component](docs/sdks/installs/README.md#teardown_install_component) - teardown an install component
* [create_install_config](docs/sdks/installs/README.md#create_install_config) - create an install config
* [update_install_config](docs/sdks/installs/README.md#update_install_config) - create an install config
* [get_install_deploys](docs/sdks/installs/README.md#get_install_deploys) - get all deploys to an install
* [create_install_deploy](docs/sdks/installs/README.md#create_install_deploy) - deploy a build to an install
* [get_install_latest_deploy](docs/sdks/installs/README.md#get_install_latest_deploy) - get an install deploy
* [get_install_deploy](docs/sdks/installs/README.md#get_install_deploy) - get an install deploy
* [deprovision_install](docs/sdks/installs/README.md#deprovision_install) - deprovision an install
* [deprovision_install_sandbox](docs/sdks/installs/README.md#deprovision_install_sandbox) - deprovision an install
* [get_install_events](docs/sdks/installs/README.md#get_install_events) - get events for an install
* [get_install_event](docs/sdks/installs/README.md#get_install_event) - get an install event
* [forget_install](docs/sdks/installs/README.md#forget_install) - forget an install
* [get_install_inputs](docs/sdks/installs/README.md#get_install_inputs) - get an installs inputs
* [update_install_inputs](docs/sdks/installs/README.md#update_install_inputs) - Updates install input config for app
* [create_install_inputs](docs/sdks/installs/README.md#create_install_inputs) - create install inputs
* [get_current_install_inputs](docs/sdks/installs/README.md#get_current_install_inputs) - get an installs current inputs
* [phone_home](docs/sdks/installs/README.md#phone_home) - phone home for an install
* [get_install_readme](docs/sdks/installs/README.md#get_install_readme) - get install readme rendered with
* [reprovision_install](docs/sdks/installs/README.md#reprovision_install) - reprovision an install
* [reprovision_install_sandbox](docs/sdks/installs/README.md#reprovision_install_sandbox) - reprovision an install sandbox
* [~~retry_workflow~~](docs/sdks/installs/README.md#retry_workflow) - rerun the workflow steps starting from input step id, can be used to retry a failed step :warning: **Deprecated**
* [get_install_runner_group](docs/sdks/installs/README.md#get_install_runner_group) - Get an install's runner group
* [get_install_sandbox_runs](docs/sdks/installs/README.md#get_install_sandbox_runs) - get an installs sandbox runs
* [get_install_stack_by_install_id](docs/sdks/installs/README.md#get_install_stack_by_install_id) - get an install stack by install ID
* [get_install_stack_runs](docs/sdks/installs/README.md#get_install_stack_runs) - get an install's stack runs
* [get_install_state](docs/sdks/installs/README.md#get_install_state) - Get the current state of an install.
* [sync_secrets](docs/sdks/installs/README.md#sync_secrets) - sync secrets install
* [get_workflows](docs/sdks/installs/README.md#get_workflows) - get workflows
* [get_workflow](docs/sdks/installs/README.md#get_workflow) - get a workflow
* [update_workflow](docs/sdks/installs/README.md#update_workflow) - update a workflow
* [cancel_workflow](docs/sdks/installs/README.md#cancel_workflow) - cancel an ongoing workflow
* [retry_owner_workflow_by_id](docs/sdks/installs/README.md#retry_owner_workflow_by_id) - rerun the workflow steps starting from input step id, can be used to retry a failed step
* [get_workflow_steps](docs/sdks/installs/README.md#get_workflow_steps) - get a workflow step
* [get_workflow_step](docs/sdks/installs/README.md#get_workflow_step) - get a workflow step
* [get_workflow_step_approval](docs/sdks/installs/README.md#get_workflow_step_approval) - get an workflow step approval
* [get_workflow_step_approval_contents](docs/sdks/installs/README.md#get_workflow_step_approval_contents) - get a workflow step approval contents
* [create_workflow_step_approval_response](docs/sdks/installs/README.md#create_workflow_step_approval_response) - deploy a build to an install


### [orgs](docs/sdks/orgs/README.md)

* [get_orgs](docs/sdks/orgs/README.md#get_orgs) - Return current user's orgs
* [create_org](docs/sdks/orgs/README.md#create_org) - create a new org
* [delete_org](docs/sdks/orgs/README.md#delete_org) - Delete an org
* [get_org](docs/sdks/orgs/README.md#get_org) - Get an org
* [update_org](docs/sdks/orgs/README.md#update_org) - Update current org
* [get_org_acounts](docs/sdks/orgs/README.md#get_org_acounts) - Get user accounts for current org
* [get_org_invites](docs/sdks/orgs/README.md#get_org_invites) - Return org invites
* [create_org_invite](docs/sdks/orgs/README.md#create_org_invite) - Invite a user to the current org
* [remove_user](docs/sdks/orgs/README.md#remove_user) - Remove a user from the current org
* [get_org_runner_group](docs/sdks/orgs/README.md#get_org_runner_group) - Get an org's runner group
* [add_user](docs/sdks/orgs/README.md#add_user) - Add a user to the current org

### [releases](docs/sdks/releases/README.md)

* [get_app_releases](docs/sdks/releases/README.md#get_app_releases) - get all releases for an app
* [get_component_releases](docs/sdks/releases/README.md#get_component_releases) - get all releases for a component
* [create_component_release](docs/sdks/releases/README.md#create_component_release) - create a release
* [get_release](docs/sdks/releases/README.md#get_release) - get a release
* [get_release_steps](docs/sdks/releases/README.md#get_release_steps) - get a release

### [runners](docs/sdks/runners/README.md)

* [get_log_stream](docs/sdks/runners/README.md#get_log_stream) - get a log stream
* [log_stream_read_logs](docs/sdks/runners/README.md#log_stream_read_logs) - read a log stream's logs
* [get_runner_job](docs/sdks/runners/README.md#get_runner_job) - get runner job
* [cancel_runner_job](docs/sdks/runners/README.md#cancel_runner_job) - cancel runner job
* [get_runner_job_executions](docs/sdks/runners/README.md#get_runner_job_executions) - get runner job executions
* [get_runner_job_plan](docs/sdks/runners/README.md#get_runner_job_plan) - get runner job plan
* [get_terraform_workspace_states_json](docs/sdks/runners/README.md#get_terraform_workspace_states_json) - get terraform states json
* [get_terraform_workspace_states_json_by_id](docs/sdks/runners/README.md#get_terraform_workspace_states_json_by_id) - get terraform state json by id. This output is same as "terraform show --json"
* [get_terraform_workspace_state_json_resources](docs/sdks/runners/README.md#get_terraform_workspace_state_json_resources) - get terraform state resources. This output is similar to "terraform state list"
* [get_terraform_states](docs/sdks/runners/README.md#get_terraform_states) - get terraform states
* [get_terraform_workspace_state_by_id](docs/sdks/runners/README.md#get_terraform_workspace_state_by_id) - get terraform state by ID
* [get_terraform_workspace_state_resources](docs/sdks/runners/README.md#get_terraform_workspace_state_resources) - get terraform state resources
* [get_runner](docs/sdks/runners/README.md#get_runner) - get a runner
* [get_runner_connect_status](docs/sdks/runners/README.md#get_runner_connect_status) - get a runner connection satus based on heartbeat
* [force_shut_down_runner](docs/sdks/runners/README.md#force_shut_down_runner) - force shut down a runner
* [graceful_shut_down_runner](docs/sdks/runners/README.md#graceful_shut_down_runner) - shut down a runner
* [get_runner_jobs](docs/sdks/runners/README.md#get_runner_jobs) - get runner jobs
* [get_runner_latest_heart_beat](docs/sdks/runners/README.md#get_runner_latest_heart_beat) - get a runner
* [shut_down_runner_mng](docs/sdks/runners/README.md#shut_down_runner_mng) - shut down an install runner management process
* [mng_vm_shut_down](docs/sdks/runners/README.md#mng_vm_shut_down) - shut down an install runner VM
* [update_runner_mng](docs/sdks/runners/README.md#update_runner_mng) - shut down an install runner management process
* [get_runner_recent_health_checks](docs/sdks/runners/README.md#get_runner_recent_health_checks) - get recent health checks
* [get_runner_settings](docs/sdks/runners/README.md#get_runner_settings) - get runner settings
* [update_runner_settings](docs/sdks/runners/README.md#update_runner_settings) - update a runner job execution
* [get_terraform_current_state_data](docs/sdks/runners/README.md#get_terraform_current_state_data) - get current terraform
* [update_terraform_state](docs/sdks/runners/README.md#update_terraform_state) - update terraform state
* [create_terraform_workspace](docs/sdks/runners/README.md#create_terraform_workspace) - create terraform workspace
* [delete_terraform_workspace](docs/sdks/runners/README.md#delete_terraform_workspace) - delete terraform workspace
* [get_terraform_workspace](docs/sdks/runners/README.md#get_terraform_workspace) - get  terraform workspace
* [get_terraform_workspaces](docs/sdks/runners/README.md#get_terraform_workspaces) - get  terraform workspaces
* [get_terraform_workspace_lock](docs/sdks/runners/README.md#get_terraform_workspace_lock) - get terraform workspace lock
* [lock_terraform_workspace](docs/sdks/runners/README.md#lock_terraform_workspace) - lock terraform state
* [unlock_terraform_workspace](docs/sdks/runners/README.md#unlock_terraform_workspace) - unlock terraform workspace

### [runners_runner](docs/sdks/runnersrunner/README.md)

* [get_runner_job](docs/sdks/runnersrunner/README.md#get_runner_job) - get runner job
* [get_runner_job_executions](docs/sdks/runnersrunner/README.md#get_runner_job_executions) - get runner job executions
* [get_runner_job_plan](docs/sdks/runnersrunner/README.md#get_runner_job_plan) - get runner job plan
* [get_terraform_states](docs/sdks/runnersrunner/README.md#get_terraform_states) - get terraform states
* [get_terraform_workspace_state_by_id](docs/sdks/runnersrunner/README.md#get_terraform_workspace_state_by_id) - get terraform state by ID
* [get_terraform_workspace_state_resources](docs/sdks/runnersrunner/README.md#get_terraform_workspace_state_resources) - get terraform state resources
* [get_runner](docs/sdks/runnersrunner/README.md#get_runner) - get a runner
* [get_terraform_current_state_data](docs/sdks/runnersrunner/README.md#get_terraform_current_state_data) - get current terraform
* [update_terraform_state](docs/sdks/runnersrunner/README.md#update_terraform_state) - update terraform state
* [create_terraform_workspace](docs/sdks/runnersrunner/README.md#create_terraform_workspace) - create terraform workspace
* [delete_terraform_workspace](docs/sdks/runnersrunner/README.md#delete_terraform_workspace) - delete terraform workspace
* [get_terraform_workspace](docs/sdks/runnersrunner/README.md#get_terraform_workspace) - get  terraform workspace
* [get_terraform_workspaces](docs/sdks/runnersrunner/README.md#get_terraform_workspaces) - get  terraform workspaces
* [lock_terraform_workspace](docs/sdks/runnersrunner/README.md#lock_terraform_workspace) - lock terraform state
* [unlock_terraform_workspace](docs/sdks/runnersrunner/README.md#unlock_terraform_workspace) - unlock terraform workspace

### [vcs](docs/sdks/vcs/README.md)

* [create_vcs_connection_callback](docs/sdks/vcs/README.md#create_vcs_connection_callback) - public connection to create a vcs connection via a callback
* [get_org_vcs_connections](docs/sdks/vcs/README.md#get_org_vcs_connections) - get vcs connection for an org
* [create_vcs_connection](docs/sdks/vcs/README.md#create_vcs_connection) - create a vcs connection for Github
* [get_vcs_connection](docs/sdks/vcs/README.md#get_vcs_connection) - returns a vcs connection for an org

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from nuon import Nuon, models
from nuon.utils import BackoffStrategy, RetryConfig
import os


with Nuon() as n_client:

    res = n_client.actions.get_action_workflow_config(security=models.GetActionWorkflowConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), action_workflow_config_id="<id>",
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from nuon import Nuon, models
from nuon.utils import BackoffStrategy, RetryConfig
import os


with Nuon(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
) as n_client:

    res = n_client.actions.get_action_workflow_config(security=models.GetActionWorkflowConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), action_workflow_config_id="<id>")

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`NuonError`](./src/nuon/errors/nuonerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

### Example
```python
from nuon import Nuon, errors, models
import os


with Nuon() as n_client:
    res = None
    try:

        res = n_client.actions.get_action_workflow_config(security=models.GetActionWorkflowConfigSecurity(
            api_key=os.getenv("NUON_API_KEY", ""),
        ), action_workflow_config_id="<id>")

        # Handle response
        print(res)


    except errors.NuonError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, errors.StderrErrResponseError):
            print(e.data.description)  # Optional[str]
            print(e.data.error)  # Optional[str]
            print(e.data.user_error)  # Optional[bool]
```

### Error Classes
**Primary errors:**
* [`NuonError`](./src/nuon/errors/nuonerror.py): The base class for HTTP error responses.
  * [`StderrErrResponseError`](./src/nuon/errors/stderrerrresponseerror.py): Bad Request. *

<details><summary>Less common errors (5)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`NuonError`](./src/nuon/errors/nuonerror.py)**:
* [`ResponseValidationError`](./src/nuon/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](#available-resources-and-operations) to see if the error is applicable.
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from nuon import Nuon, models
import os


with Nuon(
    server_url="https://api.nuon.co/",
) as n_client:

    res = n_client.actions.get_action_workflow_config(security=models.GetActionWorkflowConfigSecurity(
        api_key=os.getenv("NUON_API_KEY", ""),
    ), action_workflow_config_id="<id>")

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from nuon import Nuon
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Nuon(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from nuon import Nuon
from nuon.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Nuon(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Nuon` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from nuon import Nuon
def main():

    with Nuon() as n_client:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Nuon() as n_client:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from nuon import Nuon
import logging

logging.basicConfig(level=logging.DEBUG)
s = Nuon(debug_logger=logging.getLogger("nuon"))
```

You can also enable a default debug logger by setting an environment variable `NUON_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=nuon&utm_campaign=python)
