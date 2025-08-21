from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.state_inputs_state_inputs import StateInputsStateInputs


T = TypeVar("T", bound="StateInputsState")


@_attrs_define
class StateInputsState:
    """
    Attributes:
        inputs (Union[Unset, StateInputsStateInputs]):
        populated (Union[Unset, bool]):
    """

    inputs: Union[Unset, "StateInputsStateInputs"] = UNSET
    populated: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inputs: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.inputs, Unset):
            inputs = self.inputs.to_dict()

        populated = self.populated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inputs is not UNSET:
            field_dict["inputs"] = inputs
        if populated is not UNSET:
            field_dict["populated"] = populated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.state_inputs_state_inputs import StateInputsStateInputs

        d = dict(src_dict)
        _inputs = d.pop("inputs", UNSET)
        inputs: Union[Unset, StateInputsStateInputs]
        if isinstance(_inputs, Unset):
            inputs = UNSET
        else:
            inputs = StateInputsStateInputs.from_dict(_inputs)

        populated = d.pop("populated", UNSET)

        state_inputs_state = cls(
            inputs=inputs,
            populated=populated,
        )

        state_inputs_state.additional_properties = d
        return state_inputs_state

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
