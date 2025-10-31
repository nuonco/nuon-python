from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_job_component_config_env_vars import AppJobComponentConfigEnvVars


T = TypeVar("T", bound="AppJobComponentConfig")


@_attrs_define
class AppJobComponentConfig:
    """
    Attributes:
        args (list[str] | Unset):
        cmd (list[str] | Unset):
        component_config_connection_id (str | Unset): value
        created_at (str | Unset):
        created_by_id (str | Unset):
        env_vars (AppJobComponentConfigEnvVars | Unset):
        id (str | Unset):
        image_url (str | Unset): Image attributes, copied from a docker_buid or external_image component.
        tag (str | Unset):
        updated_at (str | Unset):
    """

    args: list[str] | Unset = UNSET
    cmd: list[str] | Unset = UNSET
    component_config_connection_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    env_vars: AppJobComponentConfigEnvVars | Unset = UNSET
    id: str | Unset = UNSET
    image_url: str | Unset = UNSET
    tag: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        args: list[str] | Unset = UNSET
        if not isinstance(self.args, Unset):
            args = self.args

        cmd: list[str] | Unset = UNSET
        if not isinstance(self.cmd, Unset):
            cmd = self.cmd

        component_config_connection_id = self.component_config_connection_id

        created_at = self.created_at

        created_by_id = self.created_by_id

        env_vars: dict[str, Any] | Unset = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        id = self.id

        image_url = self.image_url

        tag = self.tag

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if args is not UNSET:
            field_dict["args"] = args
        if cmd is not UNSET:
            field_dict["cmd"] = cmd
        if component_config_connection_id is not UNSET:
            field_dict["component_config_connection_id"] = component_config_connection_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if id is not UNSET:
            field_dict["id"] = id
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if tag is not UNSET:
            field_dict["tag"] = tag
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_job_component_config_env_vars import AppJobComponentConfigEnvVars

        d = dict(src_dict)
        args = cast(list[str], d.pop("args", UNSET))

        cmd = cast(list[str], d.pop("cmd", UNSET))

        component_config_connection_id = d.pop("component_config_connection_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        _env_vars = d.pop("env_vars", UNSET)
        env_vars: AppJobComponentConfigEnvVars | Unset
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = AppJobComponentConfigEnvVars.from_dict(_env_vars)

        id = d.pop("id", UNSET)

        image_url = d.pop("image_url", UNSET)

        tag = d.pop("tag", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_job_component_config = cls(
            args=args,
            cmd=cmd,
            component_config_connection_id=component_config_connection_id,
            created_at=created_at,
            created_by_id=created_by_id,
            env_vars=env_vars,
            id=id,
            image_url=image_url,
            tag=tag,
            updated_at=updated_at,
        )

        app_job_component_config.additional_properties = d
        return app_job_component_config

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
