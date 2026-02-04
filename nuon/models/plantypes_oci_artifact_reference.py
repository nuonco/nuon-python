from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlantypesOCIArtifactReference")


@_attrs_define
class PlantypesOCIArtifactReference:
    """
    Attributes:
        digest (str | Unset): Digest is the immutable artifact digest (e.g., sha256:abc123...)
        tag (str | Unset): Tag is the artifact tag (typically the build ID)
        url (str | Unset): URL is the full artifact URL (e.g., registry.nuon.co/org_id/app_id)
    """

    digest: str | Unset = UNSET
    tag: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        digest = self.digest

        tag = self.tag

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if digest is not UNSET:
            field_dict["digest"] = digest
        if tag is not UNSET:
            field_dict["tag"] = tag
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        digest = d.pop("digest", UNSET)

        tag = d.pop("tag", UNSET)

        url = d.pop("url", UNSET)

        plantypes_oci_artifact_reference = cls(
            digest=digest,
            tag=tag,
            url=url,
        )

        plantypes_oci_artifact_reference.additional_properties = d
        return plantypes_oci_artifact_reference

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
