from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_workflow_type import AppWorkflowType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceInstallActivityWorkflowRef")


@_attrs_define
class ServiceInstallActivityWorkflowRef:
    """
    Attributes:
        id (str | Unset):
        name (str | Unset):
        type_ (AppWorkflowType | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: AppWorkflowType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: AppWorkflowType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AppWorkflowType(_type_)

        service_install_activity_workflow_ref = cls(
            id=id,
            name=name,
            type_=type_,
        )

        service_install_activity_workflow_ref.additional_properties = d
        return service_install_activity_workflow_ref

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
