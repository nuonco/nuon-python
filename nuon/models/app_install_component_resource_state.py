from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppInstallComponentResourceState")


@_attrs_define
class AppInstallComponentResourceState:
    """
    Attributes:
        api_group (str | Unset):
        component_id (str | Unset):
        details (str | Unset):
        health (str | Unset):
        install_component_id (str | Unset):
        install_id (str | Unset):
        kind (str | Unset):
        message (str | Unset):
        name (str | Unset):
        namespace (str | Unset):
        native_status (str | Unset):
        observed_at (str | Unset):
        org_id (str | Unset):
        owner_name (str | Unset):
        provider (str | Unset):
        runner_id (str | Unset):
        source (str | Unset): Source classifies the resource owner: "component" (an app component,
            keyed by install_component_id) or "sandbox" (install base infra, keyed by
            owner_name = helm release name). OwnerName is the display group for
            sandbox resources.
    """

    api_group: str | Unset = UNSET
    component_id: str | Unset = UNSET
    details: str | Unset = UNSET
    health: str | Unset = UNSET
    install_component_id: str | Unset = UNSET
    install_id: str | Unset = UNSET
    kind: str | Unset = UNSET
    message: str | Unset = UNSET
    name: str | Unset = UNSET
    namespace: str | Unset = UNSET
    native_status: str | Unset = UNSET
    observed_at: str | Unset = UNSET
    org_id: str | Unset = UNSET
    owner_name: str | Unset = UNSET
    provider: str | Unset = UNSET
    runner_id: str | Unset = UNSET
    source: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_group = self.api_group

        component_id = self.component_id

        details = self.details

        health = self.health

        install_component_id = self.install_component_id

        install_id = self.install_id

        kind = self.kind

        message = self.message

        name = self.name

        namespace = self.namespace

        native_status = self.native_status

        observed_at = self.observed_at

        org_id = self.org_id

        owner_name = self.owner_name

        provider = self.provider

        runner_id = self.runner_id

        source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_group is not UNSET:
            field_dict["api_group"] = api_group
        if component_id is not UNSET:
            field_dict["component_id"] = component_id
        if details is not UNSET:
            field_dict["details"] = details
        if health is not UNSET:
            field_dict["health"] = health
        if install_component_id is not UNSET:
            field_dict["install_component_id"] = install_component_id
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if message is not UNSET:
            field_dict["message"] = message
        if name is not UNSET:
            field_dict["name"] = name
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if native_status is not UNSET:
            field_dict["native_status"] = native_status
        if observed_at is not UNSET:
            field_dict["observed_at"] = observed_at
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if owner_name is not UNSET:
            field_dict["owner_name"] = owner_name
        if provider is not UNSET:
            field_dict["provider"] = provider
        if runner_id is not UNSET:
            field_dict["runner_id"] = runner_id
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_group = d.pop("api_group", UNSET)

        component_id = d.pop("component_id", UNSET)

        details = d.pop("details", UNSET)

        health = d.pop("health", UNSET)

        install_component_id = d.pop("install_component_id", UNSET)

        install_id = d.pop("install_id", UNSET)

        kind = d.pop("kind", UNSET)

        message = d.pop("message", UNSET)

        name = d.pop("name", UNSET)

        namespace = d.pop("namespace", UNSET)

        native_status = d.pop("native_status", UNSET)

        observed_at = d.pop("observed_at", UNSET)

        org_id = d.pop("org_id", UNSET)

        owner_name = d.pop("owner_name", UNSET)

        provider = d.pop("provider", UNSET)

        runner_id = d.pop("runner_id", UNSET)

        source = d.pop("source", UNSET)

        app_install_component_resource_state = cls(
            api_group=api_group,
            component_id=component_id,
            details=details,
            health=health,
            install_component_id=install_component_id,
            install_id=install_id,
            kind=kind,
            message=message,
            name=name,
            namespace=namespace,
            native_status=native_status,
            observed_at=observed_at,
            org_id=org_id,
            owner_name=owner_name,
            provider=provider,
            runner_id=runner_id,
            source=source,
        )

        app_install_component_resource_state.additional_properties = d
        return app_install_component_resource_state

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
