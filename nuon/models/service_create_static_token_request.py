from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceCreateStaticTokenRequest")


@_attrs_define
class ServiceCreateStaticTokenRequest:
    """
    Attributes:
        name (str): human-friendly name to identify the token later
        duration (str | Unset): defaults to one year Default: '8760h'.
        role (str | Unset): org role granted to the token. must be assignable to API tokens; see
            GET /v1/roles?context=api_token. defaults to org_read_only. must be
            empty for personal tokens.
        token_identity (str | Unset): "service_account" (default) creates a dedicated service account with
            the given role; "personal" issues the token against your own account
            and its existing roles, across all your orgs.
    """

    name: str
    duration: str | Unset = "8760h"
    role: str | Unset = UNSET
    token_identity: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        duration = self.duration

        role = self.role

        token_identity = self.token_identity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if duration is not UNSET:
            field_dict["duration"] = duration
        if role is not UNSET:
            field_dict["role"] = role
        if token_identity is not UNSET:
            field_dict["token_identity"] = token_identity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        duration = d.pop("duration", UNSET)

        role = d.pop("role", UNSET)

        token_identity = d.pop("token_identity", UNSET)

        service_create_static_token_request = cls(
            name=name,
            duration=duration,
            role=role,
            token_identity=token_identity,
        )

        service_create_static_token_request.additional_properties = d
        return service_create_static_token_request

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
