from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeysWorkflowTelemetry")


@_attrs_define
class KeysWorkflowTelemetry:
    """
    Attributes:
        install_id (str | Unset):
        install_name (str | Unset):
        org_id (str | Unset):
        org_name (str | Unset):
        owner_id (str | Unset):
        owner_name (str | Unset):
        owner_type (str | Unset):
        workflow_id (str | Unset):
        workflow_type (str | Unset):
    """

    install_id: str | Unset = UNSET
    install_name: str | Unset = UNSET
    org_id: str | Unset = UNSET
    org_name: str | Unset = UNSET
    owner_id: str | Unset = UNSET
    owner_name: str | Unset = UNSET
    owner_type: str | Unset = UNSET
    workflow_id: str | Unset = UNSET
    workflow_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        install_id = self.install_id

        install_name = self.install_name

        org_id = self.org_id

        org_name = self.org_name

        owner_id = self.owner_id

        owner_name = self.owner_name

        owner_type = self.owner_type

        workflow_id = self.workflow_id

        workflow_type = self.workflow_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if install_name is not UNSET:
            field_dict["install_name"] = install_name
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if org_name is not UNSET:
            field_dict["org_name"] = org_name
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if owner_name is not UNSET:
            field_dict["owner_name"] = owner_name
        if owner_type is not UNSET:
            field_dict["owner_type"] = owner_type
        if workflow_id is not UNSET:
            field_dict["workflow_id"] = workflow_id
        if workflow_type is not UNSET:
            field_dict["workflow_type"] = workflow_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        install_id = d.pop("install_id", UNSET)

        install_name = d.pop("install_name", UNSET)

        org_id = d.pop("org_id", UNSET)

        org_name = d.pop("org_name", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        owner_name = d.pop("owner_name", UNSET)

        owner_type = d.pop("owner_type", UNSET)

        workflow_id = d.pop("workflow_id", UNSET)

        workflow_type = d.pop("workflow_type", UNSET)

        keys_workflow_telemetry = cls(
            install_id=install_id,
            install_name=install_name,
            org_id=org_id,
            org_name=org_name,
            owner_id=owner_id,
            owner_name=owner_name,
            owner_type=owner_type,
            workflow_id=workflow_id,
            workflow_type=workflow_type,
        )

        keys_workflow_telemetry.additional_properties = d
        return keys_workflow_telemetry

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
