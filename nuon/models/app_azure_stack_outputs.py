from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppAzureStackOutputs")


@_attrs_define
class AppAzureStackOutputs:
    """
    Attributes:
        key_vault_id (str | Unset):
        key_vault_name (str | Unset):
        network_id (str | Unset):
        network_name (str | Unset):
        private_subnet_ids (list[str] | Unset):
        private_subnet_names (list[str] | Unset):
        public_subnet_ids (list[str] | Unset):
        public_subnet_names (list[str] | Unset):
        resource_group_id (str | Unset):
        resource_group_location (str | Unset):
        resource_group_name (str | Unset):
        subscription_id (str | Unset):
        subscription_tenant_id (str | Unset):
    """

    key_vault_id: str | Unset = UNSET
    key_vault_name: str | Unset = UNSET
    network_id: str | Unset = UNSET
    network_name: str | Unset = UNSET
    private_subnet_ids: list[str] | Unset = UNSET
    private_subnet_names: list[str] | Unset = UNSET
    public_subnet_ids: list[str] | Unset = UNSET
    public_subnet_names: list[str] | Unset = UNSET
    resource_group_id: str | Unset = UNSET
    resource_group_location: str | Unset = UNSET
    resource_group_name: str | Unset = UNSET
    subscription_id: str | Unset = UNSET
    subscription_tenant_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key_vault_id = self.key_vault_id

        key_vault_name = self.key_vault_name

        network_id = self.network_id

        network_name = self.network_name

        private_subnet_ids: list[str] | Unset = UNSET
        if not isinstance(self.private_subnet_ids, Unset):
            private_subnet_ids = self.private_subnet_ids

        private_subnet_names: list[str] | Unset = UNSET
        if not isinstance(self.private_subnet_names, Unset):
            private_subnet_names = self.private_subnet_names

        public_subnet_ids: list[str] | Unset = UNSET
        if not isinstance(self.public_subnet_ids, Unset):
            public_subnet_ids = self.public_subnet_ids

        public_subnet_names: list[str] | Unset = UNSET
        if not isinstance(self.public_subnet_names, Unset):
            public_subnet_names = self.public_subnet_names

        resource_group_id = self.resource_group_id

        resource_group_location = self.resource_group_location

        resource_group_name = self.resource_group_name

        subscription_id = self.subscription_id

        subscription_tenant_id = self.subscription_tenant_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key_vault_id is not UNSET:
            field_dict["key_vault_id"] = key_vault_id
        if key_vault_name is not UNSET:
            field_dict["key_vault_name"] = key_vault_name
        if network_id is not UNSET:
            field_dict["network_id"] = network_id
        if network_name is not UNSET:
            field_dict["network_name"] = network_name
        if private_subnet_ids is not UNSET:
            field_dict["private_subnet_ids"] = private_subnet_ids
        if private_subnet_names is not UNSET:
            field_dict["private_subnet_names"] = private_subnet_names
        if public_subnet_ids is not UNSET:
            field_dict["public_subnet_ids"] = public_subnet_ids
        if public_subnet_names is not UNSET:
            field_dict["public_subnet_names"] = public_subnet_names
        if resource_group_id is not UNSET:
            field_dict["resource_group_id"] = resource_group_id
        if resource_group_location is not UNSET:
            field_dict["resource_group_location"] = resource_group_location
        if resource_group_name is not UNSET:
            field_dict["resource_group_name"] = resource_group_name
        if subscription_id is not UNSET:
            field_dict["subscription_id"] = subscription_id
        if subscription_tenant_id is not UNSET:
            field_dict["subscription_tenant_id"] = subscription_tenant_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key_vault_id = d.pop("key_vault_id", UNSET)

        key_vault_name = d.pop("key_vault_name", UNSET)

        network_id = d.pop("network_id", UNSET)

        network_name = d.pop("network_name", UNSET)

        private_subnet_ids = cast(list[str], d.pop("private_subnet_ids", UNSET))

        private_subnet_names = cast(list[str], d.pop("private_subnet_names", UNSET))

        public_subnet_ids = cast(list[str], d.pop("public_subnet_ids", UNSET))

        public_subnet_names = cast(list[str], d.pop("public_subnet_names", UNSET))

        resource_group_id = d.pop("resource_group_id", UNSET)

        resource_group_location = d.pop("resource_group_location", UNSET)

        resource_group_name = d.pop("resource_group_name", UNSET)

        subscription_id = d.pop("subscription_id", UNSET)

        subscription_tenant_id = d.pop("subscription_tenant_id", UNSET)

        app_azure_stack_outputs = cls(
            key_vault_id=key_vault_id,
            key_vault_name=key_vault_name,
            network_id=network_id,
            network_name=network_name,
            private_subnet_ids=private_subnet_ids,
            private_subnet_names=private_subnet_names,
            public_subnet_ids=public_subnet_ids,
            public_subnet_names=public_subnet_names,
            resource_group_id=resource_group_id,
            resource_group_location=resource_group_location,
            resource_group_name=resource_group_name,
            subscription_id=subscription_id,
            subscription_tenant_id=subscription_tenant_id,
        )

        app_azure_stack_outputs.additional_properties = d
        return app_azure_stack_outputs

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
