from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlantypesGitSource")


@_attrs_define
class PlantypesGitSource:
    """
    Attributes:
        path (str):
        ref (str):
        url (str):
        recurse_submodules (bool | Unset):
    """

    path: str
    ref: str
    url: str
    recurse_submodules: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        ref = self.ref

        url = self.url

        recurse_submodules = self.recurse_submodules

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "ref": ref,
                "url": url,
            }
        )
        if recurse_submodules is not UNSET:
            field_dict["recurse_submodules"] = recurse_submodules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path")

        ref = d.pop("ref")

        url = d.pop("url")

        recurse_submodules = d.pop("recurse_submodules", UNSET)

        plantypes_git_source = cls(
            path=path,
            ref=ref,
            url=url,
            recurse_submodules=recurse_submodules,
        )

        plantypes_git_source.additional_properties = d
        return plantypes_git_source

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
