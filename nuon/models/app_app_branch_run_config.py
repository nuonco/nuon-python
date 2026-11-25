from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_app_branch_run_mode import AppAppBranchRunMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppAppBranchRunConfig")


@_attrs_define
class AppAppBranchRunConfig:
    """
    Attributes:
        github_label (str | Unset):
        mode (AppAppBranchRunMode | Unset):
        paths (list[str] | Unset): Paths and PathsIgnore are mutually exclusive, and neither accepts a pattern
            starting with "!". The check on app_branch_configs.run_config enforces this;
            AutoMigrate creates it, it is not a migration.
        paths_ignore (list[str] | Unset):
        tag_prefix (str | Unset):
    """

    github_label: str | Unset = UNSET
    mode: AppAppBranchRunMode | Unset = UNSET
    paths: list[str] | Unset = UNSET
    paths_ignore: list[str] | Unset = UNSET
    tag_prefix: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        github_label = self.github_label

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        paths: list[str] | Unset = UNSET
        if not isinstance(self.paths, Unset):
            paths = self.paths

        paths_ignore: list[str] | Unset = UNSET
        if not isinstance(self.paths_ignore, Unset):
            paths_ignore = self.paths_ignore

        tag_prefix = self.tag_prefix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if github_label is not UNSET:
            field_dict["github_label"] = github_label
        if mode is not UNSET:
            field_dict["mode"] = mode
        if paths is not UNSET:
            field_dict["paths"] = paths
        if paths_ignore is not UNSET:
            field_dict["paths_ignore"] = paths_ignore
        if tag_prefix is not UNSET:
            field_dict["tag_prefix"] = tag_prefix

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        github_label = d.pop("github_label", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: AppAppBranchRunMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = AppAppBranchRunMode(_mode)

        paths = cast(list[str], d.pop("paths", UNSET))

        paths_ignore = cast(list[str], d.pop("paths_ignore", UNSET))

        tag_prefix = d.pop("tag_prefix", UNSET)

        app_app_branch_run_config = cls(
            github_label=github_label,
            mode=mode,
            paths=paths,
            paths_ignore=paths_ignore,
            tag_prefix=tag_prefix,
        )

        app_app_branch_run_config.additional_properties = d
        return app_app_branch_run_config

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
