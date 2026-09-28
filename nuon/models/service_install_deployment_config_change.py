from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceInstallDeploymentConfigChange")


@_attrs_define
class ServiceInstallDeploymentConfigChange:
    """
    Attributes:
        is_redacted (bool | Unset):
        next_value (str | Unset):
        operation (str | Unset):
        path (str | Unset):
        previous_value (str | Unset):
    """

    is_redacted: bool | Unset = UNSET
    next_value: str | Unset = UNSET
    operation: str | Unset = UNSET
    path: str | Unset = UNSET
    previous_value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_redacted = self.is_redacted

        next_value = self.next_value

        operation = self.operation

        path = self.path

        previous_value = self.previous_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_redacted is not UNSET:
            field_dict["is_redacted"] = is_redacted
        if next_value is not UNSET:
            field_dict["next_value"] = next_value
        if operation is not UNSET:
            field_dict["operation"] = operation
        if path is not UNSET:
            field_dict["path"] = path
        if previous_value is not UNSET:
            field_dict["previous_value"] = previous_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_redacted = d.pop("is_redacted", UNSET)

        next_value = d.pop("next_value", UNSET)

        operation = d.pop("operation", UNSET)

        path = d.pop("path", UNSET)

        previous_value = d.pop("previous_value", UNSET)

        service_install_deployment_config_change = cls(
            is_redacted=is_redacted,
            next_value=next_value,
            operation=operation,
            path=path,
            previous_value=previous_value,
        )

        service_install_deployment_config_change.additional_properties = d
        return service_install_deployment_config_change

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
