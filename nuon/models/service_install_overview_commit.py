from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceInstallOverviewCommit")


@_attrs_define
class ServiceInstallOverviewCommit:
    """
    Attributes:
        app_config_id (str | Unset):
        author (str | Unset):
        awaiting_approval (bool | Unset):
        branch_id (str | Unset):
        created_at (str | Unset):
        message (str | Unset):
        run_id (str | Unset):
        run_status (str | Unset):
        sha (str | Unset):
        workflow_id (str | Unset):
    """

    app_config_id: str | Unset = UNSET
    author: str | Unset = UNSET
    awaiting_approval: bool | Unset = UNSET
    branch_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    message: str | Unset = UNSET
    run_id: str | Unset = UNSET
    run_status: str | Unset = UNSET
    sha: str | Unset = UNSET
    workflow_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config_id = self.app_config_id

        author = self.author

        awaiting_approval = self.awaiting_approval

        branch_id = self.branch_id

        created_at = self.created_at

        message = self.message

        run_id = self.run_id

        run_status = self.run_status

        sha = self.sha

        workflow_id = self.workflow_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if author is not UNSET:
            field_dict["author"] = author
        if awaiting_approval is not UNSET:
            field_dict["awaiting_approval"] = awaiting_approval
        if branch_id is not UNSET:
            field_dict["branch_id"] = branch_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if message is not UNSET:
            field_dict["message"] = message
        if run_id is not UNSET:
            field_dict["run_id"] = run_id
        if run_status is not UNSET:
            field_dict["run_status"] = run_status
        if sha is not UNSET:
            field_dict["sha"] = sha
        if workflow_id is not UNSET:
            field_dict["workflow_id"] = workflow_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_config_id = d.pop("app_config_id", UNSET)

        author = d.pop("author", UNSET)

        awaiting_approval = d.pop("awaiting_approval", UNSET)

        branch_id = d.pop("branch_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        message = d.pop("message", UNSET)

        run_id = d.pop("run_id", UNSET)

        run_status = d.pop("run_status", UNSET)

        sha = d.pop("sha", UNSET)

        workflow_id = d.pop("workflow_id", UNSET)

        service_install_overview_commit = cls(
            app_config_id=app_config_id,
            author=author,
            awaiting_approval=awaiting_approval,
            branch_id=branch_id,
            created_at=created_at,
            message=message,
            run_id=run_id,
            run_status=run_status,
            sha=sha,
            workflow_id=workflow_id,
        )

        service_install_overview_commit.additional_properties = d
        return service_install_overview_commit

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
