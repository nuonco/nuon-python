from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceBundleResponse")


@_attrs_define
class ServiceBundleResponse:
    """
    Attributes:
        app_config_id (str | Unset):
        app_id (str | Unset):
        created_at (str | Unset):
        id (str | Unset):
        manifest_digest (str | Unset):
        oci_index_digest (str | Unset):
        oci_root_digest (str | Unset):
        schema_version (int | Unset):
        size (int | Unset):
        status (str | Unset):
        status_description (str | Unset):
        target_platform (str | Unset):
        transport_checksum (str | Unset):
        verified_at (str | Unset):
    """

    app_config_id: str | Unset = UNSET
    app_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    id: str | Unset = UNSET
    manifest_digest: str | Unset = UNSET
    oci_index_digest: str | Unset = UNSET
    oci_root_digest: str | Unset = UNSET
    schema_version: int | Unset = UNSET
    size: int | Unset = UNSET
    status: str | Unset = UNSET
    status_description: str | Unset = UNSET
    target_platform: str | Unset = UNSET
    transport_checksum: str | Unset = UNSET
    verified_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config_id = self.app_config_id

        app_id = self.app_id

        created_at = self.created_at

        id = self.id

        manifest_digest = self.manifest_digest

        oci_index_digest = self.oci_index_digest

        oci_root_digest = self.oci_root_digest

        schema_version = self.schema_version

        size = self.size

        status = self.status

        status_description = self.status_description

        target_platform = self.target_platform

        transport_checksum = self.transport_checksum

        verified_at = self.verified_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if manifest_digest is not UNSET:
            field_dict["manifest_digest"] = manifest_digest
        if oci_index_digest is not UNSET:
            field_dict["oci_index_digest"] = oci_index_digest
        if oci_root_digest is not UNSET:
            field_dict["oci_root_digest"] = oci_root_digest
        if schema_version is not UNSET:
            field_dict["schema_version"] = schema_version
        if size is not UNSET:
            field_dict["size"] = size
        if status is not UNSET:
            field_dict["status"] = status
        if status_description is not UNSET:
            field_dict["status_description"] = status_description
        if target_platform is not UNSET:
            field_dict["target_platform"] = target_platform
        if transport_checksum is not UNSET:
            field_dict["transport_checksum"] = transport_checksum
        if verified_at is not UNSET:
            field_dict["verified_at"] = verified_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_config_id = d.pop("app_config_id", UNSET)

        app_id = d.pop("app_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        id = d.pop("id", UNSET)

        manifest_digest = d.pop("manifest_digest", UNSET)

        oci_index_digest = d.pop("oci_index_digest", UNSET)

        oci_root_digest = d.pop("oci_root_digest", UNSET)

        schema_version = d.pop("schema_version", UNSET)

        size = d.pop("size", UNSET)

        status = d.pop("status", UNSET)

        status_description = d.pop("status_description", UNSET)

        target_platform = d.pop("target_platform", UNSET)

        transport_checksum = d.pop("transport_checksum", UNSET)

        verified_at = d.pop("verified_at", UNSET)

        service_bundle_response = cls(
            app_config_id=app_config_id,
            app_id=app_id,
            created_at=created_at,
            id=id,
            manifest_digest=manifest_digest,
            oci_index_digest=oci_index_digest,
            oci_root_digest=oci_root_digest,
            schema_version=schema_version,
            size=size,
            status=status,
            status_description=status_description,
            target_platform=target_platform,
            transport_checksum=transport_checksum,
            verified_at=verified_at,
        )

        service_bundle_response.additional_properties = d
        return service_bundle_response

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
