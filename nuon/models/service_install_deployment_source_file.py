from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_install_deployment_source_file_change import ServiceInstallDeploymentSourceFileChange
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceInstallDeploymentSourceFile")


@_attrs_define
class ServiceInstallDeploymentSourceFile:
    """
    Attributes:
        after_executable (bool | Unset):
        before_executable (bool | Unset):
        change (ServiceInstallDeploymentSourceFileChange | Unset):
        path (str | Unset):
    """

    after_executable: bool | Unset = UNSET
    before_executable: bool | Unset = UNSET
    change: ServiceInstallDeploymentSourceFileChange | Unset = UNSET
    path: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        after_executable = self.after_executable

        before_executable = self.before_executable

        change: str | Unset = UNSET
        if not isinstance(self.change, Unset):
            change = self.change.value

        path = self.path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if after_executable is not UNSET:
            field_dict["after_executable"] = after_executable
        if before_executable is not UNSET:
            field_dict["before_executable"] = before_executable
        if change is not UNSET:
            field_dict["change"] = change
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        after_executable = d.pop("after_executable", UNSET)

        before_executable = d.pop("before_executable", UNSET)

        _change = d.pop("change", UNSET)
        change: ServiceInstallDeploymentSourceFileChange | Unset
        if isinstance(_change, Unset):
            change = UNSET
        else:
            change = ServiceInstallDeploymentSourceFileChange(_change)

        path = d.pop("path", UNSET)

        service_install_deployment_source_file = cls(
            after_executable=after_executable,
            before_executable=before_executable,
            change=change,
            path=path,
        )

        service_install_deployment_source_file.additional_properties = d
        return service_install_deployment_source_file

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
