from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceCreateRunbookInputRequest")


@_attrs_define
class ServiceCreateRunbookInputRequest:
    """
    Attributes:
        name (str):
        default (str | Unset):
        description (str | Unset):
        display_name (str | Unset):
        required (bool | Unset):
        sensitive (bool | Unset):
        type_ (str | Unset):
    """

    name: str
    default: str | Unset = UNSET
    description: str | Unset = UNSET
    display_name: str | Unset = UNSET
    required: bool | Unset = UNSET
    sensitive: bool | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        default = self.default

        description = self.description

        display_name = self.display_name

        required = self.required

        sensitive = self.sensitive

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if default is not UNSET:
            field_dict["default"] = default
        if description is not UNSET:
            field_dict["description"] = description
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if required is not UNSET:
            field_dict["required"] = required
        if sensitive is not UNSET:
            field_dict["sensitive"] = sensitive
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        default = d.pop("default", UNSET)

        description = d.pop("description", UNSET)

        display_name = d.pop("display_name", UNSET)

        required = d.pop("required", UNSET)

        sensitive = d.pop("sensitive", UNSET)

        type_ = d.pop("type", UNSET)

        service_create_runbook_input_request = cls(
            name=name,
            default=default,
            description=description,
            display_name=display_name,
            required=required,
            sensitive=sensitive,
            type_=type_,
        )

        service_create_runbook_input_request.additional_properties = d
        return service_create_runbook_input_request

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
