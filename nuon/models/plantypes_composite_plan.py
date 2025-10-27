from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plantypes_action_workflow_run_plan import PlantypesActionWorkflowRunPlan
    from ..models.plantypes_build_plan import PlantypesBuildPlan
    from ..models.plantypes_deploy_plan import PlantypesDeployPlan
    from ..models.plantypes_sandbox_run_plan import PlantypesSandboxRunPlan
    from ..models.plantypes_sync_oci_plan import PlantypesSyncOCIPlan
    from ..models.plantypes_sync_secrets_plan import PlantypesSyncSecretsPlan


T = TypeVar("T", bound="PlantypesCompositePlan")


@_attrs_define
class PlantypesCompositePlan:
    """
    Attributes:
        action_workflow_run_plan (Union[Unset, PlantypesActionWorkflowRunPlan]):
        build_plan (Union[Unset, PlantypesBuildPlan]):
        deploy_plan (Union[Unset, PlantypesDeployPlan]):
        sandbox_run_plan (Union[Unset, PlantypesSandboxRunPlan]):
        sync_oci_plan (Union[Unset, PlantypesSyncOCIPlan]):
        sync_secrets_plan (Union[Unset, PlantypesSyncSecretsPlan]):
    """

    action_workflow_run_plan: Union[Unset, "PlantypesActionWorkflowRunPlan"] = UNSET
    build_plan: Union[Unset, "PlantypesBuildPlan"] = UNSET
    deploy_plan: Union[Unset, "PlantypesDeployPlan"] = UNSET
    sandbox_run_plan: Union[Unset, "PlantypesSandboxRunPlan"] = UNSET
    sync_oci_plan: Union[Unset, "PlantypesSyncOCIPlan"] = UNSET
    sync_secrets_plan: Union[Unset, "PlantypesSyncSecretsPlan"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_workflow_run_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.action_workflow_run_plan, Unset):
            action_workflow_run_plan = self.action_workflow_run_plan.to_dict()

        build_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.build_plan, Unset):
            build_plan = self.build_plan.to_dict()

        deploy_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.deploy_plan, Unset):
            deploy_plan = self.deploy_plan.to_dict()

        sandbox_run_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sandbox_run_plan, Unset):
            sandbox_run_plan = self.sandbox_run_plan.to_dict()

        sync_oci_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sync_oci_plan, Unset):
            sync_oci_plan = self.sync_oci_plan.to_dict()

        sync_secrets_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sync_secrets_plan, Unset):
            sync_secrets_plan = self.sync_secrets_plan.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action_workflow_run_plan is not UNSET:
            field_dict["action_workflow_run_plan"] = action_workflow_run_plan
        if build_plan is not UNSET:
            field_dict["build_plan"] = build_plan
        if deploy_plan is not UNSET:
            field_dict["deploy_plan"] = deploy_plan
        if sandbox_run_plan is not UNSET:
            field_dict["sandbox_run_plan"] = sandbox_run_plan
        if sync_oci_plan is not UNSET:
            field_dict["sync_oci_plan"] = sync_oci_plan
        if sync_secrets_plan is not UNSET:
            field_dict["sync_secrets_plan"] = sync_secrets_plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plantypes_action_workflow_run_plan import PlantypesActionWorkflowRunPlan
        from ..models.plantypes_build_plan import PlantypesBuildPlan
        from ..models.plantypes_deploy_plan import PlantypesDeployPlan
        from ..models.plantypes_sandbox_run_plan import PlantypesSandboxRunPlan
        from ..models.plantypes_sync_oci_plan import PlantypesSyncOCIPlan
        from ..models.plantypes_sync_secrets_plan import PlantypesSyncSecretsPlan

        d = dict(src_dict)
        _action_workflow_run_plan = d.pop("action_workflow_run_plan", UNSET)
        action_workflow_run_plan: Union[Unset, PlantypesActionWorkflowRunPlan]
        if isinstance(_action_workflow_run_plan, Unset):
            action_workflow_run_plan = UNSET
        else:
            action_workflow_run_plan = PlantypesActionWorkflowRunPlan.from_dict(_action_workflow_run_plan)

        _build_plan = d.pop("build_plan", UNSET)
        build_plan: Union[Unset, PlantypesBuildPlan]
        if isinstance(_build_plan, Unset):
            build_plan = UNSET
        else:
            build_plan = PlantypesBuildPlan.from_dict(_build_plan)

        _deploy_plan = d.pop("deploy_plan", UNSET)
        deploy_plan: Union[Unset, PlantypesDeployPlan]
        if isinstance(_deploy_plan, Unset):
            deploy_plan = UNSET
        else:
            deploy_plan = PlantypesDeployPlan.from_dict(_deploy_plan)

        _sandbox_run_plan = d.pop("sandbox_run_plan", UNSET)
        sandbox_run_plan: Union[Unset, PlantypesSandboxRunPlan]
        if isinstance(_sandbox_run_plan, Unset):
            sandbox_run_plan = UNSET
        else:
            sandbox_run_plan = PlantypesSandboxRunPlan.from_dict(_sandbox_run_plan)

        _sync_oci_plan = d.pop("sync_oci_plan", UNSET)
        sync_oci_plan: Union[Unset, PlantypesSyncOCIPlan]
        if isinstance(_sync_oci_plan, Unset):
            sync_oci_plan = UNSET
        else:
            sync_oci_plan = PlantypesSyncOCIPlan.from_dict(_sync_oci_plan)

        _sync_secrets_plan = d.pop("sync_secrets_plan", UNSET)
        sync_secrets_plan: Union[Unset, PlantypesSyncSecretsPlan]
        if isinstance(_sync_secrets_plan, Unset):
            sync_secrets_plan = UNSET
        else:
            sync_secrets_plan = PlantypesSyncSecretsPlan.from_dict(_sync_secrets_plan)

        plantypes_composite_plan = cls(
            action_workflow_run_plan=action_workflow_run_plan,
            build_plan=build_plan,
            deploy_plan=deploy_plan,
            sandbox_run_plan=sandbox_run_plan,
            sync_oci_plan=sync_oci_plan,
            sync_secrets_plan=sync_secrets_plan,
        )

        plantypes_composite_plan.additional_properties = d
        return plantypes_composite_plan

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
