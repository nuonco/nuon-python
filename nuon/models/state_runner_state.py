from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StateRunnerState")


@_attrs_define
class StateRunnerState:
    """
    Attributes:
        id (Union[Unset, str]):
        populated (Union[Unset, bool]):
        runner_group_id (Union[Unset, str]):
        status (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    populated: Union[Unset, bool] = UNSET
    runner_group_id: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        populated = self.populated

        runner_group_id = self.runner_group_id

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if populated is not UNSET:
            field_dict["populated"] = populated
        if runner_group_id is not UNSET:
            field_dict["runner_group_id"] = runner_group_id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        populated = d.pop("populated", UNSET)

        runner_group_id = d.pop("runner_group_id", UNSET)

        status = d.pop("status", UNSET)

        state_runner_state = cls(
            id=id,
            populated=populated,
            runner_group_id=runner_group_id,
            status=status,
        )

        state_runner_state.additional_properties = d
        return state_runner_state

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
