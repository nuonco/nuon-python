from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlantypesKubernetesSecretSync")


@_attrs_define
class PlantypesKubernetesSecretSync:
    """
    Attributes:
        format_ (str | Unset): NOTE(jm): this should probably come from the app config, but for now we just use string
            parsing to avoid
            updating the runner job and save time.
        key_name (str | Unset):
        name (str | Unset):
        namespace (str | Unset):
        secret_arn (str | Unset):
        secret_name (str | Unset): the name of the secret from the config
    """

    format_: str | Unset = UNSET
    key_name: str | Unset = UNSET
    name: str | Unset = UNSET
    namespace: str | Unset = UNSET
    secret_arn: str | Unset = UNSET
    secret_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        format_ = self.format_

        key_name = self.key_name

        name = self.name

        namespace = self.namespace

        secret_arn = self.secret_arn

        secret_name = self.secret_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if format_ is not UNSET:
            field_dict["format"] = format_
        if key_name is not UNSET:
            field_dict["key_name"] = key_name
        if name is not UNSET:
            field_dict["name"] = name
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if secret_arn is not UNSET:
            field_dict["secret_arn"] = secret_arn
        if secret_name is not UNSET:
            field_dict["secret_name"] = secret_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        format_ = d.pop("format", UNSET)

        key_name = d.pop("key_name", UNSET)

        name = d.pop("name", UNSET)

        namespace = d.pop("namespace", UNSET)

        secret_arn = d.pop("secret_arn", UNSET)

        secret_name = d.pop("secret_name", UNSET)

        plantypes_kubernetes_secret_sync = cls(
            format_=format_,
            key_name=key_name,
            name=name,
            namespace=namespace,
            secret_arn=secret_arn,
            secret_name=secret_name,
        )

        plantypes_kubernetes_secret_sync.additional_properties = d
        return plantypes_kubernetes_secret_sync

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
