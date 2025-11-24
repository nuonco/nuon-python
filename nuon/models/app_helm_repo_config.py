from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppHelmRepoConfig")


@_attrs_define
class AppHelmRepoConfig:
    """
    Attributes:
        chart (Union[Unset, str]):
        repo_url (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    chart: Union[Unset, str] = UNSET
    repo_url: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chart = self.chart

        repo_url = self.repo_url

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chart is not UNSET:
            field_dict["chart"] = chart
        if repo_url is not UNSET:
            field_dict["repo_url"] = repo_url
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chart = d.pop("chart", UNSET)

        repo_url = d.pop("repo_url", UNSET)

        version = d.pop("version", UNSET)

        app_helm_repo_config = cls(
            chart=chart,
            repo_url=repo_url,
            version=version,
        )

        app_helm_repo_config.additional_properties = d
        return app_helm_repo_config

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
