from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_cloud_connection_preset import AppCloudConnectionPreset
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_setup_response_permissions_policy import ServiceSetupResponsePermissionsPolicy
    from ..models.service_setup_response_trust_policy import ServiceSetupResponseTrustPolicy


T = TypeVar("T", bound="ServiceSetupResponse")


@_attrs_define
class ServiceSetupResponse:
    """
    Attributes:
        audience (str | Unset):
        cli (str | Unset):
        cloudformation (str | Unset):
        issuer_url (str | Unset):
        permissions_policy (ServiceSetupResponsePermissionsPolicy | Unset):
        preset (AppCloudConnectionPreset | Unset):
        subject (str | Unset):
        terraform (str | Unset):
        trust_policy (ServiceSetupResponseTrustPolicy | Unset):
    """

    audience: str | Unset = UNSET
    cli: str | Unset = UNSET
    cloudformation: str | Unset = UNSET
    issuer_url: str | Unset = UNSET
    permissions_policy: ServiceSetupResponsePermissionsPolicy | Unset = UNSET
    preset: AppCloudConnectionPreset | Unset = UNSET
    subject: str | Unset = UNSET
    terraform: str | Unset = UNSET
    trust_policy: ServiceSetupResponseTrustPolicy | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audience = self.audience

        cli = self.cli

        cloudformation = self.cloudformation

        issuer_url = self.issuer_url

        permissions_policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.permissions_policy, Unset):
            permissions_policy = self.permissions_policy.to_dict()

        preset: str | Unset = UNSET
        if not isinstance(self.preset, Unset):
            preset = self.preset.value

        subject = self.subject

        terraform = self.terraform

        trust_policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trust_policy, Unset):
            trust_policy = self.trust_policy.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if audience is not UNSET:
            field_dict["audience"] = audience
        if cli is not UNSET:
            field_dict["cli"] = cli
        if cloudformation is not UNSET:
            field_dict["cloudformation"] = cloudformation
        if issuer_url is not UNSET:
            field_dict["issuer_url"] = issuer_url
        if permissions_policy is not UNSET:
            field_dict["permissions_policy"] = permissions_policy
        if preset is not UNSET:
            field_dict["preset"] = preset
        if subject is not UNSET:
            field_dict["subject"] = subject
        if terraform is not UNSET:
            field_dict["terraform"] = terraform
        if trust_policy is not UNSET:
            field_dict["trust_policy"] = trust_policy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_setup_response_permissions_policy import (
            ServiceSetupResponsePermissionsPolicy,  # noqa: PLC0415
        )
        from ..models.service_setup_response_trust_policy import ServiceSetupResponseTrustPolicy  # noqa: PLC0415

        d = dict(src_dict)
        audience = d.pop("audience", UNSET)

        cli = d.pop("cli", UNSET)

        cloudformation = d.pop("cloudformation", UNSET)

        issuer_url = d.pop("issuer_url", UNSET)

        _permissions_policy = d.pop("permissions_policy", UNSET)
        permissions_policy: ServiceSetupResponsePermissionsPolicy | Unset
        if isinstance(_permissions_policy, Unset):
            permissions_policy = UNSET
        else:
            permissions_policy = ServiceSetupResponsePermissionsPolicy.from_dict(_permissions_policy)

        _preset = d.pop("preset", UNSET)
        preset: AppCloudConnectionPreset | Unset
        if isinstance(_preset, Unset):
            preset = UNSET
        else:
            preset = AppCloudConnectionPreset(_preset)

        subject = d.pop("subject", UNSET)

        terraform = d.pop("terraform", UNSET)

        _trust_policy = d.pop("trust_policy", UNSET)
        trust_policy: ServiceSetupResponseTrustPolicy | Unset
        if isinstance(_trust_policy, Unset):
            trust_policy = UNSET
        else:
            trust_policy = ServiceSetupResponseTrustPolicy.from_dict(_trust_policy)

        service_setup_response = cls(
            audience=audience,
            cli=cli,
            cloudformation=cloudformation,
            issuer_url=issuer_url,
            permissions_policy=permissions_policy,
            preset=preset,
            subject=subject,
            terraform=terraform,
            trust_policy=trust_policy,
        )

        service_setup_response.additional_properties = d
        return service_setup_response

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
