from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_source_file_diff import ConfigSourceFileDiff


T = TypeVar("T", bound="ConfigSourceArchiveDiff")


@_attrs_define
class ConfigSourceArchiveDiff:
    """
    Attributes:
        files (list[ConfigSourceFileDiff] | Unset):
        total_files (int | Unset):
        unchanged (int | Unset):
    """

    files: list[ConfigSourceFileDiff] | Unset = UNSET
    total_files: int | Unset = UNSET
    unchanged: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        total_files = self.total_files

        unchanged = self.unchanged

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if files is not UNSET:
            field_dict["files"] = files
        if total_files is not UNSET:
            field_dict["total_files"] = total_files
        if unchanged is not UNSET:
            field_dict["unchanged"] = unchanged

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_source_file_diff import ConfigSourceFileDiff  # noqa: PLC0415

        d = dict(src_dict)
        _files = d.pop("files", UNSET)
        files: list[ConfigSourceFileDiff] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = ConfigSourceFileDiff.from_dict(files_item_data)

                files.append(files_item)

        total_files = d.pop("total_files", UNSET)

        unchanged = d.pop("unchanged", UNSET)

        config_source_archive_diff = cls(
            files=files,
            total_files=total_files,
            unchanged=unchanged,
        )

        config_source_archive_diff.additional_properties = d
        return config_source_archive_diff

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
