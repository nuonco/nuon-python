from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_create_ad_hoc_action_request_env_vars import ServiceCreateAdHocActionRequestEnvVars


T = TypeVar("T", bound="ServiceCreateAdHocActionRequest")


@_attrs_define
class ServiceCreateAdHocActionRequest:
    """
    Attributes:
        command (str | Unset):
        env_vars (ServiceCreateAdHocActionRequestEnvVars | Unset):
        inline_contents (str | Unset):
        name (str | Unset):
        timeout (int | Unset):
    """

    command: str | Unset = UNSET
    env_vars: ServiceCreateAdHocActionRequestEnvVars | Unset = UNSET
    inline_contents: str | Unset = UNSET
    name: str | Unset = UNSET
    timeout: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        command = self.command

        env_vars: dict[str, Any] | Unset = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        inline_contents = self.inline_contents

        name = self.name

        timeout = self.timeout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if command is not UNSET:
            field_dict["command"] = command
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if inline_contents is not UNSET:
            field_dict["inline_contents"] = inline_contents
        if name is not UNSET:
            field_dict["name"] = name
        if timeout is not UNSET:
            field_dict["timeout"] = timeout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_create_ad_hoc_action_request_env_vars import ServiceCreateAdHocActionRequestEnvVars

        d = dict(src_dict)
        command = d.pop("command", UNSET)

        _env_vars = d.pop("env_vars", UNSET)
        env_vars: ServiceCreateAdHocActionRequestEnvVars | Unset
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = ServiceCreateAdHocActionRequestEnvVars.from_dict(_env_vars)

        inline_contents = d.pop("inline_contents", UNSET)

        name = d.pop("name", UNSET)

        timeout = d.pop("timeout", UNSET)

        service_create_ad_hoc_action_request = cls(
            command=command,
            env_vars=env_vars,
            inline_contents=inline_contents,
            name=name,
            timeout=timeout,
        )

        service_create_ad_hoc_action_request.additional_properties = d
        return service_create_ad_hoc_action_request

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
