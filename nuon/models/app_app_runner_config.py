from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_app_runner_type import AppAppRunnerType
from ..models.app_cloud_platform import AppCloudPlatform
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_app_runner_config_env_vars import AppAppRunnerConfigEnvVars


T = TypeVar("T", bound="AppAppRunnerConfig")


@_attrs_define
class AppAppRunnerConfig:
    """
    Attributes:
        app_config_id (str | Unset):
        app_id (str | Unset):
        app_runner_type (AppAppRunnerType | Unset):
        cloud_platform (AppCloudPlatform | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        env_vars (AppAppRunnerConfigEnvVars | Unset):
        helm_driver (str | Unset):
        id (str | Unset):
        init_script (str | Unset): takes a URL to a bash script ⤵  which will be `curl | bash`-ed on the VM. usually via
            user-data or equivalent.
        org_id (str | Unset):
        updated_at (str | Unset):
    """

    app_config_id: str | Unset = UNSET
    app_id: str | Unset = UNSET
    app_runner_type: AppAppRunnerType | Unset = UNSET
    cloud_platform: AppCloudPlatform | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    env_vars: AppAppRunnerConfigEnvVars | Unset = UNSET
    helm_driver: str | Unset = UNSET
    id: str | Unset = UNSET
    init_script: str | Unset = UNSET
    org_id: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config_id = self.app_config_id

        app_id = self.app_id

        app_runner_type: str | Unset = UNSET
        if not isinstance(self.app_runner_type, Unset):
            app_runner_type = self.app_runner_type.value

        cloud_platform: str | Unset = UNSET
        if not isinstance(self.cloud_platform, Unset):
            cloud_platform = self.cloud_platform.value

        created_at = self.created_at

        created_by_id = self.created_by_id

        env_vars: dict[str, Any] | Unset = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        helm_driver = self.helm_driver

        id = self.id

        init_script = self.init_script

        org_id = self.org_id

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if app_runner_type is not UNSET:
            field_dict["app_runner_type"] = app_runner_type
        if cloud_platform is not UNSET:
            field_dict["cloud_platform"] = cloud_platform
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if helm_driver is not UNSET:
            field_dict["helm_driver"] = helm_driver
        if id is not UNSET:
            field_dict["id"] = id
        if init_script is not UNSET:
            field_dict["init_script"] = init_script
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_app_runner_config_env_vars import AppAppRunnerConfigEnvVars

        d = dict(src_dict)
        app_config_id = d.pop("app_config_id", UNSET)

        app_id = d.pop("app_id", UNSET)

        _app_runner_type = d.pop("app_runner_type", UNSET)
        app_runner_type: AppAppRunnerType | Unset
        if isinstance(_app_runner_type, Unset):
            app_runner_type = UNSET
        else:
            app_runner_type = AppAppRunnerType(_app_runner_type)

        _cloud_platform = d.pop("cloud_platform", UNSET)
        cloud_platform: AppCloudPlatform | Unset
        if isinstance(_cloud_platform, Unset):
            cloud_platform = UNSET
        else:
            cloud_platform = AppCloudPlatform(_cloud_platform)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        _env_vars = d.pop("env_vars", UNSET)
        env_vars: AppAppRunnerConfigEnvVars | Unset
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = AppAppRunnerConfigEnvVars.from_dict(_env_vars)

        helm_driver = d.pop("helm_driver", UNSET)

        id = d.pop("id", UNSET)

        init_script = d.pop("init_script", UNSET)

        org_id = d.pop("org_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_app_runner_config = cls(
            app_config_id=app_config_id,
            app_id=app_id,
            app_runner_type=app_runner_type,
            cloud_platform=cloud_platform,
            created_at=created_at,
            created_by_id=created_by_id,
            env_vars=env_vars,
            helm_driver=helm_driver,
            id=id,
            init_script=init_script,
            org_id=org_id,
            updated_at=updated_at,
        )

        app_app_runner_config.additional_properties = d
        return app_app_runner_config

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
