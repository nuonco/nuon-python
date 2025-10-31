from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.state_sandbox_state_outputs import StateSandboxStateOutputs


T = TypeVar("T", bound="StateSandboxState")


@_attrs_define
class StateSandboxState:
    """
    Attributes:
        outputs (StateSandboxStateOutputs | Unset):
        populated (bool | Unset):
        recent_runs (list[StateSandboxState] | Unset):
        status (str | Unset):
        type_ (str | Unset):
        version (str | Unset):
    """

    outputs: StateSandboxStateOutputs | Unset = UNSET
    populated: bool | Unset = UNSET
    recent_runs: list[StateSandboxState] | Unset = UNSET
    status: str | Unset = UNSET
    type_: str | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        outputs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.outputs, Unset):
            outputs = self.outputs.to_dict()

        populated = self.populated

        recent_runs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.recent_runs, Unset):
            recent_runs = []
            for recent_runs_item_data in self.recent_runs:
                recent_runs_item = recent_runs_item_data.to_dict()
                recent_runs.append(recent_runs_item)

        status = self.status

        type_ = self.type_

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if outputs is not UNSET:
            field_dict["outputs"] = outputs
        if populated is not UNSET:
            field_dict["populated"] = populated
        if recent_runs is not UNSET:
            field_dict["recent_runs"] = recent_runs
        if status is not UNSET:
            field_dict["status"] = status
        if type_ is not UNSET:
            field_dict["type"] = type_
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.state_sandbox_state_outputs import StateSandboxStateOutputs

        d = dict(src_dict)
        _outputs = d.pop("outputs", UNSET)
        outputs: StateSandboxStateOutputs | Unset
        if isinstance(_outputs, Unset):
            outputs = UNSET
        else:
            outputs = StateSandboxStateOutputs.from_dict(_outputs)

        populated = d.pop("populated", UNSET)

        recent_runs = []
        _recent_runs = d.pop("recent_runs", UNSET)
        for recent_runs_item_data in _recent_runs or []:
            recent_runs_item = StateSandboxState.from_dict(recent_runs_item_data)

            recent_runs.append(recent_runs_item)

        status = d.pop("status", UNSET)

        type_ = d.pop("type", UNSET)

        version = d.pop("version", UNSET)

        state_sandbox_state = cls(
            outputs=outputs,
            populated=populated,
            recent_runs=recent_runs,
            status=status,
            type_=type_,
            version=version,
        )

        state_sandbox_state.additional_properties = d
        return state_sandbox_state

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
