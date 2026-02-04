from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_user import GithubUser
    from ..models.service_vcs_connection_account import ServiceVCSConnectionAccount
    from ..models.service_vcs_connection_status_response_permissions import (
        ServiceVCSConnectionStatusResponsePermissions,
    )


T = TypeVar("T", bound="ServiceVCSConnectionStatusResponse")


@_attrs_define
class ServiceVCSConnectionStatusResponse:
    """
    Attributes:
        account (ServiceVCSConnectionAccount | Unset):
        checked_at (str | Unset):
        error (str | Unset):
        github_install_id (str | Unset):
        permissions (ServiceVCSConnectionStatusResponsePermissions | Unset):
        repository_selection (str | Unset):
        status (str | Unset):
        suspended_at (str | Unset):
        suspended_by (GithubUser | Unset):
    """

    account: ServiceVCSConnectionAccount | Unset = UNSET
    checked_at: str | Unset = UNSET
    error: str | Unset = UNSET
    github_install_id: str | Unset = UNSET
    permissions: ServiceVCSConnectionStatusResponsePermissions | Unset = UNSET
    repository_selection: str | Unset = UNSET
    status: str | Unset = UNSET
    suspended_at: str | Unset = UNSET
    suspended_by: GithubUser | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account, Unset):
            account = self.account.to_dict()

        checked_at = self.checked_at

        error = self.error

        github_install_id = self.github_install_id

        permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        repository_selection = self.repository_selection

        status = self.status

        suspended_at = self.suspended_at

        suspended_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.suspended_by, Unset):
            suspended_by = self.suspended_by.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account is not UNSET:
            field_dict["account"] = account
        if checked_at is not UNSET:
            field_dict["checked_at"] = checked_at
        if error is not UNSET:
            field_dict["error"] = error
        if github_install_id is not UNSET:
            field_dict["github_install_id"] = github_install_id
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if repository_selection is not UNSET:
            field_dict["repository_selection"] = repository_selection
        if status is not UNSET:
            field_dict["status"] = status
        if suspended_at is not UNSET:
            field_dict["suspended_at"] = suspended_at
        if suspended_by is not UNSET:
            field_dict["suspended_by"] = suspended_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_user import GithubUser
        from ..models.service_vcs_connection_account import ServiceVCSConnectionAccount
        from ..models.service_vcs_connection_status_response_permissions import (
            ServiceVCSConnectionStatusResponsePermissions,
        )

        d = dict(src_dict)
        _account = d.pop("account", UNSET)
        account: ServiceVCSConnectionAccount | Unset
        if isinstance(_account, Unset):
            account = UNSET
        else:
            account = ServiceVCSConnectionAccount.from_dict(_account)

        checked_at = d.pop("checked_at", UNSET)

        error = d.pop("error", UNSET)

        github_install_id = d.pop("github_install_id", UNSET)

        _permissions = d.pop("permissions", UNSET)
        permissions: ServiceVCSConnectionStatusResponsePermissions | Unset
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = ServiceVCSConnectionStatusResponsePermissions.from_dict(_permissions)

        repository_selection = d.pop("repository_selection", UNSET)

        status = d.pop("status", UNSET)

        suspended_at = d.pop("suspended_at", UNSET)

        _suspended_by = d.pop("suspended_by", UNSET)
        suspended_by: GithubUser | Unset
        if isinstance(_suspended_by, Unset):
            suspended_by = UNSET
        else:
            suspended_by = GithubUser.from_dict(_suspended_by)

        service_vcs_connection_status_response = cls(
            account=account,
            checked_at=checked_at,
            error=error,
            github_install_id=github_install_id,
            permissions=permissions,
            repository_selection=repository_selection,
            status=status,
            suspended_at=suspended_at,
            suspended_by=suspended_by,
        )

        service_vcs_connection_status_response.additional_properties = d
        return service_vcs_connection_status_response

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
