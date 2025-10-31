from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceCreateAppRequest")


@_attrs_define
class ServiceCreateAppRequest:
    """
    Attributes:
        name (str):
        description (str | Unset):
        display_name (str | Unset):
        slack_webhook_url (str | Unset):
    """

    name: str
    description: str | Unset = UNSET
    display_name: str | Unset = UNSET
    slack_webhook_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        display_name = self.display_name

        slack_webhook_url = self.slack_webhook_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if slack_webhook_url is not UNSET:
            field_dict["slack_webhook_url"] = slack_webhook_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        display_name = d.pop("display_name", UNSET)

        slack_webhook_url = d.pop("slack_webhook_url", UNSET)

        service_create_app_request = cls(
            name=name,
            description=description,
            display_name=display_name,
            slack_webhook_url=slack_webhook_url,
        )

        service_create_app_request.additional_properties = d
        return service_create_app_request

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
