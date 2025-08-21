from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_workflow_step_response_type import AppWorkflowStepResponseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppWorkflowStepApprovalResponse")


@_attrs_define
class AppWorkflowStepApprovalResponse:
    """
    Attributes:
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        id (Union[Unset, str]):
        install_workflow_step_approval_id (Union[Unset, str]): the approval the response belongs to
        note (Union[Unset, str]):
        type_ (Union[Unset, AppWorkflowStepResponseType]):
        updated_at (Union[Unset, str]):
    """

    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    install_workflow_step_approval_id: Union[Unset, str] = UNSET
    note: Union[Unset, str] = UNSET
    type_: Union[Unset, AppWorkflowStepResponseType] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        install_workflow_step_approval_id = self.install_workflow_step_approval_id

        note = self.note

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
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
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        install_workflow_step_approval_id = d.pop("install_workflow_step_approval_id", UNSET)

        note = d.pop("note", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, AppWorkflowStepResponseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AppWorkflowStepResponseType(_type_)

        updated_at = d.pop("updated_at", UNSET)

        app_workflow_step_approval_response = cls(
            created_at=created_at,
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
