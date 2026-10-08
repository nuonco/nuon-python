from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppAppBundlePlatformRuntime")


@_attrs_define
class AppAppBundlePlatformRuntime:
    """
    Attributes:
        runner_binary_url (str | Unset):
    """

    runner_binary_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        runner_binary_url = self.runner_binary_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if runner_binary_url is not UNSET:
            field_dict["runner_binary_url"] = runner_binary_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        runner_binary_url = d.pop("runner_binary_url", UNSET)

        app_app_bundle_platform_runtime = cls(
            runner_binary_url=runner_binary_url,
        )

        app_app_bundle_platform_runtime.additional_properties = d
        return app_app_bundle_platform_runtime

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
