from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_series_point_labels import ServiceSeriesPointLabels


T = TypeVar("T", bound="ServiceSeriesPoint")


@_attrs_define
class ServiceSeriesPoint:
    """
    Attributes:
        denies (int | Unset):
        evaluations (int | Unset):
        labels (ServiceSeriesPointLabels | Unset):
        passes (int | Unset):
        warns (int | Unset):
    """

    denies: int | Unset = UNSET
    evaluations: int | Unset = UNSET
    labels: ServiceSeriesPointLabels | Unset = UNSET
    passes: int | Unset = UNSET
    warns: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        denies = self.denies

        evaluations = self.evaluations

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        passes = self.passes

        warns = self.warns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if denies is not UNSET:
            field_dict["denies"] = denies
        if evaluations is not UNSET:
            field_dict["evaluations"] = evaluations
        if labels is not UNSET:
            field_dict["labels"] = labels
        if passes is not UNSET:
            field_dict["passes"] = passes
        if warns is not UNSET:
            field_dict["warns"] = warns

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_series_point_labels import ServiceSeriesPointLabels

        d = dict(src_dict)
        denies = d.pop("denies", UNSET)

        evaluations = d.pop("evaluations", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: ServiceSeriesPointLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = ServiceSeriesPointLabels.from_dict(_labels)

        passes = d.pop("passes", UNSET)

        warns = d.pop("warns", UNSET)

        service_series_point = cls(
            denies=denies,
            evaluations=evaluations,
            labels=labels,
            passes=passes,
            warns=warns,
        )

        service_series_point.additional_properties = d
        return service_series_point

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
