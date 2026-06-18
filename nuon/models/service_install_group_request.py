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
        install_ids (list[str] | Unset):
        label_selector (GithubComNuoncoNuonPkgLabelsSelector | Unset):
        order (int | Unset):
        use_for_previews (bool | Unset):
    """

    name: str
    install_ids: list[str] | Unset = UNSET
    label_selector: GithubComNuoncoNuonPkgLabelsSelector | Unset = UNSET
    order: int | Unset = UNSET
    use_for_previews: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        install_ids: list[str] | Unset = UNSET
        if not isinstance(self.install_ids, Unset):
            install_ids = self.install_ids

        label_selector: dict[str, Any] | Unset = UNSET
        if not isinstance(self.label_selector, Unset):
            label_selector = self.label_selector.to_dict()

        order = self.order

        use_for_previews = self.use_for_previews

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if install_ids is not UNSET:
            field_dict["install_ids"] = install_ids
        if label_selector is not UNSET:
            field_dict["label_selector"] = label_selector
        if order is not UNSET:
            field_dict["order"] = order
        if use_for_previews is not UNSET:
            field_dict["use_for_previews"] = use_for_previews

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_nuonco_nuon_pkg_labels_selector import GithubComNuoncoNuonPkgLabelsSelector

        d = dict(src_dict)
        name = d.pop("name")

        install_ids = cast(list[str], d.pop("install_ids", UNSET))

        _label_selector = d.pop("label_selector", UNSET)
        label_selector: GithubComNuoncoNuonPkgLabelsSelector | Unset
        if isinstance(_label_selector, Unset):
            label_selector = UNSET
        else:
            label_selector = GithubComNuoncoNuonPkgLabelsSelector.from_dict(_label_selector)

        order = d.pop("order", UNSET)

        use_for_previews = d.pop("use_for_previews", UNSET)

        service_install_group_request = cls(
            name=name,
            install_ids=install_ids,
            label_selector=label_selector,
            order=order,
            use_for_previews=use_for_previews,
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
