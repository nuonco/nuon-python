from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceAzureACRImageConfigRequest")


@_attrs_define
class ServiceAzureACRImageConfigRequest:
    """
    Attributes:
        client_id (str | Unset):
        registry_url (str | Unset):
        tenant_id (str | Unset):
    """

    client_id: str | Unset = UNSET
    registry_url: str | Unset = UNSET
    tenant_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_id = self.client_id

        registry_url = self.registry_url

        tenant_id = self.tenant_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if registry_url is not UNSET:
            field_dict["registry_url"] = registry_url
        if tenant_id is not UNSET:
            field_dict["tenant_id"] = tenant_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_id = d.pop("client_id", UNSET)

        registry_url = d.pop("registry_url", UNSET)

        tenant_id = d.pop("tenant_id", UNSET)

        service_azure_acr_image_config_request = cls(
            client_id=client_id,
            registry_url=registry_url,
            tenant_id=tenant_id,
        )

        service_azure_acr_image_config_request.additional_properties = d
        return service_azure_acr_image_config_request

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
