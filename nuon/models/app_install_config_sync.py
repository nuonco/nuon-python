from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_composite_status import AppCompositeStatus
    from ..models.app_install_config_sync_metadata import AppInstallConfigSyncMetadata
    from ..models.app_install_config_version import AppInstallConfigVersion
    from ..models.app_vcs_connection_commit import AppVCSConnectionCommit


T = TypeVar("T", bound="AppInstallConfigSync")


@_attrs_define
class AppInstallConfigSync:
    """
    Attributes:
        app_branch_config_id (str | Unset):
        app_branch_id (str | Unset):
        app_branch_run_id (str | Unset):
        app_install_config_sync_id (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        install_id (str | Unset):
        metadata (AppInstallConfigSyncMetadata | Unset):
        org_id (str | Unset):
        status (AppCompositeStatus | Unset):
        triggered_by (str | Unset):
        updated_at (str | Unset):
        vcs_connection_commit (AppVCSConnectionCommit | Unset):
        versions (list[AppInstallConfigVersion] | Unset):
    """

    app_branch_config_id: str | Unset = UNSET
    app_branch_id: str | Unset = UNSET
    app_branch_run_id: str | Unset = UNSET
    app_install_config_sync_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    install_id: str | Unset = UNSET
    metadata: AppInstallConfigSyncMetadata | Unset = UNSET
    org_id: str | Unset = UNSET
    status: AppCompositeStatus | Unset = UNSET
    triggered_by: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    vcs_connection_commit: AppVCSConnectionCommit | Unset = UNSET
    versions: list[AppInstallConfigVersion] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_branch_config_id = self.app_branch_config_id

        app_branch_id = self.app_branch_id

        app_branch_run_id = self.app_branch_run_id

        app_install_config_sync_id = self.app_install_config_sync_id

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        install_id = self.install_id

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        org_id = self.org_id

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        triggered_by = self.triggered_by

        updated_at = self.updated_at

        vcs_connection_commit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vcs_connection_commit, Unset):
            vcs_connection_commit = self.vcs_connection_commit.to_dict()

        versions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.versions, Unset):
            versions = []
            for versions_item_data in self.versions:
                versions_item = versions_item_data.to_dict()
                versions.append(versions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_branch_config_id is not UNSET:
            field_dict["app_branch_config_id"] = app_branch_config_id
        if app_branch_id is not UNSET:
            field_dict["app_branch_id"] = app_branch_id
        if app_branch_run_id is not UNSET:
            field_dict["app_branch_run_id"] = app_branch_run_id
        if app_install_config_sync_id is not UNSET:
            field_dict["app_install_config_sync_id"] = app_install_config_sync_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if status is not UNSET:
            field_dict["status"] = status
        if triggered_by is not UNSET:
            field_dict["triggered_by"] = triggered_by
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if vcs_connection_commit is not UNSET:
            field_dict["vcs_connection_commit"] = vcs_connection_commit
        if versions is not UNSET:
            field_dict["versions"] = versions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_composite_status import AppCompositeStatus
        from ..models.app_install_config_sync_metadata import AppInstallConfigSyncMetadata
        from ..models.app_install_config_version import AppInstallConfigVersion
        from ..models.app_vcs_connection_commit import AppVCSConnectionCommit

        d = dict(src_dict)
        app_branch_config_id = d.pop("app_branch_config_id", UNSET)

        app_branch_id = d.pop("app_branch_id", UNSET)

        app_branch_run_id = d.pop("app_branch_run_id", UNSET)

        app_install_config_sync_id = d.pop("app_install_config_sync_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        install_id = d.pop("install_id", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: AppInstallConfigSyncMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = AppInstallConfigSyncMetadata.from_dict(_metadata)

        org_id = d.pop("org_id", UNSET)

        _status = d.pop("status", UNSET)
        status: AppCompositeStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppCompositeStatus.from_dict(_status)

        triggered_by = d.pop("triggered_by", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _vcs_connection_commit = d.pop("vcs_connection_commit", UNSET)
        vcs_connection_commit: AppVCSConnectionCommit | Unset
        if isinstance(_vcs_connection_commit, Unset):
            vcs_connection_commit = UNSET
        else:
            vcs_connection_commit = AppVCSConnectionCommit.from_dict(_vcs_connection_commit)

        _versions = d.pop("versions", UNSET)
        versions: list[AppInstallConfigVersion] | Unset = UNSET
        if _versions is not UNSET:
            versions = []
            for versions_item_data in _versions:
                versions_item = AppInstallConfigVersion.from_dict(versions_item_data)

                versions.append(versions_item)

        app_install_config_sync = cls(
            app_branch_config_id=app_branch_config_id,
            app_branch_id=app_branch_id,
            app_branch_run_id=app_branch_run_id,
            app_install_config_sync_id=app_install_config_sync_id,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            install_id=install_id,
            metadata=metadata,
            org_id=org_id,
            status=status,
            triggered_by=triggered_by,
            updated_at=updated_at,
            vcs_connection_commit=vcs_connection_commit,
            versions=versions,
        )

        app_install_config_sync.additional_properties = d
        return app_install_config_sync

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
