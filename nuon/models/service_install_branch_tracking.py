from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

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
        commits_behind (int | None | Unset):
        directory (str | Unset):
        expected_commit (ServiceInstallOverviewCommit | Unset):
        git_branch (str | Unset):
        pending_commits (list[ServiceInstallOverviewCommit] | Unset):
        repo (str | Unset):
        runs_behind (int | None | Unset):
        selected_commit (ServiceInstallOverviewCommit | Unset):
        status (str | Unset):
        successful_runs (list[ServiceInstallOverviewCommit] | Unset):
        target_branch (str | Unset):
    """

    applied_commit: ServiceInstallOverviewCommit | Unset = UNSET
    branch_id: str | Unset = UNSET
    commits_behind: int | None | Unset = UNSET
    directory: str | Unset = UNSET
    expected_commit: ServiceInstallOverviewCommit | Unset = UNSET
    git_branch: str | Unset = UNSET
    pending_commits: list[ServiceInstallOverviewCommit] | Unset = UNSET
    repo: str | Unset = UNSET
    runs_behind: int | None | Unset = UNSET
    selected_commit: ServiceInstallOverviewCommit | Unset = UNSET
    status: str | Unset = UNSET
    successful_runs: list[ServiceInstallOverviewCommit] | Unset = UNSET
    target_branch: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        applied_commit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.applied_commit, Unset):
            applied_commit = self.applied_commit.to_dict()

        branch_id = self.branch_id

        commits_behind: int | None | Unset
        if isinstance(self.commits_behind, Unset):
            commits_behind = UNSET
        else:
            commits_behind = self.commits_behind

        directory = self.directory

        expected_commit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expected_commit, Unset):
            expected_commit = self.expected_commit.to_dict()

        git_branch = self.git_branch

        pending_commits: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pending_commits, Unset):
            pending_commits = []
            for pending_commits_item_data in self.pending_commits:
                pending_commits_item = pending_commits_item_data.to_dict()
                pending_commits.append(pending_commits_item)

        repo = self.repo

        runs_behind: int | None | Unset
        if isinstance(self.runs_behind, Unset):
            runs_behind = UNSET
        else:
            runs_behind = self.runs_behind

        selected_commit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.selected_commit, Unset):
            selected_commit = self.selected_commit.to_dict()

        status = self.status

        successful_runs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.successful_runs, Unset):
            successful_runs = []
            for successful_runs_item_data in self.successful_runs:
                successful_runs_item = successful_runs_item_data.to_dict()
                successful_runs.append(successful_runs_item)

        target_branch = self.target_branch

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if applied_commit is not UNSET:
            field_dict["applied_commit"] = applied_commit
        if branch_id is not UNSET:
            field_dict["branch_id"] = branch_id
        if commits_behind is not UNSET:
            field_dict["commits_behind"] = commits_behind
        if directory is not UNSET:
            field_dict["directory"] = directory
        if expected_commit is not UNSET:
            field_dict["expected_commit"] = expected_commit
        if git_branch is not UNSET:
            field_dict["git_branch"] = git_branch
        if pending_commits is not UNSET:
            field_dict["pending_commits"] = pending_commits
        if repo is not UNSET:
            field_dict["repo"] = repo
        if runs_behind is not UNSET:
            field_dict["runs_behind"] = runs_behind
        if selected_commit is not UNSET:
            field_dict["selected_commit"] = selected_commit
        if status is not UNSET:
            field_dict["status"] = status
        if successful_runs is not UNSET:
            field_dict["successful_runs"] = successful_runs
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

        def _parse_commits_behind(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        commits_behind = _parse_commits_behind(d.pop("commits_behind", UNSET))

        directory = d.pop("directory", UNSET)

        _expected_commit = d.pop("expected_commit", UNSET)
        expected_commit: ServiceInstallOverviewCommit | Unset
        if isinstance(_expected_commit, Unset):
            expected_commit = UNSET
        else:
            expected_commit = ServiceInstallOverviewCommit.from_dict(_expected_commit)

        git_branch = d.pop("git_branch", UNSET)

        _pending_commits = d.pop("pending_commits", UNSET)
        pending_commits: list[ServiceInstallOverviewCommit] | Unset = UNSET
        if _pending_commits is not UNSET:
            pending_commits = []
            for pending_commits_item_data in _pending_commits:
                pending_commits_item = ServiceInstallOverviewCommit.from_dict(pending_commits_item_data)

                pending_commits.append(pending_commits_item)

        repo = d.pop("repo", UNSET)

        def _parse_runs_behind(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        runs_behind = _parse_runs_behind(d.pop("runs_behind", UNSET))

        _selected_commit = d.pop("selected_commit", UNSET)
        selected_commit: ServiceInstallOverviewCommit | Unset
        if isinstance(_selected_commit, Unset):
            selected_commit = UNSET
        else:
            selected_commit = ServiceInstallOverviewCommit.from_dict(_selected_commit)

        status = d.pop("status", UNSET)

        _successful_runs = d.pop("successful_runs", UNSET)
        successful_runs: list[ServiceInstallOverviewCommit] | Unset = UNSET
        if _successful_runs is not UNSET:
            successful_runs = []
            for successful_runs_item_data in _successful_runs:
                successful_runs_item = ServiceInstallOverviewCommit.from_dict(successful_runs_item_data)

                successful_runs.append(successful_runs_item)

        target_branch = d.pop("target_branch", UNSET)

        service_install_branch_tracking = cls(
            applied_commit=applied_commit,
            branch_id=branch_id,
            commits_behind=commits_behind,
            directory=directory,
            expected_commit=expected_commit,
            git_branch=git_branch,
            pending_commits=pending_commits,
            repo=repo,
            runs_behind=runs_behind,
            selected_commit=selected_commit,
            status=status,
            successful_runs=successful_runs,
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
