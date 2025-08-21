from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
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
        cloud_platform (Union[Unset, str]):
        config_directory (Union[Unset, str]):
        config_repo (Union[Unset, str]):
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        description (Union[Unset, str]):
        display_name (Union[Unset, str]):
        id (Union[Unset, str]):
        input_config (Union[Unset, AppAppInputConfig]):
        links (Union[Unset, AppAppLinks]):
        name (Union[Unset, str]):
        notifications_config (Union[Unset, AppNotificationsConfig]):
        org_id (Union[Unset, str]):
        runner_config (Union[Unset, AppAppRunnerConfig]):
        runner_type (Union[Unset, str]):
        sandbox_config (Union[Unset, AppAppSandboxConfig]):
        status (Union[Unset, str]):
        status_description (Union[Unset, str]):
        updated_at (Union[Unset, str]):
    """

    cloud_platform: Union[Unset, str] = UNSET
    config_directory: Union[Unset, str] = UNSET
    config_repo: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    input_config: Union[Unset, "AppAppInputConfig"] = UNSET
    links: Union[Unset, "AppAppLinks"] = UNSET
    name: Union[Unset, str] = UNSET
    notifications_config: Union[Unset, "AppNotificationsConfig"] = UNSET
    org_id: Union[Unset, str] = UNSET
    runner_config: Union[Unset, "AppAppRunnerConfig"] = UNSET
    runner_type: Union[Unset, str] = UNSET
    sandbox_config: Union[Unset, "AppAppSandboxConfig"] = UNSET
    status: Union[Unset, str] = UNSET
    status_description: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cloud_platform = self.cloud_platform

        config_directory = self.config_directory

        config_repo = self.config_repo

        created_at = self.created_at

        created_by_id = self.created_by_id

        description = self.description

        display_name = self.display_name

        id = self.id

        input_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.input_config, Unset):
            input_config = self.input_config.to_dict()

        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        name = self.name

        notifications_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.notifications_config, Unset):
            notifications_config = self.notifications_config.to_dict()

        org_id = self.org_id

        runner_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.runner_config, Unset):
            runner_config = self.runner_config.to_dict()

        runner_type = self.runner_type

        sandbox_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sandbox_config, Unset):
            sandbox_config = self.sandbox_config.to_dict()

        status = self.status

        status_description = self.status_description

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cloud_platform is not UNSET:
            field_dict["cloud_platform"] = cloud_platform
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
        from ..models.app_app_input_config import AppAppInputConfig
        from ..models.app_app_links import AppAppLinks
        from ..models.app_app_runner_config import AppAppRunnerConfig
        from ..models.app_app_sandbox_config import AppAppSandboxConfig
        from ..models.app_notifications_config import AppNotificationsConfig

        d = dict(src_dict)
        cloud_platform = d.pop("cloud_platform", UNSET)

        config_directory = d.pop("config_directory", UNSET)

        config_repo = d.pop("config_repo", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        description = d.pop("description", UNSET)

        display_name = d.pop("display_name", UNSET)

        id = d.pop("id", UNSET)

        _input_config = d.pop("input_config", UNSET)
        input_config: Union[Unset, AppAppInputConfig]
        if isinstance(_input_config, Unset):
            input_config = UNSET
        else:
            input_config = AppAppInputConfig.from_dict(_input_config)

        _links = d.pop("links", UNSET)
        links: Union[Unset, AppAppLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = AppAppLinks.from_dict(_links)

        name = d.pop("name", UNSET)

        _notifications_config = d.pop("notifications_config", UNSET)
        notifications_config: Union[Unset, AppNotificationsConfig]
        if isinstance(_notifications_config, Unset):
            notifications_config = UNSET
        else:
            notifications_config = AppNotificationsConfig.from_dict(_notifications_config)

        org_id = d.pop("org_id", UNSET)

        _runner_config = d.pop("runner_config", UNSET)
        runner_config: Union[Unset, AppAppRunnerConfig]
        if isinstance(_runner_config, Unset):
            runner_config = UNSET
        else:
            runner_config = AppAppRunnerConfig.from_dict(_runner_config)

        runner_type = d.pop("runner_type", UNSET)

        _sandbox_config = d.pop("sandbox_config", UNSET)
        sandbox_config: Union[Unset, AppAppSandboxConfig]
        if isinstance(_sandbox_config, Unset):
            sandbox_config = UNSET
        else:
            sandbox_config = AppAppSandboxConfig.from_dict(_sandbox_config)

        status = d.pop("status", UNSET)

        status_description = d.pop("status_description", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_app = cls(
            cloud_platform=cloud_platform,
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
