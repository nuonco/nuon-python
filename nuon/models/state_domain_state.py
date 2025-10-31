from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StateDomainState")


@_attrs_define
class StateDomainState:
    """
    Attributes:
        internal_domain (str | Unset):
        populated (bool | Unset):
        public_domain (str | Unset):
    """

    internal_domain: str | Unset = UNSET
    populated: bool | Unset = UNSET
    public_domain: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        internal_domain = self.internal_domain

        populated = self.populated

        public_domain = self.public_domain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if internal_domain is not UNSET:
            field_dict["internal_domain"] = internal_domain
        if populated is not UNSET:
            field_dict["populated"] = populated
        if public_domain is not UNSET:
            field_dict["public_domain"] = public_domain

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        internal_domain = d.pop("internal_domain", UNSET)

        populated = d.pop("populated", UNSET)

        public_domain = d.pop("public_domain", UNSET)

        state_domain_state = cls(
            internal_domain=internal_domain,
            populated=populated,
            public_domain=public_domain,
        )

        state_domain_state.additional_properties = d
        return state_domain_state

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
