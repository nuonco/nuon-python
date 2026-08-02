from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_update_oidc_trust_policy_request_claim_conditions import (
        ServiceUpdateOIDCTrustPolicyRequestClaimConditions,
    )


T = TypeVar("T", bound="ServiceUpdateOIDCTrustPolicyRequest")


@_attrs_define
class ServiceUpdateOIDCTrustPolicyRequest:
    """
    Attributes:
        audience (str | Unset):
        claim_conditions (ServiceUpdateOIDCTrustPolicyRequestClaimConditions | Unset):
        enabled (bool | None | Unset):
        issuer_url (str | Unset):
        name (str | Unset):
        role (str | Unset):
        token_duration_seconds (int | Unset):
    """

    audience: str | Unset = UNSET
    claim_conditions: ServiceUpdateOIDCTrustPolicyRequestClaimConditions | Unset = UNSET
    enabled: bool | None | Unset = UNSET
    issuer_url: str | Unset = UNSET
    name: str | Unset = UNSET
    role: str | Unset = UNSET
    token_duration_seconds: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audience = self.audience

        claim_conditions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.claim_conditions, Unset):
            claim_conditions = self.claim_conditions.to_dict()

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        issuer_url = self.issuer_url

        name = self.name

        role = self.role

        token_duration_seconds = self.token_duration_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if audience is not UNSET:
            field_dict["audience"] = audience
        if claim_conditions is not UNSET:
            field_dict["claim_conditions"] = claim_conditions
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if issuer_url is not UNSET:
            field_dict["issuer_url"] = issuer_url
        if name is not UNSET:
            field_dict["name"] = name
        if role is not UNSET:
            field_dict["role"] = role
        if token_duration_seconds is not UNSET:
            field_dict["token_duration_seconds"] = token_duration_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_update_oidc_trust_policy_request_claim_conditions import (
            ServiceUpdateOIDCTrustPolicyRequestClaimConditions,
        )

        d = dict(src_dict)
        audience = d.pop("audience", UNSET)

        _claim_conditions = d.pop("claim_conditions", UNSET)
        claim_conditions: ServiceUpdateOIDCTrustPolicyRequestClaimConditions | Unset
        if isinstance(_claim_conditions, Unset):
            claim_conditions = UNSET
        else:
            claim_conditions = ServiceUpdateOIDCTrustPolicyRequestClaimConditions.from_dict(_claim_conditions)

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        issuer_url = d.pop("issuer_url", UNSET)

        name = d.pop("name", UNSET)

        role = d.pop("role", UNSET)

        token_duration_seconds = d.pop("token_duration_seconds", UNSET)

        service_update_oidc_trust_policy_request = cls(
            audience=audience,
            claim_conditions=claim_conditions,
            enabled=enabled,
            issuer_url=issuer_url,
            name=name,
            role=role,
            token_duration_seconds=token_duration_seconds,
        )

        service_update_oidc_trust_policy_request.additional_properties = d
        return service_update_oidc_trust_policy_request

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
