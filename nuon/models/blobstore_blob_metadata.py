from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BlobstoreBlobMetadata")


@_attrs_define
class BlobstoreBlobMetadata:
    """
    Attributes:
        blob_id (str | Unset): S3 key (blob_id)
        checksum (str | Unset): SHA256 checksum
        content_type (str | Unset): MIME type
        created_at (str | Unset): ISO 8601 timestamp
        created_by (str | Unset): Account ID who created the blob
        s3_key (str | Unset): Full S3 path: org_id/blob_id
        size (int | Unset): Size in bytes
    """

    blob_id: str | Unset = UNSET
    checksum: str | Unset = UNSET
    content_type: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by: str | Unset = UNSET
    s3_key: str | Unset = UNSET
    size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        blob_id = self.blob_id

        checksum = self.checksum

        content_type = self.content_type

        created_at = self.created_at

        created_by = self.created_by

        s3_key = self.s3_key

        size = self.size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if blob_id is not UNSET:
            field_dict["blob_id"] = blob_id
        if checksum is not UNSET:
            field_dict["checksum"] = checksum
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if s3_key is not UNSET:
            field_dict["s3_key"] = s3_key
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        blob_id = d.pop("blob_id", UNSET)

        checksum = d.pop("checksum", UNSET)

        content_type = d.pop("content_type", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by = d.pop("created_by", UNSET)

        s3_key = d.pop("s3_key", UNSET)

        size = d.pop("size", UNSET)

        blobstore_blob_metadata = cls(
            blob_id=blob_id,
            checksum=checksum,
            content_type=content_type,
            created_at=created_at,
            created_by=created_by,
            s3_key=s3_key,
            size=size,
        )

        blobstore_blob_metadata.additional_properties = d
        return blobstore_blob_metadata

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
