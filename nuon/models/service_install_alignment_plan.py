from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_workflow_step_approval_type import AppWorkflowStepApprovalType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceInstallAlignmentPlan")


@_attrs_define
class ServiceInstallAlignmentPlan:
    """
    Attributes:
        approval_id (str | Unset):
        changes_create (int | Unset):
        changes_delete (int | Unset):
        changes_noop (int | Unset):
        changes_replace (int | Unset):
        changes_update (int | Unset):
        created_at (str | Unset):
        owner_id (str | Unset):
        owner_type (str | Unset):
        plan_only (bool | Unset):
        step_id (str | Unset):
        type_ (AppWorkflowStepApprovalType | Unset):
        workflow_id (str | Unset):
    """

    approval_id: str | Unset = UNSET
    changes_create: int | Unset = UNSET
    changes_delete: int | Unset = UNSET
    changes_noop: int | Unset = UNSET
    changes_replace: int | Unset = UNSET
    changes_update: int | Unset = UNSET
    created_at: str | Unset = UNSET
    owner_id: str | Unset = UNSET
    owner_type: str | Unset = UNSET
    plan_only: bool | Unset = UNSET
    step_id: str | Unset = UNSET
    type_: AppWorkflowStepApprovalType | Unset = UNSET
    workflow_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        approval_id = self.approval_id

        changes_create = self.changes_create

        changes_delete = self.changes_delete

        changes_noop = self.changes_noop

        changes_replace = self.changes_replace

        changes_update = self.changes_update

        created_at = self.created_at

        owner_id = self.owner_id

        owner_type = self.owner_type

        plan_only = self.plan_only

        step_id = self.step_id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        workflow_id = self.workflow_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if approval_id is not UNSET:
            field_dict["approval_id"] = approval_id
        if changes_create is not UNSET:
            field_dict["changes_create"] = changes_create
        if changes_delete is not UNSET:
            field_dict["changes_delete"] = changes_delete
        if changes_noop is not UNSET:
            field_dict["changes_noop"] = changes_noop
        if changes_replace is not UNSET:
            field_dict["changes_replace"] = changes_replace
        if changes_update is not UNSET:
            field_dict["changes_update"] = changes_update
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if owner_type is not UNSET:
            field_dict["owner_type"] = owner_type
        if plan_only is not UNSET:
            field_dict["plan_only"] = plan_only
        if step_id is not UNSET:
            field_dict["step_id"] = step_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if workflow_id is not UNSET:
            field_dict["workflow_id"] = workflow_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        approval_id = d.pop("approval_id", UNSET)

        changes_create = d.pop("changes_create", UNSET)

        changes_delete = d.pop("changes_delete", UNSET)

        changes_noop = d.pop("changes_noop", UNSET)

        changes_replace = d.pop("changes_replace", UNSET)

        changes_update = d.pop("changes_update", UNSET)

        created_at = d.pop("created_at", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        owner_type = d.pop("owner_type", UNSET)

        plan_only = d.pop("plan_only", UNSET)

        step_id = d.pop("step_id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: AppWorkflowStepApprovalType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AppWorkflowStepApprovalType(_type_)

        workflow_id = d.pop("workflow_id", UNSET)

        service_install_alignment_plan = cls(
            approval_id=approval_id,
            changes_create=changes_create,
            changes_delete=changes_delete,
            changes_noop=changes_noop,
            changes_replace=changes_replace,
            changes_update=changes_update,
            created_at=created_at,
            owner_id=owner_id,
            owner_type=owner_type,
            plan_only=plan_only,
            step_id=step_id,
            type_=type_,
            workflow_id=workflow_id,
        )

        service_install_alignment_plan.additional_properties = d
        return service_install_alignment_plan

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
