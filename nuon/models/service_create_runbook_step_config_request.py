from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_trigger_filter import AppTriggerFilter
    from ..models.service_create_runbook_step_config_request_env_vars import (
        ServiceCreateRunbookStepConfigRequestEnvVars,
    )


T = TypeVar("T", bound="ServiceCreateRunbookStepConfigRequest")


@_attrs_define
class ServiceCreateRunbookStepConfigRequest:
    """
    Attributes:
        name (str):
        type_ (str):
        action_name (str | Unset):
        command (str | Unset):
        component_name (str | Unset):
        deploy_dependents (bool | Unset):
        env_vars (ServiceCreateRunbookStepConfigRequestEnvVars | Unset):
        event_types (list[str] | Unset):
        filters (list[AppTriggerFilter] | Unset):
        idx (int | Unset):
        inline_contents (str | Unset):
        plan_only (bool | Unset):
        role (str | Unset):
        skip_component_deploys (bool | Unset):
        tear_down_dependents (bool | Unset):
        timeout (int | Unset):
        trigger (str | Unset):
    """

    name: str
    type_: str
    action_name: str | Unset = UNSET
    command: str | Unset = UNSET
    component_name: str | Unset = UNSET
    deploy_dependents: bool | Unset = UNSET
    env_vars: ServiceCreateRunbookStepConfigRequestEnvVars | Unset = UNSET
    event_types: list[str] | Unset = UNSET
    filters: list[AppTriggerFilter] | Unset = UNSET
    idx: int | Unset = UNSET
    inline_contents: str | Unset = UNSET
    plan_only: bool | Unset = UNSET
    role: str | Unset = UNSET
    skip_component_deploys: bool | Unset = UNSET
    tear_down_dependents: bool | Unset = UNSET
    timeout: int | Unset = UNSET
    trigger: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        action_name = self.action_name

        command = self.command

        component_name = self.component_name

        deploy_dependents = self.deploy_dependents

        env_vars: dict[str, Any] | Unset = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        event_types: list[str] | Unset = UNSET
        if not isinstance(self.event_types, Unset):
            event_types = self.event_types

        filters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = []
            for filters_item_data in self.filters:
                filters_item = filters_item_data.to_dict()
                filters.append(filters_item)

        idx = self.idx

        inline_contents = self.inline_contents

        plan_only = self.plan_only

        role = self.role

        skip_component_deploys = self.skip_component_deploys

        tear_down_dependents = self.tear_down_dependents

        timeout = self.timeout

        trigger = self.trigger

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
            }
        )
        if action_name is not UNSET:
            field_dict["action_name"] = action_name
        if command is not UNSET:
            field_dict["command"] = command
        if component_name is not UNSET:
            field_dict["component_name"] = component_name
        if deploy_dependents is not UNSET:
            field_dict["deploy_dependents"] = deploy_dependents
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if event_types is not UNSET:
            field_dict["event_types"] = event_types
        if filters is not UNSET:
            field_dict["filters"] = filters
        if idx is not UNSET:
            field_dict["idx"] = idx
        if inline_contents is not UNSET:
            field_dict["inline_contents"] = inline_contents
        if plan_only is not UNSET:
            field_dict["plan_only"] = plan_only
        if role is not UNSET:
            field_dict["role"] = role
        if skip_component_deploys is not UNSET:
            field_dict["skip_component_deploys"] = skip_component_deploys
        if tear_down_dependents is not UNSET:
            field_dict["tear_down_dependents"] = tear_down_dependents
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if trigger is not UNSET:
            field_dict["trigger"] = trigger

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_trigger_filter import AppTriggerFilter
        from ..models.service_create_runbook_step_config_request_env_vars import (
            ServiceCreateRunbookStepConfigRequestEnvVars,
        )

        d = dict(src_dict)
        name = d.pop("name")

        type_ = d.pop("type")

        action_name = d.pop("action_name", UNSET)

        command = d.pop("command", UNSET)

        component_name = d.pop("component_name", UNSET)

        deploy_dependents = d.pop("deploy_dependents", UNSET)

        _env_vars = d.pop("env_vars", UNSET)
        env_vars: ServiceCreateRunbookStepConfigRequestEnvVars | Unset
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = ServiceCreateRunbookStepConfigRequestEnvVars.from_dict(_env_vars)

        event_types = cast(list[str], d.pop("event_types", UNSET))

        _filters = d.pop("filters", UNSET)
        filters: list[AppTriggerFilter] | Unset = UNSET
        if _filters is not UNSET:
            filters = []
            for filters_item_data in _filters:
                filters_item = AppTriggerFilter.from_dict(filters_item_data)

                filters.append(filters_item)

        idx = d.pop("idx", UNSET)

        inline_contents = d.pop("inline_contents", UNSET)

        plan_only = d.pop("plan_only", UNSET)

        role = d.pop("role", UNSET)

        skip_component_deploys = d.pop("skip_component_deploys", UNSET)

        tear_down_dependents = d.pop("tear_down_dependents", UNSET)

        timeout = d.pop("timeout", UNSET)

        trigger = d.pop("trigger", UNSET)

        service_create_runbook_step_config_request = cls(
            name=name,
            type_=type_,
            action_name=action_name,
            command=command,
            component_name=component_name,
            deploy_dependents=deploy_dependents,
            env_vars=env_vars,
            event_types=event_types,
            filters=filters,
            idx=idx,
            inline_contents=inline_contents,
            plan_only=plan_only,
            role=role,
            skip_component_deploys=skip_component_deploys,
            tear_down_dependents=tear_down_dependents,
            timeout=timeout,
            trigger=trigger,
        )

        service_create_runbook_step_config_request.additional_properties = d
        return service_create_runbook_step_config_request

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
