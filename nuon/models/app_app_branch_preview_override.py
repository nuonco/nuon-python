from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_app_branch_run_preview_mode import AppAppBranchRunPreviewMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppAppBranchPreviewOverride")


@_attrs_define
class AppAppBranchPreviewOverride:
    """
    Attributes:
        install_id (str | Unset):
        mode (AppAppBranchRunPreviewMode | Unset):
    """

    install_id: str | Unset = UNSET
    mode: AppAppBranchRunPreviewMode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        install_id = self.install_id

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        install_id = d.pop("install_id", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: AppAppBranchRunPreviewMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = AppAppBranchRunPreviewMode(_mode)

        app_app_branch_preview_override = cls(
            install_id=install_id,
            mode=mode,
        )

        app_app_branch_preview_override.additional_properties = d
        return app_app_branch_preview_override

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
