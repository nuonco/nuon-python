from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_powertoolsdev_mono_pkg_aws_credentials_config import (
        GithubComPowertoolsdevMonoPkgAwsCredentialsConfig,
    )
    from ..models.kube_cluster_info import KubeClusterInfo
    from ..models.plantypes_action_workflow_run_plan_attrs import PlantypesActionWorkflowRunPlanAttrs
    from ..models.plantypes_action_workflow_run_plan_builtin_env_vars import (
        PlantypesActionWorkflowRunPlanBuiltinEnvVars,
    )
    from ..models.plantypes_action_workflow_run_plan_override_env_vars import (
        PlantypesActionWorkflowRunPlanOverrideEnvVars,
    )
    from ..models.plantypes_action_workflow_run_step_plan import PlantypesActionWorkflowRunStepPlan
    from ..models.plantypes_sandbox_mode import PlantypesSandboxMode


T = TypeVar("T", bound="PlantypesActionWorkflowRunPlan")


@_attrs_define
class PlantypesActionWorkflowRunPlan:
    """
    Attributes:
        attrs (Union[Unset, PlantypesActionWorkflowRunPlanAttrs]):
        aws_auth (Union[Unset, GithubComPowertoolsdevMonoPkgAwsCredentialsConfig]):
        builtin_env_vars (Union[Unset, PlantypesActionWorkflowRunPlanBuiltinEnvVars]):
        cluster_info (Union[Unset, KubeClusterInfo]):
        id (Union[Unset, str]):
        install_id (Union[Unset, str]):
        override_env_vars (Union[Unset, PlantypesActionWorkflowRunPlanOverrideEnvVars]):
        sandbox_mode (Union[Unset, PlantypesSandboxMode]):
        steps (Union[Unset, list['PlantypesActionWorkflowRunStepPlan']]):
    """

    attrs: Union[Unset, "PlantypesActionWorkflowRunPlanAttrs"] = UNSET
    aws_auth: Union[Unset, "GithubComPowertoolsdevMonoPkgAwsCredentialsConfig"] = UNSET
    builtin_env_vars: Union[Unset, "PlantypesActionWorkflowRunPlanBuiltinEnvVars"] = UNSET
    cluster_info: Union[Unset, "KubeClusterInfo"] = UNSET
    id: Union[Unset, str] = UNSET
    install_id: Union[Unset, str] = UNSET
    override_env_vars: Union[Unset, "PlantypesActionWorkflowRunPlanOverrideEnvVars"] = UNSET
    sandbox_mode: Union[Unset, "PlantypesSandboxMode"] = UNSET
    steps: Union[Unset, list["PlantypesActionWorkflowRunStepPlan"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attrs: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.attrs, Unset):
            attrs = self.attrs.to_dict()

        aws_auth: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.aws_auth, Unset):
            aws_auth = self.aws_auth.to_dict()

        builtin_env_vars: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.builtin_env_vars, Unset):
            builtin_env_vars = self.builtin_env_vars.to_dict()

        cluster_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cluster_info, Unset):
            cluster_info = self.cluster_info.to_dict()

        id = self.id

        install_id = self.install_id

        override_env_vars: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.override_env_vars, Unset):
            override_env_vars = self.override_env_vars.to_dict()

        sandbox_mode: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sandbox_mode, Unset):
            sandbox_mode = self.sandbox_mode.to_dict()

        steps: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item = steps_item_data.to_dict()
                steps.append(steps_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attrs is not UNSET:
            field_dict["attrs"] = attrs
        if aws_auth is not UNSET:
            field_dict["aws_auth"] = aws_auth
        if builtin_env_vars is not UNSET:
            field_dict["builtin_env_vars"] = builtin_env_vars
        if cluster_info is not UNSET:
            field_dict["cluster_info"] = cluster_info
        if id is not UNSET:
            field_dict["id"] = id
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if override_env_vars is not UNSET:
            field_dict["override_env_vars"] = override_env_vars
        if sandbox_mode is not UNSET:
            field_dict["sandbox_mode"] = sandbox_mode
        if steps is not UNSET:
            field_dict["steps"] = steps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_powertoolsdev_mono_pkg_aws_credentials_config import (
            GithubComPowertoolsdevMonoPkgAwsCredentialsConfig,
        )
        from ..models.kube_cluster_info import KubeClusterInfo
        from ..models.plantypes_action_workflow_run_plan_attrs import PlantypesActionWorkflowRunPlanAttrs
        from ..models.plantypes_action_workflow_run_plan_builtin_env_vars import (
            PlantypesActionWorkflowRunPlanBuiltinEnvVars,
        )
        from ..models.plantypes_action_workflow_run_plan_override_env_vars import (
            PlantypesActionWorkflowRunPlanOverrideEnvVars,
        )
        from ..models.plantypes_action_workflow_run_step_plan import PlantypesActionWorkflowRunStepPlan
        from ..models.plantypes_sandbox_mode import PlantypesSandboxMode

        d = dict(src_dict)
        _attrs = d.pop("attrs", UNSET)
        attrs: Union[Unset, PlantypesActionWorkflowRunPlanAttrs]
        if isinstance(_attrs, Unset):
            attrs = UNSET
        else:
            attrs = PlantypesActionWorkflowRunPlanAttrs.from_dict(_attrs)

        _aws_auth = d.pop("aws_auth", UNSET)
        aws_auth: Union[Unset, GithubComPowertoolsdevMonoPkgAwsCredentialsConfig]
        if isinstance(_aws_auth, Unset):
            aws_auth = UNSET
        else:
            aws_auth = GithubComPowertoolsdevMonoPkgAwsCredentialsConfig.from_dict(_aws_auth)

        _builtin_env_vars = d.pop("builtin_env_vars", UNSET)
        builtin_env_vars: Union[Unset, PlantypesActionWorkflowRunPlanBuiltinEnvVars]
        if isinstance(_builtin_env_vars, Unset):
            builtin_env_vars = UNSET
        else:
            builtin_env_vars = PlantypesActionWorkflowRunPlanBuiltinEnvVars.from_dict(_builtin_env_vars)

        _cluster_info = d.pop("cluster_info", UNSET)
        cluster_info: Union[Unset, KubeClusterInfo]
        if isinstance(_cluster_info, Unset):
            cluster_info = UNSET
        else:
            cluster_info = KubeClusterInfo.from_dict(_cluster_info)

        id = d.pop("id", UNSET)

        install_id = d.pop("install_id", UNSET)

        _override_env_vars = d.pop("override_env_vars", UNSET)
        override_env_vars: Union[Unset, PlantypesActionWorkflowRunPlanOverrideEnvVars]
        if isinstance(_override_env_vars, Unset):
            override_env_vars = UNSET
        else:
            override_env_vars = PlantypesActionWorkflowRunPlanOverrideEnvVars.from_dict(_override_env_vars)

        _sandbox_mode = d.pop("sandbox_mode", UNSET)
        sandbox_mode: Union[Unset, PlantypesSandboxMode]
        if isinstance(_sandbox_mode, Unset):
            sandbox_mode = UNSET
        else:
            sandbox_mode = PlantypesSandboxMode.from_dict(_sandbox_mode)

        steps = []
        _steps = d.pop("steps", UNSET)
        for steps_item_data in _steps or []:
            steps_item = PlantypesActionWorkflowRunStepPlan.from_dict(steps_item_data)

            steps.append(steps_item)

        plantypes_action_workflow_run_plan = cls(
            attrs=attrs,
            aws_auth=aws_auth,
            builtin_env_vars=builtin_env_vars,
            cluster_info=cluster_info,
            id=id,
            install_id=install_id,
            override_env_vars=override_env_vars,
            sandbox_mode=sandbox_mode,
            steps=steps,
        )

        plantypes_action_workflow_run_plan.additional_properties = d
        return plantypes_action_workflow_run_plan

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
