from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

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
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        features (Union[Unset, TypesStringBoolMap]):
        id (Union[Unset, str]):
        links (Union[Unset, AppOrgLinks]):
        logo_url (Union[Unset, str]):
        name (Union[Unset, str]):
        notifications_config (Union[Unset, AppNotificationsConfig]):
        runner_group (Union[Unset, AppRunnerGroup]):
        sandbox_mode (Union[Unset, bool]):
        status (Union[Unset, str]):
        status_description (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        vcs_connections (Union[Unset, list['AppVCSConnection']]):
    """

    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    features: Union[Unset, "TypesStringBoolMap"] = UNSET
    id: Union[Unset, str] = UNSET
    links: Union[Unset, "AppOrgLinks"] = UNSET
    logo_url: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    notifications_config: Union[Unset, "AppNotificationsConfig"] = UNSET
    runner_group: Union[Unset, "AppRunnerGroup"] = UNSET
    sandbox_mode: Union[Unset, bool] = UNSET
    status: Union[Unset, str] = UNSET
    status_description: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    vcs_connections: Union[Unset, list["AppVCSConnection"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        features: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.features, Unset):
            features = self.features.to_dict()

        id = self.id

        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        logo_url = self.logo_url

        name = self.name

        notifications_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.notifications_config, Unset):
            notifications_config = self.notifications_config.to_dict()

        runner_group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.runner_group, Unset):
            runner_group = self.runner_group.to_dict()

        sandbox_mode = self.sandbox_mode

        status = self.status

        status_description = self.status_description

        updated_at = self.updated_at

        vcs_connections: Union[Unset, list[dict[str, Any]]] = UNSET
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
        features: Union[Unset, TypesStringBoolMap]
        if isinstance(_features, Unset):
            features = UNSET
        else:
            features = TypesStringBoolMap.from_dict(_features)

        id = d.pop("id", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, AppOrgLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = AppOrgLinks.from_dict(_links)

        logo_url = d.pop("logo_url", UNSET)

        name = d.pop("name", UNSET)

        _notifications_config = d.pop("notifications_config", UNSET)
        notifications_config: Union[Unset, AppNotificationsConfig]
        if isinstance(_notifications_config, Unset):
            notifications_config = UNSET
        else:
            notifications_config = AppNotificationsConfig.from_dict(_notifications_config)

        _runner_group = d.pop("runner_group", UNSET)
        runner_group: Union[Unset, AppRunnerGroup]
        if isinstance(_runner_group, Unset):
            runner_group = UNSET
        else:
            runner_group = AppRunnerGroup.from_dict(_runner_group)

        sandbox_mode = d.pop("sandbox_mode", UNSET)

        status = d.pop("status", UNSET)

        status_description = d.pop("status_description", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        vcs_connections = []
        _vcs_connections = d.pop("vcs_connections", UNSET)
        for vcs_connections_item_data in _vcs_connections or []:
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
