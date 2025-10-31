from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_operation_status import AppOperationStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_install_event_payload import AppInstallEventPayload


T = TypeVar("T", bound="AppInstallEvent")


@_attrs_define
class AppInstallEvent:
    """
    Attributes:
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        install_id (str | Unset):
        operation (str | Unset):
        operation_name (str | Unset):
        operation_status (AppOperationStatus | Unset):
        org_id (str | Unset):
        payload (AppInstallEventPayload | Unset):
        updated_at (str | Unset):
    """

    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    install_id: str | Unset = UNSET
    operation: str | Unset = UNSET
    operation_name: str | Unset = UNSET
    operation_status: AppOperationStatus | Unset = UNSET
    org_id: str | Unset = UNSET
    payload: AppInstallEventPayload | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        install_id = self.install_id

        operation = self.operation

        operation_name = self.operation_name

        operation_status: str | Unset = UNSET
        if not isinstance(self.operation_status, Unset):
            operation_status = self.operation_status.value

        org_id = self.org_id

        payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if operation is not UNSET:
            field_dict["operation"] = operation
        if operation_name is not UNSET:
            field_dict["operation_name"] = operation_name
        if operation_status is not UNSET:
            field_dict["operation_status"] = operation_status
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if payload is not UNSET:
            field_dict["payload"] = payload
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_install_event_payload import AppInstallEventPayload

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        install_id = d.pop("install_id", UNSET)

        operation = d.pop("operation", UNSET)

        operation_name = d.pop("operation_name", UNSET)

        _operation_status = d.pop("operation_status", UNSET)
        operation_status: AppOperationStatus | Unset
        if isinstance(_operation_status, Unset):
            operation_status = UNSET
        else:
            operation_status = AppOperationStatus(_operation_status)

        org_id = d.pop("org_id", UNSET)

        _payload = d.pop("payload", UNSET)
        payload: AppInstallEventPayload | Unset
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = AppInstallEventPayload.from_dict(_payload)

        updated_at = d.pop("updated_at", UNSET)

        app_install_event = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            install_id=install_id,
            operation=operation,
            operation_name=operation_name,
            operation_status=operation_status,
            org_id=org_id,
            payload=payload,
            updated_at=updated_at,
        )

        app_install_event.additional_properties = d
        return app_install_event

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
