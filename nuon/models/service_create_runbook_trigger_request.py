from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_runbook_trigger_type import AppRunbookTriggerType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceCreateRunbookTriggerRequest")


@_attrs_define
class ServiceCreateRunbookTriggerRequest:
    """
    Attributes:
        type_ (AppRunbookTriggerType):
        cron_schedule (str | Unset):
    """

    type_: AppRunbookTriggerType
    cron_schedule: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        cron_schedule = self.cron_schedule

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if cron_schedule is not UNSET:
            field_dict["cron_schedule"] = cron_schedule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = AppRunbookTriggerType(d.pop("type"))

        cron_schedule = d.pop("cron_schedule", UNSET)

        service_create_runbook_trigger_request = cls(
            type_=type_,
            cron_schedule=cron_schedule,
        )

        service_create_runbook_trigger_request.additional_properties = d
        return service_create_runbook_trigger_request

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
