from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceInstallDeploymentImage")


@_attrs_define
class ServiceInstallDeploymentImage:
    """
    Attributes:
        next_tag (str | Unset):
        previous_tag (str | Unset):
        repository (str | Unset):
    """

    next_tag: str | Unset = UNSET
    previous_tag: str | Unset = UNSET
    repository: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        next_tag = self.next_tag

        previous_tag = self.previous_tag

        repository = self.repository

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if next_tag is not UNSET:
            field_dict["next_tag"] = next_tag
        if previous_tag is not UNSET:
            field_dict["previous_tag"] = previous_tag
        if repository is not UNSET:
            field_dict["repository"] = repository

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        next_tag = d.pop("next_tag", UNSET)

        previous_tag = d.pop("previous_tag", UNSET)

        repository = d.pop("repository", UNSET)

        service_install_deployment_image = cls(
            next_tag=next_tag,
            previous_tag=previous_tag,
            repository=repository,
        )

        service_install_deployment_image.additional_properties = d
        return service_install_deployment_image

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
