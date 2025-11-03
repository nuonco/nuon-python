from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_app_input import AppAppInput


T = TypeVar("T", bound="AppAppInputGroup")


@_attrs_define
class AppAppInputGroup:
    """
    Attributes:
        app_input_id (str | Unset):
        app_inputs (list[AppAppInput] | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        description (str | Unset):
        display_name (str | Unset):
        id (str | Unset):
        index (int | Unset):
        name (str | Unset):
        org_id (str | Unset):
        updated_at (str | Unset):
    """

    app_input_id: str | Unset = UNSET
    app_inputs: list[AppAppInput] | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    description: str | Unset = UNSET
    display_name: str | Unset = UNSET
    id: str | Unset = UNSET
    index: int | Unset = UNSET
    name: str | Unset = UNSET
    org_id: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_input_id = self.app_input_id

        app_inputs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.app_inputs, Unset):
            app_inputs = []
            for app_inputs_item_data in self.app_inputs:
                app_inputs_item = app_inputs_item_data.to_dict()
                app_inputs.append(app_inputs_item)

        created_at = self.created_at

        created_by_id = self.created_by_id

        description = self.description

        display_name = self.display_name

        id = self.id

        index = self.index

        name = self.name

        org_id = self.org_id

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_input_id is not UNSET:
            field_dict["app_input_id"] = app_input_id
        if app_inputs is not UNSET:
            field_dict["app_inputs"] = app_inputs
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if description is not UNSET:
            field_dict["description"] = description
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if id is not UNSET:
            field_dict["id"] = id
        if index is not UNSET:
            field_dict["index"] = index
        if name is not UNSET:
            field_dict["name"] = name
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_app_input import AppAppInput

        d = dict(src_dict)
        app_input_id = d.pop("app_input_id", UNSET)

        _app_inputs = d.pop("app_inputs", UNSET)
        app_inputs: list[AppAppInput] | Unset = UNSET
        if _app_inputs is not UNSET:
            app_inputs = []
            for app_inputs_item_data in _app_inputs:
                app_inputs_item = AppAppInput.from_dict(app_inputs_item_data)

                app_inputs.append(app_inputs_item)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        description = d.pop("description", UNSET)

        display_name = d.pop("display_name", UNSET)

        id = d.pop("id", UNSET)

        index = d.pop("index", UNSET)

        name = d.pop("name", UNSET)

        org_id = d.pop("org_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_app_input_group = cls(
            app_input_id=app_input_id,
            app_inputs=app_inputs,
            created_at=created_at,
            created_by_id=created_by_id,
            description=description,
            display_name=display_name,
            id=id,
            index=index,
            name=name,
            org_id=org_id,
            updated_at=updated_at,
        )

        app_app_input_group.additional_properties = d
        return app_app_input_group

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
