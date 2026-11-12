from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServiceCreateImageRepositoryRequest")


@_attrs_define
class ServiceCreateImageRepositoryRequest:
    """
    Attributes:
        cloud_connection_id (str):
        repository (str):
    """

    cloud_connection_id: str
    repository: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cloud_connection_id = self.cloud_connection_id

        repository = self.repository

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cloud_connection_id": cloud_connection_id,
                "repository": repository,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cloud_connection_id = d.pop("cloud_connection_id")

        repository = d.pop("repository")

        service_create_image_repository_request = cls(
            cloud_connection_id=cloud_connection_id,
            repository=repository,
        )

        service_create_image_repository_request.additional_properties = d
        return service_create_image_repository_request

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
