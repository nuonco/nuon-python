from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_app_fleet_counts import ServiceAppFleetCounts
    from ..models.service_app_fleet_group import ServiceAppFleetGroup
    from ..models.service_app_fleet_target_run import ServiceAppFleetTargetRun


T = TypeVar("T", bound="ServiceAppFleetBranch")


@_attrs_define
class ServiceAppFleetBranch:
    """
    Attributes:
        counts (ServiceAppFleetCounts | Unset):
        groups (list[ServiceAppFleetGroup] | Unset):
        id (str | Unset):
        name (str | Unset):
        target_run (ServiceAppFleetTargetRun | Unset):
    """

    counts: ServiceAppFleetCounts | Unset = UNSET
    groups: list[ServiceAppFleetGroup] | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    target_run: ServiceAppFleetTargetRun | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        counts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.counts, Unset):
            counts = self.counts.to_dict()

        groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        id = self.id

        name = self.name

        target_run: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target_run, Unset):
            target_run = self.target_run.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if counts is not UNSET:
            field_dict["counts"] = counts
        if groups is not UNSET:
            field_dict["groups"] = groups
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if target_run is not UNSET:
            field_dict["target_run"] = target_run

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_app_fleet_counts import ServiceAppFleetCounts  # noqa: PLC0415
        from ..models.service_app_fleet_group import ServiceAppFleetGroup  # noqa: PLC0415
        from ..models.service_app_fleet_target_run import ServiceAppFleetTargetRun  # noqa: PLC0415

        d = dict(src_dict)
        _counts = d.pop("counts", UNSET)
        counts: ServiceAppFleetCounts | Unset
        if isinstance(_counts, Unset):
            counts = UNSET
        else:
            counts = ServiceAppFleetCounts.from_dict(_counts)

        _groups = d.pop("groups", UNSET)
        groups: list[ServiceAppFleetGroup] | Unset = UNSET
        if _groups is not UNSET:
            groups = []
            for groups_item_data in _groups:
                groups_item = ServiceAppFleetGroup.from_dict(groups_item_data)

                groups.append(groups_item)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _target_run = d.pop("target_run", UNSET)
        target_run: ServiceAppFleetTargetRun | Unset
        if isinstance(_target_run, Unset):
            target_run = UNSET
        else:
            target_run = ServiceAppFleetTargetRun.from_dict(_target_run)

        service_app_fleet_branch = cls(
            counts=counts,
            groups=groups,
            id=id,
            name=name,
            target_run=target_run,
        )

        service_app_fleet_branch.additional_properties = d
        return service_app_fleet_branch

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
