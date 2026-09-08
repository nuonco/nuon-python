from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_app_branch_run_preview_mode import AppAppBranchRunPreviewMode
from ..models.app_app_branch_run_preview_source import AppAppBranchRunPreviewSource
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServicePreviewRunRequest")


@_attrs_define
class ServicePreviewRunRequest:
    """
    Attributes:
        git_ref (str | Unset):
        head_sha (str | Unset):
        install_id (str | Unset):
        mode (AppAppBranchRunPreviewMode | Unset):
        pr_number (int | Unset):
        source (AppAppBranchRunPreviewSource | Unset):
    """

    git_ref: str | Unset = UNSET
    head_sha: str | Unset = UNSET
    install_id: str | Unset = UNSET
    mode: AppAppBranchRunPreviewMode | Unset = UNSET
    pr_number: int | Unset = UNSET
    source: AppAppBranchRunPreviewSource | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        git_ref = self.git_ref

        head_sha = self.head_sha

        install_id = self.install_id

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        pr_number = self.pr_number

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if git_ref is not UNSET:
            field_dict["git_ref"] = git_ref
        if head_sha is not UNSET:
            field_dict["head_sha"] = head_sha
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if mode is not UNSET:
            field_dict["mode"] = mode
        if pr_number is not UNSET:
            field_dict["pr_number"] = pr_number
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        git_ref = d.pop("git_ref", UNSET)

        head_sha = d.pop("head_sha", UNSET)

        install_id = d.pop("install_id", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: AppAppBranchRunPreviewMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = AppAppBranchRunPreviewMode(_mode)

        pr_number = d.pop("pr_number", UNSET)

        _source = d.pop("source", UNSET)
        source: AppAppBranchRunPreviewSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = AppAppBranchRunPreviewSource(_source)

        service_preview_run_request = cls(
            git_ref=git_ref,
            head_sha=head_sha,
            install_id=install_id,
            mode=mode,
            pr_number=pr_number,
            source=source,
        )

        service_preview_run_request.additional_properties = d
        return service_preview_run_request

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
