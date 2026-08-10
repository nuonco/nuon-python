from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_create_oidc_trust_policy_request_claim_conditions import (
        ServiceCreateOIDCTrustPolicyRequestClaimConditions,
    )


T = TypeVar("T", bound="ServiceCreateOIDCTrustPolicyRequest")


@_attrs_define
class ServiceCreateOIDCTrustPolicyRequest:
    """
    Attributes:
        audience (str): expected `aud` claim value
        claim_conditions (ServiceCreateOIDCTrustPolicyRequestClaimConditions): map of claim name -> pattern; all must
            match. A `sub` condition is
            required. Patterns are exact strings or globs where `*` cannot cross
            `:` segments.
        issuer_url (str): exact `iss` claim value; also used for OIDC discovery + JWKS fetching
        name (str): human-friendly name to identify the policy
        role (str | Unset): org role granted to exchanged tokens. must be assignable to trust
            policies; see GET /v1/roles?context=oidc_trust_policy. defaults to
            org_read_only.
        token_duration_seconds (int | Unset): lifetime of exchanged tokens in seconds. defaults to 3600, max 86400.
    """

    audience: str
    claim_conditions: ServiceCreateOIDCTrustPolicyRequestClaimConditions
    issuer_url: str
    name: str
    role: str | Unset = UNSET
    token_duration_seconds: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audience = self.audience

        claim_conditions = self.claim_conditions.to_dict()

        issuer_url = self.issuer_url

        name = self.name

        role = self.role

        token_duration_seconds = self.token_duration_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "audience": audience,
                "claim_conditions": claim_conditions,
                "issuer_url": issuer_url,
                "name": name,
            }
        )
        if role is not UNSET:
            field_dict["role"] = role
        if token_duration_seconds is not UNSET:
            field_dict["token_duration_seconds"] = token_duration_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_create_oidc_trust_policy_request_claim_conditions import (
            ServiceCreateOIDCTrustPolicyRequestClaimConditions,
        )

        d = dict(src_dict)
        audience = d.pop("audience")

        claim_conditions = ServiceCreateOIDCTrustPolicyRequestClaimConditions.from_dict(d.pop("claim_conditions"))

        issuer_url = d.pop("issuer_url")

        name = d.pop("name")

        role = d.pop("role", UNSET)

        token_duration_seconds = d.pop("token_duration_seconds", UNSET)

        service_create_oidc_trust_policy_request = cls(
            audience=audience,
            claim_conditions=claim_conditions,
            issuer_url=issuer_url,
            name=name,
            role=role,
            token_duration_seconds=token_duration_seconds,
        )

        service_create_oidc_trust_policy_request.additional_properties = d
        return service_create_oidc_trust_policy_request

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
