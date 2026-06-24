from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppStackVersionRunRoleDiff")


@_attrs_define
class AppStackVersionRunRoleDiff:
    """
    Attributes:
        disabled (list[str] | Unset):
        enabled (list[str] | Unset):
    """

    disabled: list[str] | Unset = UNSET
    enabled: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        disabled: list[str] | Unset = UNSET
        if not isinstance(self.disabled, Unset):
            disabled = self.disabled

        enabled: list[str] | Unset = UNSET
        if not isinstance(self.enabled, Unset):
            enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        disabled = cast(list[str], d.pop("disabled", UNSET))

        enabled = cast(list[str], d.pop("enabled", UNSET))

        app_stack_version_run_role_diff = cls(
            disabled=disabled,
            enabled=enabled,
        )

        app_stack_version_run_role_diff.additional_properties = d
        return app_stack_version_run_role_diff

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
