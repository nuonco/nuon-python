from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_notifications_config import AppNotificationsConfig
    from ..models.app_org_links import AppOrgLinks
    from ..models.app_runner_group import AppRunnerGroup
    from ..models.app_vcs_connection import AppVCSConnection
    from ..models.types_string_bool_map import TypesStringBoolMap


T = TypeVar("T", bound="AppOrg")


@_attrs_define
class AppOrg:
    """
    Attributes:
        created_at (str | Unset):
        created_by_id (str | Unset):
        features (TypesStringBoolMap | Unset):
        id (str | Unset):
        links (AppOrgLinks | Unset):
        logo_url (str | Unset):
        name (str | Unset):
        notifications_config (AppNotificationsConfig | Unset):
        runner_group (AppRunnerGroup | Unset):
        sandbox_mode (bool | Unset):
        status (str | Unset):
        status_description (str | Unset):
        updated_at (str | Unset):
        vcs_connections (list[AppVCSConnection] | Unset):
    """

    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    features: TypesStringBoolMap | Unset = UNSET
    id: str | Unset = UNSET
    links: AppOrgLinks | Unset = UNSET
    logo_url: str | Unset = UNSET
    name: str | Unset = UNSET
    notifications_config: AppNotificationsConfig | Unset = UNSET
    runner_group: AppRunnerGroup | Unset = UNSET
    sandbox_mode: bool | Unset = UNSET
    status: str | Unset = UNSET
    status_description: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    vcs_connections: list[AppVCSConnection] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        features: dict[str, Any] | Unset = UNSET
        if not isinstance(self.features, Unset):
            features = self.features.to_dict()

        id = self.id

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        logo_url = self.logo_url

        name = self.name

        notifications_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.notifications_config, Unset):
            notifications_config = self.notifications_config.to_dict()

        runner_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.runner_group, Unset):
            runner_group = self.runner_group.to_dict()

        sandbox_mode = self.sandbox_mode

        status = self.status

        status_description = self.status_description

        updated_at = self.updated_at

        vcs_connections: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.vcs_connections, Unset):
            vcs_connections = []
            for vcs_connections_item_data in self.vcs_connections:
                vcs_connections_item = vcs_connections_item_data.to_dict()
                vcs_connections.append(vcs_connections_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if features is not UNSET:
            field_dict["features"] = features
        if id is not UNSET:
            field_dict["id"] = id
        if links is not UNSET:
            field_dict["links"] = links
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if name is not UNSET:
            field_dict["name"] = name
        if notifications_config is not UNSET:
            field_dict["notifications_config"] = notifications_config
        if runner_group is not UNSET:
            field_dict["runner_group"] = runner_group
        if sandbox_mode is not UNSET:
            field_dict["sandbox_mode"] = sandbox_mode
        if status is not UNSET:
            field_dict["status"] = status
        if status_description is not UNSET:
            field_dict["status_description"] = status_description
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if vcs_connections is not UNSET:
            field_dict["vcs_connections"] = vcs_connections

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_notifications_config import AppNotificationsConfig
        from ..models.app_org_links import AppOrgLinks
        from ..models.app_runner_group import AppRunnerGroup
        from ..models.app_vcs_connection import AppVCSConnection
        from ..models.types_string_bool_map import TypesStringBoolMap

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        _features = d.pop("features", UNSET)
        features: TypesStringBoolMap | Unset
        if isinstance(_features, Unset):
            features = UNSET
        else:
            features = TypesStringBoolMap.from_dict(_features)

        id = d.pop("id", UNSET)

        _links = d.pop("links", UNSET)
        links: AppOrgLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = AppOrgLinks.from_dict(_links)

        logo_url = d.pop("logo_url", UNSET)

        name = d.pop("name", UNSET)

        _notifications_config = d.pop("notifications_config", UNSET)
        notifications_config: AppNotificationsConfig | Unset
        if isinstance(_notifications_config, Unset):
            notifications_config = UNSET
        else:
            notifications_config = AppNotificationsConfig.from_dict(_notifications_config)

        _runner_group = d.pop("runner_group", UNSET)
        runner_group: AppRunnerGroup | Unset
        if isinstance(_runner_group, Unset):
            runner_group = UNSET
        else:
            runner_group = AppRunnerGroup.from_dict(_runner_group)

        sandbox_mode = d.pop("sandbox_mode", UNSET)

        status = d.pop("status", UNSET)

        status_description = d.pop("status_description", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _vcs_connections = d.pop("vcs_connections", UNSET)
        vcs_connections: list[AppVCSConnection] | Unset = UNSET
        if _vcs_connections is not UNSET:
            vcs_connections = []
            for vcs_connections_item_data in _vcs_connections:
                vcs_connections_item = AppVCSConnection.from_dict(vcs_connections_item_data)

                vcs_connections.append(vcs_connections_item)

        app_org = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            features=features,
            id=id,
            links=links,
            logo_url=logo_url,
            name=name,
            notifications_config=notifications_config,
            runner_group=runner_group,
            sandbox_mode=sandbox_mode,
            status=status,
            status_description=status_description,
            updated_at=updated_at,
            vcs_connections=vcs_connections,
        )

        app_org.additional_properties = d
        return app_org

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
