from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppbundleRunbookStep")


@_attrs_define
class AppbundleRunbookStep:
    """
    Attributes:
        component (str | Unset): Component scopes a health-gate to one component by name; empty gates
            on every component's health.
        kind (str | Unset):
        ref_id (str | Unset):
    """

    component: str | Unset = UNSET
    kind: str | Unset = UNSET
    ref_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component = self.component

        kind = self.kind

        ref_id = self.ref_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if component is not UNSET:
            field_dict["component"] = component
        if kind is not UNSET:
            field_dict["kind"] = kind
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        component = d.pop("component", UNSET)

        kind = d.pop("kind", UNSET)

        ref_id = d.pop("ref_id", UNSET)

        appbundle_runbook_step = cls(
            component=component,
            kind=kind,
            ref_id=ref_id,
        )

        appbundle_runbook_step.additional_properties = d
        return appbundle_runbook_step

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
