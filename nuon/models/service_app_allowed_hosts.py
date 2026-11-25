from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_app_allowed_hosts_categories import ServiceAppAllowedHostsCategories


T = TypeVar("T", bound="ServiceAppAllowedHosts")


@_attrs_define
class ServiceAppAllowedHosts:
    """
    Attributes:
        categories (ServiceAppAllowedHostsCategories | Unset):
        mode (str | Unset):
    """

    categories: ServiceAppAllowedHostsCategories | Unset = UNSET
    mode: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        categories: dict[str, Any] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories.to_dict()

        mode = self.mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if categories is not UNSET:
            field_dict["categories"] = categories
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_app_allowed_hosts_categories import ServiceAppAllowedHostsCategories  # noqa: PLC0415

        d = dict(src_dict)
        _categories = d.pop("categories", UNSET)
        categories: ServiceAppAllowedHostsCategories | Unset
        if isinstance(_categories, Unset):
            categories = UNSET
        else:
            categories = ServiceAppAllowedHostsCategories.from_dict(_categories)

        mode = d.pop("mode", UNSET)

        service_app_allowed_hosts = cls(
            categories=categories,
            mode=mode,
        )

        service_app_allowed_hosts.additional_properties = d
        return service_app_allowed_hosts

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
