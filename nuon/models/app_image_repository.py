from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_image_repository_platform import AppImageRepositoryPlatform
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_cloud_connection import AppCloudConnection


T = TypeVar("T", bound="AppImageRepository")


@_attrs_define
class AppImageRepository:
    """
    Attributes:
        cloud_connection (AppCloudConnection | Unset):
        cloud_connection_id (str | Unset):
        created_at (str | Unset):
        id (str | Unset):
        image_url_prefix (str | Unset):
        org_id (str | Unset):
        platform (AppImageRepositoryPlatform | Unset):
        repository (str | Unset):
        updated_at (str | Unset):
    """

    cloud_connection: AppCloudConnection | Unset = UNSET
    cloud_connection_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    id: str | Unset = UNSET
    image_url_prefix: str | Unset = UNSET
    org_id: str | Unset = UNSET
    platform: AppImageRepositoryPlatform | Unset = UNSET
    repository: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cloud_connection: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cloud_connection, Unset):
            cloud_connection = self.cloud_connection.to_dict()

        cloud_connection_id = self.cloud_connection_id

        created_at = self.created_at

        id = self.id

        image_url_prefix = self.image_url_prefix

        org_id = self.org_id

        platform: str | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        repository = self.repository

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cloud_connection is not UNSET:
            field_dict["cloud_connection"] = cloud_connection
        if cloud_connection_id is not UNSET:
            field_dict["cloud_connection_id"] = cloud_connection_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if image_url_prefix is not UNSET:
            field_dict["image_url_prefix"] = image_url_prefix
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if platform is not UNSET:
            field_dict["platform"] = platform
        if repository is not UNSET:
            field_dict["repository"] = repository
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_cloud_connection import AppCloudConnection  # noqa: PLC0415

        d = dict(src_dict)
        _cloud_connection = d.pop("cloud_connection", UNSET)
        cloud_connection: AppCloudConnection | Unset
        if isinstance(_cloud_connection, Unset):
            cloud_connection = UNSET
        else:
            cloud_connection = AppCloudConnection.from_dict(_cloud_connection)

        cloud_connection_id = d.pop("cloud_connection_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        id = d.pop("id", UNSET)

        image_url_prefix = d.pop("image_url_prefix", UNSET)

        org_id = d.pop("org_id", UNSET)

        _platform = d.pop("platform", UNSET)
        platform: AppImageRepositoryPlatform | Unset
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = AppImageRepositoryPlatform(_platform)

        repository = d.pop("repository", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_image_repository = cls(
            cloud_connection=cloud_connection,
            cloud_connection_id=cloud_connection_id,
            created_at=created_at,
            id=id,
            image_url_prefix=image_url_prefix,
            org_id=org_id,
            platform=platform,
            repository=repository,
            updated_at=updated_at,
        )

        app_image_repository.additional_properties = d
        return app_image_repository

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
