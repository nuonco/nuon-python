from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_app_config import AppAppConfig
    from ..models.app_app_input_config import AppAppInputConfig
    from ..models.app_app_links import AppAppLinks
    from ..models.app_app_runner_config import AppAppRunnerConfig
    from ..models.app_app_sandbox_config import AppAppSandboxConfig
    from ..models.app_notifications_config import AppNotificationsConfig


T = TypeVar("T", bound="AppApp")


@_attrs_define
class AppApp:
    """
    Attributes:
        app_configs (list[AppAppConfig] | Unset):
        cloud_platform (str | Unset):
        config_count (int | Unset): Transient field for config count (not persisted to database)
        config_directory (str | Unset):
        config_repo (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        description (str | Unset):
        display_name (str | Unset):
        id (str | Unset):
        input_config (AppAppInputConfig | Unset):
        links (AppAppLinks | Unset):
        name (str | Unset):
        notifications_config (AppNotificationsConfig | Unset):
        org_id (str | Unset):
        runner_config (AppAppRunnerConfig | Unset):
        runner_type (str | Unset):
        sandbox_config (AppAppSandboxConfig | Unset):
        status (str | Unset):
        status_description (str | Unset):
        updated_at (str | Unset):
    """

    app_configs: list[AppAppConfig] | Unset = UNSET
    cloud_platform: str | Unset = UNSET
    config_count: int | Unset = UNSET
    config_directory: str | Unset = UNSET
    config_repo: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    description: str | Unset = UNSET
    display_name: str | Unset = UNSET
    id: str | Unset = UNSET
    input_config: AppAppInputConfig | Unset = UNSET
    links: AppAppLinks | Unset = UNSET
    name: str | Unset = UNSET
    notifications_config: AppNotificationsConfig | Unset = UNSET
    org_id: str | Unset = UNSET
    runner_config: AppAppRunnerConfig | Unset = UNSET
    runner_type: str | Unset = UNSET
    sandbox_config: AppAppSandboxConfig | Unset = UNSET
    status: str | Unset = UNSET
    status_description: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_configs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.app_configs, Unset):
            app_configs = []
            for app_configs_item_data in self.app_configs:
                app_configs_item = app_configs_item_data.to_dict()
                app_configs.append(app_configs_item)

        cloud_platform = self.cloud_platform

        config_count = self.config_count

        config_directory = self.config_directory

        config_repo = self.config_repo

        created_at = self.created_at

        created_by_id = self.created_by_id

        description = self.description

        display_name = self.display_name

        id = self.id

        input_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_config, Unset):
            input_config = self.input_config.to_dict()

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        name = self.name

        notifications_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.notifications_config, Unset):
            notifications_config = self.notifications_config.to_dict()

        org_id = self.org_id

        runner_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.runner_config, Unset):
            runner_config = self.runner_config.to_dict()

        runner_type = self.runner_type

        sandbox_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sandbox_config, Unset):
            sandbox_config = self.sandbox_config.to_dict()

        status = self.status

        status_description = self.status_description

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_configs is not UNSET:
            field_dict["app_configs"] = app_configs
        if cloud_platform is not UNSET:
            field_dict["cloud_platform"] = cloud_platform
        if config_count is not UNSET:
            field_dict["config_count"] = config_count
        if config_directory is not UNSET:
            field_dict["config_directory"] = config_directory
        if config_repo is not UNSET:
            field_dict["config_repo"] = config_repo
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if description is not UNSET:
            field_dict["description"] = description
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if id is not UNSET:
            field_dict["id"] = id
        if input_config is not UNSET:
            field_dict["input_config"] = input_config
        if links is not UNSET:
            field_dict["links"] = links
        if name is not UNSET:
            field_dict["name"] = name
        if notifications_config is not UNSET:
            field_dict["notifications_config"] = notifications_config
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if runner_config is not UNSET:
            field_dict["runner_config"] = runner_config
        if runner_type is not UNSET:
            field_dict["runner_type"] = runner_type
        if sandbox_config is not UNSET:
            field_dict["sandbox_config"] = sandbox_config
        if status is not UNSET:
            field_dict["status"] = status
        if status_description is not UNSET:
            field_dict["status_description"] = status_description
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_app_config import AppAppConfig
        from ..models.app_app_input_config import AppAppInputConfig
        from ..models.app_app_links import AppAppLinks
        from ..models.app_app_runner_config import AppAppRunnerConfig
        from ..models.app_app_sandbox_config import AppAppSandboxConfig
        from ..models.app_notifications_config import AppNotificationsConfig

        d = dict(src_dict)
        _app_configs = d.pop("app_configs", UNSET)
        app_configs: list[AppAppConfig] | Unset = UNSET
        if _app_configs is not UNSET:
            app_configs = []
            for app_configs_item_data in _app_configs:
                app_configs_item = AppAppConfig.from_dict(app_configs_item_data)

                app_configs.append(app_configs_item)

        cloud_platform = d.pop("cloud_platform", UNSET)

        config_count = d.pop("config_count", UNSET)

        config_directory = d.pop("config_directory", UNSET)

        config_repo = d.pop("config_repo", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        description = d.pop("description", UNSET)

        display_name = d.pop("display_name", UNSET)

        id = d.pop("id", UNSET)

        _input_config = d.pop("input_config", UNSET)
        input_config: AppAppInputConfig | Unset
        if isinstance(_input_config, Unset):
            input_config = UNSET
        else:
            input_config = AppAppInputConfig.from_dict(_input_config)

        _links = d.pop("links", UNSET)
        links: AppAppLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = AppAppLinks.from_dict(_links)

        name = d.pop("name", UNSET)

        _notifications_config = d.pop("notifications_config", UNSET)
        notifications_config: AppNotificationsConfig | Unset
        if isinstance(_notifications_config, Unset):
            notifications_config = UNSET
        else:
            notifications_config = AppNotificationsConfig.from_dict(_notifications_config)

        org_id = d.pop("org_id", UNSET)

        _runner_config = d.pop("runner_config", UNSET)
        runner_config: AppAppRunnerConfig | Unset
        if isinstance(_runner_config, Unset):
            runner_config = UNSET
        else:
            runner_config = AppAppRunnerConfig.from_dict(_runner_config)

        runner_type = d.pop("runner_type", UNSET)

        _sandbox_config = d.pop("sandbox_config", UNSET)
        sandbox_config: AppAppSandboxConfig | Unset
        if isinstance(_sandbox_config, Unset):
            sandbox_config = UNSET
        else:
            sandbox_config = AppAppSandboxConfig.from_dict(_sandbox_config)

        status = d.pop("status", UNSET)

        status_description = d.pop("status_description", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_app = cls(
            app_configs=app_configs,
            cloud_platform=cloud_platform,
            config_count=config_count,
            config_directory=config_directory,
            config_repo=config_repo,
            created_at=created_at,
            created_by_id=created_by_id,
            description=description,
            display_name=display_name,
            id=id,
            input_config=input_config,
            links=links,
            name=name,
            notifications_config=notifications_config,
            org_id=org_id,
            runner_config=runner_config,
            runner_type=runner_type,
            sandbox_config=sandbox_config,
            status=status,
            status_description=status_description,
            updated_at=updated_at,
        )

        app_app.additional_properties = d
        return app_app

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
