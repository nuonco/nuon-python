from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceUpdateAppBranchConfigRequest")


@_attrs_define
class ServiceUpdateAppBranchConfigRequest:
    """
    Attributes:
        ignore_changes_regex (None | str | Unset): IgnoreChangesRegex marks a run not-attempted when every changed file
            path in
            it matches this RE2 pattern. Send an empty string to clear it.
        send_statuses_on_ignore (bool | None | Unset): SendStatusesOnIgnore posts a successful commit status for ignored
            runs.
    """

    ignore_changes_regex: None | str | Unset = UNSET
    send_statuses_on_ignore: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ignore_changes_regex: None | str | Unset
        if isinstance(self.ignore_changes_regex, Unset):
            ignore_changes_regex = UNSET
        else:
            ignore_changes_regex = self.ignore_changes_regex

        send_statuses_on_ignore: bool | None | Unset
        if isinstance(self.send_statuses_on_ignore, Unset):
            send_statuses_on_ignore = UNSET
        else:
            send_statuses_on_ignore = self.send_statuses_on_ignore

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ignore_changes_regex is not UNSET:
            field_dict["ignore_changes_regex"] = ignore_changes_regex
        if send_statuses_on_ignore is not UNSET:
            field_dict["send_statuses_on_ignore"] = send_statuses_on_ignore

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_ignore_changes_regex(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ignore_changes_regex = _parse_ignore_changes_regex(d.pop("ignore_changes_regex", UNSET))

        def _parse_send_statuses_on_ignore(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        send_statuses_on_ignore = _parse_send_statuses_on_ignore(d.pop("send_statuses_on_ignore", UNSET))

        service_update_app_branch_config_request = cls(
            ignore_changes_regex=ignore_changes_regex,
            send_statuses_on_ignore=send_statuses_on_ignore,
        )

        service_update_app_branch_config_request.additional_properties = d
        return service_update_app_branch_config_request

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
