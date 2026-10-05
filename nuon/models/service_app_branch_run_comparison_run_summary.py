from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_vcs_connection_commit import AppVCSConnectionCommit


T = TypeVar("T", bound="ServiceAppBranchRunComparisonRunSummary")


@_attrs_define
class ServiceAppBranchRunComparisonRunSummary:
    """
    Attributes:
        app_config_id (str | Unset):
        base_branch (str | Unset):
        created_at (str | Unset):
        event_type (str | Unset):
        id (str | Unset):
        pr_number (int | Unset):
        status (str | Unset):
        vcs_connection_commit (AppVCSConnectionCommit | Unset):
        workflow_id (str | Unset):
    """

    app_config_id: str | Unset = UNSET
    base_branch: str | Unset = UNSET
    created_at: str | Unset = UNSET
    event_type: str | Unset = UNSET
    id: str | Unset = UNSET
    pr_number: int | Unset = UNSET
    status: str | Unset = UNSET
    vcs_connection_commit: AppVCSConnectionCommit | Unset = UNSET
    workflow_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config_id = self.app_config_id

        base_branch = self.base_branch

        created_at = self.created_at

        event_type = self.event_type

        id = self.id

        pr_number = self.pr_number

        status = self.status

        vcs_connection_commit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vcs_connection_commit, Unset):
            vcs_connection_commit = self.vcs_connection_commit.to_dict()

        workflow_id = self.workflow_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if base_branch is not UNSET:
            field_dict["base_branch"] = base_branch
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if id is not UNSET:
            field_dict["id"] = id
        if pr_number is not UNSET:
            field_dict["pr_number"] = pr_number
        if status is not UNSET:
            field_dict["status"] = status
        if vcs_connection_commit is not UNSET:
            field_dict["vcs_connection_commit"] = vcs_connection_commit
        if workflow_id is not UNSET:
            field_dict["workflow_id"] = workflow_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_vcs_connection_commit import AppVCSConnectionCommit  # noqa: PLC0415

        d = dict(src_dict)
        app_config_id = d.pop("app_config_id", UNSET)

        base_branch = d.pop("base_branch", UNSET)

        created_at = d.pop("created_at", UNSET)

        event_type = d.pop("event_type", UNSET)

        id = d.pop("id", UNSET)

        pr_number = d.pop("pr_number", UNSET)

        status = d.pop("status", UNSET)

        _vcs_connection_commit = d.pop("vcs_connection_commit", UNSET)
        vcs_connection_commit: AppVCSConnectionCommit | Unset
        if isinstance(_vcs_connection_commit, Unset):
            vcs_connection_commit = UNSET
        else:
            vcs_connection_commit = AppVCSConnectionCommit.from_dict(_vcs_connection_commit)

        workflow_id = d.pop("workflow_id", UNSET)

        service_app_branch_run_comparison_run_summary = cls(
            app_config_id=app_config_id,
            base_branch=base_branch,
            created_at=created_at,
            event_type=event_type,
            id=id,
            pr_number=pr_number,
            status=status,
            vcs_connection_commit=vcs_connection_commit,
            workflow_id=workflow_id,
        )

        service_app_branch_run_comparison_run_summary.additional_properties = d
        return service_app_branch_run_comparison_run_summary

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
