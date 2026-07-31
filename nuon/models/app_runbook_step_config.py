from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_runbook_step_config_env_vars import AppRunbookStepConfigEnvVars
    from ..models.app_trigger_filter import AppTriggerFilter


T = TypeVar("T", bound="AppRunbookStepConfig")


@_attrs_define
class AppRunbookStepConfig:
    """
    Attributes:
        action_workflow_id (str | Unset): action reference field
        command (str | Unset): inline action fields
        component_name (str | Unset): deploy / tear-down fields
        created_at (str | Unset):
        created_by_id (str | Unset):
        deploy_dependents (bool | Unset):
        env_vars (AppRunbookStepConfigEnvVars | Unset):
        event_types (list[str] | Unset):
        filters (list[AppTriggerFilter] | Unset):
        id (str | Unset):
        idx (int | Unset):
        inline_contents (str | Unset):
        name (str | Unset):
        plan_only (bool | Unset):
        role (str | Unset):
        runbook_config_id (str | Unset):
        skip_component_deploys (bool | Unset): sandbox lifecycle fields
        tear_down_dependents (bool | Unset):
        timeout (int | Unset):
        trigger_id (str | Unset):
        trigger_name (str | Unset):
        type_ (str | Unset):
        updated_at (str | Unset):
    """

    action_workflow_id: str | Unset = UNSET
    command: str | Unset = UNSET
    component_name: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    deploy_dependents: bool | Unset = UNSET
    env_vars: AppRunbookStepConfigEnvVars | Unset = UNSET
    event_types: list[str] | Unset = UNSET
    filters: list[AppTriggerFilter] | Unset = UNSET
    id: str | Unset = UNSET
    idx: int | Unset = UNSET
    inline_contents: str | Unset = UNSET
    name: str | Unset = UNSET
    plan_only: bool | Unset = UNSET
    role: str | Unset = UNSET
    runbook_config_id: str | Unset = UNSET
    skip_component_deploys: bool | Unset = UNSET
    tear_down_dependents: bool | Unset = UNSET
    timeout: int | Unset = UNSET
    trigger_id: str | Unset = UNSET
    trigger_name: str | Unset = UNSET
    type_: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_workflow_id = self.action_workflow_id

        command = self.command

        component_name = self.component_name

        created_at = self.created_at

        created_by_id = self.created_by_id

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

        id = self.id

        idx = self.idx

        inline_contents = self.inline_contents

        name = self.name

        plan_only = self.plan_only

        role = self.role

        runbook_config_id = self.runbook_config_id

        skip_component_deploys = self.skip_component_deploys

        tear_down_dependents = self.tear_down_dependents

        timeout = self.timeout

        trigger_id = self.trigger_id

        trigger_name = self.trigger_name

        type_ = self.type_

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action_workflow_id is not UNSET:
            field_dict["action_workflow_id"] = action_workflow_id
        if command is not UNSET:
            field_dict["command"] = command
        if component_name is not UNSET:
            field_dict["component_name"] = component_name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if deploy_dependents is not UNSET:
            field_dict["deploy_dependents"] = deploy_dependents
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if event_types is not UNSET:
            field_dict["event_types"] = event_types
        if filters is not UNSET:
            field_dict["filters"] = filters
        if id is not UNSET:
            field_dict["id"] = id
        if idx is not UNSET:
            field_dict["idx"] = idx
        if inline_contents is not UNSET:
            field_dict["inline_contents"] = inline_contents
        if name is not UNSET:
            field_dict["name"] = name
        if plan_only is not UNSET:
            field_dict["plan_only"] = plan_only
        if role is not UNSET:
            field_dict["role"] = role
        if runbook_config_id is not UNSET:
            field_dict["runbook_config_id"] = runbook_config_id
        if skip_component_deploys is not UNSET:
            field_dict["skip_component_deploys"] = skip_component_deploys
        if tear_down_dependents is not UNSET:
            field_dict["tear_down_dependents"] = tear_down_dependents
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if trigger_id is not UNSET:
            field_dict["trigger_id"] = trigger_id
        if trigger_name is not UNSET:
            field_dict["trigger_name"] = trigger_name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_runbook_step_config_env_vars import AppRunbookStepConfigEnvVars
        from ..models.app_trigger_filter import AppTriggerFilter

        d = dict(src_dict)
        action_workflow_id = d.pop("action_workflow_id", UNSET)

        command = d.pop("command", UNSET)

        component_name = d.pop("component_name", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        deploy_dependents = d.pop("deploy_dependents", UNSET)

        _env_vars = d.pop("env_vars", UNSET)
        env_vars: AppRunbookStepConfigEnvVars | Unset
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = AppRunbookStepConfigEnvVars.from_dict(_env_vars)

        event_types = cast(list[str], d.pop("event_types", UNSET))

        _filters = d.pop("filters", UNSET)
        filters: list[AppTriggerFilter] | Unset = UNSET
        if _filters is not UNSET:
            filters = []
            for filters_item_data in _filters:
                filters_item = AppTriggerFilter.from_dict(filters_item_data)

                filters.append(filters_item)

        id = d.pop("id", UNSET)

        idx = d.pop("idx", UNSET)

        inline_contents = d.pop("inline_contents", UNSET)

        name = d.pop("name", UNSET)

        plan_only = d.pop("plan_only", UNSET)

        role = d.pop("role", UNSET)

        runbook_config_id = d.pop("runbook_config_id", UNSET)

        skip_component_deploys = d.pop("skip_component_deploys", UNSET)

        tear_down_dependents = d.pop("tear_down_dependents", UNSET)

        timeout = d.pop("timeout", UNSET)

        trigger_id = d.pop("trigger_id", UNSET)

        trigger_name = d.pop("trigger_name", UNSET)

        type_ = d.pop("type", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_runbook_step_config = cls(
            action_workflow_id=action_workflow_id,
            command=command,
            component_name=component_name,
            created_at=created_at,
            created_by_id=created_by_id,
            deploy_dependents=deploy_dependents,
            env_vars=env_vars,
            event_types=event_types,
            filters=filters,
            id=id,
            idx=idx,
            inline_contents=inline_contents,
            name=name,
            plan_only=plan_only,
            role=role,
            runbook_config_id=runbook_config_id,
            skip_component_deploys=skip_component_deploys,
            tear_down_dependents=tear_down_dependents,
            timeout=timeout,
            trigger_id=trigger_id,
            trigger_name=trigger_name,
            type_=type_,
            updated_at=updated_at,
        )

        app_runbook_step_config.additional_properties = d
        return app_runbook_step_config

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
