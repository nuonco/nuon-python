from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

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
        annotations (Union[Unset, AppOCIArtifactAnnotations]):
        architecture (Union[Unset, str]):
        artifact_type (Union[Unset, str]):
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        digest (Union[Unset, str]):
        id (Union[Unset, str]):
        media_type (Union[Unset, str]):
        org_id (Union[Unset, str]):
        os (Union[Unset, str]): Platform fields
        os_features (Union[Unset, list[str]]):
        os_version (Union[Unset, str]):
        owner_id (Union[Unset, str]):
        owner_type (Union[Unset, str]):
        repository (Union[Unset, str]):
        size (Union[Unset, int]):
        tag (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        urls (Union[Unset, list[str]]):
        variant (Union[Unset, str]):
    """

    annotations: Union[Unset, "AppOCIArtifactAnnotations"] = UNSET
    architecture: Union[Unset, str] = UNSET
    artifact_type: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    digest: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    media_type: Union[Unset, str] = UNSET
    org_id: Union[Unset, str] = UNSET
    os: Union[Unset, str] = UNSET
    os_features: Union[Unset, list[str]] = UNSET
    os_version: Union[Unset, str] = UNSET
    owner_id: Union[Unset, str] = UNSET
    owner_type: Union[Unset, str] = UNSET
    repository: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    tag: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    urls: Union[Unset, list[str]] = UNSET
    variant: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        annotations: Union[Unset, dict[str, Any]] = UNSET
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

        os_features: Union[Unset, list[str]] = UNSET
        if not isinstance(self.os_features, Unset):
            os_features = self.os_features

        os_version = self.os_version

        owner_id = self.owner_id

        owner_type = self.owner_type

        repository = self.repository

        size = self.size

        tag = self.tag

        updated_at = self.updated_at

        urls: Union[Unset, list[str]] = UNSET
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
        annotations: Union[Unset, AppOCIArtifactAnnotations]
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
