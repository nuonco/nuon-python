from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_app_branch_run_preview_mode import AppAppBranchRunPreviewMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_nuonco_nuon_pkg_labels_selector import GithubComNuoncoNuonPkgLabelsSelector


T = TypeVar("T", bound="AppAppBranchPreviewConfig")


@_attrs_define
class AppAppBranchPreviewConfig:
    """
    Attributes:
        comment (bool | Unset):
        ignore_drafts (bool | Unset):
        install_id (str | Unset):
        install_name (str | Unset):
        label_selector (GithubComNuoncoNuonPkgLabelsSelector | Unset):
        mode (AppAppBranchRunPreviewMode | Unset):
        react (bool | Unset):
        set_statuses (bool | Unset):
    """

    comment: bool | Unset = UNSET
    ignore_drafts: bool | Unset = UNSET
    install_id: str | Unset = UNSET
    install_name: str | Unset = UNSET
    label_selector: GithubComNuoncoNuonPkgLabelsSelector | Unset = UNSET
    mode: AppAppBranchRunPreviewMode | Unset = UNSET
    react: bool | Unset = UNSET
    set_statuses: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        ignore_drafts = self.ignore_drafts

        install_id = self.install_id

        install_name = self.install_name

        label_selector: dict[str, Any] | Unset = UNSET
        if not isinstance(self.label_selector, Unset):
            label_selector = self.label_selector.to_dict()

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        react = self.react

        set_statuses = self.set_statuses

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment is not UNSET:
            field_dict["comment"] = comment
        if ignore_drafts is not UNSET:
            field_dict["ignore_drafts"] = ignore_drafts
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if install_name is not UNSET:
            field_dict["install_name"] = install_name
        if label_selector is not UNSET:
            field_dict["label_selector"] = label_selector
        if mode is not UNSET:
            field_dict["mode"] = mode
        if react is not UNSET:
            field_dict["react"] = react
        if set_statuses is not UNSET:
            field_dict["set_statuses"] = set_statuses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_nuonco_nuon_pkg_labels_selector import (
            GithubComNuoncoNuonPkgLabelsSelector,  # noqa: PLC0415
        )

        d = dict(src_dict)
        comment = d.pop("comment", UNSET)

        ignore_drafts = d.pop("ignore_drafts", UNSET)

        install_id = d.pop("install_id", UNSET)

        install_name = d.pop("install_name", UNSET)

        _label_selector = d.pop("label_selector", UNSET)
        label_selector: GithubComNuoncoNuonPkgLabelsSelector | Unset
        if isinstance(_label_selector, Unset):
            label_selector = UNSET
        else:
            label_selector = GithubComNuoncoNuonPkgLabelsSelector.from_dict(_label_selector)

        _mode = d.pop("mode", UNSET)
        mode: AppAppBranchRunPreviewMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = AppAppBranchRunPreviewMode(_mode)

        react = d.pop("react", UNSET)

        set_statuses = d.pop("set_statuses", UNSET)

        app_app_branch_preview_config = cls(
            comment=comment,
            ignore_drafts=ignore_drafts,
            install_id=install_id,
            install_name=install_name,
            label_selector=label_selector,
            mode=mode,
            react=react,
            set_statuses=set_statuses,
        )

        app_app_branch_preview_config.additional_properties = d
        return app_app_branch_preview_config

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
