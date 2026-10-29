from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.helpers_preview_source_pr_label import HelpersPreviewSourcePRLabel


T = TypeVar("T", bound="HelpersPreviewSourcePR")


@_attrs_define
class HelpersPreviewSourcePR:
    """
    Attributes:
        author (str | Unset):
        author_avatar_url (str | Unset):
        created_at (str | Unset):
        head_ref (str | Unset):
        head_sha (str | Unset):
        is_draft (bool | Unset):
        labels (list[HelpersPreviewSourcePRLabel] | Unset):
        pr_number (int | Unset):
        title (str | Unset):
        updated_at (str | Unset):
        url (str | Unset):
    """

    author: str | Unset = UNSET
    author_avatar_url: str | Unset = UNSET
    created_at: str | Unset = UNSET
    head_ref: str | Unset = UNSET
    head_sha: str | Unset = UNSET
    is_draft: bool | Unset = UNSET
    labels: list[HelpersPreviewSourcePRLabel] | Unset = UNSET
    pr_number: int | Unset = UNSET
    title: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author = self.author

        author_avatar_url = self.author_avatar_url

        created_at = self.created_at

        head_ref = self.head_ref

        head_sha = self.head_sha

        is_draft = self.is_draft

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        pr_number = self.pr_number

        title = self.title

        updated_at = self.updated_at

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author
        if author_avatar_url is not UNSET:
            field_dict["author_avatar_url"] = author_avatar_url
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if head_ref is not UNSET:
            field_dict["head_ref"] = head_ref
        if head_sha is not UNSET:
            field_dict["head_sha"] = head_sha
        if is_draft is not UNSET:
            field_dict["is_draft"] = is_draft
        if labels is not UNSET:
            field_dict["labels"] = labels
        if pr_number is not UNSET:
            field_dict["pr_number"] = pr_number
        if title is not UNSET:
            field_dict["title"] = title
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.helpers_preview_source_pr_label import HelpersPreviewSourcePRLabel  # noqa: PLC0415

        d = dict(src_dict)
        author = d.pop("author", UNSET)

        author_avatar_url = d.pop("author_avatar_url", UNSET)

        created_at = d.pop("created_at", UNSET)

        head_ref = d.pop("head_ref", UNSET)

        head_sha = d.pop("head_sha", UNSET)

        is_draft = d.pop("is_draft", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: list[HelpersPreviewSourcePRLabel] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = HelpersPreviewSourcePRLabel.from_dict(labels_item_data)

                labels.append(labels_item)

        pr_number = d.pop("pr_number", UNSET)

        title = d.pop("title", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        helpers_preview_source_pr = cls(
            author=author,
            author_avatar_url=author_avatar_url,
            created_at=created_at,
            head_ref=head_ref,
            head_sha=head_sha,
            is_draft=is_draft,
            labels=labels,
            pr_number=pr_number,
            title=title,
            updated_at=updated_at,
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
