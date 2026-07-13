from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.compositeerrors_section_kind import CompositeerrorsSectionKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="CompositeerrorsSection")


@_attrs_define
class CompositeerrorsSection:
    """
    Attributes:
        body (str | Unset):
        heading (str | Unset):
        kind (CompositeerrorsSectionKind | Unset):
    """

    body: str | Unset = UNSET
    heading: str | Unset = UNSET
    kind: CompositeerrorsSectionKind | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        heading = self.heading

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if body is not UNSET:
            field_dict["body"] = body
        if heading is not UNSET:
            field_dict["heading"] = heading
        if kind is not UNSET:
            field_dict["kind"] = kind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        body = d.pop("body", UNSET)

        heading = d.pop("heading", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: CompositeerrorsSectionKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = CompositeerrorsSectionKind(_kind)

        compositeerrors_section = cls(
            body=body,
            heading=heading,
            kind=kind,
        )

        compositeerrors_section.additional_properties = d
        return compositeerrors_section

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
