from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_connected_github_vcs_config import AppConnectedGithubVCSConfig
    from ..models.app_helm_component_config_values import AppHelmComponentConfigValues
    from ..models.app_helm_config import AppHelmConfig
    from ..models.app_public_git_vcs_config import AppPublicGitVCSConfig


T = TypeVar("T", bound="AppHelmComponentConfig")


@_attrs_define
class AppHelmComponentConfig:
    """
    Attributes:
        chart_name (str | Unset): Helm specific configurations
        component_config_connection_id (str | Unset): parent reference
        connected_github_vcs_config (AppConnectedGithubVCSConfig | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        helm_config_json (AppHelmConfig | Unset):
        id (str | Unset):
        namespace (str | Unset):
        public_git_vcs_config (AppPublicGitVCSConfig | Unset):
        storage_driver (str | Unset):
        take_ownership (bool | Unset): Newer config fields that we don't need a column for
        updated_at (str | Unset):
        values (AppHelmComponentConfigValues | Unset):
        values_files (list[str] | Unset):
    """

    chart_name: str | Unset = UNSET
    component_config_connection_id: str | Unset = UNSET
    connected_github_vcs_config: AppConnectedGithubVCSConfig | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    helm_config_json: AppHelmConfig | Unset = UNSET
    id: str | Unset = UNSET
    namespace: str | Unset = UNSET
    public_git_vcs_config: AppPublicGitVCSConfig | Unset = UNSET
    storage_driver: str | Unset = UNSET
    take_ownership: bool | Unset = UNSET
    updated_at: str | Unset = UNSET
    values: AppHelmComponentConfigValues | Unset = UNSET
    values_files: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chart_name = self.chart_name

        component_config_connection_id = self.component_config_connection_id

        connected_github_vcs_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.connected_github_vcs_config, Unset):
            connected_github_vcs_config = self.connected_github_vcs_config.to_dict()

        created_at = self.created_at

        created_by_id = self.created_by_id

        helm_config_json: dict[str, Any] | Unset = UNSET
        if not isinstance(self.helm_config_json, Unset):
            helm_config_json = self.helm_config_json.to_dict()

        id = self.id

        namespace = self.namespace

        public_git_vcs_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.public_git_vcs_config, Unset):
            public_git_vcs_config = self.public_git_vcs_config.to_dict()

        storage_driver = self.storage_driver

        take_ownership = self.take_ownership

        updated_at = self.updated_at

        values: dict[str, Any] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = self.values.to_dict()

        values_files: list[str] | Unset = UNSET
        if not isinstance(self.values_files, Unset):
            values_files = self.values_files

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chart_name is not UNSET:
            field_dict["chart_name"] = chart_name
        if component_config_connection_id is not UNSET:
            field_dict["component_config_connection_id"] = component_config_connection_id
        if connected_github_vcs_config is not UNSET:
            field_dict["connected_github_vcs_config"] = connected_github_vcs_config
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if helm_config_json is not UNSET:
            field_dict["helm_config_json"] = helm_config_json
        if id is not UNSET:
            field_dict["id"] = id
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if public_git_vcs_config is not UNSET:
            field_dict["public_git_vcs_config"] = public_git_vcs_config
        if storage_driver is not UNSET:
            field_dict["storage_driver"] = storage_driver
        if take_ownership is not UNSET:
            field_dict["take_ownership"] = take_ownership
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if values is not UNSET:
            field_dict["values"] = values
        if values_files is not UNSET:
            field_dict["values_files"] = values_files

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_connected_github_vcs_config import AppConnectedGithubVCSConfig
        from ..models.app_helm_component_config_values import AppHelmComponentConfigValues
        from ..models.app_helm_config import AppHelmConfig
        from ..models.app_public_git_vcs_config import AppPublicGitVCSConfig

        d = dict(src_dict)
        chart_name = d.pop("chart_name", UNSET)

        component_config_connection_id = d.pop("component_config_connection_id", UNSET)

        _connected_github_vcs_config = d.pop("connected_github_vcs_config", UNSET)
        connected_github_vcs_config: AppConnectedGithubVCSConfig | Unset
        if isinstance(_connected_github_vcs_config, Unset):
            connected_github_vcs_config = UNSET
        else:
            connected_github_vcs_config = AppConnectedGithubVCSConfig.from_dict(_connected_github_vcs_config)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        _helm_config_json = d.pop("helm_config_json", UNSET)
        helm_config_json: AppHelmConfig | Unset
        if isinstance(_helm_config_json, Unset):
            helm_config_json = UNSET
        else:
            helm_config_json = AppHelmConfig.from_dict(_helm_config_json)

        id = d.pop("id", UNSET)

        namespace = d.pop("namespace", UNSET)

        _public_git_vcs_config = d.pop("public_git_vcs_config", UNSET)
        public_git_vcs_config: AppPublicGitVCSConfig | Unset
        if isinstance(_public_git_vcs_config, Unset):
            public_git_vcs_config = UNSET
        else:
            public_git_vcs_config = AppPublicGitVCSConfig.from_dict(_public_git_vcs_config)

        storage_driver = d.pop("storage_driver", UNSET)

        take_ownership = d.pop("take_ownership", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _values = d.pop("values", UNSET)
        values: AppHelmComponentConfigValues | Unset
        if isinstance(_values, Unset):
            values = UNSET
        else:
            values = AppHelmComponentConfigValues.from_dict(_values)

        values_files = cast(list[str], d.pop("values_files", UNSET))

        app_helm_component_config = cls(
            chart_name=chart_name,
            component_config_connection_id=component_config_connection_id,
            connected_github_vcs_config=connected_github_vcs_config,
            created_at=created_at,
            created_by_id=created_by_id,
            helm_config_json=helm_config_json,
            id=id,
            namespace=namespace,
            public_git_vcs_config=public_git_vcs_config,
            storage_driver=storage_driver,
            take_ownership=take_ownership,
            updated_at=updated_at,
            values=values,
            values_files=values_files,
        )

        app_helm_component_config.additional_properties = d
        return app_helm_component_config

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
