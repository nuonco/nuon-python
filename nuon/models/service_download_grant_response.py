from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceDownloadGrantResponse")


@_attrs_define
class ServiceDownloadGrantResponse:
    """
    Attributes:
        expires_at (str | Unset):
        filename (str | Unset):
        manifest_digest (str | Unset):
        size (int | Unset):
        supports_range (bool | Unset):
        transport_checksum (str | Unset):
        url (str | Unset):
    """

    expires_at: str | Unset = UNSET
    filename: str | Unset = UNSET
    manifest_digest: str | Unset = UNSET
    size: int | Unset = UNSET
    supports_range: bool | Unset = UNSET
    transport_checksum: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expires_at = self.expires_at

        filename = self.filename

        manifest_digest = self.manifest_digest

        size = self.size

        supports_range = self.supports_range

        transport_checksum = self.transport_checksum

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if filename is not UNSET:
            field_dict["filename"] = filename
        if manifest_digest is not UNSET:
            field_dict["manifest_digest"] = manifest_digest
        if size is not UNSET:
            field_dict["size"] = size
        if supports_range is not UNSET:
            field_dict["supports_range"] = supports_range
        if transport_checksum is not UNSET:
            field_dict["transport_checksum"] = transport_checksum
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expires_at = d.pop("expires_at", UNSET)

        filename = d.pop("filename", UNSET)

        manifest_digest = d.pop("manifest_digest", UNSET)

        size = d.pop("size", UNSET)

        supports_range = d.pop("supports_range", UNSET)

        transport_checksum = d.pop("transport_checksum", UNSET)

        url = d.pop("url", UNSET)

        service_download_grant_response = cls(
            expires_at=expires_at,
            filename=filename,
            manifest_digest=manifest_digest,
            size=size,
            supports_range=supports_range,
            transport_checksum=transport_checksum,
            url=url,
        )

        service_download_grant_response.additional_properties = d
        return service_download_grant_response

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
