from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_runbook_trigger_type import AppRunbookTriggerType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppRunbookTriggerConfig")


@_attrs_define
class AppRunbookTriggerConfig:
    """
    Attributes:
        app_config_id (str | Unset):
        app_id (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        cron_schedule (str | Unset):
        id (str | Unset):
        runbook_config_id (str | Unset):
        type_ (AppRunbookTriggerType | Unset):
        updated_at (str | Unset):
    """

    app_config_id: str | Unset = UNSET
    app_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    cron_schedule: str | Unset = UNSET
    id: str | Unset = UNSET
    runbook_config_id: str | Unset = UNSET
    type_: AppRunbookTriggerType | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config_id = self.app_config_id

        app_id = self.app_id

        created_at = self.created_at

        created_by_id = self.created_by_id

        cron_schedule = self.cron_schedule

        id = self.id

        runbook_config_id = self.runbook_config_id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if cron_schedule is not UNSET:
            field_dict["cron_schedule"] = cron_schedule
        if id is not UNSET:
            field_dict["id"] = id
        if runbook_config_id is not UNSET:
            field_dict["runbook_config_id"] = runbook_config_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_config_id = d.pop("app_config_id", UNSET)

        app_id = d.pop("app_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        cron_schedule = d.pop("cron_schedule", UNSET)

        id = d.pop("id", UNSET)

        runbook_config_id = d.pop("runbook_config_id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: AppRunbookTriggerType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AppRunbookTriggerType(_type_)

        updated_at = d.pop("updated_at", UNSET)

        app_runbook_trigger_config = cls(
            app_config_id=app_config_id,
            app_id=app_id,
            created_at=created_at,
            created_by_id=created_by_id,
            cron_schedule=cron_schedule,
            id=id,
            runbook_config_id=runbook_config_id,
            type_=type_,
            updated_at=updated_at,
        )

        app_runbook_trigger_config.additional_properties = d
        return app_runbook_trigger_config

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
