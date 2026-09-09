from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HelpersPreviewSourcePR")


@_attrs_define
class HelpersPreviewSourcePR:
    """
    Attributes:
        head_ref (str | Unset):
        head_sha (str | Unset):
        pr_number (int | Unset):
        title (str | Unset):
        url (str | Unset):
    """

    head_ref: str | Unset = UNSET
    head_sha: str | Unset = UNSET
    pr_number: int | Unset = UNSET
    title: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        head_ref = self.head_ref

        head_sha = self.head_sha

        pr_number = self.pr_number

        title = self.title

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if head_ref is not UNSET:
            field_dict["head_ref"] = head_ref
        if head_sha is not UNSET:
            field_dict["head_sha"] = head_sha
        if pr_number is not UNSET:
            field_dict["pr_number"] = pr_number
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        head_ref = d.pop("head_ref", UNSET)

        head_sha = d.pop("head_sha", UNSET)

        pr_number = d.pop("pr_number", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        helpers_preview_source_pr = cls(
            head_ref=head_ref,
            head_sha=head_sha,
            pr_number=pr_number,
            title=title,
            url=url,
        )

        helpers_preview_source_pr.additional_properties = d
        return helpers_preview_source_pr

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
