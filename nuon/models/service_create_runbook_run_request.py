from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_create_runbook_run_request_inputs import ServiceCreateRunbookRunRequestInputs
    from ..models.service_create_runbook_run_step_selection import ServiceCreateRunbookRunStepSelection


T = TypeVar("T", bound="ServiceCreateRunbookRunRequest")


@_attrs_define
class ServiceCreateRunbookRunRequest:
    """
    Attributes:
        inputs (ServiceCreateRunbookRunRequestInputs | Unset):
        steps (list[ServiceCreateRunbookRunStepSelection] | Unset):
    """

    inputs: ServiceCreateRunbookRunRequestInputs | Unset = UNSET
    steps: list[ServiceCreateRunbookRunStepSelection] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inputs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inputs, Unset):
            inputs = self.inputs.to_dict()

        steps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item = steps_item_data.to_dict()
                steps.append(steps_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inputs is not UNSET:
            field_dict["inputs"] = inputs
        if steps is not UNSET:
            field_dict["steps"] = steps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_create_runbook_run_request_inputs import ServiceCreateRunbookRunRequestInputs
        from ..models.service_create_runbook_run_step_selection import ServiceCreateRunbookRunStepSelection

        d = dict(src_dict)
        _inputs = d.pop("inputs", UNSET)
        inputs: ServiceCreateRunbookRunRequestInputs | Unset
        if isinstance(_inputs, Unset):
            inputs = UNSET
        else:
            inputs = ServiceCreateRunbookRunRequestInputs.from_dict(_inputs)

        _steps = d.pop("steps", UNSET)
        steps: list[ServiceCreateRunbookRunStepSelection] | Unset = UNSET
        if _steps is not UNSET:
            steps = []
            for steps_item_data in _steps:
                steps_item = ServiceCreateRunbookRunStepSelection.from_dict(steps_item_data)

                steps.append(steps_item)

        service_create_runbook_run_request = cls(
            inputs=inputs,
            steps=steps,
        )

        service_create_runbook_run_request.additional_properties = d
        return service_create_runbook_run_request

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
