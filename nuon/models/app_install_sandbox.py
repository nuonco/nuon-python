from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_composite_status import AppCompositeStatus
    from ..models.app_install_sandbox_run import AppInstallSandboxRun
    from ..models.app_terraform_workspace import AppTerraformWorkspace


T = TypeVar("T", bound="AppInstallSandbox")


@_attrs_define
class AppInstallSandbox:
    """
    Attributes:
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        install_id (str | Unset):
        install_sandbox_runs (list[AppInstallSandboxRun] | Unset):
        status (str | Unset):
        status_description (str | Unset):
        status_v2 (AppCompositeStatus | Unset):
        terraform_workspace (AppTerraformWorkspace | Unset):
        updated_at (str | Unset):
    """

    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    install_id: str | Unset = UNSET
    install_sandbox_runs: list[AppInstallSandboxRun] | Unset = UNSET
    status: str | Unset = UNSET
    status_description: str | Unset = UNSET
    status_v2: AppCompositeStatus | Unset = UNSET
    terraform_workspace: AppTerraformWorkspace | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        install_id = self.install_id

        install_sandbox_runs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.install_sandbox_runs, Unset):
            install_sandbox_runs = []
            for install_sandbox_runs_item_data in self.install_sandbox_runs:
                install_sandbox_runs_item = install_sandbox_runs_item_data.to_dict()
                install_sandbox_runs.append(install_sandbox_runs_item)

        status = self.status

        status_description = self.status_description

        status_v2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status_v2, Unset):
            status_v2 = self.status_v2.to_dict()

        terraform_workspace: dict[str, Any] | Unset = UNSET
        if not isinstance(self.terraform_workspace, Unset):
            terraform_workspace = self.terraform_workspace.to_dict()

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if install_sandbox_runs is not UNSET:
            field_dict["install_sandbox_runs"] = install_sandbox_runs
        if status is not UNSET:
            field_dict["status"] = status
        if status_description is not UNSET:
            field_dict["status_description"] = status_description
        if status_v2 is not UNSET:
            field_dict["status_v2"] = status_v2
        if terraform_workspace is not UNSET:
            field_dict["terraform_workspace"] = terraform_workspace
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_composite_status import AppCompositeStatus
        from ..models.app_install_sandbox_run import AppInstallSandboxRun
        from ..models.app_terraform_workspace import AppTerraformWorkspace

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        install_id = d.pop("install_id", UNSET)

        _install_sandbox_runs = d.pop("install_sandbox_runs", UNSET)
        install_sandbox_runs: list[AppInstallSandboxRun] | Unset = UNSET
        if _install_sandbox_runs is not UNSET:
            install_sandbox_runs = []
            for install_sandbox_runs_item_data in _install_sandbox_runs:
                install_sandbox_runs_item = AppInstallSandboxRun.from_dict(install_sandbox_runs_item_data)

                install_sandbox_runs.append(install_sandbox_runs_item)

        status = d.pop("status", UNSET)

        status_description = d.pop("status_description", UNSET)

        _status_v2 = d.pop("status_v2", UNSET)
        status_v2: AppCompositeStatus | Unset
        if isinstance(_status_v2, Unset):
            status_v2 = UNSET
        else:
            status_v2 = AppCompositeStatus.from_dict(_status_v2)

        _terraform_workspace = d.pop("terraform_workspace", UNSET)
        terraform_workspace: AppTerraformWorkspace | Unset
        if isinstance(_terraform_workspace, Unset):
            terraform_workspace = UNSET
        else:
            terraform_workspace = AppTerraformWorkspace.from_dict(_terraform_workspace)

        updated_at = d.pop("updated_at", UNSET)

        app_install_sandbox = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            install_id=install_id,
            install_sandbox_runs=install_sandbox_runs,
            status=status,
            status_description=status_description,
            status_v2=status_v2,
            terraform_workspace=terraform_workspace,
            updated_at=updated_at,
        )

        app_install_sandbox.additional_properties = d
        return app_install_sandbox

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
