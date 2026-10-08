from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_install_deployment_type import ServiceInstallDeploymentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_install_deployment_step import ServiceInstallDeploymentStep


T = TypeVar("T", bound="ServiceInstallDeploymentSummary")


@_attrs_define
class ServiceInstallDeploymentSummary:
    """
    Attributes:
        activity (str | Unset):
        created_at (str | Unset):
        finished (bool | Unset):
        id (str | Unset):
        status (str | Unset):
        steps (list[ServiceInstallDeploymentStep] | Unset):
        title (str | Unset):
        type_ (ServiceInstallDeploymentType | Unset):
    """

    activity: str | Unset = UNSET
    created_at: str | Unset = UNSET
    finished: bool | Unset = UNSET
    id: str | Unset = UNSET
    status: str | Unset = UNSET
    steps: list[ServiceInstallDeploymentStep] | Unset = UNSET
    title: str | Unset = UNSET
    type_: ServiceInstallDeploymentType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity = self.activity

        created_at = self.created_at

        finished = self.finished

        id = self.id

        status = self.status

        steps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item = steps_item_data.to_dict()
                steps.append(steps_item)

        title = self.title

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activity is not UNSET:
            field_dict["activity"] = activity
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if finished is not UNSET:
            field_dict["finished"] = finished
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if steps is not UNSET:
            field_dict["steps"] = steps
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_install_deployment_step import ServiceInstallDeploymentStep  # noqa: PLC0415

        d = dict(src_dict)
        activity = d.pop("activity", UNSET)

        created_at = d.pop("created_at", UNSET)

        finished = d.pop("finished", UNSET)

        id = d.pop("id", UNSET)

        status = d.pop("status", UNSET)

        _steps = d.pop("steps", UNSET)
        steps: list[ServiceInstallDeploymentStep] | Unset = UNSET
        if _steps is not UNSET:
            steps = []
            for steps_item_data in _steps:
                steps_item = ServiceInstallDeploymentStep.from_dict(steps_item_data)

                steps.append(steps_item)

        title = d.pop("title", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: ServiceInstallDeploymentType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ServiceInstallDeploymentType(_type_)

        service_install_deployment_summary = cls(
            activity=activity,
            created_at=created_at,
            finished=finished,
            id=id,
            status=status,
            steps=steps,
            title=title,
            type_=type_,
        )

        service_install_deployment_summary.additional_properties = d
        return service_install_deployment_summary

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
