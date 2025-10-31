from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceCreateInstallComponentDeployRequest")


@_attrs_define
class ServiceCreateInstallComponentDeployRequest:
    """
    Attributes:
        build_id (str | Unset):
        deploy_dependents (bool | Unset):
        plan_only (bool | Unset):
    """

    build_id: str | Unset = UNSET
    deploy_dependents: bool | Unset = UNSET
    plan_only: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        build_id = self.build_id

        deploy_dependents = self.deploy_dependents

        plan_only = self.plan_only

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if build_id is not UNSET:
            field_dict["build_id"] = build_id
        if deploy_dependents is not UNSET:
            field_dict["deploy_dependents"] = deploy_dependents
        if plan_only is not UNSET:
            field_dict["plan_only"] = plan_only

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        build_id = d.pop("build_id", UNSET)

        deploy_dependents = d.pop("deploy_dependents", UNSET)

        plan_only = d.pop("plan_only", UNSET)

        service_create_install_component_deploy_request = cls(
            build_id=build_id,
            deploy_dependents=deploy_dependents,
            plan_only=plan_only,
        )

        service_create_install_component_deploy_request.additional_properties = d
        return service_create_install_component_deploy_request

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
