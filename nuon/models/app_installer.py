from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_installer_type import AppInstallerType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_app import AppApp
    from ..models.app_installer_metadata import AppInstallerMetadata


T = TypeVar("T", bound="AppInstaller")


@_attrs_define
class AppInstaller:
    """
    Attributes:
        apps (list[AppApp] | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        metadata (AppInstallerMetadata | Unset):
        org_id (str | Unset):
        type_ (AppInstallerType | Unset):
        updated_at (str | Unset):
    """

    apps: list[AppApp] | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    metadata: AppInstallerMetadata | Unset = UNSET
    org_id: str | Unset = UNSET
    type_: AppInstallerType | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        apps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.apps, Unset):
            apps = []
            for apps_item_data in self.apps:
                apps_item = apps_item_data.to_dict()
                apps.append(apps_item)

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        org_id = self.org_id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if apps is not UNSET:
            field_dict["apps"] = apps
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_app import AppApp
        from ..models.app_installer_metadata import AppInstallerMetadata

        d = dict(src_dict)
        apps = []
        _apps = d.pop("apps", UNSET)
        for apps_item_data in _apps or []:
            apps_item = AppApp.from_dict(apps_item_data)

            apps.append(apps_item)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: AppInstallerMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = AppInstallerMetadata.from_dict(_metadata)

        org_id = d.pop("org_id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: AppInstallerType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AppInstallerType(_type_)

        updated_at = d.pop("updated_at", UNSET)

        app_installer = cls(
            apps=apps,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            metadata=metadata,
            org_id=org_id,
            type_=type_,
            updated_at=updated_at,
        )

        app_installer.additional_properties = d
        return app_installer

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
