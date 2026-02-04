from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.state_action_workflow_state import StateActionWorkflowState


T = TypeVar("T", bound="StateActionsStateWorkflows")


@_attrs_define
class StateActionsStateWorkflows:
    """ """

    additional_properties: dict[str, StateActionWorkflowState] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.state_action_workflow_state import StateActionWorkflowState

        d = dict(src_dict)
        state_actions_state_workflows = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = StateActionWorkflowState.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        state_actions_state_workflows.additional_properties = additional_properties
        return state_actions_state_workflows

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> StateActionWorkflowState:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: StateActionWorkflowState) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
