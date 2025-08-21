from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_create_action_workflow_config_step_request import ServiceCreateActionWorkflowConfigStepRequest
    from ..models.service_create_action_workflow_config_trigger_request import (
        ServiceCreateActionWorkflowConfigTriggerRequest,
    )


T = TypeVar("T", bound="ServiceCreateActionWorkflowConfigRequest")


@_attrs_define
class ServiceCreateActionWorkflowConfigRequest:
    """
    Attributes:
        app_config_id (str):
        steps (list['ServiceCreateActionWorkflowConfigStepRequest']):
        triggers (list['ServiceCreateActionWorkflowConfigTriggerRequest']):
        dependencies (Union[Unset, list[str]]):
        references (Union[Unset, list[str]]):
        timeout (Union[Unset, int]):
    """

    app_config_id: str
    steps: list["ServiceCreateActionWorkflowConfigStepRequest"]
    triggers: list["ServiceCreateActionWorkflowConfigTriggerRequest"]
    dependencies: Union[Unset, list[str]] = UNSET
    references: Union[Unset, list[str]] = UNSET
    timeout: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config_id = self.app_config_id

        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        triggers = []
        for triggers_item_data in self.triggers:
            triggers_item = triggers_item_data.to_dict()
            triggers.append(triggers_item)

        dependencies: Union[Unset, list[str]] = UNSET
        if not isinstance(self.dependencies, Unset):
            dependencies = self.dependencies

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        timeout = self.timeout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app_config_id": app_config_id,
                "steps": steps,
                "triggers": triggers,
            }
        )
        if dependencies is not UNSET:
            field_dict["dependencies"] = dependencies
        if references is not UNSET:
            field_dict["references"] = references
        if timeout is not UNSET:
            field_dict["timeout"] = timeout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_create_action_workflow_config_step_request import (
            ServiceCreateActionWorkflowConfigStepRequest,
        )
        from ..models.service_create_action_workflow_config_trigger_request import (
            ServiceCreateActionWorkflowConfigTriggerRequest,
        )

        d = dict(src_dict)
        app_config_id = d.pop("app_config_id")

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = ServiceCreateActionWorkflowConfigStepRequest.from_dict(steps_item_data)

            steps.append(steps_item)

        triggers = []
        _triggers = d.pop("triggers")
        for triggers_item_data in _triggers:
            triggers_item = ServiceCreateActionWorkflowConfigTriggerRequest.from_dict(triggers_item_data)

            triggers.append(triggers_item)

        dependencies = cast(list[str], d.pop("dependencies", UNSET))

        references = cast(list[str], d.pop("references", UNSET))

        timeout = d.pop("timeout", UNSET)

        service_create_action_workflow_config_request = cls(
            app_config_id=app_config_id,
            steps=steps,
            triggers=triggers,
            dependencies=dependencies,
            references=references,
            timeout=timeout,
        )

        service_create_action_workflow_config_request.additional_properties = d
        return service_create_action_workflow_config_request

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
