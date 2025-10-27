from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_powertoolsdev_mono_pkg_aws_credentials_config import (
        GithubComPowertoolsdevMonoPkgAwsCredentialsConfig,
    )
    from ..models.github_com_powertoolsdev_mono_pkg_azure_credentials_config import (
        GithubComPowertoolsdevMonoPkgAzureCredentialsConfig,
    )
    from ..models.github_com_powertoolsdev_mono_pkg_types_state_state import (
        GithubComPowertoolsdevMonoPkgTypesStateState,
    )
    from ..models.kube_cluster_info import KubeClusterInfo
    from ..models.plantypes_terraform_backend import PlantypesTerraformBackend
    from ..models.plantypes_terraform_deploy_hooks import PlantypesTerraformDeployHooks
    from ..models.plantypes_terraform_deploy_plan_env_vars import PlantypesTerraformDeployPlanEnvVars
    from ..models.plantypes_terraform_deploy_plan_policies import PlantypesTerraformDeployPlanPolicies
    from ..models.plantypes_terraform_deploy_plan_vars import PlantypesTerraformDeployPlanVars


T = TypeVar("T", bound="PlantypesTerraformDeployPlan")


@_attrs_define
class PlantypesTerraformDeployPlan:
    """
    Attributes:
        aws_auth (Union[Unset, GithubComPowertoolsdevMonoPkgAwsCredentialsConfig]):
        azure_auth (Union[Unset, GithubComPowertoolsdevMonoPkgAzureCredentialsConfig]):
        cluster_info (Union[Unset, KubeClusterInfo]):
        env_vars (Union[Unset, PlantypesTerraformDeployPlanEnvVars]):
        hooks (Union[Unset, PlantypesTerraformDeployHooks]):
        plan_json (Union[Unset, list[int]]):
        policies (Union[Unset, PlantypesTerraformDeployPlanPolicies]):
        state (Union[Unset, GithubComPowertoolsdevMonoPkgTypesStateState]):
        terraform_backend (Union[Unset, PlantypesTerraformBackend]):
        vars_ (Union[Unset, PlantypesTerraformDeployPlanVars]):
        vars_files (Union[Unset, list[str]]):
    """

    aws_auth: Union[Unset, "GithubComPowertoolsdevMonoPkgAwsCredentialsConfig"] = UNSET
    azure_auth: Union[Unset, "GithubComPowertoolsdevMonoPkgAzureCredentialsConfig"] = UNSET
    cluster_info: Union[Unset, "KubeClusterInfo"] = UNSET
    env_vars: Union[Unset, "PlantypesTerraformDeployPlanEnvVars"] = UNSET
    hooks: Union[Unset, "PlantypesTerraformDeployHooks"] = UNSET
    plan_json: Union[Unset, list[int]] = UNSET
    policies: Union[Unset, "PlantypesTerraformDeployPlanPolicies"] = UNSET
    state: Union[Unset, "GithubComPowertoolsdevMonoPkgTypesStateState"] = UNSET
    terraform_backend: Union[Unset, "PlantypesTerraformBackend"] = UNSET
    vars_: Union[Unset, "PlantypesTerraformDeployPlanVars"] = UNSET
    vars_files: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aws_auth: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.aws_auth, Unset):
            aws_auth = self.aws_auth.to_dict()

        azure_auth: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.azure_auth, Unset):
            azure_auth = self.azure_auth.to_dict()

        cluster_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cluster_info, Unset):
            cluster_info = self.cluster_info.to_dict()

        env_vars: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        hooks: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.hooks, Unset):
            hooks = self.hooks.to_dict()

        plan_json: Union[Unset, list[int]] = UNSET
        if not isinstance(self.plan_json, Unset):
            plan_json = self.plan_json

        policies: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.policies, Unset):
            policies = self.policies.to_dict()

        state: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        terraform_backend: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.terraform_backend, Unset):
            terraform_backend = self.terraform_backend.to_dict()

        vars_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vars_, Unset):
            vars_ = self.vars_.to_dict()

        vars_files: Union[Unset, list[str]] = UNSET
        if not isinstance(self.vars_files, Unset):
            vars_files = self.vars_files

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aws_auth is not UNSET:
            field_dict["aws_auth"] = aws_auth
        if azure_auth is not UNSET:
            field_dict["azure_auth"] = azure_auth
        if cluster_info is not UNSET:
            field_dict["cluster_info"] = cluster_info
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if hooks is not UNSET:
            field_dict["hooks"] = hooks
        if plan_json is not UNSET:
            field_dict["plan_json"] = plan_json
        if policies is not UNSET:
            field_dict["policies"] = policies
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
        from ..models.github_com_powertoolsdev_mono_pkg_aws_credentials_config import (
            GithubComPowertoolsdevMonoPkgAwsCredentialsConfig,
        )
        from ..models.github_com_powertoolsdev_mono_pkg_azure_credentials_config import (
            GithubComPowertoolsdevMonoPkgAzureCredentialsConfig,
        )
        from ..models.github_com_powertoolsdev_mono_pkg_types_state_state import (
            GithubComPowertoolsdevMonoPkgTypesStateState,
        )
        from ..models.kube_cluster_info import KubeClusterInfo
        from ..models.plantypes_terraform_backend import PlantypesTerraformBackend
        from ..models.plantypes_terraform_deploy_hooks import PlantypesTerraformDeployHooks
        from ..models.plantypes_terraform_deploy_plan_env_vars import PlantypesTerraformDeployPlanEnvVars
        from ..models.plantypes_terraform_deploy_plan_policies import PlantypesTerraformDeployPlanPolicies
        from ..models.plantypes_terraform_deploy_plan_vars import PlantypesTerraformDeployPlanVars

        d = dict(src_dict)
        _aws_auth = d.pop("aws_auth", UNSET)
        aws_auth: Union[Unset, GithubComPowertoolsdevMonoPkgAwsCredentialsConfig]
        if isinstance(_aws_auth, Unset):
            aws_auth = UNSET
        else:
            aws_auth = GithubComPowertoolsdevMonoPkgAwsCredentialsConfig.from_dict(_aws_auth)

        _azure_auth = d.pop("azure_auth", UNSET)
        azure_auth: Union[Unset, GithubComPowertoolsdevMonoPkgAzureCredentialsConfig]
        if isinstance(_azure_auth, Unset):
            azure_auth = UNSET
        else:
            azure_auth = GithubComPowertoolsdevMonoPkgAzureCredentialsConfig.from_dict(_azure_auth)

        _cluster_info = d.pop("cluster_info", UNSET)
        cluster_info: Union[Unset, KubeClusterInfo]
        if isinstance(_cluster_info, Unset):
            cluster_info = UNSET
        else:
            cluster_info = KubeClusterInfo.from_dict(_cluster_info)

        _env_vars = d.pop("env_vars", UNSET)
        env_vars: Union[Unset, PlantypesTerraformDeployPlanEnvVars]
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = PlantypesTerraformDeployPlanEnvVars.from_dict(_env_vars)

        _hooks = d.pop("hooks", UNSET)
        hooks: Union[Unset, PlantypesTerraformDeployHooks]
        if isinstance(_hooks, Unset):
            hooks = UNSET
        else:
            hooks = PlantypesTerraformDeployHooks.from_dict(_hooks)

        plan_json = cast(list[int], d.pop("plan_json", UNSET))

        _policies = d.pop("policies", UNSET)
        policies: Union[Unset, PlantypesTerraformDeployPlanPolicies]
        if isinstance(_policies, Unset):
            policies = UNSET
        else:
            policies = PlantypesTerraformDeployPlanPolicies.from_dict(_policies)

        _state = d.pop("state", UNSET)
        state: Union[Unset, GithubComPowertoolsdevMonoPkgTypesStateState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = GithubComPowertoolsdevMonoPkgTypesStateState.from_dict(_state)

        _terraform_backend = d.pop("terraform_backend", UNSET)
        terraform_backend: Union[Unset, PlantypesTerraformBackend]
        if isinstance(_terraform_backend, Unset):
            terraform_backend = UNSET
        else:
            terraform_backend = PlantypesTerraformBackend.from_dict(_terraform_backend)

        _vars_ = d.pop("vars", UNSET)
        vars_: Union[Unset, PlantypesTerraformDeployPlanVars]
        if isinstance(_vars_, Unset):
            vars_ = UNSET
        else:
            vars_ = PlantypesTerraformDeployPlanVars.from_dict(_vars_)

        vars_files = cast(list[str], d.pop("vars_files", UNSET))

        plantypes_terraform_deploy_plan = cls(
            aws_auth=aws_auth,
            azure_auth=azure_auth,
            cluster_info=cluster_info,
            env_vars=env_vars,
            hooks=hooks,
            plan_json=plan_json,
            policies=policies,
            state=state,
            terraform_backend=terraform_backend,
            vars_=vars_,
            vars_files=vars_files,
        )

        plantypes_terraform_deploy_plan.additional_properties = d
        return plantypes_terraform_deploy_plan

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
