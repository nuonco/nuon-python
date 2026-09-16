from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_install_app_config_version import AppInstallAppConfigVersion
    from ..models.app_install_config_diff import AppInstallConfigDiff


T = TypeVar("T", bound="ServiceInstallAppConfigUpdate")


@_attrs_define
class ServiceInstallAppConfigUpdate:
    """
    Attributes:
        diff (AppInstallConfigDiff | Unset):
        version (AppInstallAppConfigVersion | Unset):
    """

    diff: AppInstallConfigDiff | Unset = UNSET
    version: AppInstallAppConfigVersion | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        diff: dict[str, Any] | Unset = UNSET
        if not isinstance(self.diff, Unset):
            diff = self.diff.to_dict()

        version: dict[str, Any] | Unset = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if diff is not UNSET:
            field_dict["diff"] = diff
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_install_app_config_version import AppInstallAppConfigVersion  # noqa: PLC0415
        from ..models.app_install_config_diff import AppInstallConfigDiff  # noqa: PLC0415

        d = dict(src_dict)
        _diff = d.pop("diff", UNSET)
        diff: AppInstallConfigDiff | Unset
        if isinstance(_diff, Unset):
            diff = UNSET
        else:
            diff = AppInstallConfigDiff.from_dict(_diff)

        _version = d.pop("version", UNSET)
        version: AppInstallAppConfigVersion | Unset
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = AppInstallAppConfigVersion.from_dict(_version)

        service_install_app_config_update = cls(
            diff=diff,
            version=version,
        )

        service_install_app_config_update.additional_properties = d
        return service_install_app_config_update

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
