from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppDriftedObject")


@_attrs_define
class AppDriftedObject:
    """
    Attributes:
        app_sandbox_config_id (Union[Unset, str]):
        component_build_id (Union[Unset, str]):
        component_name (Union[Unset, str]):
        install_component_id (Union[Unset, str]):
        install_id (Union[Unset, str]):
        install_sandbox_id (Union[Unset, str]):
        install_workflow_id (Union[Unset, str]):
        org_id (Union[Unset, str]):
        target_id (Union[Unset, str]):
        target_type (Union[Unset, str]): These fields will be populated from the drifts_view
    """

    app_sandbox_config_id: Union[Unset, str] = UNSET
    component_build_id: Union[Unset, str] = UNSET
    component_name: Union[Unset, str] = UNSET
    install_component_id: Union[Unset, str] = UNSET
    install_id: Union[Unset, str] = UNSET
    install_sandbox_id: Union[Unset, str] = UNSET
    install_workflow_id: Union[Unset, str] = UNSET
    org_id: Union[Unset, str] = UNSET
    target_id: Union[Unset, str] = UNSET
    target_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_sandbox_config_id = self.app_sandbox_config_id

        component_build_id = self.component_build_id

        component_name = self.component_name

        install_component_id = self.install_component_id

        install_id = self.install_id

        install_sandbox_id = self.install_sandbox_id

        install_workflow_id = self.install_workflow_id

        org_id = self.org_id

        target_id = self.target_id

        target_type = self.target_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_sandbox_config_id is not UNSET:
            field_dict["app_sandbox_config_id"] = app_sandbox_config_id
        if component_build_id is not UNSET:
            field_dict["component_build_id"] = component_build_id
        if component_name is not UNSET:
            field_dict["component_name"] = component_name
        if install_component_id is not UNSET:
            field_dict["install_component_id"] = install_component_id
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if install_sandbox_id is not UNSET:
            field_dict["install_sandbox_id"] = install_sandbox_id
        if install_workflow_id is not UNSET:
            field_dict["install_workflow_id"] = install_workflow_id
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if target_id is not UNSET:
            field_dict["target_id"] = target_id
        if target_type is not UNSET:
            field_dict["target_type"] = target_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_sandbox_config_id = d.pop("app_sandbox_config_id", UNSET)

        component_build_id = d.pop("component_build_id", UNSET)

        component_name = d.pop("component_name", UNSET)

        install_component_id = d.pop("install_component_id", UNSET)

        install_id = d.pop("install_id", UNSET)

        install_sandbox_id = d.pop("install_sandbox_id", UNSET)

        install_workflow_id = d.pop("install_workflow_id", UNSET)

        org_id = d.pop("org_id", UNSET)

        target_id = d.pop("target_id", UNSET)

        target_type = d.pop("target_type", UNSET)

        app_drifted_object = cls(
            app_sandbox_config_id=app_sandbox_config_id,
            component_build_id=component_build_id,
            component_name=component_name,
            install_component_id=install_component_id,
            install_id=install_id,
            install_sandbox_id=install_sandbox_id,
            install_workflow_id=install_workflow_id,
            org_id=org_id,
            target_id=target_id,
            target_type=target_type,
        )

        app_drifted_object.additional_properties = d
        return app_drifted_object

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
