from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_provider_type import AppProviderType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceAuthMeIdentity")


@_attrs_define
class ServiceAuthMeIdentity:
    """
    Attributes:
        name (str | Unset):
        picture (str | Unset):
        provider_type (AppProviderType | Unset):
    """

    name: str | Unset = UNSET
    picture: str | Unset = UNSET
    provider_type: AppProviderType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        picture = self.picture

        provider_type: str | Unset = UNSET
        if not isinstance(self.provider_type, Unset):
            provider_type = self.provider_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if picture is not UNSET:
            field_dict["picture"] = picture
        if provider_type is not UNSET:
            field_dict["provider_type"] = provider_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        picture = d.pop("picture", UNSET)

        _provider_type = d.pop("provider_type", UNSET)
        provider_type: AppProviderType | Unset
        if isinstance(_provider_type, Unset):
            provider_type = UNSET
        else:
            provider_type = AppProviderType(_provider_type)

        service_auth_me_identity = cls(
            name=name,
            picture=picture,
            provider_type=provider_type,
        )

        service_auth_me_identity.additional_properties = d
        return service_auth_me_identity

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
