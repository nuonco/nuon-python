from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceResetInstallHealthBaselineResponse")


@_attrs_define
class ServiceResetInstallHealthBaselineResponse:
    """
    Attributes:
        baseline_at (str | Unset):
    """

    baseline_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        baseline_at = self.baseline_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if baseline_at is not UNSET:
            field_dict["baseline_at"] = baseline_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        baseline_at = d.pop("baseline_at", UNSET)

        service_reset_install_health_baseline_response = cls(
            baseline_at=baseline_at,
        )

        service_reset_install_health_baseline_response.additional_properties = d
        return service_reset_install_health_baseline_response

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
