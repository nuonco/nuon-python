from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_workflow_type import AppWorkflowType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceInstallAlignmentOpenDeployment")


@_attrs_define
class ServiceInstallAlignmentOpenDeployment:
    """
    Attributes:
        created_at (str | Unset):
        id (str | Unset):
        status (str | Unset):
        type_ (AppWorkflowType | Unset):
    """

    created_at: str | Unset = UNSET
    id: str | Unset = UNSET
    status: str | Unset = UNSET
    type_: AppWorkflowType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        id = self.id

        status = self.status

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        id = d.pop("id", UNSET)

        status = d.pop("status", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: AppWorkflowType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AppWorkflowType(_type_)

        service_install_alignment_open_deployment = cls(
            created_at=created_at,
            id=id,
            status=status,
            type_=type_,
        )

        service_install_alignment_open_deployment.additional_properties = d
        return service_install_alignment_open_deployment

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
