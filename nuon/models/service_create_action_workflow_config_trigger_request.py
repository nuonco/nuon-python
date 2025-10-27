from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_action_workflow_trigger_type import AppActionWorkflowTriggerType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceCreateActionWorkflowConfigTriggerRequest")


@_attrs_define
class ServiceCreateActionWorkflowConfigTriggerRequest:
    """
    Attributes:
        type_ (AppActionWorkflowTriggerType):
        component_name (Union[Unset, str]):
        cron_schedule (Union[Unset, str]):
        index (Union[Unset, int]):
    """

    type_: AppActionWorkflowTriggerType
    component_name: Union[Unset, str] = UNSET
    cron_schedule: Union[Unset, str] = UNSET
    index: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        component_name = self.component_name

        cron_schedule = self.cron_schedule

        index = self.index

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if component_name is not UNSET:
            field_dict["component_name"] = component_name
        if cron_schedule is not UNSET:
            field_dict["cron_schedule"] = cron_schedule
        if index is not UNSET:
            field_dict["index"] = index

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = AppActionWorkflowTriggerType(d.pop("type"))

        component_name = d.pop("component_name", UNSET)

        cron_schedule = d.pop("cron_schedule", UNSET)

        index = d.pop("index", UNSET)

        service_create_action_workflow_config_trigger_request = cls(
            type_=type_,
            component_name=component_name,
            cron_schedule=cron_schedule,
            index=index,
        )

        service_create_action_workflow_config_trigger_request.additional_properties = d
        return service_create_action_workflow_config_trigger_request

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
