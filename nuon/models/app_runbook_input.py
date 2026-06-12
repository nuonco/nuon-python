from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppRunbookInput")


@_attrs_define
class AppRunbookInput:
    """
    Attributes:
        created_at (str | Unset):
        created_by_id (str | Unset):
        default (str | Unset):
        description (str | Unset):
        display_name (str | Unset):
        id (str | Unset):
        idx (int | Unset):
        name (str | Unset):
        required (bool | Unset):
        runbook_config_id (str | Unset):
        sensitive (bool | Unset):
        type_ (str | Unset):
        updated_at (str | Unset):
    """

    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    default: str | Unset = UNSET
    description: str | Unset = UNSET
    display_name: str | Unset = UNSET
    id: str | Unset = UNSET
    idx: int | Unset = UNSET
    name: str | Unset = UNSET
    required: bool | Unset = UNSET
    runbook_config_id: str | Unset = UNSET
    sensitive: bool | Unset = UNSET
    type_: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        default = self.default

        description = self.description

        display_name = self.display_name

        id = self.id

        idx = self.idx

        name = self.name

        required = self.required

        runbook_config_id = self.runbook_config_id

        sensitive = self.sensitive

        type_ = self.type_

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if default is not UNSET:
            field_dict["default"] = default
        if description is not UNSET:
            field_dict["description"] = description
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if id is not UNSET:
            field_dict["id"] = id
        if idx is not UNSET:
            field_dict["idx"] = idx
        if name is not UNSET:
            field_dict["name"] = name
        if required is not UNSET:
            field_dict["required"] = required
        if runbook_config_id is not UNSET:
            field_dict["runbook_config_id"] = runbook_config_id
        if sensitive is not UNSET:
            field_dict["sensitive"] = sensitive
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

        default = d.pop("default", UNSET)

        description = d.pop("description", UNSET)

        display_name = d.pop("display_name", UNSET)

        id = d.pop("id", UNSET)

        idx = d.pop("idx", UNSET)

        name = d.pop("name", UNSET)

        required = d.pop("required", UNSET)

        runbook_config_id = d.pop("runbook_config_id", UNSET)

        sensitive = d.pop("sensitive", UNSET)

        type_ = d.pop("type", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_runbook_input = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            default=default,
            description=description,
            display_name=display_name,
            id=id,
            idx=idx,
            name=name,
            required=required,
            runbook_config_id=runbook_config_id,
            sensitive=sensitive,
            type_=type_,
            updated_at=updated_at,
        )

        app_runbook_input.additional_properties = d
        return app_runbook_input

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
