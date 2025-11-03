from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_app_runner_config import AppAppRunnerConfig
    from ..models.app_app_sandbox_config import AppAppSandboxConfig
    from ..models.app_aws_account import AppAWSAccount
    from ..models.app_azure_account import AppAzureAccount
    from ..models.app_drifted_object import AppDriftedObject
    from ..models.app_install_action_workflow import AppInstallActionWorkflow
    from ..models.app_install_component import AppInstallComponent
    from ..models.app_install_component_statuses import AppInstallComponentStatuses
    from ..models.app_install_config import AppInstallConfig
    from ..models.app_install_event import AppInstallEvent
    from ..models.app_install_inputs import AppInstallInputs
    from ..models.app_install_links import AppInstallLinks
    from ..models.app_install_metadata import AppInstallMetadata
    from ..models.app_install_sandbox import AppInstallSandbox
    from ..models.app_install_sandbox_run import AppInstallSandboxRun
    from ..models.app_install_stack import AppInstallStack
    from ..models.app_install_state import AppInstallState
    from ..models.app_workflow import AppWorkflow


T = TypeVar("T", bound="AppInstall")


@_attrs_define
class AppInstall:
    """
    Attributes:
        app_config_id (str | Unset):
        app_id (str | Unset):
        app_runner_config (AppAppRunnerConfig | Unset):
        app_sandbox_config (AppAppSandboxConfig | Unset):
        aws_account (AppAWSAccount | Unset):
        azure_account (AppAzureAccount | Unset):
        cloud_platform (str | Unset):
        component_statuses (AppInstallComponentStatuses | Unset):
        composite_component_status (str | Unset):
        composite_component_status_description (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        drifted_objects (list[AppDriftedObject] | Unset):
        id (str | Unset):
        install_action_workflows (list[AppInstallActionWorkflow] | Unset):
        install_components (list[AppInstallComponent] | Unset):
        install_config (AppInstallConfig | Unset):
        install_events (list[AppInstallEvent] | Unset):
        install_inputs (list[AppInstallInputs] | Unset):
        install_number (int | Unset):
        install_sandbox_runs (list[AppInstallSandboxRun] | Unset):
        install_stack (AppInstallStack | Unset):
        install_states (list[AppInstallState] | Unset):
        links (AppInstallLinks | Unset):
        metadata (AppInstallMetadata | Unset):
        name (str | Unset):
        runner_id (str | Unset):
        runner_status (str | Unset):
        runner_status_description (str | Unset):
        runner_type (str | Unset):
        sandbox (AppInstallSandbox | Unset):
        sandbox_status (str | Unset):
        sandbox_status_description (str | Unset):
        status (str | Unset): TODO(jm): deprecate these fields once the terraform provider has been updated
        status_description (str | Unset):
        updated_at (str | Unset):
        workflows (list[AppWorkflow] | Unset):
    """

    app_config_id: str | Unset = UNSET
    app_id: str | Unset = UNSET
    app_runner_config: AppAppRunnerConfig | Unset = UNSET
    app_sandbox_config: AppAppSandboxConfig | Unset = UNSET
    aws_account: AppAWSAccount | Unset = UNSET
    azure_account: AppAzureAccount | Unset = UNSET
    cloud_platform: str | Unset = UNSET
    component_statuses: AppInstallComponentStatuses | Unset = UNSET
    composite_component_status: str | Unset = UNSET
    composite_component_status_description: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    drifted_objects: list[AppDriftedObject] | Unset = UNSET
    id: str | Unset = UNSET
    install_action_workflows: list[AppInstallActionWorkflow] | Unset = UNSET
    install_components: list[AppInstallComponent] | Unset = UNSET
    install_config: AppInstallConfig | Unset = UNSET
    install_events: list[AppInstallEvent] | Unset = UNSET
    install_inputs: list[AppInstallInputs] | Unset = UNSET
    install_number: int | Unset = UNSET
    install_sandbox_runs: list[AppInstallSandboxRun] | Unset = UNSET
    install_stack: AppInstallStack | Unset = UNSET
    install_states: list[AppInstallState] | Unset = UNSET
    links: AppInstallLinks | Unset = UNSET
    metadata: AppInstallMetadata | Unset = UNSET
    name: str | Unset = UNSET
    runner_id: str | Unset = UNSET
    runner_status: str | Unset = UNSET
    runner_status_description: str | Unset = UNSET
    runner_type: str | Unset = UNSET
    sandbox: AppInstallSandbox | Unset = UNSET
    sandbox_status: str | Unset = UNSET
    sandbox_status_description: str | Unset = UNSET
    status: str | Unset = UNSET
    status_description: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    workflows: list[AppWorkflow] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config_id = self.app_config_id

        app_id = self.app_id

        app_runner_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.app_runner_config, Unset):
            app_runner_config = self.app_runner_config.to_dict()

        app_sandbox_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.app_sandbox_config, Unset):
            app_sandbox_config = self.app_sandbox_config.to_dict()

        aws_account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aws_account, Unset):
            aws_account = self.aws_account.to_dict()

        azure_account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.azure_account, Unset):
            azure_account = self.azure_account.to_dict()

        cloud_platform = self.cloud_platform

        component_statuses: dict[str, Any] | Unset = UNSET
        if not isinstance(self.component_statuses, Unset):
            component_statuses = self.component_statuses.to_dict()

        composite_component_status = self.composite_component_status

        composite_component_status_description = self.composite_component_status_description

        created_at = self.created_at

        created_by_id = self.created_by_id

        drifted_objects: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.drifted_objects, Unset):
            drifted_objects = []
            for drifted_objects_item_data in self.drifted_objects:
                drifted_objects_item = drifted_objects_item_data.to_dict()
                drifted_objects.append(drifted_objects_item)

        id = self.id

        install_action_workflows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.install_action_workflows, Unset):
            install_action_workflows = []
            for install_action_workflows_item_data in self.install_action_workflows:
                install_action_workflows_item = install_action_workflows_item_data.to_dict()
                install_action_workflows.append(install_action_workflows_item)

        install_components: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.install_components, Unset):
            install_components = []
            for install_components_item_data in self.install_components:
                install_components_item = install_components_item_data.to_dict()
                install_components.append(install_components_item)

        install_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.install_config, Unset):
            install_config = self.install_config.to_dict()

        install_events: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.install_events, Unset):
            install_events = []
            for install_events_item_data in self.install_events:
                install_events_item = install_events_item_data.to_dict()
                install_events.append(install_events_item)

        install_inputs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.install_inputs, Unset):
            install_inputs = []
            for install_inputs_item_data in self.install_inputs:
                install_inputs_item = install_inputs_item_data.to_dict()
                install_inputs.append(install_inputs_item)

        install_number = self.install_number

        install_sandbox_runs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.install_sandbox_runs, Unset):
            install_sandbox_runs = []
            for install_sandbox_runs_item_data in self.install_sandbox_runs:
                install_sandbox_runs_item = install_sandbox_runs_item_data.to_dict()
                install_sandbox_runs.append(install_sandbox_runs_item)

        install_stack: dict[str, Any] | Unset = UNSET
        if not isinstance(self.install_stack, Unset):
            install_stack = self.install_stack.to_dict()

        install_states: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.install_states, Unset):
            install_states = []
            for install_states_item_data in self.install_states:
                install_states_item = install_states_item_data.to_dict()
                install_states.append(install_states_item)

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        name = self.name

        runner_id = self.runner_id

        runner_status = self.runner_status

        runner_status_description = self.runner_status_description

        runner_type = self.runner_type

        sandbox: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sandbox, Unset):
            sandbox = self.sandbox.to_dict()

        sandbox_status = self.sandbox_status

        sandbox_status_description = self.sandbox_status_description

        status = self.status

        status_description = self.status_description

        updated_at = self.updated_at

        workflows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.workflows, Unset):
            workflows = []
            for workflows_item_data in self.workflows:
                workflows_item = workflows_item_data.to_dict()
                workflows.append(workflows_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if app_runner_config is not UNSET:
            field_dict["app_runner_config"] = app_runner_config
        if app_sandbox_config is not UNSET:
            field_dict["app_sandbox_config"] = app_sandbox_config
        if aws_account is not UNSET:
            field_dict["aws_account"] = aws_account
        if azure_account is not UNSET:
            field_dict["azure_account"] = azure_account
        if cloud_platform is not UNSET:
            field_dict["cloud_platform"] = cloud_platform
        if component_statuses is not UNSET:
            field_dict["component_statuses"] = component_statuses
        if composite_component_status is not UNSET:
            field_dict["composite_component_status"] = composite_component_status
        if composite_component_status_description is not UNSET:
            field_dict["composite_component_status_description"] = composite_component_status_description
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if drifted_objects is not UNSET:
            field_dict["drifted_objects"] = drifted_objects
        if id is not UNSET:
            field_dict["id"] = id
        if install_action_workflows is not UNSET:
            field_dict["install_action_workflows"] = install_action_workflows
        if install_components is not UNSET:
            field_dict["install_components"] = install_components
        if install_config is not UNSET:
            field_dict["install_config"] = install_config
        if install_events is not UNSET:
            field_dict["install_events"] = install_events
        if install_inputs is not UNSET:
            field_dict["install_inputs"] = install_inputs
        if install_number is not UNSET:
            field_dict["install_number"] = install_number
        if install_sandbox_runs is not UNSET:
            field_dict["install_sandbox_runs"] = install_sandbox_runs
        if install_stack is not UNSET:
            field_dict["install_stack"] = install_stack
        if install_states is not UNSET:
            field_dict["install_states"] = install_states
        if links is not UNSET:
            field_dict["links"] = links
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name
        if runner_id is not UNSET:
            field_dict["runner_id"] = runner_id
        if runner_status is not UNSET:
            field_dict["runner_status"] = runner_status
        if runner_status_description is not UNSET:
            field_dict["runner_status_description"] = runner_status_description
        if runner_type is not UNSET:
            field_dict["runner_type"] = runner_type
        if sandbox is not UNSET:
            field_dict["sandbox"] = sandbox
        if sandbox_status is not UNSET:
            field_dict["sandbox_status"] = sandbox_status
        if sandbox_status_description is not UNSET:
            field_dict["sandbox_status_description"] = sandbox_status_description
        if status is not UNSET:
            field_dict["status"] = status
        if status_description is not UNSET:
            field_dict["status_description"] = status_description
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if workflows is not UNSET:
            field_dict["workflows"] = workflows

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_app_runner_config import AppAppRunnerConfig
        from ..models.app_app_sandbox_config import AppAppSandboxConfig
        from ..models.app_aws_account import AppAWSAccount
        from ..models.app_azure_account import AppAzureAccount
        from ..models.app_drifted_object import AppDriftedObject
        from ..models.app_install_action_workflow import AppInstallActionWorkflow
        from ..models.app_install_component import AppInstallComponent
        from ..models.app_install_component_statuses import AppInstallComponentStatuses
        from ..models.app_install_config import AppInstallConfig
        from ..models.app_install_event import AppInstallEvent
        from ..models.app_install_inputs import AppInstallInputs
        from ..models.app_install_links import AppInstallLinks
        from ..models.app_install_metadata import AppInstallMetadata
        from ..models.app_install_sandbox import AppInstallSandbox
        from ..models.app_install_sandbox_run import AppInstallSandboxRun
        from ..models.app_install_stack import AppInstallStack
        from ..models.app_install_state import AppInstallState
        from ..models.app_workflow import AppWorkflow

        d = dict(src_dict)
        app_config_id = d.pop("app_config_id", UNSET)

        app_id = d.pop("app_id", UNSET)

        _app_runner_config = d.pop("app_runner_config", UNSET)
        app_runner_config: AppAppRunnerConfig | Unset
        if isinstance(_app_runner_config, Unset):
            app_runner_config = UNSET
        else:
            app_runner_config = AppAppRunnerConfig.from_dict(_app_runner_config)

        _app_sandbox_config = d.pop("app_sandbox_config", UNSET)
        app_sandbox_config: AppAppSandboxConfig | Unset
        if isinstance(_app_sandbox_config, Unset):
            app_sandbox_config = UNSET
        else:
            app_sandbox_config = AppAppSandboxConfig.from_dict(_app_sandbox_config)

        _aws_account = d.pop("aws_account", UNSET)
        aws_account: AppAWSAccount | Unset
        if isinstance(_aws_account, Unset):
            aws_account = UNSET
        else:
            aws_account = AppAWSAccount.from_dict(_aws_account)

        _azure_account = d.pop("azure_account", UNSET)
        azure_account: AppAzureAccount | Unset
        if isinstance(_azure_account, Unset):
            azure_account = UNSET
        else:
            azure_account = AppAzureAccount.from_dict(_azure_account)

        cloud_platform = d.pop("cloud_platform", UNSET)

        _component_statuses = d.pop("component_statuses", UNSET)
        component_statuses: AppInstallComponentStatuses | Unset
        if isinstance(_component_statuses, Unset):
            component_statuses = UNSET
        else:
            component_statuses = AppInstallComponentStatuses.from_dict(_component_statuses)

        composite_component_status = d.pop("composite_component_status", UNSET)

        composite_component_status_description = d.pop("composite_component_status_description", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        _drifted_objects = d.pop("drifted_objects", UNSET)
        drifted_objects: list[AppDriftedObject] | Unset = UNSET
        if _drifted_objects is not UNSET:
            drifted_objects = []
            for drifted_objects_item_data in _drifted_objects:
                drifted_objects_item = AppDriftedObject.from_dict(drifted_objects_item_data)

                drifted_objects.append(drifted_objects_item)

        id = d.pop("id", UNSET)

        _install_action_workflows = d.pop("install_action_workflows", UNSET)
        install_action_workflows: list[AppInstallActionWorkflow] | Unset = UNSET
        if _install_action_workflows is not UNSET:
            install_action_workflows = []
            for install_action_workflows_item_data in _install_action_workflows:
                install_action_workflows_item = AppInstallActionWorkflow.from_dict(install_action_workflows_item_data)

                install_action_workflows.append(install_action_workflows_item)

        _install_components = d.pop("install_components", UNSET)
        install_components: list[AppInstallComponent] | Unset = UNSET
        if _install_components is not UNSET:
            install_components = []
            for install_components_item_data in _install_components:
                install_components_item = AppInstallComponent.from_dict(install_components_item_data)

                install_components.append(install_components_item)

        _install_config = d.pop("install_config", UNSET)
        install_config: AppInstallConfig | Unset
        if isinstance(_install_config, Unset):
            install_config = UNSET
        else:
            install_config = AppInstallConfig.from_dict(_install_config)

        _install_events = d.pop("install_events", UNSET)
        install_events: list[AppInstallEvent] | Unset = UNSET
        if _install_events is not UNSET:
            install_events = []
            for install_events_item_data in _install_events:
                install_events_item = AppInstallEvent.from_dict(install_events_item_data)

                install_events.append(install_events_item)

        _install_inputs = d.pop("install_inputs", UNSET)
        install_inputs: list[AppInstallInputs] | Unset = UNSET
        if _install_inputs is not UNSET:
            install_inputs = []
            for install_inputs_item_data in _install_inputs:
                install_inputs_item = AppInstallInputs.from_dict(install_inputs_item_data)

                install_inputs.append(install_inputs_item)

        install_number = d.pop("install_number", UNSET)

        _install_sandbox_runs = d.pop("install_sandbox_runs", UNSET)
        install_sandbox_runs: list[AppInstallSandboxRun] | Unset = UNSET
        if _install_sandbox_runs is not UNSET:
            install_sandbox_runs = []
            for install_sandbox_runs_item_data in _install_sandbox_runs:
                install_sandbox_runs_item = AppInstallSandboxRun.from_dict(install_sandbox_runs_item_data)

                install_sandbox_runs.append(install_sandbox_runs_item)

        _install_stack = d.pop("install_stack", UNSET)
        install_stack: AppInstallStack | Unset
        if isinstance(_install_stack, Unset):
            install_stack = UNSET
        else:
            install_stack = AppInstallStack.from_dict(_install_stack)

        _install_states = d.pop("install_states", UNSET)
        install_states: list[AppInstallState] | Unset = UNSET
        if _install_states is not UNSET:
            install_states = []
            for install_states_item_data in _install_states:
                install_states_item = AppInstallState.from_dict(install_states_item_data)

                install_states.append(install_states_item)

        _links = d.pop("links", UNSET)
        links: AppInstallLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = AppInstallLinks.from_dict(_links)

        _metadata = d.pop("metadata", UNSET)
        metadata: AppInstallMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = AppInstallMetadata.from_dict(_metadata)

        name = d.pop("name", UNSET)

        runner_id = d.pop("runner_id", UNSET)

        runner_status = d.pop("runner_status", UNSET)

        runner_status_description = d.pop("runner_status_description", UNSET)

        runner_type = d.pop("runner_type", UNSET)

        _sandbox = d.pop("sandbox", UNSET)
        sandbox: AppInstallSandbox | Unset
        if isinstance(_sandbox, Unset):
            sandbox = UNSET
        else:
            sandbox = AppInstallSandbox.from_dict(_sandbox)

        sandbox_status = d.pop("sandbox_status", UNSET)

        sandbox_status_description = d.pop("sandbox_status_description", UNSET)

        status = d.pop("status", UNSET)

        status_description = d.pop("status_description", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _workflows = d.pop("workflows", UNSET)
        workflows: list[AppWorkflow] | Unset = UNSET
        if _workflows is not UNSET:
            workflows = []
            for workflows_item_data in _workflows:
                workflows_item = AppWorkflow.from_dict(workflows_item_data)

                workflows.append(workflows_item)

        app_install = cls(
            app_config_id=app_config_id,
            app_id=app_id,
            app_runner_config=app_runner_config,
            app_sandbox_config=app_sandbox_config,
            aws_account=aws_account,
            azure_account=azure_account,
            cloud_platform=cloud_platform,
            component_statuses=component_statuses,
            composite_component_status=composite_component_status,
            composite_component_status_description=composite_component_status_description,
            created_at=created_at,
            created_by_id=created_by_id,
            drifted_objects=drifted_objects,
            id=id,
            install_action_workflows=install_action_workflows,
            install_components=install_components,
            install_config=install_config,
            install_events=install_events,
            install_inputs=install_inputs,
            install_number=install_number,
            install_sandbox_runs=install_sandbox_runs,
            install_stack=install_stack,
            install_states=install_states,
            links=links,
            metadata=metadata,
            name=name,
            runner_id=runner_id,
            runner_status=runner_status,
            runner_status_description=runner_status_description,
            runner_type=runner_type,
            sandbox=sandbox,
            sandbox_status=sandbox_status,
            sandbox_status_description=sandbox_status_description,
            status=status,
            status_description=status_description,
            updated_at=updated_at,
            workflows=workflows,
        )

        app_install.additional_properties = d
        return app_install

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
