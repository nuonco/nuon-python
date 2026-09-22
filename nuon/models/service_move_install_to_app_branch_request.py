from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServiceMoveInstallToAppBranchRequest")


@_attrs_define
class ServiceMoveInstallToAppBranchRequest:
    """
    Attributes:
        app_branch_id (str): AppBranchID is the branch to move the install to. It must belong to the
            install's app and have an app config to deploy.
    """

    app_branch_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_branch_id = self.app_branch_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app_branch_id": app_branch_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_branch_id = d.pop("app_branch_id")

        service_move_install_to_app_branch_request = cls(
            app_branch_id=app_branch_id,
        )

        service_move_install_to_app_branch_request.additional_properties = d
        return service_move_install_to_app_branch_request

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
