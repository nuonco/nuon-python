from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceInstallDeploymentSourceFileContent")


@_attrs_define
class ServiceInstallDeploymentSourceFileContent:
    """
    Attributes:
        after (str | Unset):
        before (str | Unset):
        path (str | Unset):
        unavailable_reason (str | Unset):
    """

    after: str | Unset = UNSET
    before: str | Unset = UNSET
    path: str | Unset = UNSET
    unavailable_reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        after = self.after

        before = self.before

        path = self.path

        unavailable_reason = self.unavailable_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if after is not UNSET:
            field_dict["after"] = after
        if before is not UNSET:
            field_dict["before"] = before
        if path is not UNSET:
            field_dict["path"] = path
        if unavailable_reason is not UNSET:
            field_dict["unavailable_reason"] = unavailable_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        after = d.pop("after", UNSET)

        before = d.pop("before", UNSET)

        path = d.pop("path", UNSET)

        unavailable_reason = d.pop("unavailable_reason", UNSET)

        service_install_deployment_source_file_content = cls(
            after=after,
            before=before,
            path=path,
            unavailable_reason=unavailable_reason,
        )

        service_install_deployment_source_file_content.additional_properties = d
        return service_install_deployment_source_file_content

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
