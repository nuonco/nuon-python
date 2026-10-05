from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.signature_authority import SignatureAuthority


T = TypeVar("T", bound="SignatureVerification")


@_attrs_define
class SignatureVerification:
    """
    Attributes:
        authorities (list[SignatureAuthority] | Unset):
        require_signature (bool | Unset):
    """

    authorities: list[SignatureAuthority] | Unset = UNSET
    require_signature: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authorities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.authorities, Unset):
            authorities = []
            for authorities_item_data in self.authorities:
                authorities_item = authorities_item_data.to_dict()
                authorities.append(authorities_item)

        require_signature = self.require_signature

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authorities is not UNSET:
            field_dict["authorities"] = authorities
        if require_signature is not UNSET:
            field_dict["require_signature"] = require_signature

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.signature_authority import SignatureAuthority  # noqa: PLC0415

        d = dict(src_dict)
        _authorities = d.pop("authorities", UNSET)
        authorities: list[SignatureAuthority] | Unset = UNSET
        if _authorities is not UNSET:
            authorities = []
            for authorities_item_data in _authorities:
                authorities_item = SignatureAuthority.from_dict(authorities_item_data)

                authorities.append(authorities_item)

        require_signature = d.pop("require_signature", UNSET)

        signature_verification = cls(
            authorities=authorities,
            require_signature=require_signature,
        )

        signature_verification.additional_properties = d
        return signature_verification

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
