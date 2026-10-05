from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppAppConfigRef")


@_attrs_define
class AppAppConfigRef:
    """
    Attributes:
        applied_config_at (str | Unset):
        applied_config_by_id (str | Unset):
        applied_config_by_type (str | Unset):
        applied_config_id (str | Unset):
        expected_config_id (str | Unset):
    """

    applied_config_at: str | Unset = UNSET
    applied_config_by_id: str | Unset = UNSET
    applied_config_by_type: str | Unset = UNSET
    applied_config_id: str | Unset = UNSET
    expected_config_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        applied_config_at = self.applied_config_at

        applied_config_by_id = self.applied_config_by_id

        applied_config_by_type = self.applied_config_by_type

        applied_config_id = self.applied_config_id

        expected_config_id = self.expected_config_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if applied_config_at is not UNSET:
            field_dict["applied_config_at"] = applied_config_at
        if applied_config_by_id is not UNSET:
            field_dict["applied_config_by_id"] = applied_config_by_id
        if applied_config_by_type is not UNSET:
            field_dict["applied_config_by_type"] = applied_config_by_type
        if applied_config_id is not UNSET:
            field_dict["applied_config_id"] = applied_config_id
        if expected_config_id is not UNSET:
            field_dict["expected_config_id"] = expected_config_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        applied_config_at = d.pop("applied_config_at", UNSET)

        applied_config_by_id = d.pop("applied_config_by_id", UNSET)

        applied_config_by_type = d.pop("applied_config_by_type", UNSET)

        applied_config_id = d.pop("applied_config_id", UNSET)

        expected_config_id = d.pop("expected_config_id", UNSET)

        app_app_config_ref = cls(
            applied_config_at=applied_config_at,
            applied_config_by_id=applied_config_by_id,
            applied_config_by_type=applied_config_by_type,
            applied_config_id=applied_config_id,
            expected_config_id=expected_config_id,
        )

        app_app_config_ref.additional_properties = d
        return app_app_config_ref

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
