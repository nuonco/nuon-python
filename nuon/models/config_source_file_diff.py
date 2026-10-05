from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigSourceFileDiff")


@_attrs_define
class ConfigSourceFileDiff:
    """
    Attributes:
        after_sha256 (str | Unset):
        after_size (int | Unset):
        before_sha256 (str | Unset):
        before_size (int | Unset):
        op (str | Unset):
        patch (str | Unset):
        patch_truncated (bool | Unset):
        path (str | Unset):
    """

    after_sha256: str | Unset = UNSET
    after_size: int | Unset = UNSET
    before_sha256: str | Unset = UNSET
    before_size: int | Unset = UNSET
    op: str | Unset = UNSET
    patch: str | Unset = UNSET
    patch_truncated: bool | Unset = UNSET
    path: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        after_sha256 = self.after_sha256

        after_size = self.after_size

        before_sha256 = self.before_sha256

        before_size = self.before_size

        op = self.op

        patch = self.patch

        patch_truncated = self.patch_truncated

        path = self.path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if after_sha256 is not UNSET:
            field_dict["after_sha256"] = after_sha256
        if after_size is not UNSET:
            field_dict["after_size"] = after_size
        if before_sha256 is not UNSET:
            field_dict["before_sha256"] = before_sha256
        if before_size is not UNSET:
            field_dict["before_size"] = before_size
        if op is not UNSET:
            field_dict["op"] = op
        if patch is not UNSET:
            field_dict["patch"] = patch
        if patch_truncated is not UNSET:
            field_dict["patch_truncated"] = patch_truncated
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        after_sha256 = d.pop("after_sha256", UNSET)

        after_size = d.pop("after_size", UNSET)

        before_sha256 = d.pop("before_sha256", UNSET)

        before_size = d.pop("before_size", UNSET)

        op = d.pop("op", UNSET)

        patch = d.pop("patch", UNSET)

        patch_truncated = d.pop("patch_truncated", UNSET)

        path = d.pop("path", UNSET)

        config_source_file_diff = cls(
            after_sha256=after_sha256,
            after_size=after_size,
            before_sha256=before_sha256,
            before_size=before_size,
            op=op,
            patch=patch,
            patch_truncated=patch_truncated,
            path=path,
        )

        config_source_file_diff.additional_properties = d
        return config_source_file_diff

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
