from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceCreateAppConfigRequest")


@_attrs_define
class ServiceCreateAppConfigRequest:
    """
    Attributes:
        app_branch_id (str | Unset): AppBranchID optionally links this config to an app branch.
            When set, triggers an app branch run after sync.
        cli_version (str | Unset):
        plan_only (bool | Unset): PlanOnly creates a preview run (plan without apply). Only used with AppBranchID.
        readme (str | Unset): not required Readme
    """

    app_branch_id: str | Unset = UNSET
    cli_version: str | Unset = UNSET
    plan_only: bool | Unset = UNSET
    readme: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_branch_id = self.app_branch_id

        cli_version = self.cli_version

        plan_only = self.plan_only

        readme = self.readme

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_branch_id is not UNSET:
            field_dict["app_branch_id"] = app_branch_id
        if cli_version is not UNSET:
            field_dict["cli_version"] = cli_version
        if plan_only is not UNSET:
            field_dict["plan_only"] = plan_only
        if readme is not UNSET:
            field_dict["readme"] = readme

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_branch_id = d.pop("app_branch_id", UNSET)

        cli_version = d.pop("cli_version", UNSET)

        plan_only = d.pop("plan_only", UNSET)

        readme = d.pop("readme", UNSET)

        service_create_app_config_request = cls(
            app_branch_id=app_branch_id,
            cli_version=cli_version,
            plan_only=plan_only,
            readme=readme,
        )

        service_create_app_config_request.additional_properties = d
        return service_create_app_config_request

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
