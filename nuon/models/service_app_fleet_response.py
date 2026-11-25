from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_app_fleet_branch import ServiceAppFleetBranch
    from ..models.service_app_fleet_summary import ServiceAppFleetSummary


T = TypeVar("T", bound="ServiceAppFleetResponse")


@_attrs_define
class ServiceAppFleetResponse:
    """
    Attributes:
        branches (list[ServiceAppFleetBranch] | Unset):
        summary (ServiceAppFleetSummary | Unset):
    """

    branches: list[ServiceAppFleetBranch] | Unset = UNSET
    summary: ServiceAppFleetSummary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        branches: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.branches, Unset):
            branches = []
            for branches_item_data in self.branches:
                branches_item = branches_item_data.to_dict()
                branches.append(branches_item)

        summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if branches is not UNSET:
            field_dict["branches"] = branches
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_app_fleet_branch import ServiceAppFleetBranch  # noqa: PLC0415
        from ..models.service_app_fleet_summary import ServiceAppFleetSummary  # noqa: PLC0415

        d = dict(src_dict)
        _branches = d.pop("branches", UNSET)
        branches: list[ServiceAppFleetBranch] | Unset = UNSET
        if _branches is not UNSET:
            branches = []
            for branches_item_data in _branches:
                branches_item = ServiceAppFleetBranch.from_dict(branches_item_data)

                branches.append(branches_item)

        _summary = d.pop("summary", UNSET)
        summary: ServiceAppFleetSummary | Unset
        if isinstance(_summary, Unset):
            summary = UNSET
        else:
            summary = ServiceAppFleetSummary.from_dict(_summary)

        service_app_fleet_response = cls(
            branches=branches,
            summary=summary,
        )

        service_app_fleet_response.additional_properties = d
        return service_app_fleet_response

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
