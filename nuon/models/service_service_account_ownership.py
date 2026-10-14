from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceServiceAccountOwnership")


@_attrs_define
class ServiceServiceAccountOwnership:
    """
    Attributes:
        install_id (str | Unset):
        instance_key (str | Unset):
        owner_id (str | Unset):
        owner_name (str | Unset):
        owner_type (str | Unset):
        purpose (str | Unset):
    """

    install_id: str | Unset = UNSET
    instance_key: str | Unset = UNSET
    owner_id: str | Unset = UNSET
    owner_name: str | Unset = UNSET
    owner_type: str | Unset = UNSET
    purpose: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        install_id = self.install_id

        instance_key = self.instance_key

        owner_id = self.owner_id

        owner_name = self.owner_name

        owner_type = self.owner_type

        purpose = self.purpose

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if instance_key is not UNSET:
            field_dict["instance_key"] = instance_key
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if owner_name is not UNSET:
            field_dict["owner_name"] = owner_name
        if owner_type is not UNSET:
            field_dict["owner_type"] = owner_type
        if purpose is not UNSET:
            field_dict["purpose"] = purpose

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        install_id = d.pop("install_id", UNSET)

        instance_key = d.pop("instance_key", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        owner_name = d.pop("owner_name", UNSET)

        owner_type = d.pop("owner_type", UNSET)

        purpose = d.pop("purpose", UNSET)

        service_service_account_ownership = cls(
            install_id=install_id,
            instance_key=instance_key,
            owner_id=owner_id,
            owner_name=owner_name,
            owner_type=owner_type,
            purpose=purpose,
        )

        service_service_account_ownership.additional_properties = d
        return service_service_account_ownership

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
