from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_oci_artifact_annotations import AppOCIArtifactAnnotations


T = TypeVar("T", bound="AppOCIArtifact")


@_attrs_define
class AppOCIArtifact:
    """
    Attributes:
        annotations (AppOCIArtifactAnnotations | Unset):
        architecture (str | Unset):
        artifact_type (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        digest (str | Unset):
        id (str | Unset):
        media_type (str | Unset):
        org_id (str | Unset):
        os (str | Unset): Platform fields
        os_features (list[str] | Unset):
        os_version (str | Unset):
        owner_id (str | Unset):
        owner_type (str | Unset):
        repository (str | Unset):
        size (int | Unset):
        tag (str | Unset):
        updated_at (str | Unset):
        urls (list[str] | Unset):
        variant (str | Unset):
    """

    annotations: AppOCIArtifactAnnotations | Unset = UNSET
    architecture: str | Unset = UNSET
    artifact_type: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    digest: str | Unset = UNSET
    id: str | Unset = UNSET
    media_type: str | Unset = UNSET
    org_id: str | Unset = UNSET
    os: str | Unset = UNSET
    os_features: list[str] | Unset = UNSET
    os_version: str | Unset = UNSET
    owner_id: str | Unset = UNSET
    owner_type: str | Unset = UNSET
    repository: str | Unset = UNSET
    size: int | Unset = UNSET
    tag: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    urls: list[str] | Unset = UNSET
    variant: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        annotations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = self.annotations.to_dict()

        architecture = self.architecture

        artifact_type = self.artifact_type

        created_at = self.created_at

        created_by_id = self.created_by_id

        digest = self.digest

        id = self.id

        media_type = self.media_type

        org_id = self.org_id

        os = self.os

        os_features: list[str] | Unset = UNSET
        if not isinstance(self.os_features, Unset):
            os_features = self.os_features

        os_version = self.os_version

        owner_id = self.owner_id

        owner_type = self.owner_type

        repository = self.repository

        size = self.size

        tag = self.tag

        updated_at = self.updated_at

        urls: list[str] | Unset = UNSET
        if not isinstance(self.urls, Unset):
            urls = self.urls

        variant = self.variant

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if architecture is not UNSET:
            field_dict["architecture"] = architecture
        if artifact_type is not UNSET:
            field_dict["artifact_type"] = artifact_type
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if digest is not UNSET:
            field_dict["digest"] = digest
        if id is not UNSET:
            field_dict["id"] = id
        if media_type is not UNSET:
            field_dict["media_type"] = media_type
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if os is not UNSET:
            field_dict["os"] = os
        if os_features is not UNSET:
            field_dict["os_features"] = os_features
        if os_version is not UNSET:
            field_dict["os_version"] = os_version
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if owner_type is not UNSET:
            field_dict["owner_type"] = owner_type
        if repository is not UNSET:
            field_dict["repository"] = repository
        if size is not UNSET:
            field_dict["size"] = size
        if tag is not UNSET:
            field_dict["tag"] = tag
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if urls is not UNSET:
            field_dict["urls"] = urls
        if variant is not UNSET:
            field_dict["variant"] = variant

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_oci_artifact_annotations import AppOCIArtifactAnnotations

        d = dict(src_dict)
        _annotations = d.pop("annotations", UNSET)
        annotations: AppOCIArtifactAnnotations | Unset
        if isinstance(_annotations, Unset):
            annotations = UNSET
        else:
            annotations = AppOCIArtifactAnnotations.from_dict(_annotations)

        architecture = d.pop("architecture", UNSET)

        artifact_type = d.pop("artifact_type", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        digest = d.pop("digest", UNSET)

        id = d.pop("id", UNSET)

        media_type = d.pop("media_type", UNSET)

        org_id = d.pop("org_id", UNSET)

        os = d.pop("os", UNSET)

        os_features = cast(list[str], d.pop("os_features", UNSET))

        os_version = d.pop("os_version", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        owner_type = d.pop("owner_type", UNSET)

        repository = d.pop("repository", UNSET)

        size = d.pop("size", UNSET)

        tag = d.pop("tag", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        urls = cast(list[str], d.pop("urls", UNSET))

        variant = d.pop("variant", UNSET)

        app_oci_artifact = cls(
            annotations=annotations,
            architecture=architecture,
            artifact_type=artifact_type,
            created_at=created_at,
            created_by_id=created_by_id,
            digest=digest,
            id=id,
            media_type=media_type,
            org_id=org_id,
            os=os,
            os_features=os_features,
            os_version=os_version,
            owner_id=owner_id,
            owner_type=owner_type,
            repository=repository,
            size=size,
            tag=tag,
            updated_at=updated_at,
            urls=urls,
            variant=variant,
        )

        app_oci_artifact.additional_properties = d
        return app_oci_artifact

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
