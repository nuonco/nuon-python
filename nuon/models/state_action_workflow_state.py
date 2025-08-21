from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.state_action_workflow_state_outputs import StateActionWorkflowStateOutputs


T = TypeVar("T", bound="StateActionWorkflowState")


@_attrs_define
class StateActionWorkflowState:
    """
    Attributes:
        id (Union[Unset, str]):
        outputs (Union[Unset, StateActionWorkflowStateOutputs]):
        populated (Union[Unset, bool]):
        status (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    outputs: Union[Unset, "StateActionWorkflowStateOutputs"] = UNSET
    populated: Union[Unset, bool] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        outputs: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.outputs, Unset):
            outputs = self.outputs.to_dict()

        populated = self.populated

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if outputs is not UNSET:
            field_dict["outputs"] = outputs
        if populated is not UNSET:
            field_dict["populated"] = populated
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.state_action_workflow_state_outputs import StateActionWorkflowStateOutputs

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _outputs = d.pop("outputs", UNSET)
        outputs: Union[Unset, StateActionWorkflowStateOutputs]
        if isinstance(_outputs, Unset):
            outputs = UNSET
        else:
            outputs = StateActionWorkflowStateOutputs.from_dict(_outputs)

        populated = d.pop("populated", UNSET)

        status = d.pop("status", UNSET)

        state_action_workflow_state = cls(
            id=id,
            outputs=outputs,
            populated=populated,
            status=status,
        )

        state_action_workflow_state.additional_properties = d
        return state_action_workflow_state

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
