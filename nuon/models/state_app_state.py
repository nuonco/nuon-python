from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.state_app_state_variables import StateAppStateVariables


T = TypeVar("T", bound="StateAppState")


@_attrs_define
class StateAppState:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        populated (Union[Unset, bool]):
        status (Union[Unset, str]):
        variables (Union[Unset, StateAppStateVariables]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    populated: Union[Unset, bool] = UNSET
    status: Union[Unset, str] = UNSET
    variables: Union[Unset, "StateAppStateVariables"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        populated = self.populated

        status = self.status

        variables: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.variables, Unset):
            variables = self.variables.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if populated is not UNSET:
            field_dict["populated"] = populated
        if status is not UNSET:
            field_dict["status"] = status
        if variables is not UNSET:
            field_dict["variables"] = variables

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.state_app_state_variables import StateAppStateVariables

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        populated = d.pop("populated", UNSET)

        status = d.pop("status", UNSET)

        _variables = d.pop("variables", UNSET)
        variables: Union[Unset, StateAppStateVariables]
        if isinstance(_variables, Unset):
            variables = UNSET
        else:
            variables = StateAppStateVariables.from_dict(_variables)

        state_app_state = cls(
            id=id,
            name=name,
            populated=populated,
            status=status,
            variables=variables,
        )

        state_app_state.additional_properties = d
        return state_app_state

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
