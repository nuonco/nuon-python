from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_composite_status import AppCompositeStatus
    from ..models.app_install_config_sync import AppInstallConfigSync
    from ..models.app_install_config_version_metadata import AppInstallConfigVersionMetadata
    from ..models.blobstore_blob import BlobstoreBlob


T = TypeVar("T", bound="AppInstallConfigVersion")


@_attrs_define
class AppInstallConfigVersion:
    """
    Attributes:
        created (bool | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        diff (BlobstoreBlob | Unset):
        file_path (str | Unset):
        id (str | Unset):
        install_config_sync (AppInstallConfigSync | Unset):
        install_config_sync_id (str | Unset):
        install_id (str | Unset):
        install_name (str | Unset):
        metadata (AppInstallConfigVersionMetadata | Unset):
        org_id (str | Unset):
        status (AppCompositeStatus | Unset):
        updated_at (str | Unset):
    """

    created: bool | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    diff: BlobstoreBlob | Unset = UNSET
    file_path: str | Unset = UNSET
    id: str | Unset = UNSET
    install_config_sync: AppInstallConfigSync | Unset = UNSET
    install_config_sync_id: str | Unset = UNSET
    install_id: str | Unset = UNSET
    install_name: str | Unset = UNSET
    metadata: AppInstallConfigVersionMetadata | Unset = UNSET
    org_id: str | Unset = UNSET
    status: AppCompositeStatus | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        created_at = self.created_at

        created_by_id = self.created_by_id

        diff: dict[str, Any] | Unset = UNSET
        if not isinstance(self.diff, Unset):
            diff = self.diff.to_dict()

        file_path = self.file_path

        id = self.id

        install_config_sync: dict[str, Any] | Unset = UNSET
        if not isinstance(self.install_config_sync, Unset):
            install_config_sync = self.install_config_sync.to_dict()

        install_config_sync_id = self.install_config_sync_id

        install_id = self.install_id

        install_name = self.install_name

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        org_id = self.org_id

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if diff is not UNSET:
            field_dict["diff"] = diff
        if file_path is not UNSET:
            field_dict["file_path"] = file_path
        if id is not UNSET:
            field_dict["id"] = id
        if install_config_sync is not UNSET:
            field_dict["install_config_sync"] = install_config_sync
        if install_config_sync_id is not UNSET:
            field_dict["install_config_sync_id"] = install_config_sync_id
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if install_name is not UNSET:
            field_dict["install_name"] = install_name
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_composite_status import AppCompositeStatus
        from ..models.app_install_config_sync import AppInstallConfigSync
        from ..models.app_install_config_version_metadata import AppInstallConfigVersionMetadata
        from ..models.blobstore_blob import BlobstoreBlob

        d = dict(src_dict)
        created = d.pop("created", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        _diff = d.pop("diff", UNSET)
        diff: BlobstoreBlob | Unset
        if isinstance(_diff, Unset):
            diff = UNSET
        else:
            diff = BlobstoreBlob.from_dict(_diff)

        file_path = d.pop("file_path", UNSET)

        id = d.pop("id", UNSET)

        _install_config_sync = d.pop("install_config_sync", UNSET)
        install_config_sync: AppInstallConfigSync | Unset
        if isinstance(_install_config_sync, Unset):
            install_config_sync = UNSET
        else:
            install_config_sync = AppInstallConfigSync.from_dict(_install_config_sync)

        install_config_sync_id = d.pop("install_config_sync_id", UNSET)

        install_id = d.pop("install_id", UNSET)

        install_name = d.pop("install_name", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: AppInstallConfigVersionMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = AppInstallConfigVersionMetadata.from_dict(_metadata)

        org_id = d.pop("org_id", UNSET)

        _status = d.pop("status", UNSET)
        status: AppCompositeStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppCompositeStatus.from_dict(_status)

        updated_at = d.pop("updated_at", UNSET)

        app_install_config_version = cls(
            created=created,
            created_at=created_at,
            created_by_id=created_by_id,
            diff=diff,
            file_path=file_path,
            id=id,
            install_config_sync=install_config_sync,
            install_config_sync_id=install_config_sync_id,
            install_id=install_id,
            install_name=install_name,
            metadata=metadata,
            org_id=org_id,
            status=status,
            updated_at=updated_at,
        )

        app_install_config_version.additional_properties = d
        return app_install_config_version

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
