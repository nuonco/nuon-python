from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_app_config_status import AppAppConfigStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_action_workflow_config import AppActionWorkflowConfig
    from ..models.app_app_branch import AppAppBranch
    from ..models.app_app_break_glass_config import AppAppBreakGlassConfig
    from ..models.app_app_input_config import AppAppInputConfig
    from ..models.app_app_operation_role_config import AppAppOperationRoleConfig
    from ..models.app_app_permissions_config import AppAppPermissionsConfig
    from ..models.app_app_policies_config import AppAppPoliciesConfig
    from ..models.app_app_runner_config import AppAppRunnerConfig
    from ..models.app_app_sandbox_config import AppAppSandboxConfig
    from ..models.app_app_secrets_config import AppAppSecretsConfig
    from ..models.app_app_stack_config import AppAppStackConfig
    from ..models.app_component_config_connection import AppComponentConfigConnection
    from ..models.app_composite_status import AppCompositeStatus
    from ..models.app_vcs_connection_commit import AppVCSConnectionCommit
    from ..models.blobstore_blob import BlobstoreBlob


T = TypeVar("T", bound="AppAppConfig")


@_attrs_define
class AppAppConfig:
    """
    Attributes:
        action_ids (list[str] | Unset):
        action_workflow_configs (list[AppActionWorkflowConfig] | Unset):
        app_branch (AppAppBranch | Unset):
        app_branch_id (str | Unset):
        app_id (str | Unset):
        break_glass (AppAppBreakGlassConfig | Unset):
        checksum (str | Unset):
        cli_version (str | Unset):
        component_config_connections (list[AppComponentConfigConnection] | Unset):
        component_ids (list[str] | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        input_ (AppAppInputConfig | Unset):
        intermediate_config (BlobstoreBlob | Unset):
        operation_role_config (AppAppOperationRoleConfig | Unset):
        org_id (str | Unset):
        permissions (AppAppPermissionsConfig | Unset):
        policies (AppAppPoliciesConfig | Unset):
        readme (str | Unset):
        runner (AppAppRunnerConfig | Unset):
        sandbox (AppAppSandboxConfig | Unset):
        secrets (AppAppSecretsConfig | Unset):
        stack (AppAppStackConfig | Unset):
        state (str | Unset):
        status (AppAppConfigStatus | Unset):
        status_description (str | Unset):
        status_v2 (AppCompositeStatus | Unset):
        updated_at (str | Unset):
        vcs_connection_commit (AppVCSConnectionCommit | Unset):
        version (int | Unset): fields that are filled in via after query or views
    """

    action_ids: list[str] | Unset = UNSET
    action_workflow_configs: list[AppActionWorkflowConfig] | Unset = UNSET
    app_branch: AppAppBranch | Unset = UNSET
    app_branch_id: str | Unset = UNSET
    app_id: str | Unset = UNSET
    break_glass: AppAppBreakGlassConfig | Unset = UNSET
    checksum: str | Unset = UNSET
    cli_version: str | Unset = UNSET
    component_config_connections: list[AppComponentConfigConnection] | Unset = UNSET
    component_ids: list[str] | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    input_: AppAppInputConfig | Unset = UNSET
    intermediate_config: BlobstoreBlob | Unset = UNSET
    operation_role_config: AppAppOperationRoleConfig | Unset = UNSET
    org_id: str | Unset = UNSET
    permissions: AppAppPermissionsConfig | Unset = UNSET
    policies: AppAppPoliciesConfig | Unset = UNSET
    readme: str | Unset = UNSET
    runner: AppAppRunnerConfig | Unset = UNSET
    sandbox: AppAppSandboxConfig | Unset = UNSET
    secrets: AppAppSecretsConfig | Unset = UNSET
    stack: AppAppStackConfig | Unset = UNSET
    state: str | Unset = UNSET
    status: AppAppConfigStatus | Unset = UNSET
    status_description: str | Unset = UNSET
    status_v2: AppCompositeStatus | Unset = UNSET
    updated_at: str | Unset = UNSET
    vcs_connection_commit: AppVCSConnectionCommit | Unset = UNSET
    version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_ids: list[str] | Unset = UNSET
        if not isinstance(self.action_ids, Unset):
            action_ids = self.action_ids

        action_workflow_configs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.action_workflow_configs, Unset):
            action_workflow_configs = []
            for action_workflow_configs_item_data in self.action_workflow_configs:
                action_workflow_configs_item = action_workflow_configs_item_data.to_dict()
                action_workflow_configs.append(action_workflow_configs_item)

        app_branch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.app_branch, Unset):
            app_branch = self.app_branch.to_dict()

        app_branch_id = self.app_branch_id

        app_id = self.app_id

        break_glass: dict[str, Any] | Unset = UNSET
        if not isinstance(self.break_glass, Unset):
            break_glass = self.break_glass.to_dict()

        checksum = self.checksum

        cli_version = self.cli_version

        component_config_connections: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.component_config_connections, Unset):
            component_config_connections = []
            for component_config_connections_item_data in self.component_config_connections:
                component_config_connections_item = component_config_connections_item_data.to_dict()
                component_config_connections.append(component_config_connections_item)

        component_ids: list[str] | Unset = UNSET
        if not isinstance(self.component_ids, Unset):
            component_ids = self.component_ids

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        input_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_, Unset):
            input_ = self.input_.to_dict()

        intermediate_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.intermediate_config, Unset):
            intermediate_config = self.intermediate_config.to_dict()

        operation_role_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.operation_role_config, Unset):
            operation_role_config = self.operation_role_config.to_dict()

        org_id = self.org_id

        permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        policies: dict[str, Any] | Unset = UNSET
        if not isinstance(self.policies, Unset):
            policies = self.policies.to_dict()

        readme = self.readme

        runner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.runner, Unset):
            runner = self.runner.to_dict()

        sandbox: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sandbox, Unset):
            sandbox = self.sandbox.to_dict()

        secrets: dict[str, Any] | Unset = UNSET
        if not isinstance(self.secrets, Unset):
            secrets = self.secrets.to_dict()

        stack: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stack, Unset):
            stack = self.stack.to_dict()

        state = self.state

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        status_description = self.status_description

        status_v2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status_v2, Unset):
            status_v2 = self.status_v2.to_dict()

        updated_at = self.updated_at

        vcs_connection_commit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vcs_connection_commit, Unset):
            vcs_connection_commit = self.vcs_connection_commit.to_dict()

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action_ids is not UNSET:
            field_dict["action_ids"] = action_ids
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
        if intermediate_config is not UNSET:
            field_dict["intermediate_config"] = intermediate_config
        if operation_role_config is not UNSET:
            field_dict["operation_role_config"] = operation_role_config
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
        if status_v2 is not UNSET:
            field_dict["status_v2"] = status_v2
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
        from ..models.app_app_operation_role_config import AppAppOperationRoleConfig
        from ..models.app_app_permissions_config import AppAppPermissionsConfig
        from ..models.app_app_policies_config import AppAppPoliciesConfig
        from ..models.app_app_runner_config import AppAppRunnerConfig
        from ..models.app_app_sandbox_config import AppAppSandboxConfig
        from ..models.app_app_secrets_config import AppAppSecretsConfig
        from ..models.app_app_stack_config import AppAppStackConfig
        from ..models.app_component_config_connection import AppComponentConfigConnection
        from ..models.app_composite_status import AppCompositeStatus
        from ..models.app_vcs_connection_commit import AppVCSConnectionCommit
        from ..models.blobstore_blob import BlobstoreBlob

        d = dict(src_dict)
        action_ids = cast(list[str], d.pop("action_ids", UNSET))

        _action_workflow_configs = d.pop("action_workflow_configs", UNSET)
        action_workflow_configs: list[AppActionWorkflowConfig] | Unset = UNSET
        if _action_workflow_configs is not UNSET:
            action_workflow_configs = []
            for action_workflow_configs_item_data in _action_workflow_configs:
                action_workflow_configs_item = AppActionWorkflowConfig.from_dict(action_workflow_configs_item_data)

                action_workflow_configs.append(action_workflow_configs_item)

        _app_branch = d.pop("app_branch", UNSET)
        app_branch: AppAppBranch | Unset
        if isinstance(_app_branch, Unset):
            app_branch = UNSET
        else:
            app_branch = AppAppBranch.from_dict(_app_branch)

        app_branch_id = d.pop("app_branch_id", UNSET)

        app_id = d.pop("app_id", UNSET)

        _break_glass = d.pop("break_glass", UNSET)
        break_glass: AppAppBreakGlassConfig | Unset
        if isinstance(_break_glass, Unset):
            break_glass = UNSET
        else:
            break_glass = AppAppBreakGlassConfig.from_dict(_break_glass)

        checksum = d.pop("checksum", UNSET)

        cli_version = d.pop("cli_version", UNSET)

        _component_config_connections = d.pop("component_config_connections", UNSET)
        component_config_connections: list[AppComponentConfigConnection] | Unset = UNSET
        if _component_config_connections is not UNSET:
            component_config_connections = []
            for component_config_connections_item_data in _component_config_connections:
                component_config_connections_item = AppComponentConfigConnection.from_dict(
                    component_config_connections_item_data
                )

                component_config_connections.append(component_config_connections_item)

        component_ids = cast(list[str], d.pop("component_ids", UNSET))

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        _input_ = d.pop("input", UNSET)
        input_: AppAppInputConfig | Unset
        if isinstance(_input_, Unset):
            input_ = UNSET
        else:
            input_ = AppAppInputConfig.from_dict(_input_)

        _intermediate_config = d.pop("intermediate_config", UNSET)
        intermediate_config: BlobstoreBlob | Unset
        if isinstance(_intermediate_config, Unset):
            intermediate_config = UNSET
        else:
            intermediate_config = BlobstoreBlob.from_dict(_intermediate_config)

        _operation_role_config = d.pop("operation_role_config", UNSET)
        operation_role_config: AppAppOperationRoleConfig | Unset
        if isinstance(_operation_role_config, Unset):
            operation_role_config = UNSET
        else:
            operation_role_config = AppAppOperationRoleConfig.from_dict(_operation_role_config)

        org_id = d.pop("org_id", UNSET)

        _permissions = d.pop("permissions", UNSET)
        permissions: AppAppPermissionsConfig | Unset
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = AppAppPermissionsConfig.from_dict(_permissions)

        _policies = d.pop("policies", UNSET)
        policies: AppAppPoliciesConfig | Unset
        if isinstance(_policies, Unset):
            policies = UNSET
        else:
            policies = AppAppPoliciesConfig.from_dict(_policies)

        readme = d.pop("readme", UNSET)

        _runner = d.pop("runner", UNSET)
        runner: AppAppRunnerConfig | Unset
        if isinstance(_runner, Unset):
            runner = UNSET
        else:
            runner = AppAppRunnerConfig.from_dict(_runner)

        _sandbox = d.pop("sandbox", UNSET)
        sandbox: AppAppSandboxConfig | Unset
        if isinstance(_sandbox, Unset):
            sandbox = UNSET
        else:
            sandbox = AppAppSandboxConfig.from_dict(_sandbox)

        _secrets = d.pop("secrets", UNSET)
        secrets: AppAppSecretsConfig | Unset
        if isinstance(_secrets, Unset):
            secrets = UNSET
        else:
            secrets = AppAppSecretsConfig.from_dict(_secrets)

        _stack = d.pop("stack", UNSET)
        stack: AppAppStackConfig | Unset
        if isinstance(_stack, Unset):
            stack = UNSET
        else:
            stack = AppAppStackConfig.from_dict(_stack)

        state = d.pop("state", UNSET)

        _status = d.pop("status", UNSET)
        status: AppAppConfigStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppAppConfigStatus(_status)

        status_description = d.pop("status_description", UNSET)

        _status_v2 = d.pop("status_v2", UNSET)
        status_v2: AppCompositeStatus | Unset
        if isinstance(_status_v2, Unset):
            status_v2 = UNSET
        else:
            status_v2 = AppCompositeStatus.from_dict(_status_v2)

        updated_at = d.pop("updated_at", UNSET)

        _vcs_connection_commit = d.pop("vcs_connection_commit", UNSET)
        vcs_connection_commit: AppVCSConnectionCommit | Unset
        if isinstance(_vcs_connection_commit, Unset):
            vcs_connection_commit = UNSET
        else:
            vcs_connection_commit = AppVCSConnectionCommit.from_dict(_vcs_connection_commit)

        version = d.pop("version", UNSET)

        app_app_config = cls(
            action_ids=action_ids,
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
            intermediate_config=intermediate_config,
            operation_role_config=operation_role_config,
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
            status_v2=status_v2,
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
