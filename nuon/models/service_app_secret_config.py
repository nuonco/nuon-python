from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceAppSecretConfig")


@_attrs_define
class ServiceAppSecretConfig:
    """
    Attributes:
        description (str):
        display_name (str):
        name (str):
        auto_generate (bool | Unset):
        default (str | Unset):
        format_ (str | Unset):
        kubernetes_secret_name (str | Unset):
        kubernetes_secret_namespace (str | Unset):
        kubernetes_sync (bool | Unset):
        required (bool | Unset):
    """

    description: str
    display_name: str
    name: str
    auto_generate: bool | Unset = UNSET
    default: str | Unset = UNSET
    format_: str | Unset = UNSET
    kubernetes_secret_name: str | Unset = UNSET
    kubernetes_secret_namespace: str | Unset = UNSET
    kubernetes_sync: bool | Unset = UNSET
    required: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        display_name = self.display_name

        name = self.name

        auto_generate = self.auto_generate

        default = self.default

        format_ = self.format_

        kubernetes_secret_name = self.kubernetes_secret_name

        kubernetes_secret_namespace = self.kubernetes_secret_namespace

        kubernetes_sync = self.kubernetes_sync

        required = self.required

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "display_name": display_name,
                "name": name,
            }
        )
        if auto_generate is not UNSET:
            field_dict["auto_generate"] = auto_generate
        if default is not UNSET:
            field_dict["default"] = default
        if format_ is not UNSET:
            field_dict["format"] = format_
        if kubernetes_secret_name is not UNSET:
            field_dict["kubernetes_secret_name"] = kubernetes_secret_name
        if kubernetes_secret_namespace is not UNSET:
            field_dict["kubernetes_secret_namespace"] = kubernetes_secret_namespace
        if kubernetes_sync is not UNSET:
            field_dict["kubernetes_sync"] = kubernetes_sync
        if required is not UNSET:
            field_dict["required"] = required

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        display_name = d.pop("display_name")

        name = d.pop("name")

        auto_generate = d.pop("auto_generate", UNSET)

        default = d.pop("default", UNSET)

        format_ = d.pop("format", UNSET)

        kubernetes_secret_name = d.pop("kubernetes_secret_name", UNSET)

        kubernetes_secret_namespace = d.pop("kubernetes_secret_namespace", UNSET)

        kubernetes_sync = d.pop("kubernetes_sync", UNSET)

        required = d.pop("required", UNSET)

        service_app_secret_config = cls(
            description=description,
            display_name=display_name,
            name=name,
            auto_generate=auto_generate,
            default=default,
            format_=format_,
            kubernetes_secret_name=kubernetes_secret_name,
            kubernetes_secret_namespace=kubernetes_secret_namespace,
            kubernetes_sync=kubernetes_sync,
            required=required,
        )

        service_app_secret_config.additional_properties = d
        return service_app_secret_config

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
