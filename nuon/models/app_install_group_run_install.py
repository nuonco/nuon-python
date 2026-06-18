from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppInstallGroupRunInstall")


@_attrs_define
class AppInstallGroupRunInstall:
    """
    Attributes:
        install_id (str | Unset):
        status (str | Unset):
        workflow_id (str | Unset):
    """

    install_id: str | Unset = UNSET
    status: str | Unset = UNSET
    workflow_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        install_id = self.install_id

        status = self.status

        workflow_id = self.workflow_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if status is not UNSET:
            field_dict["status"] = status
        if workflow_id is not UNSET:
            field_dict["workflow_id"] = workflow_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        install_id = d.pop("install_id", UNSET)

        status = d.pop("status", UNSET)

        workflow_id = d.pop("workflow_id", UNSET)

        app_install_group_run_install = cls(
            install_id=install_id,
            status=status,
            workflow_id=workflow_id,
        )

        app_install_group_run_install.additional_properties = d
        return app_install_group_run_install

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
