from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_cloud_connection_platform import AppCloudConnectionPlatform
from ..models.app_cloud_connection_preset import AppCloudConnectionPreset
from ..models.app_cloud_connection_status import AppCloudConnectionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_queue import AppQueue


T = TypeVar("T", bound="AppCloudConnection")


@_attrs_define
class AppCloudConnection:
    """
    Attributes:
        created_at (str | Unset):
        created_by_id (str | Unset):
        default_region (str | Unset):
        id (str | Unset):
        last_verified_at (str | Unset):
        name (str | Unset):
        org_id (str | Unset):
        platform (AppCloudConnectionPlatform | Unset):
        preset (AppCloudConnectionPreset | Unset):
        principal (str | Unset):
        queues (list[AppQueue] | Unset):
        status (AppCloudConnectionStatus | Unset):
        status_message (str | Unset):
        target_id (str | Unset):
        updated_at (str | Unset):
        verification_requested_at (str | Unset):
    """

    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    default_region: str | Unset = UNSET
    id: str | Unset = UNSET
    last_verified_at: str | Unset = UNSET
    name: str | Unset = UNSET
    org_id: str | Unset = UNSET
    platform: AppCloudConnectionPlatform | Unset = UNSET
    preset: AppCloudConnectionPreset | Unset = UNSET
    principal: str | Unset = UNSET
    queues: list[AppQueue] | Unset = UNSET
    status: AppCloudConnectionStatus | Unset = UNSET
    status_message: str | Unset = UNSET
    target_id: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    verification_requested_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        default_region = self.default_region

        id = self.id

        last_verified_at = self.last_verified_at

        name = self.name

        org_id = self.org_id

        platform: str | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        preset: str | Unset = UNSET
        if not isinstance(self.preset, Unset):
            preset = self.preset.value

        principal = self.principal

        queues: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.queues, Unset):
            queues = []
            for queues_item_data in self.queues:
                queues_item = queues_item_data.to_dict()
                queues.append(queues_item)

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        status_message = self.status_message

        target_id = self.target_id

        updated_at = self.updated_at

        verification_requested_at = self.verification_requested_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if default_region is not UNSET:
            field_dict["default_region"] = default_region
        if id is not UNSET:
            field_dict["id"] = id
        if last_verified_at is not UNSET:
            field_dict["last_verified_at"] = last_verified_at
        if name is not UNSET:
            field_dict["name"] = name
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if platform is not UNSET:
            field_dict["platform"] = platform
        if preset is not UNSET:
            field_dict["preset"] = preset
        if principal is not UNSET:
            field_dict["principal"] = principal
        if queues is not UNSET:
            field_dict["queues"] = queues
        if status is not UNSET:
            field_dict["status"] = status
        if status_message is not UNSET:
            field_dict["status_message"] = status_message
        if target_id is not UNSET:
            field_dict["target_id"] = target_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if verification_requested_at is not UNSET:
            field_dict["verification_requested_at"] = verification_requested_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_queue import AppQueue  # noqa: PLC0415

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        default_region = d.pop("default_region", UNSET)

        id = d.pop("id", UNSET)

        last_verified_at = d.pop("last_verified_at", UNSET)

        name = d.pop("name", UNSET)

        org_id = d.pop("org_id", UNSET)

        _platform = d.pop("platform", UNSET)
        platform: AppCloudConnectionPlatform | Unset
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = AppCloudConnectionPlatform(_platform)

        _preset = d.pop("preset", UNSET)
        preset: AppCloudConnectionPreset | Unset
        if isinstance(_preset, Unset):
            preset = UNSET
        else:
            preset = AppCloudConnectionPreset(_preset)

        principal = d.pop("principal", UNSET)

        _queues = d.pop("queues", UNSET)
        queues: list[AppQueue] | Unset = UNSET
        if _queues is not UNSET:
            queues = []
            for queues_item_data in _queues:
                queues_item = AppQueue.from_dict(queues_item_data)

                queues.append(queues_item)

        _status = d.pop("status", UNSET)
        status: AppCloudConnectionStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppCloudConnectionStatus(_status)

        status_message = d.pop("status_message", UNSET)

        target_id = d.pop("target_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        verification_requested_at = d.pop("verification_requested_at", UNSET)

        app_cloud_connection = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            default_region=default_region,
            id=id,
            last_verified_at=last_verified_at,
            name=name,
            org_id=org_id,
            platform=platform,
            preset=preset,
            principal=principal,
            queues=queues,
            status=status,
            status_message=status_message,
            target_id=target_id,
            updated_at=updated_at,
            verification_requested_at=verification_requested_at,
        )

        app_cloud_connection.additional_properties = d
        return app_cloud_connection

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
