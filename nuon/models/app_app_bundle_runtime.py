from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_app_bundle_runtime_platforms import AppAppBundleRuntimePlatforms


T = TypeVar("T", bound="AppAppBundleRuntime")


@_attrs_define
class AppAppBundleRuntime:
    """
    Attributes:
        platforms (AppAppBundleRuntimePlatforms | Unset):
        runner_image_tag (str | Unset):
        runner_image_url (str | Unset):
    """

    platforms: AppAppBundleRuntimePlatforms | Unset = UNSET
    runner_image_tag: str | Unset = UNSET
    runner_image_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platforms: dict[str, Any] | Unset = UNSET
        if not isinstance(self.platforms, Unset):
            platforms = self.platforms.to_dict()

        runner_image_tag = self.runner_image_tag

        runner_image_url = self.runner_image_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if platforms is not UNSET:
            field_dict["platforms"] = platforms
        if runner_image_tag is not UNSET:
            field_dict["runner_image_tag"] = runner_image_tag
        if runner_image_url is not UNSET:
            field_dict["runner_image_url"] = runner_image_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_app_bundle_runtime_platforms import AppAppBundleRuntimePlatforms  # noqa: PLC0415

        d = dict(src_dict)
        _platforms = d.pop("platforms", UNSET)
        platforms: AppAppBundleRuntimePlatforms | Unset
        if isinstance(_platforms, Unset):
            platforms = UNSET
        else:
            platforms = AppAppBundleRuntimePlatforms.from_dict(_platforms)

        runner_image_tag = d.pop("runner_image_tag", UNSET)

        runner_image_url = d.pop("runner_image_url", UNSET)

        app_app_bundle_runtime = cls(
            platforms=platforms,
            runner_image_tag=runner_image_tag,
            runner_image_url=runner_image_url,
        )

        app_app_bundle_runtime.additional_properties = d
        return app_app_bundle_runtime

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
