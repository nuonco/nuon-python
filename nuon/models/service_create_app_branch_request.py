from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServiceCreateAppBranchRequest")


@_attrs_define
class ServiceCreateAppBranchRequest:
    """
    Attributes:
        connected_github_vcs_config_id (str):
        name (str):
    """

    connected_github_vcs_config_id: str
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connected_github_vcs_config_id = self.connected_github_vcs_config_id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connected_github_vcs_config_id": connected_github_vcs_config_id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connected_github_vcs_config_id = d.pop("connected_github_vcs_config_id")

        name = d.pop("name")

        service_create_app_branch_request = cls(
            connected_github_vcs_config_id=connected_github_vcs_config_id,
            name=name,
        )

        service_create_app_branch_request.additional_properties = d
        return service_create_app_branch_request

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
