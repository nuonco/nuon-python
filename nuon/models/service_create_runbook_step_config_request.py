from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
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
        deploy_dependencies (bool | Unset):
        env_vars (ServiceCreateRunbookStepConfigRequestEnvVars | Unset):
        idx (int | Unset):
        inline_contents (str | Unset):
        role (str | Unset):
        timeout (int | Unset):
    """

    name: str
    type_: str
    action_name: str | Unset = UNSET
    command: str | Unset = UNSET
    component_name: str | Unset = UNSET
    deploy_dependencies: bool | Unset = UNSET
    env_vars: ServiceCreateRunbookStepConfigRequestEnvVars | Unset = UNSET
    idx: int | Unset = UNSET
    inline_contents: str | Unset = UNSET
    role: str | Unset = UNSET
    timeout: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        action_name = self.action_name

        command = self.command

        component_name = self.component_name

        deploy_dependencies = self.deploy_dependencies

        env_vars: dict[str, Any] | Unset = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        idx = self.idx

        inline_contents = self.inline_contents

        role = self.role

        timeout = self.timeout

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
        if deploy_dependencies is not UNSET:
            field_dict["deploy_dependencies"] = deploy_dependencies
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if idx is not UNSET:
            field_dict["idx"] = idx
        if inline_contents is not UNSET:
            field_dict["inline_contents"] = inline_contents
        if role is not UNSET:
            field_dict["role"] = role
        if timeout is not UNSET:
            field_dict["timeout"] = timeout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_create_runbook_step_config_request_env_vars import (
            ServiceCreateRunbookStepConfigRequestEnvVars,
        )

        d = dict(src_dict)
        name = d.pop("name")

        type_ = d.pop("type")

        action_name = d.pop("action_name", UNSET)

        command = d.pop("command", UNSET)

        component_name = d.pop("component_name", UNSET)

        deploy_dependencies = d.pop("deploy_dependencies", UNSET)

        _env_vars = d.pop("env_vars", UNSET)
        env_vars: ServiceCreateRunbookStepConfigRequestEnvVars | Unset
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = ServiceCreateRunbookStepConfigRequestEnvVars.from_dict(_env_vars)

        idx = d.pop("idx", UNSET)

        inline_contents = d.pop("inline_contents", UNSET)

        role = d.pop("role", UNSET)

        timeout = d.pop("timeout", UNSET)

        service_create_runbook_step_config_request = cls(
            name=name,
            type_=type_,
            action_name=action_name,
            command=command,
            component_name=component_name,
            deploy_dependencies=deploy_dependencies,
            env_vars=env_vars,
            idx=idx,
            inline_contents=inline_contents,
            role=role,
            timeout=timeout,
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
