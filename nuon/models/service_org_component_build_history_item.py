from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_component_build import AppComponentBuild


T = TypeVar("T", bound="ServiceOrgComponentBuildHistoryItem")


@_attrs_define
class ServiceOrgComponentBuildHistoryItem:
    """
    Attributes:
        app_id (str | Unset):
        build (AppComponentBuild | Unset):
        build_runner_job_id (str | Unset):
        component_id (str | Unset):
        component_name (str | Unset):
    """

    app_id: str | Unset = UNSET
    build: AppComponentBuild | Unset = UNSET
    build_runner_job_id: str | Unset = UNSET
    component_id: str | Unset = UNSET
    component_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        build: dict[str, Any] | Unset = UNSET
        if not isinstance(self.build, Unset):
            build = self.build.to_dict()

        build_runner_job_id = self.build_runner_job_id

        component_id = self.component_id

        component_name = self.component_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if build is not UNSET:
            field_dict["build"] = build
        if build_runner_job_id is not UNSET:
            field_dict["build_runner_job_id"] = build_runner_job_id
        if component_id is not UNSET:
            field_dict["component_id"] = component_id
        if component_name is not UNSET:
            field_dict["component_name"] = component_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_component_build import AppComponentBuild

        d = dict(src_dict)
        app_id = d.pop("app_id", UNSET)

        _build = d.pop("build", UNSET)
        build: AppComponentBuild | Unset
        if isinstance(_build, Unset):
            build = UNSET
        else:
            build = AppComponentBuild.from_dict(_build)

        build_runner_job_id = d.pop("build_runner_job_id", UNSET)

        component_id = d.pop("component_id", UNSET)

        component_name = d.pop("component_name", UNSET)

        service_org_component_build_history_item = cls(
            app_id=app_id,
            build=build,
            build_runner_job_id=build_runner_job_id,
            component_id=component_id,
            component_name=component_name,
        )

        service_org_component_build_history_item.additional_properties = d
        return service_org_component_build_history_item

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
