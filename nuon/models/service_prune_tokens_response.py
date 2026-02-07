from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServicePruneTokensResponse")


@_attrs_define
class ServicePruneTokensResponse:
    """
    Attributes:
        invalidated_count (int | Unset):
    """

    invalidated_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        invalidated_count = self.invalidated_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invalidated_count is not UNSET:
            field_dict["invalidated_count"] = invalidated_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        invalidated_count = d.pop("invalidated_count", UNSET)

        service_prune_tokens_response = cls(
            invalidated_count=invalidated_count,
        )

        service_prune_tokens_response.additional_properties = d
        return service_prune_tokens_response

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
