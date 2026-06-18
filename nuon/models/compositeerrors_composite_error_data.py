from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.compositeerrors_severity import CompositeerrorsSeverity
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compositeerrors_section import CompositeerrorsSection


T = TypeVar("T", bound="CompositeerrorsCompositeErrorData")


@_attrs_define
class CompositeerrorsCompositeErrorData:
    """
    Attributes:
        data (list[int] | Unset):
        message (str | Unset):
        sections (list[CompositeerrorsSection] | Unset):
        severity (CompositeerrorsSeverity | Unset):
        type_ (str | Unset):
    """

    data: list[int] | Unset = UNSET
    message: str | Unset = UNSET
    sections: list[CompositeerrorsSection] | Unset = UNSET
    severity: CompositeerrorsSeverity | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: list[int] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data

        message = self.message

        sections: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sections, Unset):
            sections = []
            for sections_item_data in self.sections:
                sections_item = sections_item_data.to_dict()
                sections.append(sections_item)

        severity: str | Unset = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if message is not UNSET:
            field_dict["message"] = message
        if sections is not UNSET:
            field_dict["sections"] = sections
        if severity is not UNSET:
            field_dict["severity"] = severity
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compositeerrors_section import CompositeerrorsSection

        d = dict(src_dict)
        data = cast(list[int], d.pop("data", UNSET))

        message = d.pop("message", UNSET)

        _sections = d.pop("sections", UNSET)
        sections: list[CompositeerrorsSection] | Unset = UNSET
        if _sections is not UNSET:
            sections = []
            for sections_item_data in _sections:
                sections_item = CompositeerrorsSection.from_dict(sections_item_data)

                sections.append(sections_item)

        _severity = d.pop("severity", UNSET)
        severity: CompositeerrorsSeverity | Unset
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = CompositeerrorsSeverity(_severity)

        type_ = d.pop("type", UNSET)

        compositeerrors_composite_error_data = cls(
            data=data,
            message=message,
            sections=sections,
            severity=severity,
            type_=type_,
        )

        compositeerrors_composite_error_data.additional_properties = d
        return compositeerrors_composite_error_data

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
