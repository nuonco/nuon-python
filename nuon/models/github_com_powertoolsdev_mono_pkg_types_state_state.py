from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_powertoolsdev_mono_pkg_types_state_state_components import (
        GithubComPowertoolsdevMonoPkgTypesStateStateComponents,
    )
    from ..models.state_actions_state import StateActionsState
    from ..models.state_app_state import StateAppState
    from ..models.state_cloud_account import StateCloudAccount
    from ..models.state_domain_state import StateDomainState
    from ..models.state_inputs_state import StateInputsState
    from ..models.state_install_stack_state import StateInstallStackState
    from ..models.state_install_state import StateInstallState
    from ..models.state_org_state import StateOrgState
    from ..models.state_runner_state import StateRunnerState
    from ..models.state_sandbox_state import StateSandboxState
    from ..models.state_secrets_state import StateSecretsState


T = TypeVar("T", bound="GithubComPowertoolsdevMonoPkgTypesStateState")


@_attrs_define
class GithubComPowertoolsdevMonoPkgTypesStateState:
    """
    Attributes:
        actions (StateActionsState | Unset):
        app (StateAppState | Unset):
        cloud_account (StateCloudAccount | Unset):
        components (GithubComPowertoolsdevMonoPkgTypesStateStateComponents | Unset):
        domain (StateDomainState | Unset):
        id (str | Unset):
        inputs (StateInputsState | Unset):
        install (StateInstallState | Unset):
        install_stack (StateInstallStackState | Unset):
        name (str | Unset):
        org (StateOrgState | Unset):
        runner (StateRunnerState | Unset):
        sandbox (StateSandboxState | Unset):
        secrets (StateSecretsState | Unset):
        stale_at (str | Unset): loaded from the database but not part of the state itself
    """

    actions: StateActionsState | Unset = UNSET
    app: StateAppState | Unset = UNSET
    cloud_account: StateCloudAccount | Unset = UNSET
    components: GithubComPowertoolsdevMonoPkgTypesStateStateComponents | Unset = UNSET
    domain: StateDomainState | Unset = UNSET
    id: str | Unset = UNSET
    inputs: StateInputsState | Unset = UNSET
    install: StateInstallState | Unset = UNSET
    install_stack: StateInstallStackState | Unset = UNSET
    name: str | Unset = UNSET
    org: StateOrgState | Unset = UNSET
    runner: StateRunnerState | Unset = UNSET
    sandbox: StateSandboxState | Unset = UNSET
    secrets: StateSecretsState | Unset = UNSET
    stale_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        actions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actions, Unset):
            actions = self.actions.to_dict()

        app: dict[str, Any] | Unset = UNSET
        if not isinstance(self.app, Unset):
            app = self.app.to_dict()

        cloud_account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cloud_account, Unset):
            cloud_account = self.cloud_account.to_dict()

        components: dict[str, Any] | Unset = UNSET
        if not isinstance(self.components, Unset):
            components = self.components.to_dict()

        domain: dict[str, Any] | Unset = UNSET
        if not isinstance(self.domain, Unset):
            domain = self.domain.to_dict()

        id = self.id

        inputs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inputs, Unset):
            inputs = self.inputs.to_dict()

        install: dict[str, Any] | Unset = UNSET
        if not isinstance(self.install, Unset):
            install = self.install.to_dict()

        install_stack: dict[str, Any] | Unset = UNSET
        if not isinstance(self.install_stack, Unset):
            install_stack = self.install_stack.to_dict()

        name = self.name

        org: dict[str, Any] | Unset = UNSET
        if not isinstance(self.org, Unset):
            org = self.org.to_dict()

        runner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.runner, Unset):
            runner = self.runner.to_dict()

        sandbox: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sandbox, Unset):
            sandbox = self.sandbox.to_dict()

        secrets: dict[str, Any] | Unset = UNSET
        if not isinstance(self.secrets, Unset):
            secrets = self.secrets.to_dict()

        stale_at = self.stale_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if actions is not UNSET:
            field_dict["actions"] = actions
        if app is not UNSET:
            field_dict["app"] = app
        if cloud_account is not UNSET:
            field_dict["cloud_account"] = cloud_account
        if components is not UNSET:
            field_dict["components"] = components
        if domain is not UNSET:
            field_dict["domain"] = domain
        if id is not UNSET:
            field_dict["id"] = id
        if inputs is not UNSET:
            field_dict["inputs"] = inputs
        if install is not UNSET:
            field_dict["install"] = install
        if install_stack is not UNSET:
            field_dict["install_stack"] = install_stack
        if name is not UNSET:
            field_dict["name"] = name
        if org is not UNSET:
            field_dict["org"] = org
        if runner is not UNSET:
            field_dict["runner"] = runner
        if sandbox is not UNSET:
            field_dict["sandbox"] = sandbox
        if secrets is not UNSET:
            field_dict["secrets"] = secrets
        if stale_at is not UNSET:
            field_dict["stale_at"] = stale_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_powertoolsdev_mono_pkg_types_state_state_components import (
            GithubComPowertoolsdevMonoPkgTypesStateStateComponents,
        )
        from ..models.state_actions_state import StateActionsState
        from ..models.state_app_state import StateAppState
        from ..models.state_cloud_account import StateCloudAccount
        from ..models.state_domain_state import StateDomainState
        from ..models.state_inputs_state import StateInputsState
        from ..models.state_install_stack_state import StateInstallStackState
        from ..models.state_install_state import StateInstallState
        from ..models.state_org_state import StateOrgState
        from ..models.state_runner_state import StateRunnerState
        from ..models.state_sandbox_state import StateSandboxState
        from ..models.state_secrets_state import StateSecretsState

        d = dict(src_dict)
        _actions = d.pop("actions", UNSET)
        actions: StateActionsState | Unset
        if isinstance(_actions, Unset):
            actions = UNSET
        else:
            actions = StateActionsState.from_dict(_actions)

        _app = d.pop("app", UNSET)
        app: StateAppState | Unset
        if isinstance(_app, Unset):
            app = UNSET
        else:
            app = StateAppState.from_dict(_app)

        _cloud_account = d.pop("cloud_account", UNSET)
        cloud_account: StateCloudAccount | Unset
        if isinstance(_cloud_account, Unset):
            cloud_account = UNSET
        else:
            cloud_account = StateCloudAccount.from_dict(_cloud_account)

        _components = d.pop("components", UNSET)
        components: GithubComPowertoolsdevMonoPkgTypesStateStateComponents | Unset
        if isinstance(_components, Unset):
            components = UNSET
        else:
            components = GithubComPowertoolsdevMonoPkgTypesStateStateComponents.from_dict(_components)

        _domain = d.pop("domain", UNSET)
        domain: StateDomainState | Unset
        if isinstance(_domain, Unset):
            domain = UNSET
        else:
            domain = StateDomainState.from_dict(_domain)

        id = d.pop("id", UNSET)

        _inputs = d.pop("inputs", UNSET)
        inputs: StateInputsState | Unset
        if isinstance(_inputs, Unset):
            inputs = UNSET
        else:
            inputs = StateInputsState.from_dict(_inputs)

        _install = d.pop("install", UNSET)
        install: StateInstallState | Unset
        if isinstance(_install, Unset):
            install = UNSET
        else:
            install = StateInstallState.from_dict(_install)

        _install_stack = d.pop("install_stack", UNSET)
        install_stack: StateInstallStackState | Unset
        if isinstance(_install_stack, Unset):
            install_stack = UNSET
        else:
            install_stack = StateInstallStackState.from_dict(_install_stack)

        name = d.pop("name", UNSET)

        _org = d.pop("org", UNSET)
        org: StateOrgState | Unset
        if isinstance(_org, Unset):
            org = UNSET
        else:
            org = StateOrgState.from_dict(_org)

        _runner = d.pop("runner", UNSET)
        runner: StateRunnerState | Unset
        if isinstance(_runner, Unset):
            runner = UNSET
        else:
            runner = StateRunnerState.from_dict(_runner)

        _sandbox = d.pop("sandbox", UNSET)
        sandbox: StateSandboxState | Unset
        if isinstance(_sandbox, Unset):
            sandbox = UNSET
        else:
            sandbox = StateSandboxState.from_dict(_sandbox)

        _secrets = d.pop("secrets", UNSET)
        secrets: StateSecretsState | Unset
        if isinstance(_secrets, Unset):
            secrets = UNSET
        else:
            secrets = StateSecretsState.from_dict(_secrets)

        stale_at = d.pop("stale_at", UNSET)

        github_com_powertoolsdev_mono_pkg_types_state_state = cls(
            actions=actions,
            app=app,
            cloud_account=cloud_account,
            components=components,
            domain=domain,
            id=id,
            inputs=inputs,
            install=install,
            install_stack=install_stack,
            name=name,
            org=org,
            runner=runner,
            sandbox=sandbox,
            secrets=secrets,
            stale_at=stale_at,
        )

        github_com_powertoolsdev_mono_pkg_types_state_state.additional_properties = d
        return github_com_powertoolsdev_mono_pkg_types_state_state

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
