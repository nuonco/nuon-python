from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.service_create_user_journey_step_req import ServiceCreateUserJourneyStepReq


T = TypeVar("T", bound="ServiceCreateUserJourneyRequest")


@_attrs_define
class ServiceCreateUserJourneyRequest:
    """
    Attributes:
        name (str):
        steps (list[ServiceCreateUserJourneyStepReq]):
        title (str):
    """

    name: str
    steps: list[ServiceCreateUserJourneyStepReq]
    title: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "steps": steps,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_create_user_journey_step_req import ServiceCreateUserJourneyStepReq

        d = dict(src_dict)
        name = d.pop("name")

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = ServiceCreateUserJourneyStepReq.from_dict(steps_item_data)

            steps.append(steps_item)

        title = d.pop("title")

        service_create_user_journey_request = cls(
            name=name,
            steps=steps,
            title=title,
        )

        service_create_user_journey_request.additional_properties = d
        return service_create_user_journey_request

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
