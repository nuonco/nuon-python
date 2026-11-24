from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_nuonco_nuon_pkg_labels_labels import GithubComNuoncoNuonPkgLabelsLabels
    from ..models.service_app_fleet_counts import ServiceAppFleetCounts
    from ..models.service_app_fleet_install import ServiceAppFleetInstall


T = TypeVar("T", bound="ServiceAppFleetGroup")


@_attrs_define
class ServiceAppFleetGroup:
    """
    Attributes:
        counts (ServiceAppFleetCounts | Unset):
        has_more (bool | Unset):
        installs (list[ServiceAppFleetInstall] | Unset):
        match_labels (GithubComNuoncoNuonPkgLabelsLabels | Unset):
        name (str | Unset):
        order (int | Unset):
    """

    counts: ServiceAppFleetCounts | Unset = UNSET
    has_more: bool | Unset = UNSET
    installs: list[ServiceAppFleetInstall] | Unset = UNSET
    match_labels: GithubComNuoncoNuonPkgLabelsLabels | Unset = UNSET
    name: str | Unset = UNSET
    order: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        counts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.counts, Unset):
            counts = self.counts.to_dict()

        has_more = self.has_more

        installs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.installs, Unset):
            installs = []
            for installs_item_data in self.installs:
                installs_item = installs_item_data.to_dict()
                installs.append(installs_item)

        match_labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_labels, Unset):
            match_labels = self.match_labels.to_dict()

        name = self.name

        order = self.order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if counts is not UNSET:
            field_dict["counts"] = counts
        if has_more is not UNSET:
            field_dict["has_more"] = has_more
        if installs is not UNSET:
            field_dict["installs"] = installs
        if match_labels is not UNSET:
            field_dict["match_labels"] = match_labels
        if name is not UNSET:
            field_dict["name"] = name
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_nuonco_nuon_pkg_labels_labels import GithubComNuoncoNuonPkgLabelsLabels  # noqa: PLC0415
        from ..models.service_app_fleet_counts import ServiceAppFleetCounts  # noqa: PLC0415
        from ..models.service_app_fleet_install import ServiceAppFleetInstall  # noqa: PLC0415

        d = dict(src_dict)
        _counts = d.pop("counts", UNSET)
        counts: ServiceAppFleetCounts | Unset
        if isinstance(_counts, Unset):
            counts = UNSET
        else:
            counts = ServiceAppFleetCounts.from_dict(_counts)

        has_more = d.pop("has_more", UNSET)

        _installs = d.pop("installs", UNSET)
        installs: list[ServiceAppFleetInstall] | Unset = UNSET
        if _installs is not UNSET:
            installs = []
            for installs_item_data in _installs:
                installs_item = ServiceAppFleetInstall.from_dict(installs_item_data)

                installs.append(installs_item)

        _match_labels = d.pop("match_labels", UNSET)
        match_labels: GithubComNuoncoNuonPkgLabelsLabels | Unset
        if isinstance(_match_labels, Unset):
            match_labels = UNSET
        else:
            match_labels = GithubComNuoncoNuonPkgLabelsLabels.from_dict(_match_labels)

        name = d.pop("name", UNSET)

        order = d.pop("order", UNSET)

        service_app_fleet_group = cls(
            counts=counts,
            has_more=has_more,
            installs=installs,
            match_labels=match_labels,
            name=name,
            order=order,
        )

        service_app_fleet_group.additional_properties = d
        return service_app_fleet_group

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
