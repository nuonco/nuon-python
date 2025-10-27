from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_component_build_status import AppComponentBuildStatus
from ..models.app_install_deploy_status import AppInstallDeployStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_component import AppComponent
    from ..models.app_component_config_connection import AppComponentConfigConnection


T = TypeVar("T", bound="AppInstallComponentSummary")


@_attrs_define
class AppInstallComponentSummary:
    """
    Attributes:
        build_status (Union[Unset, AppComponentBuildStatus]):
        build_status_description (Union[Unset, str]):
        component_config (Union[Unset, AppComponentConfigConnection]):
        component_id (Union[Unset, str]):
        component_name (Union[Unset, str]):
        dependencies (Union[Unset, list['AppComponent']]):
        deploy_status (Union[Unset, AppInstallDeployStatus]):
        deploy_status_description (Union[Unset, str]):
        drifted_status (Union[Unset, bool]):
        id (Union[Unset, str]):
    """

    build_status: Union[Unset, AppComponentBuildStatus] = UNSET
    build_status_description: Union[Unset, str] = UNSET
    component_config: Union[Unset, "AppComponentConfigConnection"] = UNSET
    component_id: Union[Unset, str] = UNSET
    component_name: Union[Unset, str] = UNSET
    dependencies: Union[Unset, list["AppComponent"]] = UNSET
    deploy_status: Union[Unset, AppInstallDeployStatus] = UNSET
    deploy_status_description: Union[Unset, str] = UNSET
    drifted_status: Union[Unset, bool] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        build_status: Union[Unset, str] = UNSET
        if not isinstance(self.build_status, Unset):
            build_status = self.build_status.value

        build_status_description = self.build_status_description

        component_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.component_config, Unset):
            component_config = self.component_config.to_dict()

        component_id = self.component_id

        component_name = self.component_name

        dependencies: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.dependencies, Unset):
            dependencies = []
            for dependencies_item_data in self.dependencies:
                dependencies_item = dependencies_item_data.to_dict()
                dependencies.append(dependencies_item)

        deploy_status: Union[Unset, str] = UNSET
        if not isinstance(self.deploy_status, Unset):
            deploy_status = self.deploy_status.value

        deploy_status_description = self.deploy_status_description

        drifted_status = self.drifted_status

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if build_status is not UNSET:
            field_dict["build_status"] = build_status
        if build_status_description is not UNSET:
            field_dict["build_status_description"] = build_status_description
        if component_config is not UNSET:
            field_dict["component_config"] = component_config
        if component_id is not UNSET:
            field_dict["component_id"] = component_id
        if component_name is not UNSET:
            field_dict["component_name"] = component_name
        if dependencies is not UNSET:
            field_dict["dependencies"] = dependencies
        if deploy_status is not UNSET:
            field_dict["deploy_status"] = deploy_status
        if deploy_status_description is not UNSET:
            field_dict["deploy_status_description"] = deploy_status_description
        if drifted_status is not UNSET:
            field_dict["drifted_status"] = drifted_status
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_component import AppComponent
        from ..models.app_component_config_connection import AppComponentConfigConnection

        d = dict(src_dict)
        _build_status = d.pop("build_status", UNSET)
        build_status: Union[Unset, AppComponentBuildStatus]
        if isinstance(_build_status, Unset):
            build_status = UNSET
        else:
            build_status = AppComponentBuildStatus(_build_status)

        build_status_description = d.pop("build_status_description", UNSET)

        _component_config = d.pop("component_config", UNSET)
        component_config: Union[Unset, AppComponentConfigConnection]
        if isinstance(_component_config, Unset):
            component_config = UNSET
        else:
            component_config = AppComponentConfigConnection.from_dict(_component_config)

        component_id = d.pop("component_id", UNSET)

        component_name = d.pop("component_name", UNSET)

        dependencies = []
        _dependencies = d.pop("dependencies", UNSET)
        for dependencies_item_data in _dependencies or []:
            dependencies_item = AppComponent.from_dict(dependencies_item_data)

            dependencies.append(dependencies_item)

        _deploy_status = d.pop("deploy_status", UNSET)
        deploy_status: Union[Unset, AppInstallDeployStatus]
        if isinstance(_deploy_status, Unset):
            deploy_status = UNSET
        else:
            deploy_status = AppInstallDeployStatus(_deploy_status)

        deploy_status_description = d.pop("deploy_status_description", UNSET)

        drifted_status = d.pop("drifted_status", UNSET)

        id = d.pop("id", UNSET)

        app_install_component_summary = cls(
            build_status=build_status,
            build_status_description=build_status_description,
            component_config=component_config,
            component_id=component_id,
            component_name=component_name,
            dependencies=dependencies,
            deploy_status=deploy_status,
            deploy_status_description=deploy_status_description,
            drifted_status=drifted_status,
            id=id,
        )

        app_install_component_summary.additional_properties = d
        return app_install_component_summary

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
