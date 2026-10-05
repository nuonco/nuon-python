from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_install_config_drift_component import ServiceInstallConfigDriftComponent
    from ..models.service_install_config_drift_resource import ServiceInstallConfigDriftResource


T = TypeVar("T", bound="ServiceInstallConfigDrift")


@_attrs_define
class ServiceInstallConfigDrift:
    """
    Attributes:
        components (list[ServiceInstallConfigDriftComponent] | Unset):
        current_app_config_id (str | Unset):
        sandbox (ServiceInstallConfigDriftResource | Unset):
        stack (ServiceInstallConfigDriftResource | Unset):
    """

    components: list[ServiceInstallConfigDriftComponent] | Unset = UNSET
    current_app_config_id: str | Unset = UNSET
    sandbox: ServiceInstallConfigDriftResource | Unset = UNSET
    stack: ServiceInstallConfigDriftResource | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        components: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.components, Unset):
            components = []
            for components_item_data in self.components:
                components_item = components_item_data.to_dict()
                components.append(components_item)

        current_app_config_id = self.current_app_config_id

        sandbox: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sandbox, Unset):
            sandbox = self.sandbox.to_dict()

        stack: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stack, Unset):
            stack = self.stack.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if components is not UNSET:
            field_dict["components"] = components
        if current_app_config_id is not UNSET:
            field_dict["current_app_config_id"] = current_app_config_id
        if sandbox is not UNSET:
            field_dict["sandbox"] = sandbox
        if stack is not UNSET:
            field_dict["stack"] = stack

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_install_config_drift_component import ServiceInstallConfigDriftComponent  # noqa: PLC0415
        from ..models.service_install_config_drift_resource import ServiceInstallConfigDriftResource  # noqa: PLC0415

        d = dict(src_dict)
        _components = d.pop("components", UNSET)
        components: list[ServiceInstallConfigDriftComponent] | Unset = UNSET
        if _components is not UNSET:
            components = []
            for components_item_data in _components:
                components_item = ServiceInstallConfigDriftComponent.from_dict(components_item_data)

                components.append(components_item)

        current_app_config_id = d.pop("current_app_config_id", UNSET)

        _sandbox = d.pop("sandbox", UNSET)
        sandbox: ServiceInstallConfigDriftResource | Unset
        if isinstance(_sandbox, Unset):
            sandbox = UNSET
        else:
            sandbox = ServiceInstallConfigDriftResource.from_dict(_sandbox)

        _stack = d.pop("stack", UNSET)
        stack: ServiceInstallConfigDriftResource | Unset
        if isinstance(_stack, Unset):
            stack = UNSET
        else:
            stack = ServiceInstallConfigDriftResource.from_dict(_stack)

        service_install_config_drift = cls(
            components=components,
            current_app_config_id=current_app_config_id,
            sandbox=sandbox,
            stack=stack,
        )

        service_install_config_drift.additional_properties = d
        return service_install_config_drift

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
