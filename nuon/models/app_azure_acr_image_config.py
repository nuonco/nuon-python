from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppAzureACRImageConfig")


@_attrs_define
class AppAzureACRImageConfig:
    """
    Attributes:
        client_id (str | Unset):
        component_config_id (str | Unset): connection to parent model
        component_config_type (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        registry_url (str | Unset): actual configuration
        tenant_id (str | Unset):
        updated_at (str | Unset):
    """

    client_id: str | Unset = UNSET
    component_config_id: str | Unset = UNSET
    component_config_type: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    registry_url: str | Unset = UNSET
    tenant_id: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_id = self.client_id

        component_config_id = self.component_config_id

        component_config_type = self.component_config_type

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        registry_url = self.registry_url

        tenant_id = self.tenant_id

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if component_config_id is not UNSET:
            field_dict["component_config_id"] = component_config_id
        if component_config_type is not UNSET:
            field_dict["component_config_type"] = component_config_type
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if registry_url is not UNSET:
            field_dict["registry_url"] = registry_url
        if tenant_id is not UNSET:
            field_dict["tenant_id"] = tenant_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_id = d.pop("client_id", UNSET)

        component_config_id = d.pop("component_config_id", UNSET)

        component_config_type = d.pop("component_config_type", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        registry_url = d.pop("registry_url", UNSET)

        tenant_id = d.pop("tenant_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_azure_acr_image_config = cls(
            client_id=client_id,
            component_config_id=component_config_id,
            component_config_type=component_config_type,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            registry_url=registry_url,
            tenant_id=tenant_id,
            updated_at=updated_at,
        )

        app_azure_acr_image_config.additional_properties = d
        return app_azure_acr_image_config

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
