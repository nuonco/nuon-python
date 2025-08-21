from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceUpdateAppRequest")


@_attrs_define
class ServiceUpdateAppRequest:
    """
    Attributes:
        config_directory (Union[Unset, str]):
        config_repo (Union[Unset, str]):
        description (Union[Unset, str]):
        display_name (Union[Unset, str]):
        name (Union[Unset, str]):
        slack_webhook_url (Union[Unset, str]):
    """

    config_directory: Union[Unset, str] = UNSET
    config_repo: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    slack_webhook_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config_directory = self.config_directory

        config_repo = self.config_repo

        description = self.description

        display_name = self.display_name

        name = self.name

        slack_webhook_url = self.slack_webhook_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config_directory is not UNSET:
            field_dict["config_directory"] = config_directory
        if config_repo is not UNSET:
            field_dict["config_repo"] = config_repo
        if description is not UNSET:
            field_dict["description"] = description
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if name is not UNSET:
            field_dict["name"] = name
        if slack_webhook_url is not UNSET:
            field_dict["slack_webhook_url"] = slack_webhook_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        config_directory = d.pop("config_directory", UNSET)

        config_repo = d.pop("config_repo", UNSET)

        description = d.pop("description", UNSET)

        display_name = d.pop("display_name", UNSET)

        name = d.pop("name", UNSET)

        slack_webhook_url = d.pop("slack_webhook_url", UNSET)

        service_update_app_request = cls(
            config_directory=config_directory,
            config_repo=config_repo,
            description=description,
            display_name=display_name,
            name=name,
            slack_webhook_url=slack_webhook_url,
        )

        service_update_app_request.additional_properties = d
        return service_update_app_request

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
