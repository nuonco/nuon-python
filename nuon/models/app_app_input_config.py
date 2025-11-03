from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_app_input import AppAppInput
    from ..models.app_app_input_group import AppAppInputGroup
    from ..models.app_install_inputs import AppInstallInputs


T = TypeVar("T", bound="AppAppInputConfig")


@_attrs_define
class AppAppInputConfig:
    """
    Attributes:
        app_config_id (str | Unset):
        app_id (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        input_groups (list[AppAppInputGroup] | Unset):
        inputs (list[AppAppInput] | Unset):
        install_inputs (list[AppInstallInputs] | Unset):
        org_id (str | Unset):
        updated_at (str | Unset):
    """

    app_config_id: str | Unset = UNSET
    app_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    input_groups: list[AppAppInputGroup] | Unset = UNSET
    inputs: list[AppAppInput] | Unset = UNSET
    install_inputs: list[AppInstallInputs] | Unset = UNSET
    org_id: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config_id = self.app_config_id

        app_id = self.app_id

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        input_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.input_groups, Unset):
            input_groups = []
            for input_groups_item_data in self.input_groups:
                input_groups_item = input_groups_item_data.to_dict()
                input_groups.append(input_groups_item)

        inputs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.inputs, Unset):
            inputs = []
            for inputs_item_data in self.inputs:
                inputs_item = inputs_item_data.to_dict()
                inputs.append(inputs_item)

        install_inputs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.install_inputs, Unset):
            install_inputs = []
            for install_inputs_item_data in self.install_inputs:
                install_inputs_item = install_inputs_item_data.to_dict()
                install_inputs.append(install_inputs_item)

        org_id = self.org_id

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if input_groups is not UNSET:
            field_dict["input_groups"] = input_groups
        if inputs is not UNSET:
            field_dict["inputs"] = inputs
        if install_inputs is not UNSET:
            field_dict["install_inputs"] = install_inputs
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_app_input import AppAppInput
        from ..models.app_app_input_group import AppAppInputGroup
        from ..models.app_install_inputs import AppInstallInputs

        d = dict(src_dict)
        app_config_id = d.pop("app_config_id", UNSET)

        app_id = d.pop("app_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        _input_groups = d.pop("input_groups", UNSET)
        input_groups: list[AppAppInputGroup] | Unset = UNSET
        if _input_groups is not UNSET:
            input_groups = []
            for input_groups_item_data in _input_groups:
                input_groups_item = AppAppInputGroup.from_dict(input_groups_item_data)

                input_groups.append(input_groups_item)

        _inputs = d.pop("inputs", UNSET)
        inputs: list[AppAppInput] | Unset = UNSET
        if _inputs is not UNSET:
            inputs = []
            for inputs_item_data in _inputs:
                inputs_item = AppAppInput.from_dict(inputs_item_data)

                inputs.append(inputs_item)

        _install_inputs = d.pop("install_inputs", UNSET)
        install_inputs: list[AppInstallInputs] | Unset = UNSET
        if _install_inputs is not UNSET:
            install_inputs = []
            for install_inputs_item_data in _install_inputs:
                install_inputs_item = AppInstallInputs.from_dict(install_inputs_item_data)

                install_inputs.append(install_inputs_item)

        org_id = d.pop("org_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_app_input_config = cls(
            app_config_id=app_config_id,
            app_id=app_id,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            input_groups=input_groups,
            inputs=inputs,
            install_inputs=install_inputs,
            org_id=org_id,
            updated_at=updated_at,
        )

        app_app_input_config.additional_properties = d
        return app_app_input_config

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
