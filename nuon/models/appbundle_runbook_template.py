from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.appbundle_runbook_step import AppbundleRunbookStep


T = TypeVar("T", bound="AppbundleRunbookTemplate")


@_attrs_define
class AppbundleRunbookTemplate:
    """
    Attributes:
        id (str | Unset):
        name (str | Unset):
        steps (list[AppbundleRunbookStep] | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    steps: list[AppbundleRunbookStep] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        steps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item = steps_item_data.to_dict()
                steps.append(steps_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if steps is not UNSET:
            field_dict["steps"] = steps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.appbundle_runbook_step import AppbundleRunbookStep  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _steps = d.pop("steps", UNSET)
        steps: list[AppbundleRunbookStep] | Unset = UNSET
        if _steps is not UNSET:
            steps = []
            for steps_item_data in _steps:
                steps_item = AppbundleRunbookStep.from_dict(steps_item_data)

                steps.append(steps_item)

        appbundle_runbook_template = cls(
            id=id,
            name=name,
            steps=steps,
        )

        appbundle_runbook_template.additional_properties = d
        return appbundle_runbook_template

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
