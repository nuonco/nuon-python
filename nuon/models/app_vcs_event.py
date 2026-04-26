from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_composite_status import AppCompositeStatus
    from ..models.app_vcs_event_payload import AppVCSEventPayload


T = TypeVar("T", bound="AppVCSEvent")


@_attrs_define
class AppVCSEvent:
    """
    Attributes:
        created_at (str | Unset):
        created_by_id (str | Unset):
        event_type (str | Unset):
        id (str | Unset):
        payload (AppVCSEventPayload | Unset):
        status (AppCompositeStatus | Unset):
        updated_at (str | Unset):
        vcs_connection_id (str | Unset):
    """

    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    event_type: str | Unset = UNSET
    id: str | Unset = UNSET
    payload: AppVCSEventPayload | Unset = UNSET
    status: AppCompositeStatus | Unset = UNSET
    updated_at: str | Unset = UNSET
    vcs_connection_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        event_type = self.event_type

        id = self.id

        payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        updated_at = self.updated_at

        vcs_connection_id = self.vcs_connection_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if id is not UNSET:
            field_dict["id"] = id
        if payload is not UNSET:
            field_dict["payload"] = payload
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if vcs_connection_id is not UNSET:
            field_dict["vcs_connection_id"] = vcs_connection_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_composite_status import AppCompositeStatus
        from ..models.app_vcs_event_payload import AppVCSEventPayload

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        event_type = d.pop("event_type", UNSET)

        id = d.pop("id", UNSET)

        _payload = d.pop("payload", UNSET)
        payload: AppVCSEventPayload | Unset
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = AppVCSEventPayload.from_dict(_payload)

        _status = d.pop("status", UNSET)
        status: AppCompositeStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppCompositeStatus.from_dict(_status)

        updated_at = d.pop("updated_at", UNSET)

        vcs_connection_id = d.pop("vcs_connection_id", UNSET)

        app_vcs_event = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            event_type=event_type,
            id=id,
            payload=payload,
            status=status,
            updated_at=updated_at,
            vcs_connection_id=vcs_connection_id,
        )

        app_vcs_event.additional_properties = d
        return app_vcs_event

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
