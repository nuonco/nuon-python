from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_app_config_status import AppAppConfigStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_action_workflow_config import AppActionWorkflowConfig
    from ..models.app_app_branch import AppAppBranch
    from ..models.app_app_break_glass_config import AppAppBreakGlassConfig
    from ..models.app_app_input_config import AppAppInputConfig
    from ..models.app_app_permissions_config import AppAppPermissionsConfig
    from ..models.app_app_policies_config import AppAppPoliciesConfig
    from ..models.app_app_runner_config import AppAppRunnerConfig
    from ..models.app_app_sandbox_config import AppAppSandboxConfig
    from ..models.app_app_secrets_config import AppAppSecretsConfig
    from ..models.app_app_stack_config import AppAppStackConfig
    from ..models.app_component_config_connection import AppComponentConfigConnection
    from ..models.app_vcs_connection_commit import AppVCSConnectionCommit


T = TypeVar("T", bound="AppAppConfig")


@_attrs_define
class AppAppConfig:
    """
    Attributes:
        action_workflow_configs (Union[Unset, list['AppActionWorkflowConfig']]):
        app_branch (Union[Unset, AppAppBranch]):
        app_branch_id (Union[Unset, str]):
        app_id (Union[Unset, str]):
        break_glass (Union[Unset, AppAppBreakGlassConfig]):
        checksum (Union[Unset, str]):
        cli_version (Union[Unset, str]):
        component_config_connections (Union[Unset, list['AppComponentConfigConnection']]):
        component_ids (Union[Unset, list[str]]):
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        id (Union[Unset, str]):
        input_ (Union[Unset, AppAppInputConfig]):
        org_id (Union[Unset, str]):
        permissions (Union[Unset, AppAppPermissionsConfig]):
        policies (Union[Unset, AppAppPoliciesConfig]):
        readme (Union[Unset, str]):
        runner (Union[Unset, AppAppRunnerConfig]):
        sandbox (Union[Unset, AppAppSandboxConfig]):
        secrets (Union[Unset, AppAppSecretsConfig]):
        stack (Union[Unset, AppAppStackConfig]):
        state (Union[Unset, str]):
        status (Union[Unset, AppAppConfigStatus]):
        status_description (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        vcs_connection_commit (Union[Unset, AppVCSConnectionCommit]):
        version (Union[Unset, int]): fields that are filled in via after query or views
    """

    action_workflow_configs: Union[Unset, list["AppActionWorkflowConfig"]] = UNSET
    app_branch: Union[Unset, "AppAppBranch"] = UNSET
    app_branch_id: Union[Unset, str] = UNSET
    app_id: Union[Unset, str] = UNSET
    break_glass: Union[Unset, "AppAppBreakGlassConfig"] = UNSET
    checksum: Union[Unset, str] = UNSET
    cli_version: Union[Unset, str] = UNSET
    component_config_connections: Union[Unset, list["AppComponentConfigConnection"]] = UNSET
    component_ids: Union[Unset, list[str]] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    input_: Union[Unset, "AppAppInputConfig"] = UNSET
    org_id: Union[Unset, str] = UNSET
    permissions: Union[Unset, "AppAppPermissionsConfig"] = UNSET
    policies: Union[Unset, "AppAppPoliciesConfig"] = UNSET
    readme: Union[Unset, str] = UNSET
    runner: Union[Unset, "AppAppRunnerConfig"] = UNSET
    sandbox: Union[Unset, "AppAppSandboxConfig"] = UNSET
    secrets: Union[Unset, "AppAppSecretsConfig"] = UNSET
    stack: Union[Unset, "AppAppStackConfig"] = UNSET
    state: Union[Unset, str] = UNSET
    status: Union[Unset, AppAppConfigStatus] = UNSET
    status_description: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    vcs_connection_commit: Union[Unset, "AppVCSConnectionCommit"] = UNSET
    version: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_workflow_configs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.action_workflow_configs, Unset):
            action_workflow_configs = []
            for action_workflow_configs_item_data in self.action_workflow_configs:
                action_workflow_configs_item = action_workflow_configs_item_data.to_dict()
                action_workflow_configs.append(action_workflow_configs_item)

        app_branch: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.app_branch, Unset):
            app_branch = self.app_branch.to_dict()

        app_branch_id = self.app_branch_id

        app_id = self.app_id

        break_glass: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.break_glass, Unset):
            break_glass = self.break_glass.to_dict()

        checksum = self.checksum

        cli_version = self.cli_version

        component_config_connections: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.component_config_connections, Unset):
            component_config_connections = []
            for component_config_connections_item_data in self.component_config_connections:
                component_config_connections_item = component_config_connections_item_data.to_dict()
                component_config_connections.append(component_config_connections_item)

        component_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.component_ids, Unset):
            component_ids = self.component_ids

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        input_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.input_, Unset):
            input_ = self.input_.to_dict()

        org_id = self.org_id

        permissions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        policies: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.policies, Unset):
            policies = self.policies.to_dict()

        readme = self.readme

        runner: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.runner, Unset):
            runner = self.runner.to_dict()

        sandbox: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sandbox, Unset):
            sandbox = self.sandbox.to_dict()

        secrets: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.secrets, Unset):
            secrets = self.secrets.to_dict()

        stack: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.stack, Unset):
            stack = self.stack.to_dict()

        state = self.state

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        status_description = self.status_description

        updated_at = self.updated_at

        vcs_connection_commit: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vcs_connection_commit, Unset):
            vcs_connection_commit = self.vcs_connection_commit.to_dict()

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action_workflow_configs is not UNSET:
            field_dict["action_workflow_configs"] = action_workflow_configs
        if app_branch is not UNSET:
            field_dict["app_branch"] = app_branch
        if app_branch_id is not UNSET:
            field_dict["app_branch_id"] = app_branch_id
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if break_glass is not UNSET:
            field_dict["break_glass"] = break_glass
        if checksum is not UNSET:
            field_dict["checksum"] = checksum
        if cli_version is not UNSET:
            field_dict["cli_version"] = cli_version
        if component_config_connections is not UNSET:
            field_dict["component_config_connections"] = component_config_connections
        if component_ids is not UNSET:
            field_dict["component_ids"] = component_ids
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if input_ is not UNSET:
            field_dict["input"] = input_
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if policies is not UNSET:
            field_dict["policies"] = policies
        if readme is not UNSET:
            field_dict["readme"] = readme
        if runner is not UNSET:
            field_dict["runner"] = runner
        if sandbox is not UNSET:
            field_dict["sandbox"] = sandbox
        if secrets is not UNSET:
            field_dict["secrets"] = secrets
        if stack is not UNSET:
            field_dict["stack"] = stack
        if state is not UNSET:
            field_dict["state"] = state
        if status is not UNSET:
            field_dict["status"] = status
        if status_description is not UNSET:
            field_dict["status_description"] = status_description
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if vcs_connection_commit is not UNSET:
            field_dict["vcs_connection_commit"] = vcs_connection_commit
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_action_workflow_config import AppActionWorkflowConfig
        from ..models.app_app_branch import AppAppBranch
        from ..models.app_app_break_glass_config import AppAppBreakGlassConfig
        from ..models.app_app_input_config import AppAppInputConfig
        from ..models.app_app_permissions_config import AppAppPermissionsConfig
        from ..models.app_app_policies_config import AppAppPoliciesConfig
        from ..models.app_app_runner_config import AppAppRunnerConfig
        from ..models.app_app_sandbox_config import AppAppSandboxConfig
        from ..models.app_app_secrets_config import AppAppSecretsConfig
        from ..models.app_app_stack_config import AppAppStackConfig
        from ..models.app_component_config_connection import AppComponentConfigConnection
        from ..models.app_vcs_connection_commit import AppVCSConnectionCommit

        d = dict(src_dict)
        action_workflow_configs = []
        _action_workflow_configs = d.pop("action_workflow_configs", UNSET)
        for action_workflow_configs_item_data in _action_workflow_configs or []:
            action_workflow_configs_item = AppActionWorkflowConfig.from_dict(action_workflow_configs_item_data)

            action_workflow_configs.append(action_workflow_configs_item)

        _app_branch = d.pop("app_branch", UNSET)
        app_branch: Union[Unset, AppAppBranch]
        if isinstance(_app_branch, Unset):
            app_branch = UNSET
        else:
            app_branch = AppAppBranch.from_dict(_app_branch)

        app_branch_id = d.pop("app_branch_id", UNSET)

        app_id = d.pop("app_id", UNSET)

        _break_glass = d.pop("break_glass", UNSET)
        break_glass: Union[Unset, AppAppBreakGlassConfig]
        if isinstance(_break_glass, Unset):
            break_glass = UNSET
        else:
            break_glass = AppAppBreakGlassConfig.from_dict(_break_glass)

        checksum = d.pop("checksum", UNSET)

        cli_version = d.pop("cli_version", UNSET)

        component_config_connections = []
        _component_config_connections = d.pop("component_config_connections", UNSET)
        for component_config_connections_item_data in _component_config_connections or []:
            component_config_connections_item = AppComponentConfigConnection.from_dict(
                component_config_connections_item_data
            )

            component_config_connections.append(component_config_connections_item)

        component_ids = cast(list[str], d.pop("component_ids", UNSET))

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        _input_ = d.pop("input", UNSET)
        input_: Union[Unset, AppAppInputConfig]
        if isinstance(_input_, Unset):
            input_ = UNSET
        else:
            input_ = AppAppInputConfig.from_dict(_input_)

        org_id = d.pop("org_id", UNSET)

        _permissions = d.pop("permissions", UNSET)
        permissions: Union[Unset, AppAppPermissionsConfig]
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = AppAppPermissionsConfig.from_dict(_permissions)

        _policies = d.pop("policies", UNSET)
        policies: Union[Unset, AppAppPoliciesConfig]
        if isinstance(_policies, Unset):
            policies = UNSET
        else:
            policies = AppAppPoliciesConfig.from_dict(_policies)

        readme = d.pop("readme", UNSET)

        _runner = d.pop("runner", UNSET)
        runner: Union[Unset, AppAppRunnerConfig]
        if isinstance(_runner, Unset):
            runner = UNSET
        else:
            runner = AppAppRunnerConfig.from_dict(_runner)

        _sandbox = d.pop("sandbox", UNSET)
        sandbox: Union[Unset, AppAppSandboxConfig]
        if isinstance(_sandbox, Unset):
            sandbox = UNSET
        else:
            sandbox = AppAppSandboxConfig.from_dict(_sandbox)

        _secrets = d.pop("secrets", UNSET)
        secrets: Union[Unset, AppAppSecretsConfig]
        if isinstance(_secrets, Unset):
            secrets = UNSET
        else:
            secrets = AppAppSecretsConfig.from_dict(_secrets)

        _stack = d.pop("stack", UNSET)
        stack: Union[Unset, AppAppStackConfig]
        if isinstance(_stack, Unset):
            stack = UNSET
        else:
            stack = AppAppStackConfig.from_dict(_stack)

        state = d.pop("state", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, AppAppConfigStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppAppConfigStatus(_status)

        status_description = d.pop("status_description", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _vcs_connection_commit = d.pop("vcs_connection_commit", UNSET)
        vcs_connection_commit: Union[Unset, AppVCSConnectionCommit]
        if isinstance(_vcs_connection_commit, Unset):
            vcs_connection_commit = UNSET
        else:
            vcs_connection_commit = AppVCSConnectionCommit.from_dict(_vcs_connection_commit)

        version = d.pop("version", UNSET)

        app_app_config = cls(
            action_workflow_configs=action_workflow_configs,
            app_branch=app_branch,
            app_branch_id=app_branch_id,
            app_id=app_id,
            break_glass=break_glass,
            checksum=checksum,
            cli_version=cli_version,
            component_config_connections=component_config_connections,
            component_ids=component_ids,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            input_=input_,
            org_id=org_id,
            permissions=permissions,
            policies=policies,
            readme=readme,
            runner=runner,
            sandbox=sandbox,
            secrets=secrets,
            stack=stack,
            state=state,
            status=status,
            status_description=status_description,
            updated_at=updated_at,
            vcs_connection_commit=vcs_connection_commit,
            version=version,
        )

        app_app_config.additional_properties = d
        return app_app_config

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
