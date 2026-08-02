from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_oidc_trust_policy_claim_conditions import AppOIDCTrustPolicyClaimConditions


T = TypeVar("T", bound="AppOIDCTrustPolicy")


@_attrs_define
class AppOIDCTrustPolicy:
    """
    Attributes:
        audience (str | Unset):
        claim_conditions (AppOIDCTrustPolicyClaimConditions | Unset): ClaimConditions maps claim names to patterns. All
            conditions must match
            for the policy to apply. Patterns are exact strings, or globs where `*`
            does not cross `:` segments.
        created_at (str | Unset):
        created_by_id (str | Unset):
        enabled (bool | Unset):
        id (str | Unset):
        issuer_url (str | Unset): IssuerURL is the exact `iss` claim value and the base URL used for OIDC
            discovery + JWKS fetching. It is always the stored, admin-configured
            value — never taken from the presented token.
        last_used_at (str | Unset):
        name (str | Unset):
        org_id (str | Unset):
        role (str | Unset):
        service_account_id (str | Unset):
        token_duration_seconds (int | Unset):
        updated_at (str | Unset):
    """

    audience: str | Unset = UNSET
    claim_conditions: AppOIDCTrustPolicyClaimConditions | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    id: str | Unset = UNSET
    issuer_url: str | Unset = UNSET
    last_used_at: str | Unset = UNSET
    name: str | Unset = UNSET
    org_id: str | Unset = UNSET
    role: str | Unset = UNSET
    service_account_id: str | Unset = UNSET
    token_duration_seconds: int | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audience = self.audience

        claim_conditions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.claim_conditions, Unset):
            claim_conditions = self.claim_conditions.to_dict()

        created_at = self.created_at

        created_by_id = self.created_by_id

        enabled = self.enabled

        id = self.id

        issuer_url = self.issuer_url

        last_used_at = self.last_used_at

        name = self.name

        org_id = self.org_id

        role = self.role

        service_account_id = self.service_account_id

        token_duration_seconds = self.token_duration_seconds

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if audience is not UNSET:
            field_dict["audience"] = audience
        if claim_conditions is not UNSET:
            field_dict["claim_conditions"] = claim_conditions
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if id is not UNSET:
            field_dict["id"] = id
        if issuer_url is not UNSET:
            field_dict["issuer_url"] = issuer_url
        if last_used_at is not UNSET:
            field_dict["last_used_at"] = last_used_at
        if name is not UNSET:
            field_dict["name"] = name
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if role is not UNSET:
            field_dict["role"] = role
        if service_account_id is not UNSET:
            field_dict["service_account_id"] = service_account_id
        if token_duration_seconds is not UNSET:
            field_dict["token_duration_seconds"] = token_duration_seconds
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_oidc_trust_policy_claim_conditions import AppOIDCTrustPolicyClaimConditions

        d = dict(src_dict)
        audience = d.pop("audience", UNSET)

        _claim_conditions = d.pop("claim_conditions", UNSET)
        claim_conditions: AppOIDCTrustPolicyClaimConditions | Unset
        if isinstance(_claim_conditions, Unset):
            claim_conditions = UNSET
        else:
            claim_conditions = AppOIDCTrustPolicyClaimConditions.from_dict(_claim_conditions)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        enabled = d.pop("enabled", UNSET)

        id = d.pop("id", UNSET)

        issuer_url = d.pop("issuer_url", UNSET)

        last_used_at = d.pop("last_used_at", UNSET)

        name = d.pop("name", UNSET)

        org_id = d.pop("org_id", UNSET)

        role = d.pop("role", UNSET)

        service_account_id = d.pop("service_account_id", UNSET)

        token_duration_seconds = d.pop("token_duration_seconds", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_oidc_trust_policy = cls(
            audience=audience,
            claim_conditions=claim_conditions,
            created_at=created_at,
            created_by_id=created_by_id,
            enabled=enabled,
            id=id,
            issuer_url=issuer_url,
            last_used_at=last_used_at,
            name=name,
            org_id=org_id,
            role=role,
            service_account_id=service_account_id,
            token_duration_seconds=token_duration_seconds,
            updated_at=updated_at,
        )

        app_oidc_trust_policy.additional_properties = d
        return app_oidc_trust_policy

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
