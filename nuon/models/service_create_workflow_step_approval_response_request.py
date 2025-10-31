from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_workflow_step_response_type import AppWorkflowStepResponseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceCreateWorkflowStepApprovalResponseRequest")


@_attrs_define
class ServiceCreateWorkflowStepApprovalResponseRequest:
    """
    Attributes:
        note (str | Unset):
        response_type (AppWorkflowStepResponseType | Unset):
    """

    note: str | Unset = UNSET
    response_type: AppWorkflowStepResponseType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        note = self.note

        response_type: str | Unset = UNSET
        if not isinstance(self.response_type, Unset):
            response_type = self.response_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if note is not UNSET:
            field_dict["note"] = note
        if response_type is not UNSET:
            field_dict["response_type"] = response_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        note = d.pop("note", UNSET)

        _response_type = d.pop("response_type", UNSET)
        response_type: AppWorkflowStepResponseType | Unset
        if isinstance(_response_type, Unset):
            response_type = UNSET
        else:
            response_type = AppWorkflowStepResponseType(_response_type)

        service_create_workflow_step_approval_response_request = cls(
            note=note,
            response_type=response_type,
        )

        service_create_workflow_step_approval_response_request.additional_properties = d
        return service_create_workflow_step_approval_response_request

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
