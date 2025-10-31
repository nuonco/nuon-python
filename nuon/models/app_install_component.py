from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_component import AppComponent
    from ..models.app_composite_status import AppCompositeStatus
    from ..models.app_drifted_object import AppDriftedObject
    from ..models.app_helm_chart import AppHelmChart
    from ..models.app_install_component_links import AppInstallComponentLinks
    from ..models.app_install_deploy import AppInstallDeploy
    from ..models.app_terraform_workspace import AppTerraformWorkspace


T = TypeVar("T", bound="AppInstallComponent")


@_attrs_define
class AppInstallComponent:
    """
    Attributes:
        component (AppComponent | Unset):
        component_id (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        drifted_object (AppDriftedObject | Unset):
        helm_chart (AppHelmChart | Unset):
        id (str | Unset):
        install_deploys (list[AppInstallDeploy] | Unset):
        install_id (str | Unset):
        links (AppInstallComponentLinks | Unset):
        status (str | Unset):
        status_description (str | Unset):
        status_v2 (AppCompositeStatus | Unset):
        terraform_workspace (AppTerraformWorkspace | Unset):
        updated_at (str | Unset):
    """

    component: AppComponent | Unset = UNSET
    component_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    drifted_object: AppDriftedObject | Unset = UNSET
    helm_chart: AppHelmChart | Unset = UNSET
    id: str | Unset = UNSET
    install_deploys: list[AppInstallDeploy] | Unset = UNSET
    install_id: str | Unset = UNSET
    links: AppInstallComponentLinks | Unset = UNSET
    status: str | Unset = UNSET
    status_description: str | Unset = UNSET
    status_v2: AppCompositeStatus | Unset = UNSET
    terraform_workspace: AppTerraformWorkspace | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component: dict[str, Any] | Unset = UNSET
        if not isinstance(self.component, Unset):
            component = self.component.to_dict()

        component_id = self.component_id

        created_at = self.created_at

        created_by_id = self.created_by_id

        drifted_object: dict[str, Any] | Unset = UNSET
        if not isinstance(self.drifted_object, Unset):
            drifted_object = self.drifted_object.to_dict()

        helm_chart: dict[str, Any] | Unset = UNSET
        if not isinstance(self.helm_chart, Unset):
            helm_chart = self.helm_chart.to_dict()

        id = self.id

        install_deploys: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.install_deploys, Unset):
            install_deploys = []
            for install_deploys_item_data in self.install_deploys:
                install_deploys_item = install_deploys_item_data.to_dict()
                install_deploys.append(install_deploys_item)

        install_id = self.install_id

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        status = self.status

        status_description = self.status_description

        status_v2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status_v2, Unset):
            status_v2 = self.status_v2.to_dict()

        terraform_workspace: dict[str, Any] | Unset = UNSET
        if not isinstance(self.terraform_workspace, Unset):
            terraform_workspace = self.terraform_workspace.to_dict()

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if component is not UNSET:
            field_dict["component"] = component
        if component_id is not UNSET:
            field_dict["component_id"] = component_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if drifted_object is not UNSET:
            field_dict["drifted_object"] = drifted_object
        if helm_chart is not UNSET:
            field_dict["helm_chart"] = helm_chart
        if id is not UNSET:
            field_dict["id"] = id
        if install_deploys is not UNSET:
            field_dict["install_deploys"] = install_deploys
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if links is not UNSET:
            field_dict["links"] = links
        if status is not UNSET:
            field_dict["status"] = status
        if status_description is not UNSET:
            field_dict["status_description"] = status_description
        if status_v2 is not UNSET:
            field_dict["status_v2"] = status_v2
        if terraform_workspace is not UNSET:
            field_dict["terraform_workspace"] = terraform_workspace
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_component import AppComponent
        from ..models.app_composite_status import AppCompositeStatus
        from ..models.app_drifted_object import AppDriftedObject
        from ..models.app_helm_chart import AppHelmChart
        from ..models.app_install_component_links import AppInstallComponentLinks
        from ..models.app_install_deploy import AppInstallDeploy
        from ..models.app_terraform_workspace import AppTerraformWorkspace

        d = dict(src_dict)
        _component = d.pop("component", UNSET)
        component: AppComponent | Unset
        if isinstance(_component, Unset):
            component = UNSET
        else:
            component = AppComponent.from_dict(_component)

        component_id = d.pop("component_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        _drifted_object = d.pop("drifted_object", UNSET)
        drifted_object: AppDriftedObject | Unset
        if isinstance(_drifted_object, Unset):
            drifted_object = UNSET
        else:
            drifted_object = AppDriftedObject.from_dict(_drifted_object)

        _helm_chart = d.pop("helm_chart", UNSET)
        helm_chart: AppHelmChart | Unset
        if isinstance(_helm_chart, Unset):
            helm_chart = UNSET
        else:
            helm_chart = AppHelmChart.from_dict(_helm_chart)

        id = d.pop("id", UNSET)

        install_deploys = []
        _install_deploys = d.pop("install_deploys", UNSET)
        for install_deploys_item_data in _install_deploys or []:
            install_deploys_item = AppInstallDeploy.from_dict(install_deploys_item_data)

            install_deploys.append(install_deploys_item)

        install_id = d.pop("install_id", UNSET)

        _links = d.pop("links", UNSET)
        links: AppInstallComponentLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = AppInstallComponentLinks.from_dict(_links)

        status = d.pop("status", UNSET)

        status_description = d.pop("status_description", UNSET)

        _status_v2 = d.pop("status_v2", UNSET)
        status_v2: AppCompositeStatus | Unset
        if isinstance(_status_v2, Unset):
            status_v2 = UNSET
        else:
            status_v2 = AppCompositeStatus.from_dict(_status_v2)

        _terraform_workspace = d.pop("terraform_workspace", UNSET)
        terraform_workspace: AppTerraformWorkspace | Unset
        if isinstance(_terraform_workspace, Unset):
            terraform_workspace = UNSET
        else:
            terraform_workspace = AppTerraformWorkspace.from_dict(_terraform_workspace)

        updated_at = d.pop("updated_at", UNSET)

        app_install_component = cls(
            component=component,
            component_id=component_id,
            created_at=created_at,
            created_by_id=created_by_id,
            drifted_object=drifted_object,
            helm_chart=helm_chart,
            id=id,
            install_deploys=install_deploys,
            install_id=install_id,
            links=links,
            status=status,
            status_description=status_description,
            status_v2=status_v2,
            terraform_workspace=terraform_workspace,
            updated_at=updated_at,
        )

        app_install_component.additional_properties = d
        return app_install_component

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
