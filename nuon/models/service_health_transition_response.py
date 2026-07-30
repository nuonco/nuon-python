from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceHealthTransitionResponse")


@_attrs_define
class ServiceHealthTransitionResponse:
    """
    Attributes:
        correlated_deploy_id (str | Unset):
        diagnosis (str | Unset):
        from_health (str | Unset):
        message (str | Unset):
        observed_at (str | Unset):
        root_resource_kind (str | Unset):
        root_resource_name (str | Unset):
        root_resource_namespace (str | Unset):
        to_health (str | Unset):
    """

    correlated_deploy_id: str | Unset = UNSET
    diagnosis: str | Unset = UNSET
    from_health: str | Unset = UNSET
    message: str | Unset = UNSET
    observed_at: str | Unset = UNSET
    root_resource_kind: str | Unset = UNSET
    root_resource_name: str | Unset = UNSET
    root_resource_namespace: str | Unset = UNSET
    to_health: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        correlated_deploy_id = self.correlated_deploy_id

        diagnosis = self.diagnosis

        from_health = self.from_health

        message = self.message

        observed_at = self.observed_at

        root_resource_kind = self.root_resource_kind

        root_resource_name = self.root_resource_name

        root_resource_namespace = self.root_resource_namespace

        to_health = self.to_health

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if correlated_deploy_id is not UNSET:
            field_dict["correlated_deploy_id"] = correlated_deploy_id
        if diagnosis is not UNSET:
            field_dict["diagnosis"] = diagnosis
        if from_health is not UNSET:
            field_dict["from_health"] = from_health
        if message is not UNSET:
            field_dict["message"] = message
        if observed_at is not UNSET:
            field_dict["observed_at"] = observed_at
        if root_resource_kind is not UNSET:
            field_dict["root_resource_kind"] = root_resource_kind
        if root_resource_name is not UNSET:
            field_dict["root_resource_name"] = root_resource_name
        if root_resource_namespace is not UNSET:
            field_dict["root_resource_namespace"] = root_resource_namespace
        if to_health is not UNSET:
            field_dict["to_health"] = to_health

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        correlated_deploy_id = d.pop("correlated_deploy_id", UNSET)

        diagnosis = d.pop("diagnosis", UNSET)

        from_health = d.pop("from_health", UNSET)

        message = d.pop("message", UNSET)

        observed_at = d.pop("observed_at", UNSET)

        root_resource_kind = d.pop("root_resource_kind", UNSET)

        root_resource_name = d.pop("root_resource_name", UNSET)

        root_resource_namespace = d.pop("root_resource_namespace", UNSET)

        to_health = d.pop("to_health", UNSET)

        service_health_transition_response = cls(
            correlated_deploy_id=correlated_deploy_id,
            diagnosis=diagnosis,
            from_health=from_health,
            message=message,
            observed_at=observed_at,
            root_resource_kind=root_resource_kind,
            root_resource_name=root_resource_name,
            root_resource_namespace=root_resource_namespace,
            to_health=to_health,
        )

        service_health_transition_response.additional_properties = d
        return service_health_transition_response

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
