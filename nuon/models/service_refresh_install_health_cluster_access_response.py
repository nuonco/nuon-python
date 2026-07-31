from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceRefreshInstallHealthClusterAccessResponse")


@_attrs_define
class ServiceRefreshInstallHealthClusterAccessResponse:
    """
    Attributes:
        cluster_found (bool | Unset):
        cluster_id (str | Unset):
        role_name (str | Unset):
    """

    cluster_found: bool | Unset = UNSET
    cluster_id: str | Unset = UNSET
    role_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cluster_found = self.cluster_found

        cluster_id = self.cluster_id

        role_name = self.role_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cluster_found is not UNSET:
            field_dict["cluster_found"] = cluster_found
        if cluster_id is not UNSET:
            field_dict["cluster_id"] = cluster_id
        if role_name is not UNSET:
            field_dict["role_name"] = role_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cluster_found = d.pop("cluster_found", UNSET)

        cluster_id = d.pop("cluster_id", UNSET)

        role_name = d.pop("role_name", UNSET)

        service_refresh_install_health_cluster_access_response = cls(
            cluster_found=cluster_found,
            cluster_id=cluster_id,
            role_name=role_name,
        )

        service_refresh_install_health_cluster_access_response.additional_properties = d
        return service_refresh_install_health_cluster_access_response

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
