from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceInstallAlignmentExplanation")


@_attrs_define
class ServiceInstallAlignmentExplanation:
    """
    Attributes:
        status (str | Unset):
        step_id (str | Unset):
        summary (str | Unset):
        workflow_id (str | Unset):
    """

    status: str | Unset = UNSET
    step_id: str | Unset = UNSET
    summary: str | Unset = UNSET
    workflow_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        step_id = self.step_id

        summary = self.summary

        workflow_id = self.workflow_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if step_id is not UNSET:
            field_dict["step_id"] = step_id
        if summary is not UNSET:
            field_dict["summary"] = summary
        if workflow_id is not UNSET:
            field_dict["workflow_id"] = workflow_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status", UNSET)

        step_id = d.pop("step_id", UNSET)

        summary = d.pop("summary", UNSET)

        workflow_id = d.pop("workflow_id", UNSET)

        service_install_alignment_explanation = cls(
            status=status,
            step_id=step_id,
            summary=summary,
            workflow_id=workflow_id,
        )

        service_install_alignment_explanation.additional_properties = d
        return service_install_alignment_explanation

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
