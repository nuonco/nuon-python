from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppInstallAuditLog")


@_attrs_define
class AppInstallAuditLog:
    """
    Attributes:
        install_id (str | Unset):
        log_line (str | Unset):
        time_stamp (str | Unset):
        type_ (str | Unset):
    """

    install_id: str | Unset = UNSET
    log_line: str | Unset = UNSET
    time_stamp: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        install_id = self.install_id

        log_line = self.log_line

        time_stamp = self.time_stamp

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if log_line is not UNSET:
            field_dict["log_line"] = log_line
        if time_stamp is not UNSET:
            field_dict["time_stamp"] = time_stamp
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        install_id = d.pop("install_id", UNSET)

        log_line = d.pop("log_line", UNSET)

        time_stamp = d.pop("time_stamp", UNSET)

        type_ = d.pop("type", UNSET)

        app_install_audit_log = cls(
            install_id=install_id,
            log_line=log_line,
            time_stamp=time_stamp,
            type_=type_,
        )

        app_install_audit_log.additional_properties = d
        return app_install_audit_log

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
