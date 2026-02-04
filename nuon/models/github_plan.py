from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubPlan")


@_attrs_define
class GithubPlan:
    """
    Attributes:
        collaborators (int | Unset):
        filled_seats (int | Unset):
        name (str | Unset):
        private_repos (int | Unset):
        seats (int | Unset):
        space (int | Unset):
    """

    collaborators: int | Unset = UNSET
    filled_seats: int | Unset = UNSET
    name: str | Unset = UNSET
    private_repos: int | Unset = UNSET
    seats: int | Unset = UNSET
    space: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collaborators = self.collaborators

        filled_seats = self.filled_seats

        name = self.name

        private_repos = self.private_repos

        seats = self.seats

        space = self.space

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if collaborators is not UNSET:
            field_dict["collaborators"] = collaborators
        if filled_seats is not UNSET:
            field_dict["filled_seats"] = filled_seats
        if name is not UNSET:
            field_dict["name"] = name
        if private_repos is not UNSET:
            field_dict["private_repos"] = private_repos
        if seats is not UNSET:
            field_dict["seats"] = seats
        if space is not UNSET:
            field_dict["space"] = space

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        collaborators = d.pop("collaborators", UNSET)

        filled_seats = d.pop("filled_seats", UNSET)

        name = d.pop("name", UNSET)

        private_repos = d.pop("private_repos", UNSET)

        seats = d.pop("seats", UNSET)

        space = d.pop("space", UNSET)

        github_plan = cls(
            collaborators=collaborators,
            filled_seats=filled_seats,
            name=name,
            private_repos=private_repos,
            seats=seats,
            space=space,
        )

        github_plan.additional_properties = d
        return github_plan

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
