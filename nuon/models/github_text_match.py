from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_match import GithubMatch


T = TypeVar("T", bound="GithubTextMatch")


@_attrs_define
class GithubTextMatch:
    """
    Attributes:
        fragment (str | Unset):
        matches (list[GithubMatch] | Unset):
        object_type (str | Unset):
        object_url (str | Unset):
        property_ (str | Unset):
    """

    fragment: str | Unset = UNSET
    matches: list[GithubMatch] | Unset = UNSET
    object_type: str | Unset = UNSET
    object_url: str | Unset = UNSET
    property_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fragment = self.fragment

        matches: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.matches, Unset):
            matches = []
            for matches_item_data in self.matches:
                matches_item = matches_item_data.to_dict()
                matches.append(matches_item)

        object_type = self.object_type

        object_url = self.object_url

        property_ = self.property_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fragment is not UNSET:
            field_dict["fragment"] = fragment
        if matches is not UNSET:
            field_dict["matches"] = matches
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if object_url is not UNSET:
            field_dict["object_url"] = object_url
        if property_ is not UNSET:
            field_dict["property"] = property_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_match import GithubMatch

        d = dict(src_dict)
        fragment = d.pop("fragment", UNSET)

        _matches = d.pop("matches", UNSET)
        matches: list[GithubMatch] | Unset = UNSET
        if _matches is not UNSET:
            matches = []
            for matches_item_data in _matches:
                matches_item = GithubMatch.from_dict(matches_item_data)

                matches.append(matches_item)

        object_type = d.pop("object_type", UNSET)

        object_url = d.pop("object_url", UNSET)

        property_ = d.pop("property", UNSET)

        github_text_match = cls(
            fragment=fragment,
            matches=matches,
            object_type=object_type,
            object_url=object_url,
            property_=property_,
        )

        github_text_match.additional_properties = d
        return github_text_match

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
