from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_install_component_resource_state import AppInstallComponentResourceState
    from ..models.service_health_transition_response import ServiceHealthTransitionResponse


T = TypeVar("T", bound="ServiceComponentHealthIncidentBundle")


@_attrs_define
class ServiceComponentHealthIncidentBundle:
    """
    Attributes:
        current_health (str | Unset):
        install_component_id (str | Unset):
        resolved (bool | Unset):
        resources (list[AppInstallComponentResourceState] | Unset):
        transition (ServiceHealthTransitionResponse | Unset):
    """

    current_health: str | Unset = UNSET
    install_component_id: str | Unset = UNSET
    resolved: bool | Unset = UNSET
    resources: list[AppInstallComponentResourceState] | Unset = UNSET
    transition: ServiceHealthTransitionResponse | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_health = self.current_health

        install_component_id = self.install_component_id

        resolved = self.resolved

        resources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.resources, Unset):
            resources = []
            for resources_item_data in self.resources:
                resources_item = resources_item_data.to_dict()
                resources.append(resources_item)

        transition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.transition, Unset):
            transition = self.transition.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_health is not UNSET:
            field_dict["current_health"] = current_health
        if install_component_id is not UNSET:
            field_dict["install_component_id"] = install_component_id
        if resolved is not UNSET:
            field_dict["resolved"] = resolved
        if resources is not UNSET:
            field_dict["resources"] = resources
        if transition is not UNSET:
            field_dict["transition"] = transition

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_install_component_resource_state import AppInstallComponentResourceState
        from ..models.service_health_transition_response import ServiceHealthTransitionResponse

        d = dict(src_dict)
        current_health = d.pop("current_health", UNSET)

        install_component_id = d.pop("install_component_id", UNSET)

        resolved = d.pop("resolved", UNSET)

        _resources = d.pop("resources", UNSET)
        resources: list[AppInstallComponentResourceState] | Unset = UNSET
        if _resources is not UNSET:
            resources = []
            for resources_item_data in _resources:
                resources_item = AppInstallComponentResourceState.from_dict(resources_item_data)

                resources.append(resources_item)

        _transition = d.pop("transition", UNSET)
        transition: ServiceHealthTransitionResponse | Unset
        if isinstance(_transition, Unset):
            transition = UNSET
        else:
            transition = ServiceHealthTransitionResponse.from_dict(_transition)

        service_component_health_incident_bundle = cls(
            current_health=current_health,
            install_component_id=install_component_id,
            resolved=resolved,
            resources=resources,
            transition=transition,
        )

        service_component_health_incident_bundle.additional_properties = d
        return service_component_health_incident_bundle

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
