from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigHelmRepoConfig")


@_attrs_define
class ConfigHelmRepoConfig:
    """
    Attributes:
        chart (str | Unset):
        repo_url (str | Unset):
        version (str | Unset):
    """

    chart: str | Unset = UNSET
    repo_url: str | Unset = UNSET
    version: str | Unset = UNSET
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
            field_dict["repoURL"] = repo_url
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chart = d.pop("chart", UNSET)

        repo_url = d.pop("repoURL", UNSET)

        version = d.pop("version", UNSET)

        config_helm_repo_config = cls(
            chart=chart,
            repo_url=repo_url,
            version=version,
        )

        config_helm_repo_config.additional_properties = d
        return config_helm_repo_config

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
