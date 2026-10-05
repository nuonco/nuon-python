from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceInstallDeploymentAppBranchRef")


@_attrs_define
class ServiceInstallDeploymentAppBranchRef:
    """
    Attributes:
        git_ref (str | Unset):
        id (str | Unset):
        name (str | Unset):
        run_id (str | Unset):
        sha (str | Unset):
    """

    git_ref: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    run_id: str | Unset = UNSET
    sha: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        git_ref = self.git_ref

        id = self.id

        name = self.name

        run_id = self.run_id

        sha = self.sha

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if git_ref is not UNSET:
            field_dict["git_ref"] = git_ref
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if run_id is not UNSET:
            field_dict["run_id"] = run_id
        if sha is not UNSET:
            field_dict["sha"] = sha

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        git_ref = d.pop("git_ref", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        run_id = d.pop("run_id", UNSET)

        sha = d.pop("sha", UNSET)

        service_install_deployment_app_branch_ref = cls(
            git_ref=git_ref,
            id=id,
            name=name,
            run_id=run_id,
            sha=sha,
        )

        service_install_deployment_app_branch_ref.additional_properties = d
        return service_install_deployment_app_branch_ref

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
