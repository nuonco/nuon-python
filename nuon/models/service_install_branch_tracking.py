from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_install_overview_commit import ServiceInstallOverviewCommit


T = TypeVar("T", bound="ServiceInstallBranchTracking")


@_attrs_define
class ServiceInstallBranchTracking:
    """
    Attributes:
        applied_commit (ServiceInstallOverviewCommit | Unset):
        branch_id (str | Unset):
        directory (str | Unset):
        expected_commit (ServiceInstallOverviewCommit | Unset):
        git_branch (str | Unset):
        repo (str | Unset):
        status (str | Unset):
        target_branch (str | Unset):
    """

    applied_commit: ServiceInstallOverviewCommit | Unset = UNSET
    branch_id: str | Unset = UNSET
    directory: str | Unset = UNSET
    expected_commit: ServiceInstallOverviewCommit | Unset = UNSET
    git_branch: str | Unset = UNSET
    repo: str | Unset = UNSET
    status: str | Unset = UNSET
    target_branch: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        applied_commit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.applied_commit, Unset):
            applied_commit = self.applied_commit.to_dict()

        branch_id = self.branch_id

        directory = self.directory

        expected_commit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expected_commit, Unset):
            expected_commit = self.expected_commit.to_dict()

        git_branch = self.git_branch

        repo = self.repo

        status = self.status

        target_branch = self.target_branch

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if applied_commit is not UNSET:
            field_dict["applied_commit"] = applied_commit
        if branch_id is not UNSET:
            field_dict["branch_id"] = branch_id
        if directory is not UNSET:
            field_dict["directory"] = directory
        if expected_commit is not UNSET:
            field_dict["expected_commit"] = expected_commit
        if git_branch is not UNSET:
            field_dict["git_branch"] = git_branch
        if repo is not UNSET:
            field_dict["repo"] = repo
        if status is not UNSET:
            field_dict["status"] = status
        if target_branch is not UNSET:
            field_dict["target_branch"] = target_branch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_install_overview_commit import ServiceInstallOverviewCommit  # noqa: PLC0415

        d = dict(src_dict)
        _applied_commit = d.pop("applied_commit", UNSET)
        applied_commit: ServiceInstallOverviewCommit | Unset
        if isinstance(_applied_commit, Unset):
            applied_commit = UNSET
        else:
            applied_commit = ServiceInstallOverviewCommit.from_dict(_applied_commit)

        branch_id = d.pop("branch_id", UNSET)

        directory = d.pop("directory", UNSET)

        _expected_commit = d.pop("expected_commit", UNSET)
        expected_commit: ServiceInstallOverviewCommit | Unset
        if isinstance(_expected_commit, Unset):
            expected_commit = UNSET
        else:
            expected_commit = ServiceInstallOverviewCommit.from_dict(_expected_commit)

        git_branch = d.pop("git_branch", UNSET)

        repo = d.pop("repo", UNSET)

        status = d.pop("status", UNSET)

        target_branch = d.pop("target_branch", UNSET)

        service_install_branch_tracking = cls(
            applied_commit=applied_commit,
            branch_id=branch_id,
            directory=directory,
            expected_commit=expected_commit,
            git_branch=git_branch,
            repo=repo,
            status=status,
            target_branch=target_branch,
        )

        service_install_branch_tracking.additional_properties = d
        return service_install_branch_tracking

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
