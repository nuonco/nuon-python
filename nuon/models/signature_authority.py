from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.signature_authority_type import SignatureAuthorityType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SignatureAuthority")


@_attrs_define
class SignatureAuthority:
    """
    Attributes:
        issuer (str | Unset):
        public_key (str | Unset):
        subject (str | Unset):
        subject_regexp (str | Unset):
        type_ (SignatureAuthorityType | Unset):
    """

    issuer: str | Unset = UNSET
    public_key: str | Unset = UNSET
    subject: str | Unset = UNSET
    subject_regexp: str | Unset = UNSET
    type_: SignatureAuthorityType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issuer = self.issuer

        public_key = self.public_key

        subject = self.subject

        subject_regexp = self.subject_regexp

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if issuer is not UNSET:
            field_dict["issuer"] = issuer
        if public_key is not UNSET:
            field_dict["public_key"] = public_key
        if subject is not UNSET:
            field_dict["subject"] = subject
        if subject_regexp is not UNSET:
            field_dict["subject_regexp"] = subject_regexp
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        issuer = d.pop("issuer", UNSET)

        public_key = d.pop("public_key", UNSET)

        subject = d.pop("subject", UNSET)

        subject_regexp = d.pop("subject_regexp", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: SignatureAuthorityType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = SignatureAuthorityType(_type_)

        signature_authority = cls(
            issuer=issuer,
            public_key=public_key,
            subject=subject,
            subject_regexp=subject_regexp,
            type_=type_,
        )

        signature_authority.additional_properties = d
        return signature_authority

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
