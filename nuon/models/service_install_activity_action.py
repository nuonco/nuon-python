from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceInstallActivityAction")


@_attrs_define
class ServiceInstallActivityAction:
    """
    Attributes:
        action_workflow_id (str | Unset):
        name (str | Unset):
        run_id (str | Unset):
        trigger_type (str | Unset):
    """

    action_workflow_id: str | Unset = UNSET
    name: str | Unset = UNSET
    run_id: str | Unset = UNSET
    trigger_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_workflow_id = self.action_workflow_id

        name = self.name

        run_id = self.run_id

        trigger_type = self.trigger_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action_workflow_id is not UNSET:
            field_dict["action_workflow_id"] = action_workflow_id
        if name is not UNSET:
            field_dict["name"] = name
        if run_id is not UNSET:
            field_dict["run_id"] = run_id
        if trigger_type is not UNSET:
            field_dict["trigger_type"] = trigger_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action_workflow_id = d.pop("action_workflow_id", UNSET)

        name = d.pop("name", UNSET)

        run_id = d.pop("run_id", UNSET)

        trigger_type = d.pop("trigger_type", UNSET)

        service_install_activity_action = cls(
            action_workflow_id=action_workflow_id,
            name=name,
            run_id=run_id,
            trigger_type=trigger_type,
        )

        service_install_activity_action.additional_properties = d
        return service_install_activity_action

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
