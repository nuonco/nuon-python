from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_install_deployment_type import ServiceInstallDeploymentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_install_deployment_affected_resources import ServiceInstallDeploymentAffectedResources
    from ..models.service_install_deployment_app_branch_ref import ServiceInstallDeploymentAppBranchRef
    from ..models.service_install_deployment_change_group import ServiceInstallDeploymentChangeGroup
    from ..models.service_install_deployment_image import ServiceInstallDeploymentImage
    from ..models.service_install_deployment_workflow_ref import ServiceInstallDeploymentWorkflowRef


T = TypeVar("T", bound="ServiceInstallDeployment")


@_attrs_define
class ServiceInstallDeployment:
    """
    Attributes:
        affected_resources (ServiceInstallDeploymentAffectedResources | Unset):
        app_branch (ServiceInstallDeploymentAppBranchRef | Unset):
        change_groups (list[ServiceInstallDeploymentChangeGroup] | Unset):
        component_name (str | Unset):
        created_at (str | Unset):
        id (str | Unset):
        image (ServiceInstallDeploymentImage | Unset):
        status (str | Unset):
        summary (str | Unset):
        title (str | Unset):
        type_ (ServiceInstallDeploymentType | Unset):
        workflow (ServiceInstallDeploymentWorkflowRef | Unset):
    """

    affected_resources: ServiceInstallDeploymentAffectedResources | Unset = UNSET
    app_branch: ServiceInstallDeploymentAppBranchRef | Unset = UNSET
    change_groups: list[ServiceInstallDeploymentChangeGroup] | Unset = UNSET
    component_name: str | Unset = UNSET
    created_at: str | Unset = UNSET
    id: str | Unset = UNSET
    image: ServiceInstallDeploymentImage | Unset = UNSET
    status: str | Unset = UNSET
    summary: str | Unset = UNSET
    title: str | Unset = UNSET
    type_: ServiceInstallDeploymentType | Unset = UNSET
    workflow: ServiceInstallDeploymentWorkflowRef | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_resources: dict[str, Any] | Unset = UNSET
        if not isinstance(self.affected_resources, Unset):
            affected_resources = self.affected_resources.to_dict()

        app_branch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.app_branch, Unset):
            app_branch = self.app_branch.to_dict()

        change_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.change_groups, Unset):
            change_groups = []
            for change_groups_item_data in self.change_groups:
                change_groups_item = change_groups_item_data.to_dict()
                change_groups.append(change_groups_item)

        component_name = self.component_name

        created_at = self.created_at

        id = self.id

        image: dict[str, Any] | Unset = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()

        status = self.status

        summary = self.summary

        title = self.title

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        workflow: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_resources is not UNSET:
            field_dict["affected_resources"] = affected_resources
        if app_branch is not UNSET:
            field_dict["app_branch"] = app_branch
        if change_groups is not UNSET:
            field_dict["change_groups"] = change_groups
        if component_name is not UNSET:
            field_dict["component_name"] = component_name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if image is not UNSET:
            field_dict["image"] = image
        if status is not UNSET:
            field_dict["status"] = status
        if summary is not UNSET:
            field_dict["summary"] = summary
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if workflow is not UNSET:
            field_dict["workflow"] = workflow

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_install_deployment_affected_resources import (
            ServiceInstallDeploymentAffectedResources,  # noqa: PLC0415
        )
        from ..models.service_install_deployment_app_branch_ref import (
            ServiceInstallDeploymentAppBranchRef,  # noqa: PLC0415
        )
        from ..models.service_install_deployment_change_group import (
            ServiceInstallDeploymentChangeGroup,  # noqa: PLC0415
        )
        from ..models.service_install_deployment_image import ServiceInstallDeploymentImage  # noqa: PLC0415
        from ..models.service_install_deployment_workflow_ref import (
            ServiceInstallDeploymentWorkflowRef,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _affected_resources = d.pop("affected_resources", UNSET)
        affected_resources: ServiceInstallDeploymentAffectedResources | Unset
        if isinstance(_affected_resources, Unset):
            affected_resources = UNSET
        else:
            affected_resources = ServiceInstallDeploymentAffectedResources.from_dict(_affected_resources)

        _app_branch = d.pop("app_branch", UNSET)
        app_branch: ServiceInstallDeploymentAppBranchRef | Unset
        if isinstance(_app_branch, Unset):
            app_branch = UNSET
        else:
            app_branch = ServiceInstallDeploymentAppBranchRef.from_dict(_app_branch)

        _change_groups = d.pop("change_groups", UNSET)
        change_groups: list[ServiceInstallDeploymentChangeGroup] | Unset = UNSET
        if _change_groups is not UNSET:
            change_groups = []
            for change_groups_item_data in _change_groups:
                change_groups_item = ServiceInstallDeploymentChangeGroup.from_dict(change_groups_item_data)

                change_groups.append(change_groups_item)

        component_name = d.pop("component_name", UNSET)

        created_at = d.pop("created_at", UNSET)

        id = d.pop("id", UNSET)

        _image = d.pop("image", UNSET)
        image: ServiceInstallDeploymentImage | Unset
        if isinstance(_image, Unset):
            image = UNSET
        else:
            image = ServiceInstallDeploymentImage.from_dict(_image)

        status = d.pop("status", UNSET)

        summary = d.pop("summary", UNSET)

        title = d.pop("title", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: ServiceInstallDeploymentType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ServiceInstallDeploymentType(_type_)

        _workflow = d.pop("workflow", UNSET)
        workflow: ServiceInstallDeploymentWorkflowRef | Unset
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = ServiceInstallDeploymentWorkflowRef.from_dict(_workflow)

        service_install_deployment = cls(
            affected_resources=affected_resources,
            app_branch=app_branch,
            change_groups=change_groups,
            component_name=component_name,
            created_at=created_at,
            id=id,
            image=image,
            status=status,
            summary=summary,
            title=title,
            type_=type_,
            workflow=workflow,
        )

        service_install_deployment.additional_properties = d
        return service_install_deployment

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
