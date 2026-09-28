from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceInstallDeploymentAffectedResources")


@_attrs_define
class ServiceInstallDeploymentAffectedResources:
    """
    Attributes:
        components (list[str] | Unset):
        images (list[str] | Unset):
        sandbox (bool | Unset):
        stack (bool | Unset):
    """

    components: list[str] | Unset = UNSET
    images: list[str] | Unset = UNSET
    sandbox: bool | Unset = UNSET
    stack: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        components: list[str] | Unset = UNSET
        if not isinstance(self.components, Unset):
            components = self.components

        images: list[str] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = self.images

        sandbox = self.sandbox

        stack = self.stack

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if components is not UNSET:
            field_dict["components"] = components
        if images is not UNSET:
            field_dict["images"] = images
        if sandbox is not UNSET:
            field_dict["sandbox"] = sandbox
        if stack is not UNSET:
            field_dict["stack"] = stack

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        components = cast(list[str], d.pop("components", UNSET))

        images = cast(list[str], d.pop("images", UNSET))

        sandbox = d.pop("sandbox", UNSET)

        stack = d.pop("stack", UNSET)

        service_install_deployment_affected_resources = cls(
            components=components,
            images=images,
            sandbox=sandbox,
            stack=stack,
        )

        service_install_deployment_affected_resources.additional_properties = d
        return service_install_deployment_affected_resources

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
