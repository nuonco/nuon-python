from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceCreateAppConfigRequest")


@_attrs_define
class ServiceCreateAppConfigRequest:
    """
    Attributes:
        cli_version (Union[Unset, str]):
        readme (Union[Unset, str]): not required Readme
    """

    cli_version: Union[Unset, str] = UNSET
    readme: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cli_version = self.cli_version

        readme = self.readme

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cli_version is not UNSET:
            field_dict["cli_version"] = cli_version
        if readme is not UNSET:
            field_dict["readme"] = readme

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cli_version = d.pop("cli_version", UNSET)

        readme = d.pop("readme", UNSET)

        service_create_app_config_request = cls(
            cli_version=cli_version,
            readme=readme,
        )

        service_create_app_config_request.additional_properties = d
        return service_create_app_config_request

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
