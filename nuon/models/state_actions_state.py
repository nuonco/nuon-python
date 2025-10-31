from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.state_actions_state_workflows import StateActionsStateWorkflows


T = TypeVar("T", bound="StateActionsState")


@_attrs_define
class StateActionsState:
    """
    Attributes:
        populated (bool | Unset):
        workflows (StateActionsStateWorkflows | Unset):
    """

    populated: bool | Unset = UNSET
    workflows: StateActionsStateWorkflows | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        populated = self.populated

        workflows: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workflows, Unset):
            workflows = self.workflows.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if populated is not UNSET:
            field_dict["populated"] = populated
        if workflows is not UNSET:
            field_dict["workflows"] = workflows

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.state_actions_state_workflows import StateActionsStateWorkflows

        d = dict(src_dict)
        populated = d.pop("populated", UNSET)

        _workflows = d.pop("workflows", UNSET)
        workflows: StateActionsStateWorkflows | Unset
        if isinstance(_workflows, Unset):
            workflows = UNSET
        else:
            workflows = StateActionsStateWorkflows.from_dict(_workflows)

        state_actions_state = cls(
            populated=populated,
            workflows=workflows,
        )

        state_actions_state.additional_properties = d
        return state_actions_state

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
