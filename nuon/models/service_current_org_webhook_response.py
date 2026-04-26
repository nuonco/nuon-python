from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceCurrentOrgWebhookResponse")


@_attrs_define
class ServiceCurrentOrgWebhookResponse:
    """
    Attributes:
        created_at (str | Unset):
        created_by_id (str | Unset):
        has_secret (bool | Unset):
        id (str | Unset):
        org_id (str | Unset):
        updated_at (str | Unset):
        webhook_url (str | Unset):
    """

    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    has_secret: bool | Unset = UNSET
    id: str | Unset = UNSET
    org_id: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    webhook_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        has_secret = self.has_secret

        id = self.id

        org_id = self.org_id

        updated_at = self.updated_at

        webhook_url = self.webhook_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if has_secret is not UNSET:
            field_dict["has_secret"] = has_secret
        if id is not UNSET:
            field_dict["id"] = id
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if webhook_url is not UNSET:
            field_dict["webhook_url"] = webhook_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        has_secret = d.pop("has_secret", UNSET)

        id = d.pop("id", UNSET)

        org_id = d.pop("org_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        webhook_url = d.pop("webhook_url", UNSET)

        service_current_org_webhook_response = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            has_secret=has_secret,
            id=id,
            org_id=org_id,
            updated_at=updated_at,
            webhook_url=webhook_url,
        )

        service_current_org_webhook_response.additional_properties = d
        return service_current_org_webhook_response

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
