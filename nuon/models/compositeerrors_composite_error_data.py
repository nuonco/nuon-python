from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.compositeerrors_severity import CompositeerrorsSeverity
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compositeerrors_hints import CompositeerrorsHints
    from ..models.compositeerrors_section import CompositeerrorsSection


T = TypeVar("T", bound="CompositeerrorsCompositeErrorData")


@_attrs_define
class CompositeerrorsCompositeErrorData:
    """
    Attributes:
        data (list[int] | Unset): Data is the typed, per-error-type payload: WHAT the error is. Closed
            schema per Type. Read to render sections and by any future view.
        hints (CompositeerrorsHints | Unset):
        message (str | Unset):
        sections (list[CompositeerrorsSection] | Unset):
        severity (CompositeerrorsSeverity | Unset):
        source_id (str | Unset): SourceID / SourceType identify the row this error originated on
            (polymorphic, same shape as OwnerID/OwnerType). Set at the record site,
            e.g. ("runner_job_execution_results", "<result id>"). Enables a future
            JOINable view without a separate error table.
        source_type (str | Unset):
        type_ (str | Unset):
        version (int | Unset): Version is the payload schema version (SchemaVersion at write time).
    """

    data: list[int] | Unset = UNSET
    hints: CompositeerrorsHints | Unset = UNSET
    message: str | Unset = UNSET
    sections: list[CompositeerrorsSection] | Unset = UNSET
    severity: CompositeerrorsSeverity | Unset = UNSET
    source_id: str | Unset = UNSET
    source_type: str | Unset = UNSET
    type_: str | Unset = UNSET
    version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: list[int] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data

        hints: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hints, Unset):
            hints = self.hints.to_dict()

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

        source_id = self.source_id

        source_type = self.source_type

        type_ = self.type_

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if hints is not UNSET:
            field_dict["hints"] = hints
        if message is not UNSET:
            field_dict["message"] = message
        if sections is not UNSET:
            field_dict["sections"] = sections
        if severity is not UNSET:
            field_dict["severity"] = severity
        if source_id is not UNSET:
            field_dict["source_id"] = source_id
        if source_type is not UNSET:
            field_dict["source_type"] = source_type
        if type_ is not UNSET:
            field_dict["type"] = type_
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compositeerrors_hints import CompositeerrorsHints
        from ..models.compositeerrors_section import CompositeerrorsSection

        d = dict(src_dict)
        data = cast(list[int], d.pop("data", UNSET))

        _hints = d.pop("hints", UNSET)
        hints: CompositeerrorsHints | Unset
        if isinstance(_hints, Unset):
            hints = UNSET
        else:
            hints = CompositeerrorsHints.from_dict(_hints)

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

        source_id = d.pop("source_id", UNSET)

        source_type = d.pop("source_type", UNSET)

        type_ = d.pop("type", UNSET)

        version = d.pop("version", UNSET)

        compositeerrors_composite_error_data = cls(
            data=data,
            hints=hints,
            message=message,
            sections=sections,
            severity=severity,
            source_id=source_id,
            source_type=source_type,
            type_=type_,
            version=version,
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
