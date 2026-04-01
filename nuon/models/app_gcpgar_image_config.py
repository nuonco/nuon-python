from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppGCPGARImageConfig")


@_attrs_define
class AppGCPGARImageConfig:
    """
    Attributes:
        component_config_id (str | Unset):
        component_config_type (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        gcp_project_id (str | Unset):
        gcp_region (str | Unset):
        id (str | Unset):
        service_account_email (str | Unset):
        updated_at (str | Unset):
        workload_identity_provider (str | Unset):
    """

    component_config_id: str | Unset = UNSET
    component_config_type: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    gcp_project_id: str | Unset = UNSET
    gcp_region: str | Unset = UNSET
    id: str | Unset = UNSET
    service_account_email: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    workload_identity_provider: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component_config_id = self.component_config_id

        component_config_type = self.component_config_type

        created_at = self.created_at

        created_by_id = self.created_by_id

        gcp_project_id = self.gcp_project_id

        gcp_region = self.gcp_region

        id = self.id

        service_account_email = self.service_account_email

        updated_at = self.updated_at

        workload_identity_provider = self.workload_identity_provider

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if component_config_id is not UNSET:
            field_dict["component_config_id"] = component_config_id
        if component_config_type is not UNSET:
            field_dict["component_config_type"] = component_config_type
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if gcp_project_id is not UNSET:
            field_dict["gcp_project_id"] = gcp_project_id
        if gcp_region is not UNSET:
            field_dict["gcp_region"] = gcp_region
        if id is not UNSET:
            field_dict["id"] = id
        if service_account_email is not UNSET:
            field_dict["service_account_email"] = service_account_email
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if workload_identity_provider is not UNSET:
            field_dict["workload_identity_provider"] = workload_identity_provider

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        component_config_id = d.pop("component_config_id", UNSET)

        component_config_type = d.pop("component_config_type", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        gcp_project_id = d.pop("gcp_project_id", UNSET)

        gcp_region = d.pop("gcp_region", UNSET)

        id = d.pop("id", UNSET)

        service_account_email = d.pop("service_account_email", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        workload_identity_provider = d.pop("workload_identity_provider", UNSET)

        app_gcpgar_image_config = cls(
            component_config_id=component_config_id,
            component_config_type=component_config_type,
            created_at=created_at,
            created_by_id=created_by_id,
            gcp_project_id=gcp_project_id,
            gcp_region=gcp_region,
            id=id,
            service_account_email=service_account_email,
            updated_at=updated_at,
            workload_identity_provider=workload_identity_provider,
        )

        app_gcpgar_image_config.additional_properties = d
        return app_gcpgar_image_config

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
