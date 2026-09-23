from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_install import AppInstall


T = TypeVar("T", bound="ServicePreviewInstallCandidatesResponse")


@_attrs_define
class ServicePreviewInstallCandidatesResponse:
    """
    Attributes:
        installs (list[AppInstall] | Unset):
    """

    installs: list[AppInstall] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        installs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.installs, Unset):
            installs = []
            for installs_item_data in self.installs:
                installs_item = installs_item_data.to_dict()
                installs.append(installs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if installs is not UNSET:
            field_dict["installs"] = installs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_install import AppInstall  # noqa: PLC0415

        d = dict(src_dict)
        _installs = d.pop("installs", UNSET)
        installs: list[AppInstall] | Unset = UNSET
        if _installs is not UNSET:
            installs = []
            for installs_item_data in _installs:
                installs_item = AppInstall.from_dict(installs_item_data)

                installs.append(installs_item)

        service_preview_install_candidates_response = cls(
            installs=installs,
        )

        service_preview_install_candidates_response.additional_properties = d
        return service_preview_install_candidates_response

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
