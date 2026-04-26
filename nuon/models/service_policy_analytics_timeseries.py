from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_timeseries_bucket import ServiceTimeseriesBucket


T = TypeVar("T", bound="ServicePolicyAnalyticsTimeseries")


@_attrs_define
class ServicePolicyAnalyticsTimeseries:
    """
    Attributes:
        buckets (list[ServiceTimeseriesBucket] | Unset):
        end (str | Unset):
        group_by (list[str] | Unset):
        interval (str | Unset):
        start (str | Unset):
    """

    buckets: list[ServiceTimeseriesBucket] | Unset = UNSET
    end: str | Unset = UNSET
    group_by: list[str] | Unset = UNSET
    interval: str | Unset = UNSET
    start: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buckets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.buckets, Unset):
            buckets = []
            for buckets_item_data in self.buckets:
                buckets_item = buckets_item_data.to_dict()
                buckets.append(buckets_item)

        end = self.end

        group_by: list[str] | Unset = UNSET
        if not isinstance(self.group_by, Unset):
            group_by = self.group_by

        interval = self.interval

        start = self.start

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if buckets is not UNSET:
            field_dict["buckets"] = buckets
        if end is not UNSET:
            field_dict["end"] = end
        if group_by is not UNSET:
            field_dict["group_by"] = group_by
        if interval is not UNSET:
            field_dict["interval"] = interval
        if start is not UNSET:
            field_dict["start"] = start

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_timeseries_bucket import ServiceTimeseriesBucket

        d = dict(src_dict)
        _buckets = d.pop("buckets", UNSET)
        buckets: list[ServiceTimeseriesBucket] | Unset = UNSET
        if _buckets is not UNSET:
            buckets = []
            for buckets_item_data in _buckets:
                buckets_item = ServiceTimeseriesBucket.from_dict(buckets_item_data)

                buckets.append(buckets_item)

        end = d.pop("end", UNSET)

        group_by = cast(list[str], d.pop("group_by", UNSET))

        interval = d.pop("interval", UNSET)

        start = d.pop("start", UNSET)

        service_policy_analytics_timeseries = cls(
            buckets=buckets,
            end=end,
            group_by=group_by,
            interval=interval,
            start=start,
        )

        service_policy_analytics_timeseries.additional_properties = d
        return service_policy_analytics_timeseries

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
