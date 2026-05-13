from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_slack_org_link_status import AppSlackOrgLinkStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppSlackOrgLink")


@_attrs_define
class AppSlackOrgLink:
    """
    Attributes:
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        linked_by_account_id (str | Unset):
        org_id (str | Unset):
        status (AppSlackOrgLinkStatus | Unset):
        team_id (str | Unset):
        updated_at (str | Unset):
    """

    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    linked_by_account_id: str | Unset = UNSET
    org_id: str | Unset = UNSET
    status: AppSlackOrgLinkStatus | Unset = UNSET
    team_id: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        linked_by_account_id = self.linked_by_account_id

        org_id = self.org_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        team_id = self.team_id

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
        if linked_by_account_id is not UNSET:
            field_dict["linked_by_account_id"] = linked_by_account_id
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if status is not UNSET:
            field_dict["status"] = status
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        linked_by_account_id = d.pop("linked_by_account_id", UNSET)

        org_id = d.pop("org_id", UNSET)

        _status = d.pop("status", UNSET)
        status: AppSlackOrgLinkStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppSlackOrgLinkStatus(_status)

        team_id = d.pop("team_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_slack_org_link = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            linked_by_account_id=linked_by_account_id,
            org_id=org_id,
            status=status,
            team_id=team_id,
            updated_at=updated_at,
        )

        app_slack_org_link.additional_properties = d
        return app_slack_org_link

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
