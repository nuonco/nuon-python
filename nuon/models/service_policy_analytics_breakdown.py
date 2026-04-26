from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_breakdown_entry import ServiceBreakdownEntry


T = TypeVar("T", bound="ServicePolicyAnalyticsBreakdown")


@_attrs_define
class ServicePolicyAnalyticsBreakdown:
    """
    Attributes:
        dimension (str | Unset):
        end (str | Unset):
        entries (list[ServiceBreakdownEntry] | Unset):
        start (str | Unset):
    """

    dimension: str | Unset = UNSET
    end: str | Unset = UNSET
    entries: list[ServiceBreakdownEntry] | Unset = UNSET
    start: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dimension = self.dimension

        end = self.end

        entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        start = self.start

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dimension is not UNSET:
            field_dict["dimension"] = dimension
        if end is not UNSET:
            field_dict["end"] = end
        if entries is not UNSET:
            field_dict["entries"] = entries
        if start is not UNSET:
            field_dict["start"] = start

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_breakdown_entry import ServiceBreakdownEntry

        d = dict(src_dict)
        dimension = d.pop("dimension", UNSET)

        end = d.pop("end", UNSET)

        _entries = d.pop("entries", UNSET)
        entries: list[ServiceBreakdownEntry] | Unset = UNSET
        if _entries is not UNSET:
            entries = []
            for entries_item_data in _entries:
                entries_item = ServiceBreakdownEntry.from_dict(entries_item_data)

                entries.append(entries_item)

        start = d.pop("start", UNSET)

        service_policy_analytics_breakdown = cls(
            dimension=dimension,
            end=end,
            entries=entries,
            start=start,
        )

        service_policy_analytics_breakdown.additional_properties = d
        return service_policy_analytics_breakdown

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
