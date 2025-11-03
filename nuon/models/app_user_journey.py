from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_user_journey_step import AppUserJourneyStep


T = TypeVar("T", bound="AppUserJourney")


@_attrs_define
class AppUserJourney:
    """
    Attributes:
        name (str | Unset):
        steps (list[AppUserJourneyStep] | Unset):
        title (str | Unset):
    """

    name: str | Unset = UNSET
    steps: list[AppUserJourneyStep] | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        steps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item = steps_item_data.to_dict()
                steps.append(steps_item)

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if steps is not UNSET:
            field_dict["steps"] = steps
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_user_journey_step import AppUserJourneyStep

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _steps = d.pop("steps", UNSET)
        steps: list[AppUserJourneyStep] | Unset = UNSET
        if _steps is not UNSET:
            steps = []
            for steps_item_data in _steps:
                steps_item = AppUserJourneyStep.from_dict(steps_item_data)

                steps.append(steps_item)

        title = d.pop("title", UNSET)

        app_user_journey = cls(
            name=name,
            steps=steps,
            title=title,
        )

        app_user_journey.additional_properties = d
        return app_user_journey

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
