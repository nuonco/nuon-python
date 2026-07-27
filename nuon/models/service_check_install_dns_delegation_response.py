from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceCheckInstallDNSDelegationResponse")


@_attrs_define
class ServiceCheckInstallDNSDelegationResponse:
    """
    Attributes:
        delegated (bool | Unset):
        domain (str | Unset):
        enabled (bool | Unset):
        expected_nameservers (list[str] | Unset):
        extra_nameservers (list[str] | Unset):
        message (str | Unset):
        missing_nameservers (list[str] | Unset):
        observed_nameservers (list[str] | Unset):
    """

    delegated: bool | Unset = UNSET
    domain: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    expected_nameservers: list[str] | Unset = UNSET
    extra_nameservers: list[str] | Unset = UNSET
    message: str | Unset = UNSET
    missing_nameservers: list[str] | Unset = UNSET
    observed_nameservers: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delegated = self.delegated

        domain = self.domain

        enabled = self.enabled

        expected_nameservers: list[str] | Unset = UNSET
        if not isinstance(self.expected_nameservers, Unset):
            expected_nameservers = self.expected_nameservers

        extra_nameservers: list[str] | Unset = UNSET
        if not isinstance(self.extra_nameservers, Unset):
            extra_nameservers = self.extra_nameservers

        message = self.message

        missing_nameservers: list[str] | Unset = UNSET
        if not isinstance(self.missing_nameservers, Unset):
            missing_nameservers = self.missing_nameservers

        observed_nameservers: list[str] | Unset = UNSET
        if not isinstance(self.observed_nameservers, Unset):
            observed_nameservers = self.observed_nameservers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delegated is not UNSET:
            field_dict["delegated"] = delegated
        if domain is not UNSET:
            field_dict["domain"] = domain
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if expected_nameservers is not UNSET:
            field_dict["expected_nameservers"] = expected_nameservers
        if extra_nameservers is not UNSET:
            field_dict["extra_nameservers"] = extra_nameservers
        if message is not UNSET:
            field_dict["message"] = message
        if missing_nameservers is not UNSET:
            field_dict["missing_nameservers"] = missing_nameservers
        if observed_nameservers is not UNSET:
            field_dict["observed_nameservers"] = observed_nameservers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delegated = d.pop("delegated", UNSET)

        domain = d.pop("domain", UNSET)

        enabled = d.pop("enabled", UNSET)

        expected_nameservers = cast(list[str], d.pop("expected_nameservers", UNSET))

        extra_nameservers = cast(list[str], d.pop("extra_nameservers", UNSET))

        message = d.pop("message", UNSET)

        missing_nameservers = cast(list[str], d.pop("missing_nameservers", UNSET))

        observed_nameservers = cast(list[str], d.pop("observed_nameservers", UNSET))

        service_check_install_dns_delegation_response = cls(
            delegated=delegated,
            domain=domain,
            enabled=enabled,
            expected_nameservers=expected_nameservers,
            extra_nameservers=extra_nameservers,
            message=message,
            missing_nameservers=missing_nameservers,
            observed_nameservers=observed_nameservers,
        )

        service_check_install_dns_delegation_response.additional_properties = d
        return service_check_install_dns_delegation_response

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
