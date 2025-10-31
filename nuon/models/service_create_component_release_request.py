from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_create_component_release_request_strategy import ServiceCreateComponentReleaseRequestStrategy


T = TypeVar("T", bound="ServiceCreateComponentReleaseRequest")


@_attrs_define
class ServiceCreateComponentReleaseRequest:
    """
    Attributes:
        auto_build (bool | Unset):
        build_id (str | Unset):
        install_ids (list[str] | Unset):
        strategy (ServiceCreateComponentReleaseRequestStrategy | Unset):
    """

    auto_build: bool | Unset = UNSET
    build_id: str | Unset = UNSET
    install_ids: list[str] | Unset = UNSET
    strategy: ServiceCreateComponentReleaseRequestStrategy | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_build = self.auto_build

        build_id = self.build_id

        install_ids: list[str] | Unset = UNSET
        if not isinstance(self.install_ids, Unset):
            install_ids = self.install_ids

        strategy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.strategy, Unset):
            strategy = self.strategy.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_build is not UNSET:
            field_dict["auto_build"] = auto_build
        if build_id is not UNSET:
            field_dict["build_id"] = build_id
        if install_ids is not UNSET:
            field_dict["install_ids"] = install_ids
        if strategy is not UNSET:
            field_dict["strategy"] = strategy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_create_component_release_request_strategy import (
            ServiceCreateComponentReleaseRequestStrategy,
        )

        d = dict(src_dict)
        auto_build = d.pop("auto_build", UNSET)

        build_id = d.pop("build_id", UNSET)

        install_ids = cast(list[str], d.pop("install_ids", UNSET))

        _strategy = d.pop("strategy", UNSET)
        strategy: ServiceCreateComponentReleaseRequestStrategy | Unset
        if isinstance(_strategy, Unset):
            strategy = UNSET
        else:
            strategy = ServiceCreateComponentReleaseRequestStrategy.from_dict(_strategy)

        service_create_component_release_request = cls(
            auto_build=auto_build,
            build_id=build_id,
            install_ids=install_ids,
            strategy=strategy,
        )

        service_create_component_release_request.additional_properties = d
        return service_create_component_release_request

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
