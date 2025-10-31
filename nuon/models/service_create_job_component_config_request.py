from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_create_job_component_config_request_env_vars import (
        ServiceCreateJobComponentConfigRequestEnvVars,
    )


T = TypeVar("T", bound="ServiceCreateJobComponentConfigRequest")


@_attrs_define
class ServiceCreateJobComponentConfigRequest:
    """
    Attributes:
        image_url (str):
        tag (str):
        app_config_id (str | Unset):
        args (list[str] | Unset):
        checksum (str | Unset):
        cmd (list[str] | Unset):
        env_vars (ServiceCreateJobComponentConfigRequestEnvVars | Unset):
        references (list[str] | Unset):
    """

    image_url: str
    tag: str
    app_config_id: str | Unset = UNSET
    args: list[str] | Unset = UNSET
    checksum: str | Unset = UNSET
    cmd: list[str] | Unset = UNSET
    env_vars: ServiceCreateJobComponentConfigRequestEnvVars | Unset = UNSET
    references: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image_url = self.image_url

        tag = self.tag

        app_config_id = self.app_config_id

        args: list[str] | Unset = UNSET
        if not isinstance(self.args, Unset):
            args = self.args

        checksum = self.checksum

        cmd: list[str] | Unset = UNSET
        if not isinstance(self.cmd, Unset):
            cmd = self.cmd

        env_vars: dict[str, Any] | Unset = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        references: list[str] | Unset = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "image_url": image_url,
                "tag": tag,
            }
        )
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if args is not UNSET:
            field_dict["args"] = args
        if checksum is not UNSET:
            field_dict["checksum"] = checksum
        if cmd is not UNSET:
            field_dict["cmd"] = cmd
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if references is not UNSET:
            field_dict["references"] = references

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_create_job_component_config_request_env_vars import (
            ServiceCreateJobComponentConfigRequestEnvVars,
        )

        d = dict(src_dict)
        image_url = d.pop("image_url")

        tag = d.pop("tag")

        app_config_id = d.pop("app_config_id", UNSET)

        args = cast(list[str], d.pop("args", UNSET))

        checksum = d.pop("checksum", UNSET)

        cmd = cast(list[str], d.pop("cmd", UNSET))

        _env_vars = d.pop("env_vars", UNSET)
        env_vars: ServiceCreateJobComponentConfigRequestEnvVars | Unset
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = ServiceCreateJobComponentConfigRequestEnvVars.from_dict(_env_vars)

        references = cast(list[str], d.pop("references", UNSET))

        service_create_job_component_config_request = cls(
            image_url=image_url,
            tag=tag,
            app_config_id=app_config_id,
            args=args,
            checksum=checksum,
            cmd=cmd,
            env_vars=env_vars,
            references=references,
        )

        service_create_job_component_config_request.additional_properties = d
        return service_create_job_component_config_request

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
