from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_runbook_step_config_env_vars import AppRunbookStepConfigEnvVars


T = TypeVar("T", bound="AppRunbookStepConfig")


@_attrs_define
class AppRunbookStepConfig:
    """
    Attributes:
        action_workflow_id (str | Unset): action reference field
        command (str | Unset): inline action fields
        component_name (str | Unset): deploy fields
        created_at (str | Unset):
        created_by_id (str | Unset):
        deploy_dependencies (bool | Unset):
        env_vars (AppRunbookStepConfigEnvVars | Unset):
        id (str | Unset):
        idx (int | Unset):
        inline_contents (str | Unset):
        name (str | Unset):
        role (str | Unset):
        runbook_config_id (str | Unset):
        timeout (int | Unset):
        type_ (str | Unset):
        updated_at (str | Unset):
    """

    action_workflow_id: str | Unset = UNSET
    command: str | Unset = UNSET
    component_name: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    deploy_dependencies: bool | Unset = UNSET
    env_vars: AppRunbookStepConfigEnvVars | Unset = UNSET
    id: str | Unset = UNSET
    idx: int | Unset = UNSET
    inline_contents: str | Unset = UNSET
    name: str | Unset = UNSET
    role: str | Unset = UNSET
    runbook_config_id: str | Unset = UNSET
    timeout: int | Unset = UNSET
    type_: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_workflow_id = self.action_workflow_id

        command = self.command

        component_name = self.component_name

        created_at = self.created_at

        created_by_id = self.created_by_id

        deploy_dependencies = self.deploy_dependencies

        env_vars: dict[str, Any] | Unset = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        id = self.id

        idx = self.idx

        inline_contents = self.inline_contents

        name = self.name

        role = self.role

        runbook_config_id = self.runbook_config_id

        timeout = self.timeout

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
        if deploy_dependencies is not UNSET:
            field_dict["deploy_dependencies"] = deploy_dependencies
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if id is not UNSET:
            field_dict["id"] = id
        if idx is not UNSET:
            field_dict["idx"] = idx
        if inline_contents is not UNSET:
            field_dict["inline_contents"] = inline_contents
        if name is not UNSET:
            field_dict["name"] = name
        if role is not UNSET:
            field_dict["role"] = role
        if runbook_config_id is not UNSET:
            field_dict["runbook_config_id"] = runbook_config_id
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_runbook_step_config_env_vars import AppRunbookStepConfigEnvVars

        d = dict(src_dict)
        action_workflow_id = d.pop("action_workflow_id", UNSET)

        command = d.pop("command", UNSET)

        component_name = d.pop("component_name", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        deploy_dependencies = d.pop("deploy_dependencies", UNSET)

        _env_vars = d.pop("env_vars", UNSET)
        env_vars: AppRunbookStepConfigEnvVars | Unset
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = AppRunbookStepConfigEnvVars.from_dict(_env_vars)

        id = d.pop("id", UNSET)

        idx = d.pop("idx", UNSET)

        inline_contents = d.pop("inline_contents", UNSET)

        name = d.pop("name", UNSET)

        role = d.pop("role", UNSET)

        runbook_config_id = d.pop("runbook_config_id", UNSET)

        timeout = d.pop("timeout", UNSET)

        type_ = d.pop("type", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_runbook_step_config = cls(
            action_workflow_id=action_workflow_id,
            command=command,
            component_name=component_name,
            created_at=created_at,
            created_by_id=created_by_id,
            deploy_dependencies=deploy_dependencies,
            env_vars=env_vars,
            id=id,
            idx=idx,
            inline_contents=inline_contents,
            name=name,
            role=role,
            runbook_config_id=runbook_config_id,
            timeout=timeout,
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
