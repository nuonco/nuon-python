from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceCreateServiceAccountTokenRequest")


@_attrs_define
class ServiceCreateServiceAccountTokenRequest:
    """
    Attributes:
        duration (str | Unset): Duration defaults to one year. Default: '8760h'.
        invalidate (bool | Unset):
    """

    duration: str | Unset = "8760h"
    invalidate: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duration = self.duration

        invalidate = self.invalidate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if duration is not UNSET:
            field_dict["duration"] = duration
        if invalidate is not UNSET:
            field_dict["invalidate"] = invalidate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        duration = d.pop("duration", UNSET)

        invalidate = d.pop("invalidate", UNSET)

        service_create_service_account_token_request = cls(
            duration=duration,
            invalidate=invalidate,
        )

        service_create_service_account_token_request.additional_properties = d
        return service_create_service_account_token_request

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
