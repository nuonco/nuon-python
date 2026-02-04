from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_vcs_connection_repo import ServiceVCSConnectionRepo


T = TypeVar("T", bound="ServiceVCSConnectionReposResponse")


@_attrs_define
class ServiceVCSConnectionReposResponse:
    """
    Attributes:
        repositories (list[ServiceVCSConnectionRepo] | Unset):
        total_count (int | Unset):
    """

    repositories: list[ServiceVCSConnectionRepo] | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repositories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.repositories, Unset):
            repositories = []
            for repositories_item_data in self.repositories:
                repositories_item = repositories_item_data.to_dict()
                repositories.append(repositories_item)

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if repositories is not UNSET:
            field_dict["repositories"] = repositories
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_vcs_connection_repo import ServiceVCSConnectionRepo

        d = dict(src_dict)
        _repositories = d.pop("repositories", UNSET)
        repositories: list[ServiceVCSConnectionRepo] | Unset = UNSET
        if _repositories is not UNSET:
            repositories = []
            for repositories_item_data in _repositories:
                repositories_item = ServiceVCSConnectionRepo.from_dict(repositories_item_data)

                repositories.append(repositories_item)

        total_count = d.pop("total_count", UNSET)

        service_vcs_connection_repos_response = cls(
            repositories=repositories,
            total_count=total_count,
        )

        service_vcs_connection_repos_response.additional_properties = d
        return service_vcs_connection_repos_response

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
