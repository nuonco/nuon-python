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
    from ..models.github_com_nuonco_nuon_pkg_gcp_credentials_config import GithubComNuoncoNuonPkgGcpCredentialsConfig
    from ..models.github_com_nuonco_nuon_pkg_types_state_state import GithubComNuoncoNuonPkgTypesStateState
    from ..models.kube_cluster_info import KubeClusterInfo
    from ..models.plantypes_pulumi_deploy_plan_config import PlantypesPulumiDeployPlanConfig
    from ..models.plantypes_pulumi_deploy_plan_env_vars import PlantypesPulumiDeployPlanEnvVars


T = TypeVar("T", bound="PlantypesPulumiDeployPlan")


@_attrs_define
class PlantypesPulumiDeployPlan:
    """
    Attributes:
        aws_auth (GithubComNuoncoNuonPkgAwsCredentialsConfig | Unset):
        azure_auth (GithubComNuoncoNuonPkgAzureCredentialsConfig | Unset):
        cluster_info (KubeClusterInfo | Unset):
        config (PlantypesPulumiDeployPlanConfig | Unset):
        destroy (bool | Unset): Destroy indicates this is a teardown operation (pulumi destroy instead of up)
        env_vars (PlantypesPulumiDeployPlanEnvVars | Unset):
        gcp_auth (GithubComNuoncoNuonPkgGcpCredentialsConfig | Unset):
        plan_json (list[int] | Unset):
        pulumi_version (str | Unset):
        runtime (str | Unset):
        stack_name (str | Unset):
        state (GithubComNuoncoNuonPkgTypesStateState | Unset):
        workspace_id (str | Unset): Reuse workspace concept for state storage
    """

    aws_auth: GithubComNuoncoNuonPkgAwsCredentialsConfig | Unset = UNSET
    azure_auth: GithubComNuoncoNuonPkgAzureCredentialsConfig | Unset = UNSET
    cluster_info: KubeClusterInfo | Unset = UNSET
    config: PlantypesPulumiDeployPlanConfig | Unset = UNSET
    destroy: bool | Unset = UNSET
    env_vars: PlantypesPulumiDeployPlanEnvVars | Unset = UNSET
    gcp_auth: GithubComNuoncoNuonPkgGcpCredentialsConfig | Unset = UNSET
    plan_json: list[int] | Unset = UNSET
    pulumi_version: str | Unset = UNSET
    runtime: str | Unset = UNSET
    stack_name: str | Unset = UNSET
    state: GithubComNuoncoNuonPkgTypesStateState | Unset = UNSET
    workspace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aws_auth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aws_auth, Unset):
            aws_auth = self.aws_auth.to_dict()

        azure_auth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.azure_auth, Unset):
            azure_auth = self.azure_auth.to_dict()

        cluster_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cluster_info, Unset):
            cluster_info = self.cluster_info.to_dict()

        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        destroy = self.destroy

        env_vars: dict[str, Any] | Unset = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        gcp_auth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gcp_auth, Unset):
            gcp_auth = self.gcp_auth.to_dict()

        plan_json: list[int] | Unset = UNSET
        if not isinstance(self.plan_json, Unset):
            plan_json = self.plan_json

        pulumi_version = self.pulumi_version

        runtime = self.runtime

        stack_name = self.stack_name

        state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aws_auth is not UNSET:
            field_dict["aws_auth"] = aws_auth
        if azure_auth is not UNSET:
            field_dict["azure_auth"] = azure_auth
        if cluster_info is not UNSET:
            field_dict["cluster_info"] = cluster_info
        if config is not UNSET:
            field_dict["config"] = config
        if destroy is not UNSET:
            field_dict["destroy"] = destroy
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if gcp_auth is not UNSET:
            field_dict["gcp_auth"] = gcp_auth
        if plan_json is not UNSET:
            field_dict["plan_json"] = plan_json
        if pulumi_version is not UNSET:
            field_dict["pulumi_version"] = pulumi_version
        if runtime is not UNSET:
            field_dict["runtime"] = runtime
        if stack_name is not UNSET:
            field_dict["stack_name"] = stack_name
        if state is not UNSET:
            field_dict["state"] = state
        if workspace_id is not UNSET:
            field_dict["workspace_id"] = workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_nuonco_nuon_pkg_aws_credentials_config import (
            GithubComNuoncoNuonPkgAwsCredentialsConfig,
        )
        from ..models.github_com_nuonco_nuon_pkg_azure_credentials_config import (
            GithubComNuoncoNuonPkgAzureCredentialsConfig,
        )
        from ..models.github_com_nuonco_nuon_pkg_gcp_credentials_config import (
            GithubComNuoncoNuonPkgGcpCredentialsConfig,
        )
        from ..models.github_com_nuonco_nuon_pkg_types_state_state import GithubComNuoncoNuonPkgTypesStateState
        from ..models.kube_cluster_info import KubeClusterInfo
        from ..models.plantypes_pulumi_deploy_plan_config import PlantypesPulumiDeployPlanConfig
        from ..models.plantypes_pulumi_deploy_plan_env_vars import PlantypesPulumiDeployPlanEnvVars

        d = dict(src_dict)
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

        _cluster_info = d.pop("cluster_info", UNSET)
        cluster_info: KubeClusterInfo | Unset
        if isinstance(_cluster_info, Unset):
            cluster_info = UNSET
        else:
            cluster_info = KubeClusterInfo.from_dict(_cluster_info)

        _config = d.pop("config", UNSET)
        config: PlantypesPulumiDeployPlanConfig | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = PlantypesPulumiDeployPlanConfig.from_dict(_config)

        destroy = d.pop("destroy", UNSET)

        _env_vars = d.pop("env_vars", UNSET)
        env_vars: PlantypesPulumiDeployPlanEnvVars | Unset
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = PlantypesPulumiDeployPlanEnvVars.from_dict(_env_vars)

        _gcp_auth = d.pop("gcp_auth", UNSET)
        gcp_auth: GithubComNuoncoNuonPkgGcpCredentialsConfig | Unset
        if isinstance(_gcp_auth, Unset):
            gcp_auth = UNSET
        else:
            gcp_auth = GithubComNuoncoNuonPkgGcpCredentialsConfig.from_dict(_gcp_auth)

        plan_json = cast(list[int], d.pop("plan_json", UNSET))

        pulumi_version = d.pop("pulumi_version", UNSET)

        runtime = d.pop("runtime", UNSET)

        stack_name = d.pop("stack_name", UNSET)

        _state = d.pop("state", UNSET)
        state: GithubComNuoncoNuonPkgTypesStateState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = GithubComNuoncoNuonPkgTypesStateState.from_dict(_state)

        workspace_id = d.pop("workspace_id", UNSET)

        plantypes_pulumi_deploy_plan = cls(
            aws_auth=aws_auth,
            azure_auth=azure_auth,
            cluster_info=cluster_info,
            config=config,
            destroy=destroy,
            env_vars=env_vars,
            gcp_auth=gcp_auth,
            plan_json=plan_json,
            pulumi_version=pulumi_version,
            runtime=runtime,
            stack_name=stack_name,
            state=state,
            workspace_id=workspace_id,
        )

        plantypes_pulumi_deploy_plan.additional_properties = d
        return plantypes_pulumi_deploy_plan

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
