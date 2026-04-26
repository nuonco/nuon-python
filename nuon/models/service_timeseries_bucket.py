from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_series_point import ServiceSeriesPoint


T = TypeVar("T", bound="ServiceTimeseriesBucket")


@_attrs_define
class ServiceTimeseriesBucket:
    """
    Attributes:
        denies (int | Unset):
        evaluations (int | Unset):
        passes (int | Unset):
        series (list[ServiceSeriesPoint] | Unset):
        time (str | Unset):
        warns (int | Unset):
    """

    denies: int | Unset = UNSET
    evaluations: int | Unset = UNSET
    passes: int | Unset = UNSET
    series: list[ServiceSeriesPoint] | Unset = UNSET
    time: str | Unset = UNSET
    warns: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        denies = self.denies

        evaluations = self.evaluations

        passes = self.passes

        series: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.series, Unset):
            series = []
            for series_item_data in self.series:
                series_item = series_item_data.to_dict()
                series.append(series_item)

        time = self.time

        warns = self.warns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if denies is not UNSET:
            field_dict["denies"] = denies
        if evaluations is not UNSET:
            field_dict["evaluations"] = evaluations
        if passes is not UNSET:
            field_dict["passes"] = passes
        if series is not UNSET:
            field_dict["series"] = series
        if time is not UNSET:
            field_dict["time"] = time
        if warns is not UNSET:
            field_dict["warns"] = warns

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_series_point import ServiceSeriesPoint

        d = dict(src_dict)
        denies = d.pop("denies", UNSET)

        evaluations = d.pop("evaluations", UNSET)

        passes = d.pop("passes", UNSET)

        _series = d.pop("series", UNSET)
        series: list[ServiceSeriesPoint] | Unset = UNSET
        if _series is not UNSET:
            series = []
            for series_item_data in _series:
                series_item = ServiceSeriesPoint.from_dict(series_item_data)

                series.append(series_item)

        time = d.pop("time", UNSET)

        warns = d.pop("warns", UNSET)

        service_timeseries_bucket = cls(
            denies=denies,
            evaluations=evaluations,
            passes=passes,
            series=series,
            time=time,
            warns=warns,
        )

        service_timeseries_bucket.additional_properties = d
        return service_timeseries_bucket

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
