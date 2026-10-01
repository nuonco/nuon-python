from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_nuonco_nuon_pkg_labels_selector import GithubComNuoncoNuonPkgLabelsSelector


T = TypeVar("T", bound="ServiceInstallGroupRequest")


@_attrs_define
class ServiceInstallGroupRequest:
    """
    Attributes:
        name (str):
        auto_approve_on_policies_passing (bool | None | Unset): AutoApproveOnPoliciesPassing approves this group's plan
            step without user
            input when its policy checks pass. Omit to leave it unset (off).
        default (bool | Unset):
        label_selector (GithubComNuoncoNuonPkgLabelsSelector | Unset):
        order (int | Unset):
    """

    name: str
    auto_approve_on_policies_passing: bool | None | Unset = UNSET
    default: bool | Unset = UNSET
    label_selector: GithubComNuoncoNuonPkgLabelsSelector | Unset = UNSET
    order: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        auto_approve_on_policies_passing: bool | None | Unset
        if isinstance(self.auto_approve_on_policies_passing, Unset):
            auto_approve_on_policies_passing = UNSET
        else:
            auto_approve_on_policies_passing = self.auto_approve_on_policies_passing

        default = self.default

        label_selector: dict[str, Any] | Unset = UNSET
        if not isinstance(self.label_selector, Unset):
            label_selector = self.label_selector.to_dict()

        order = self.order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if auto_approve_on_policies_passing is not UNSET:
            field_dict["auto_approve_on_policies_passing"] = auto_approve_on_policies_passing
        if default is not UNSET:
            field_dict["default"] = default
        if label_selector is not UNSET:
            field_dict["label_selector"] = label_selector
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_nuonco_nuon_pkg_labels_selector import (
            GithubComNuoncoNuonPkgLabelsSelector,  # noqa: PLC0415
        )

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_auto_approve_on_policies_passing(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        auto_approve_on_policies_passing = _parse_auto_approve_on_policies_passing(
            d.pop("auto_approve_on_policies_passing", UNSET)
        )

        default = d.pop("default", UNSET)

        _label_selector = d.pop("label_selector", UNSET)
        label_selector: GithubComNuoncoNuonPkgLabelsSelector | Unset
        if isinstance(_label_selector, Unset):
            label_selector = UNSET
        else:
            label_selector = GithubComNuoncoNuonPkgLabelsSelector.from_dict(_label_selector)

        order = d.pop("order", UNSET)

        service_install_group_request = cls(
            name=name,
            auto_approve_on_policies_passing=auto_approve_on_policies_passing,
            default=default,
            label_selector=label_selector,
            order=order,
        )

        service_install_group_request.additional_properties = d
        return service_install_group_request

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
