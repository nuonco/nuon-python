from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_nuonco_nuon_pkg_labels_labels import GithubComNuoncoNuonPkgLabelsLabels


T = TypeVar("T", bound="GithubComNuoncoNuonPkgLabelsSelector")


@_attrs_define
class GithubComNuoncoNuonPkgLabelsSelector:
    """
    Attributes:
        match_labels (GithubComNuoncoNuonPkgLabelsLabels | Unset):
        not_match_labels (GithubComNuoncoNuonPkgLabelsLabels | Unset):
    """

    match_labels: GithubComNuoncoNuonPkgLabelsLabels | Unset = UNSET
    not_match_labels: GithubComNuoncoNuonPkgLabelsLabels | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        match_labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_labels, Unset):
            match_labels = self.match_labels.to_dict()

        not_match_labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.not_match_labels, Unset):
            not_match_labels = self.not_match_labels.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if match_labels is not UNSET:
            field_dict["match_labels"] = match_labels
        if not_match_labels is not UNSET:
            field_dict["not_match_labels"] = not_match_labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_nuonco_nuon_pkg_labels_labels import GithubComNuoncoNuonPkgLabelsLabels

        d = dict(src_dict)
        _match_labels = d.pop("match_labels", UNSET)
        match_labels: GithubComNuoncoNuonPkgLabelsLabels | Unset
        if isinstance(_match_labels, Unset):
            match_labels = UNSET
        else:
            match_labels = GithubComNuoncoNuonPkgLabelsLabels.from_dict(_match_labels)

        _not_match_labels = d.pop("not_match_labels", UNSET)
        not_match_labels: GithubComNuoncoNuonPkgLabelsLabels | Unset
        if isinstance(_not_match_labels, Unset):
            not_match_labels = UNSET
        else:
            not_match_labels = GithubComNuoncoNuonPkgLabelsLabels.from_dict(_not_match_labels)

        github_com_nuonco_nuon_pkg_labels_selector = cls(
            match_labels=match_labels,
            not_match_labels=not_match_labels,
        )

        github_com_nuonco_nuon_pkg_labels_selector.additional_properties = d
        return github_com_nuonco_nuon_pkg_labels_selector

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
