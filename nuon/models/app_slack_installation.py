from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_slack_installation_status import AppSlackInstallationStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppSlackInstallation")


@_attrs_define
class AppSlackInstallation:
    """
    Attributes:
        app_id (str | Unset):
        bot_user_id (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        enterprise_id (str | Unset):
        id (str | Unset):
        installed_by_account_id (str | Unset):
        installed_by_slack_user_id (str | Unset):
        scope (str | Unset):
        status (AppSlackInstallationStatus | Unset):
        team_id (str | Unset): TeamID is the stable Slack workspace identifier (e.g. "T0123456789").
            Combined with deleted_at to allow re-installation after uninstall.
        team_name (str | Unset):
        updated_at (str | Unset):
    """

    app_id: str | Unset = UNSET
    bot_user_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    enterprise_id: str | Unset = UNSET
    id: str | Unset = UNSET
    installed_by_account_id: str | Unset = UNSET
    installed_by_slack_user_id: str | Unset = UNSET
    scope: str | Unset = UNSET
    status: AppSlackInstallationStatus | Unset = UNSET
    team_id: str | Unset = UNSET
    team_name: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        bot_user_id = self.bot_user_id

        created_at = self.created_at

        created_by_id = self.created_by_id

        enterprise_id = self.enterprise_id

        id = self.id

        installed_by_account_id = self.installed_by_account_id

        installed_by_slack_user_id = self.installed_by_slack_user_id

        scope = self.scope

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        team_id = self.team_id

        team_name = self.team_name

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if bot_user_id is not UNSET:
            field_dict["bot_user_id"] = bot_user_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if enterprise_id is not UNSET:
            field_dict["enterprise_id"] = enterprise_id
        if id is not UNSET:
            field_dict["id"] = id
        if installed_by_account_id is not UNSET:
            field_dict["installed_by_account_id"] = installed_by_account_id
        if installed_by_slack_user_id is not UNSET:
            field_dict["installed_by_slack_user_id"] = installed_by_slack_user_id
        if scope is not UNSET:
            field_dict["scope"] = scope
        if status is not UNSET:
            field_dict["status"] = status
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if team_name is not UNSET:
            field_dict["team_name"] = team_name
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_id = d.pop("app_id", UNSET)

        bot_user_id = d.pop("bot_user_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        enterprise_id = d.pop("enterprise_id", UNSET)

        id = d.pop("id", UNSET)

        installed_by_account_id = d.pop("installed_by_account_id", UNSET)

        installed_by_slack_user_id = d.pop("installed_by_slack_user_id", UNSET)

        scope = d.pop("scope", UNSET)

        _status = d.pop("status", UNSET)
        status: AppSlackInstallationStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppSlackInstallationStatus(_status)

        team_id = d.pop("team_id", UNSET)

        team_name = d.pop("team_name", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_slack_installation = cls(
            app_id=app_id,
            bot_user_id=bot_user_id,
            created_at=created_at,
            created_by_id=created_by_id,
            enterprise_id=enterprise_id,
            id=id,
            installed_by_account_id=installed_by_account_id,
            installed_by_slack_user_id=installed_by_slack_user_id,
            scope=scope,
            status=status,
            team_id=team_id,
            team_name=team_name,
            updated_at=updated_at,
        )

        app_slack_installation.additional_properties = d
        return app_slack_installation

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
