from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_app_branch_run_trigger import AppAppBranchRunTrigger
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppAppBranchRunMetadata")


@_attrs_define
class AppAppBranchRunMetadata:
    """
    Attributes:
        base_branch (str | Unset):
        git_ref (str | Unset):
        github_label (str | Unset):
        head_sha (str | Unset):
        is_draft (bool | Unset):
        pr_number (int | Unset):
        run_mode (str | Unset):
        tag (str | Unset):
        tag_prefix (str | Unset):
        trigger (AppAppBranchRunTrigger | Unset):
    """

    base_branch: str | Unset = UNSET
    git_ref: str | Unset = UNSET
    github_label: str | Unset = UNSET
    head_sha: str | Unset = UNSET
    is_draft: bool | Unset = UNSET
    pr_number: int | Unset = UNSET
    run_mode: str | Unset = UNSET
    tag: str | Unset = UNSET
    tag_prefix: str | Unset = UNSET
    trigger: AppAppBranchRunTrigger | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_branch = self.base_branch

        git_ref = self.git_ref

        github_label = self.github_label

        head_sha = self.head_sha

        is_draft = self.is_draft

        pr_number = self.pr_number

        run_mode = self.run_mode

        tag = self.tag

        tag_prefix = self.tag_prefix

        trigger: str | Unset = UNSET
        if not isinstance(self.trigger, Unset):
            trigger = self.trigger.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_branch is not UNSET:
            field_dict["base_branch"] = base_branch
        if git_ref is not UNSET:
            field_dict["git_ref"] = git_ref
        if github_label is not UNSET:
            field_dict["github_label"] = github_label
        if head_sha is not UNSET:
            field_dict["head_sha"] = head_sha
        if is_draft is not UNSET:
            field_dict["is_draft"] = is_draft
        if pr_number is not UNSET:
            field_dict["pr_number"] = pr_number
        if run_mode is not UNSET:
            field_dict["run_mode"] = run_mode
        if tag is not UNSET:
            field_dict["tag"] = tag
        if tag_prefix is not UNSET:
            field_dict["tag_prefix"] = tag_prefix
        if trigger is not UNSET:
            field_dict["trigger"] = trigger

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base_branch = d.pop("base_branch", UNSET)

        git_ref = d.pop("git_ref", UNSET)

        github_label = d.pop("github_label", UNSET)

        head_sha = d.pop("head_sha", UNSET)

        is_draft = d.pop("is_draft", UNSET)

        pr_number = d.pop("pr_number", UNSET)

        run_mode = d.pop("run_mode", UNSET)

        tag = d.pop("tag", UNSET)

        tag_prefix = d.pop("tag_prefix", UNSET)

        _trigger = d.pop("trigger", UNSET)
        trigger: AppAppBranchRunTrigger | Unset
        if isinstance(_trigger, Unset):
            trigger = UNSET
        else:
            trigger = AppAppBranchRunTrigger(_trigger)

        app_app_branch_run_metadata = cls(
            base_branch=base_branch,
            git_ref=git_ref,
            github_label=github_label,
            head_sha=head_sha,
            is_draft=is_draft,
            pr_number=pr_number,
            run_mode=run_mode,
            tag=tag,
            tag_prefix=tag_prefix,
            trigger=trigger,
        )

        app_app_branch_run_metadata.additional_properties = d
        return app_app_branch_run_metadata

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
