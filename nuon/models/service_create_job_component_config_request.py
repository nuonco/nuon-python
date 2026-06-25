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
    from ..models.service_create_job_component_config_request_operation_roles import (
        ServiceCreateJobComponentConfigRequestOperationRoles,
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
        auto_approve_on_policies_passing (bool | Unset):
        build_timeout (str | Unset): Duration string for build operations (e.g., "30m", "1h")
        checksum (str | Unset):
        cmd (list[str] | Unset):
        default_enabled (bool | Unset):
        deploy_timeout (str | Unset): Duration string for deploy operations (e.g., "30m", "1h")
        env_vars (ServiceCreateJobComponentConfigRequestEnvVars | Unset):
        max_auto_retries (int | Unset):
        operation_roles (ServiceCreateJobComponentConfigRequestOperationRoles | Unset):
        references (list[str] | Unset):
        skip_noops (bool | Unset):
        toggleable (bool | Unset):
    """

    image_url: str
    tag: str
    app_config_id: str | Unset = UNSET
    args: list[str] | Unset = UNSET
    auto_approve_on_policies_passing: bool | Unset = UNSET
    build_timeout: str | Unset = UNSET
    checksum: str | Unset = UNSET
    cmd: list[str] | Unset = UNSET
    default_enabled: bool | Unset = UNSET
    deploy_timeout: str | Unset = UNSET
    env_vars: ServiceCreateJobComponentConfigRequestEnvVars | Unset = UNSET
    max_auto_retries: int | Unset = UNSET
    operation_roles: ServiceCreateJobComponentConfigRequestOperationRoles | Unset = UNSET
    references: list[str] | Unset = UNSET
    skip_noops: bool | Unset = UNSET
    toggleable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image_url = self.image_url

        tag = self.tag

        app_config_id = self.app_config_id

        args: list[str] | Unset = UNSET
        if not isinstance(self.args, Unset):
            args = self.args

        auto_approve_on_policies_passing = self.auto_approve_on_policies_passing

        build_timeout = self.build_timeout

        checksum = self.checksum

        cmd: list[str] | Unset = UNSET
        if not isinstance(self.cmd, Unset):
            cmd = self.cmd

        default_enabled = self.default_enabled

        deploy_timeout = self.deploy_timeout

        env_vars: dict[str, Any] | Unset = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        max_auto_retries = self.max_auto_retries

        operation_roles: dict[str, Any] | Unset = UNSET
        if not isinstance(self.operation_roles, Unset):
            operation_roles = self.operation_roles.to_dict()

        references: list[str] | Unset = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        skip_noops = self.skip_noops

        toggleable = self.toggleable

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
        if auto_approve_on_policies_passing is not UNSET:
            field_dict["auto_approve_on_policies_passing"] = auto_approve_on_policies_passing
        if build_timeout is not UNSET:
            field_dict["build_timeout"] = build_timeout
        if checksum is not UNSET:
            field_dict["checksum"] = checksum
        if cmd is not UNSET:
            field_dict["cmd"] = cmd
        if default_enabled is not UNSET:
            field_dict["default_enabled"] = default_enabled
        if deploy_timeout is not UNSET:
            field_dict["deploy_timeout"] = deploy_timeout
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if max_auto_retries is not UNSET:
            field_dict["max_auto_retries"] = max_auto_retries
        if operation_roles is not UNSET:
            field_dict["operation_roles"] = operation_roles
        if references is not UNSET:
            field_dict["references"] = references
        if skip_noops is not UNSET:
            field_dict["skip_noops"] = skip_noops
        if toggleable is not UNSET:
            field_dict["toggleable"] = toggleable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_create_job_component_config_request_env_vars import (
            ServiceCreateJobComponentConfigRequestEnvVars,
        )
        from ..models.service_create_job_component_config_request_operation_roles import (
            ServiceCreateJobComponentConfigRequestOperationRoles,
        )

        d = dict(src_dict)
        image_url = d.pop("image_url")

        tag = d.pop("tag")

        app_config_id = d.pop("app_config_id", UNSET)

        args = cast(list[str], d.pop("args", UNSET))

        auto_approve_on_policies_passing = d.pop("auto_approve_on_policies_passing", UNSET)

        build_timeout = d.pop("build_timeout", UNSET)

        checksum = d.pop("checksum", UNSET)

        cmd = cast(list[str], d.pop("cmd", UNSET))

        default_enabled = d.pop("default_enabled", UNSET)

        deploy_timeout = d.pop("deploy_timeout", UNSET)

        _env_vars = d.pop("env_vars", UNSET)
        env_vars: ServiceCreateJobComponentConfigRequestEnvVars | Unset
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = ServiceCreateJobComponentConfigRequestEnvVars.from_dict(_env_vars)

        max_auto_retries = d.pop("max_auto_retries", UNSET)

        _operation_roles = d.pop("operation_roles", UNSET)
        operation_roles: ServiceCreateJobComponentConfigRequestOperationRoles | Unset
        if isinstance(_operation_roles, Unset):
            operation_roles = UNSET
        else:
            operation_roles = ServiceCreateJobComponentConfigRequestOperationRoles.from_dict(_operation_roles)

        references = cast(list[str], d.pop("references", UNSET))

        skip_noops = d.pop("skip_noops", UNSET)

        toggleable = d.pop("toggleable", UNSET)

        service_create_job_component_config_request = cls(
            image_url=image_url,
            tag=tag,
            app_config_id=app_config_id,
            args=args,
            auto_approve_on_policies_passing=auto_approve_on_policies_passing,
            build_timeout=build_timeout,
            checksum=checksum,
            cmd=cmd,
            default_enabled=default_enabled,
            deploy_timeout=deploy_timeout,
            env_vars=env_vars,
            max_auto_retries=max_auto_retries,
            operation_roles=operation_roles,
            references=references,
            skip_noops=skip_noops,
            toggleable=toggleable,
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
