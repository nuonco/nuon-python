from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServicePolicyAnalyticsSummary")


@_attrs_define
class ServicePolicyAnalyticsSummary:
    """
    Attributes:
        end (str | Unset):
        start (str | Unset):
        total_denies (int | Unset):
        total_evaluations (int | Unset):
        total_passes (int | Unset):
        total_warns (int | Unset):
        unique_policies (int | Unset):
        unique_reports (int | Unset):
    """

    end: str | Unset = UNSET
    start: str | Unset = UNSET
    total_denies: int | Unset = UNSET
    total_evaluations: int | Unset = UNSET
    total_passes: int | Unset = UNSET
    total_warns: int | Unset = UNSET
    unique_policies: int | Unset = UNSET
    unique_reports: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end = self.end

        start = self.start

        total_denies = self.total_denies

        total_evaluations = self.total_evaluations

        total_passes = self.total_passes

        total_warns = self.total_warns

        unique_policies = self.unique_policies

        unique_reports = self.unique_reports

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end is not UNSET:
            field_dict["end"] = end
        if start is not UNSET:
            field_dict["start"] = start
        if total_denies is not UNSET:
            field_dict["total_denies"] = total_denies
        if total_evaluations is not UNSET:
            field_dict["total_evaluations"] = total_evaluations
        if total_passes is not UNSET:
            field_dict["total_passes"] = total_passes
        if total_warns is not UNSET:
            field_dict["total_warns"] = total_warns
        if unique_policies is not UNSET:
            field_dict["unique_policies"] = unique_policies
        if unique_reports is not UNSET:
            field_dict["unique_reports"] = unique_reports

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        end = d.pop("end", UNSET)

        start = d.pop("start", UNSET)

        total_denies = d.pop("total_denies", UNSET)

        total_evaluations = d.pop("total_evaluations", UNSET)

        total_passes = d.pop("total_passes", UNSET)

        total_warns = d.pop("total_warns", UNSET)

        unique_policies = d.pop("unique_policies", UNSET)

        unique_reports = d.pop("unique_reports", UNSET)

        service_policy_analytics_summary = cls(
            end=end,
            start=start,
            total_denies=total_denies,
            total_evaluations=total_evaluations,
            total_passes=total_passes,
            total_warns=total_warns,
            unique_policies=unique_policies,
            unique_reports=unique_reports,
        )

        service_policy_analytics_summary.additional_properties = d
        return service_policy_analytics_summary

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
