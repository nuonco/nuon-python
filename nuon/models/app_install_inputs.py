from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_install_inputs_redacted_values import AppInstallInputsRedactedValues
    from ..models.app_install_inputs_values import AppInstallInputsValues


T = TypeVar("T", bound="AppInstallInputs")


@_attrs_define
class AppInstallInputs:
    """
    Attributes:
        app_input_config_id (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        install_id (str | Unset):
        org_id (str | Unset):
        redacted_values (AppInstallInputsRedactedValues | Unset):
        updated_at (str | Unset):
        values (AppInstallInputsValues | Unset):
    """

    app_input_config_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    install_id: str | Unset = UNSET
    org_id: str | Unset = UNSET
    redacted_values: AppInstallInputsRedactedValues | Unset = UNSET
    updated_at: str | Unset = UNSET
    values: AppInstallInputsValues | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_input_config_id = self.app_input_config_id

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        install_id = self.install_id

        org_id = self.org_id

        redacted_values: dict[str, Any] | Unset = UNSET
        if not isinstance(self.redacted_values, Unset):
            redacted_values = self.redacted_values.to_dict()

        updated_at = self.updated_at

        values: dict[str, Any] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = self.values.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_input_config_id is not UNSET:
            field_dict["app_input_config_id"] = app_input_config_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if redacted_values is not UNSET:
            field_dict["redacted_values"] = redacted_values
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_install_inputs_redacted_values import AppInstallInputsRedactedValues
        from ..models.app_install_inputs_values import AppInstallInputsValues

        d = dict(src_dict)
        app_input_config_id = d.pop("app_input_config_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        install_id = d.pop("install_id", UNSET)

        org_id = d.pop("org_id", UNSET)

        _redacted_values = d.pop("redacted_values", UNSET)
        redacted_values: AppInstallInputsRedactedValues | Unset
        if isinstance(_redacted_values, Unset):
            redacted_values = UNSET
        else:
            redacted_values = AppInstallInputsRedactedValues.from_dict(_redacted_values)

        updated_at = d.pop("updated_at", UNSET)

        _values = d.pop("values", UNSET)
        values: AppInstallInputsValues | Unset
        if isinstance(_values, Unset):
            values = UNSET
        else:
            values = AppInstallInputsValues.from_dict(_values)

        app_install_inputs = cls(
            app_input_config_id=app_input_config_id,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            install_id=install_id,
            org_id=org_id,
            redacted_values=redacted_values,
            updated_at=updated_at,
            values=values,
        )

        app_install_inputs.additional_properties = d
        return app_install_inputs

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
