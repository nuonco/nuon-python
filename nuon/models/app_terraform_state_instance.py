from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_terraform_state_instance_attributes import AppTerraformStateInstanceAttributes


T = TypeVar("T", bound="AppTerraformStateInstance")


@_attrs_define
class AppTerraformStateInstance:
    """
    Attributes:
        attributes (AppTerraformStateInstanceAttributes | Unset):
        schema_version (int | Unset):
        sensitive_attributes (list[Any] | Unset):
    """

    attributes: AppTerraformStateInstanceAttributes | Unset = UNSET
    schema_version: int | Unset = UNSET
    sensitive_attributes: list[Any] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        schema_version = self.schema_version

        sensitive_attributes: list[Any] | Unset = UNSET
        if not isinstance(self.sensitive_attributes, Unset):
            sensitive_attributes = self.sensitive_attributes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if schema_version is not UNSET:
            field_dict["schema_version"] = schema_version
        if sensitive_attributes is not UNSET:
            field_dict["sensitive_attributes"] = sensitive_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_terraform_state_instance_attributes import AppTerraformStateInstanceAttributes

        d = dict(src_dict)
        _attributes = d.pop("attributes", UNSET)
        attributes: AppTerraformStateInstanceAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = AppTerraformStateInstanceAttributes.from_dict(_attributes)

        schema_version = d.pop("schema_version", UNSET)

        sensitive_attributes = cast(list[Any], d.pop("sensitive_attributes", UNSET))

        app_terraform_state_instance = cls(
            attributes=attributes,
            schema_version=schema_version,
            sensitive_attributes=sensitive_attributes,
        )

        app_terraform_state_instance.additional_properties = d
        return app_terraform_state_instance

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
