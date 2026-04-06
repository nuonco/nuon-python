from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plantypes_composite_plan import PlantypesCompositePlan


T = TypeVar("T", bound="AppRunnerJobPlan")


@_attrs_define
class AppRunnerJobPlan:
    """
    Attributes:
        composite_plan (PlantypesCompositePlan | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        org_id (str | Unset):
        plan_json (str | Unset):
        runner_job_id (str | Unset):
        updated_at (str | Unset):
    """

    composite_plan: PlantypesCompositePlan | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    org_id: str | Unset = UNSET
    plan_json: str | Unset = UNSET
    runner_job_id: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        composite_plan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.composite_plan, Unset):
            composite_plan = self.composite_plan.to_dict()

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        org_id = self.org_id

        plan_json = self.plan_json

        runner_job_id = self.runner_job_id

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if composite_plan is not UNSET:
            field_dict["composite_plan"] = composite_plan
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if plan_json is not UNSET:
            field_dict["plan_json"] = plan_json
        if runner_job_id is not UNSET:
            field_dict["runner_job_id"] = runner_job_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plantypes_composite_plan import PlantypesCompositePlan

        d = dict(src_dict)
        _composite_plan = d.pop("composite_plan", UNSET)
        composite_plan: PlantypesCompositePlan | Unset
        if isinstance(_composite_plan, Unset):
            composite_plan = UNSET
        else:
            composite_plan = PlantypesCompositePlan.from_dict(_composite_plan)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        org_id = d.pop("org_id", UNSET)

        plan_json = d.pop("plan_json", UNSET)

        runner_job_id = d.pop("runner_job_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_runner_job_plan = cls(
            composite_plan=composite_plan,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            org_id=org_id,
            plan_json=plan_json,
            runner_job_id=runner_job_id,
            updated_at=updated_at,
        )

        app_runner_job_plan.additional_properties = d
        return app_runner_job_plan

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
