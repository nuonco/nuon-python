from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_account import AppAccount


T = TypeVar("T", bound="AppWorkflowStepApprovalResponse")


@_attrs_define
class AppWorkflowStepApprovalResponse:
    """
    Attributes:
        created_at (str | Unset):
        created_by (AppAccount | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        install_workflow_step_approval_id (str | Unset):
        note (str | Unset):
        type_ (str | Unset): the response type
        updated_at (str | Unset):
    """

    created_at: str | Unset = UNSET
    created_by: AppAccount | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    install_workflow_step_approval_id: str | Unset = UNSET
    note: str | Unset = UNSET
    type_: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        created_by_id = self.created_by_id

        id = self.id

        install_workflow_step_approval_id = self.install_workflow_step_approval_id

        note = self.note

        type_ = self.type_

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if install_workflow_step_approval_id is not UNSET:
            field_dict["install_workflow_step_approval_id"] = install_workflow_step_approval_id
        if note is not UNSET:
            field_dict["note"] = note
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_account import AppAccount  # noqa: PLC0415

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        _created_by = d.pop("created_by", UNSET)
        created_by: AppAccount | Unset
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = AppAccount.from_dict(_created_by)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        install_workflow_step_approval_id = d.pop("install_workflow_step_approval_id", UNSET)

        note = d.pop("note", UNSET)

        type_ = d.pop("type", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_workflow_step_approval_response = cls(
            created_at=created_at,
            created_by=created_by,
            created_by_id=created_by_id,
            id=id,
            install_workflow_step_approval_id=install_workflow_step_approval_id,
            note=note,
            type_=type_,
            updated_at=updated_at,
        )

        app_workflow_step_approval_response.additional_properties = d
        return app_workflow_step_approval_response

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
