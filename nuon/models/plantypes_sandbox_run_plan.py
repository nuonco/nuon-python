from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_nuonco_nuon_pkg_aws_credentials_config import GithubComNuoncoNuonPkgAwsCredentialsConfig
    from ..models.github_com_nuonco_nuon_pkg_azure_credentials_config import (
        GithubComNuoncoNuonPkgAzureCredentialsConfig,
    )
    from ..models.github_com_nuonco_nuon_pkg_types_state_state import GithubComNuoncoNuonPkgTypesStateState
    from ..models.plantypes_git_source import PlantypesGitSource
    from ..models.plantypes_sandbox_mode import PlantypesSandboxMode
    from ..models.plantypes_sandbox_run_plan_env_vars import PlantypesSandboxRunPlanEnvVars
    from ..models.plantypes_sandbox_run_plan_policies import PlantypesSandboxRunPlanPolicies
    from ..models.plantypes_sandbox_run_plan_vars import PlantypesSandboxRunPlanVars
    from ..models.plantypes_terraform_backend import PlantypesTerraformBackend
    from ..models.plantypes_terraform_deploy_hooks import PlantypesTerraformDeployHooks
    from ..models.plantypes_terraform_local_archive import PlantypesTerraformLocalArchive


T = TypeVar("T", bound="PlantypesSandboxRunPlan")


@_attrs_define
class PlantypesSandboxRunPlan:
    """
    Attributes:
        app_config_id (str | Unset):
        app_id (str | Unset):
        apply_plan_contents (str | Unset): The following field is for applying a plan that is already saved
        apply_plan_display (list[int] | Unset): This field is for storing a human legible plan or corollary
            representation
        aws_auth (GithubComNuoncoNuonPkgAwsCredentialsConfig | Unset):
        azure_auth (GithubComNuoncoNuonPkgAzureCredentialsConfig | Unset):
        env_vars (PlantypesSandboxRunPlanEnvVars | Unset):
        git_source (PlantypesGitSource | Unset):
        hooks (PlantypesTerraformDeployHooks | Unset):
        install_id (str | Unset):
        local_archive (PlantypesTerraformLocalArchive | Unset):
        policies (PlantypesSandboxRunPlanPolicies | Unset):
        sandbox_mode (PlantypesSandboxMode | Unset):
        state (GithubComNuoncoNuonPkgTypesStateState | Unset):
        terraform_backend (PlantypesTerraformBackend | Unset):
        vars_ (PlantypesSandboxRunPlanVars | Unset):
        vars_files (list[str] | Unset):
    """

    app_config_id: str | Unset = UNSET
    app_id: str | Unset = UNSET
    apply_plan_contents: str | Unset = UNSET
    apply_plan_display: list[int] | Unset = UNSET
    aws_auth: GithubComNuoncoNuonPkgAwsCredentialsConfig | Unset = UNSET
    azure_auth: GithubComNuoncoNuonPkgAzureCredentialsConfig | Unset = UNSET
    env_vars: PlantypesSandboxRunPlanEnvVars | Unset = UNSET
    git_source: PlantypesGitSource | Unset = UNSET
    hooks: PlantypesTerraformDeployHooks | Unset = UNSET
    install_id: str | Unset = UNSET
    local_archive: PlantypesTerraformLocalArchive | Unset = UNSET
    policies: PlantypesSandboxRunPlanPolicies | Unset = UNSET
    sandbox_mode: PlantypesSandboxMode | Unset = UNSET
    state: GithubComNuoncoNuonPkgTypesStateState | Unset = UNSET
    terraform_backend: PlantypesTerraformBackend | Unset = UNSET
    vars_: PlantypesSandboxRunPlanVars | Unset = UNSET
    vars_files: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config_id = self.app_config_id

        app_id = self.app_id

        apply_plan_contents = self.apply_plan_contents

        apply_plan_display: list[int] | Unset = UNSET
        if not isinstance(self.apply_plan_display, Unset):
            apply_plan_display = self.apply_plan_display

        aws_auth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aws_auth, Unset):
            aws_auth = self.aws_auth.to_dict()

        azure_auth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.azure_auth, Unset):
            azure_auth = self.azure_auth.to_dict()

        env_vars: dict[str, Any] | Unset = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        git_source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.git_source, Unset):
            git_source = self.git_source.to_dict()

        hooks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hooks, Unset):
            hooks = self.hooks.to_dict()

        install_id = self.install_id

        local_archive: dict[str, Any] | Unset = UNSET
        if not isinstance(self.local_archive, Unset):
            local_archive = self.local_archive.to_dict()

        policies: dict[str, Any] | Unset = UNSET
        if not isinstance(self.policies, Unset):
            policies = self.policies.to_dict()

        sandbox_mode: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sandbox_mode, Unset):
            sandbox_mode = self.sandbox_mode.to_dict()

        state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        terraform_backend: dict[str, Any] | Unset = UNSET
        if not isinstance(self.terraform_backend, Unset):
            terraform_backend = self.terraform_backend.to_dict()

        vars_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vars_, Unset):
            vars_ = self.vars_.to_dict()

        vars_files: list[str] | Unset = UNSET
        if not isinstance(self.vars_files, Unset):
            vars_files = self.vars_files

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if apply_plan_contents is not UNSET:
            field_dict["apply_plan_contents"] = apply_plan_contents
        if apply_plan_display is not UNSET:
            field_dict["apply_plan_display"] = apply_plan_display
        if aws_auth is not UNSET:
            field_dict["aws_auth"] = aws_auth
        if azure_auth is not UNSET:
            field_dict["azure_auth"] = azure_auth
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if git_source is not UNSET:
            field_dict["git_source"] = git_source
        if hooks is not UNSET:
            field_dict["hooks"] = hooks
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if local_archive is not UNSET:
            field_dict["local_archive"] = local_archive
        if policies is not UNSET:
            field_dict["policies"] = policies
        if sandbox_mode is not UNSET:
            field_dict["sandbox_mode"] = sandbox_mode
        if state is not UNSET:
            field_dict["state"] = state
        if terraform_backend is not UNSET:
            field_dict["terraform_backend"] = terraform_backend
        if vars_ is not UNSET:
            field_dict["vars"] = vars_
        if vars_files is not UNSET:
            field_dict["vars_files"] = vars_files

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_nuonco_nuon_pkg_aws_credentials_config import (
            GithubComNuoncoNuonPkgAwsCredentialsConfig,
        )
        from ..models.github_com_nuonco_nuon_pkg_azure_credentials_config import (
            GithubComNuoncoNuonPkgAzureCredentialsConfig,
        )
        from ..models.github_com_nuonco_nuon_pkg_types_state_state import GithubComNuoncoNuonPkgTypesStateState
        from ..models.plantypes_git_source import PlantypesGitSource
        from ..models.plantypes_sandbox_mode import PlantypesSandboxMode
        from ..models.plantypes_sandbox_run_plan_env_vars import PlantypesSandboxRunPlanEnvVars
        from ..models.plantypes_sandbox_run_plan_policies import PlantypesSandboxRunPlanPolicies
        from ..models.plantypes_sandbox_run_plan_vars import PlantypesSandboxRunPlanVars
        from ..models.plantypes_terraform_backend import PlantypesTerraformBackend
        from ..models.plantypes_terraform_deploy_hooks import PlantypesTerraformDeployHooks
        from ..models.plantypes_terraform_local_archive import PlantypesTerraformLocalArchive

        d = dict(src_dict)
        app_config_id = d.pop("app_config_id", UNSET)

        app_id = d.pop("app_id", UNSET)

        apply_plan_contents = d.pop("apply_plan_contents", UNSET)

        apply_plan_display = cast(list[int], d.pop("apply_plan_display", UNSET))

        _aws_auth = d.pop("aws_auth", UNSET)
        aws_auth: GithubComNuoncoNuonPkgAwsCredentialsConfig | Unset
        if isinstance(_aws_auth, Unset):
            aws_auth = UNSET
        else:
            aws_auth = GithubComNuoncoNuonPkgAwsCredentialsConfig.from_dict(_aws_auth)

        _azure_auth = d.pop("azure_auth", UNSET)
        azure_auth: GithubComNuoncoNuonPkgAzureCredentialsConfig | Unset
        if isinstance(_azure_auth, Unset):
            azure_auth = UNSET
        else:
            azure_auth = GithubComNuoncoNuonPkgAzureCredentialsConfig.from_dict(_azure_auth)

        _env_vars = d.pop("env_vars", UNSET)
        env_vars: PlantypesSandboxRunPlanEnvVars | Unset
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = PlantypesSandboxRunPlanEnvVars.from_dict(_env_vars)

        _git_source = d.pop("git_source", UNSET)
        git_source: PlantypesGitSource | Unset
        if isinstance(_git_source, Unset):
            git_source = UNSET
        else:
            git_source = PlantypesGitSource.from_dict(_git_source)

        _hooks = d.pop("hooks", UNSET)
        hooks: PlantypesTerraformDeployHooks | Unset
        if isinstance(_hooks, Unset):
            hooks = UNSET
        else:
            hooks = PlantypesTerraformDeployHooks.from_dict(_hooks)

        install_id = d.pop("install_id", UNSET)

        _local_archive = d.pop("local_archive", UNSET)
        local_archive: PlantypesTerraformLocalArchive | Unset
        if isinstance(_local_archive, Unset):
            local_archive = UNSET
        else:
            local_archive = PlantypesTerraformLocalArchive.from_dict(_local_archive)

        _policies = d.pop("policies", UNSET)
        policies: PlantypesSandboxRunPlanPolicies | Unset
        if isinstance(_policies, Unset):
            policies = UNSET
        else:
            policies = PlantypesSandboxRunPlanPolicies.from_dict(_policies)

        _sandbox_mode = d.pop("sandbox_mode", UNSET)
        sandbox_mode: PlantypesSandboxMode | Unset
        if isinstance(_sandbox_mode, Unset):
            sandbox_mode = UNSET
        else:
            sandbox_mode = PlantypesSandboxMode.from_dict(_sandbox_mode)

        _state = d.pop("state", UNSET)
        state: GithubComNuoncoNuonPkgTypesStateState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = GithubComNuoncoNuonPkgTypesStateState.from_dict(_state)

        _terraform_backend = d.pop("terraform_backend", UNSET)
        terraform_backend: PlantypesTerraformBackend | Unset
        if isinstance(_terraform_backend, Unset):
            terraform_backend = UNSET
        else:
            terraform_backend = PlantypesTerraformBackend.from_dict(_terraform_backend)

        _vars_ = d.pop("vars", UNSET)
        vars_: PlantypesSandboxRunPlanVars | Unset
        if isinstance(_vars_, Unset):
            vars_ = UNSET
        else:
            vars_ = PlantypesSandboxRunPlanVars.from_dict(_vars_)

        vars_files = cast(list[str], d.pop("vars_files", UNSET))

        plantypes_sandbox_run_plan = cls(
            app_config_id=app_config_id,
            app_id=app_id,
            apply_plan_contents=apply_plan_contents,
            apply_plan_display=apply_plan_display,
            aws_auth=aws_auth,
            azure_auth=azure_auth,
            env_vars=env_vars,
            git_source=git_source,
            hooks=hooks,
            install_id=install_id,
            local_archive=local_archive,
            policies=policies,
            sandbox_mode=sandbox_mode,
            state=state,
            terraform_backend=terraform_backend,
            vars_=vars_,
            vars_files=vars_files,
        )

        plantypes_sandbox_run_plan.additional_properties = d
        return plantypes_sandbox_run_plan

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
