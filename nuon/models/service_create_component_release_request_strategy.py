from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceCreateComponentReleaseRequestStrategy")


@_attrs_define
class ServiceCreateComponentReleaseRequestStrategy:
    """
    Attributes:
        delay (Union[Unset, str]):
        installs_per_step (Union[Unset, int]):
    """

    delay: Union[Unset, str] = UNSET
    installs_per_step: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delay = self.delay

        installs_per_step = self.installs_per_step

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delay is not UNSET:
            field_dict["delay"] = delay
        if installs_per_step is not UNSET:
            field_dict["installs_per_step"] = installs_per_step

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delay = d.pop("delay", UNSET)

        installs_per_step = d.pop("installs_per_step", UNSET)

        service_create_component_release_request_strategy = cls(
            delay=delay,
            installs_per_step=installs_per_step,
        )

        service_create_component_release_request_strategy.additional_properties = d
        return service_create_component_release_request_strategy

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
