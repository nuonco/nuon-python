from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_account import AppAccount
    from ..models.app_app_branch import AppAppBranch
    from ..models.app_app_branch_config import AppAppBranchConfig
    from ..models.app_log_stream import AppLogStream
    from ..models.app_queue_signal import AppQueueSignal
    from ..models.app_vcs_connection_commit import AppVCSConnectionCommit
    from ..models.app_workflow import AppWorkflow


T = TypeVar("T", bound="AppAppBranchRun")


@_attrs_define
class AppAppBranchRun:
    """
    Attributes:
        app_branch (AppAppBranch | Unset):
        app_branch_config (AppAppBranchConfig | Unset):
        app_config_id (str | Unset): AppConfigID is the app config that was created/synced during this run
        commit_sha (str | Unset): CommitSHA is the VCS commit that triggered or is associated with this run
            DEPRECATED: Use VCSConnectionCommit relationship instead
        completed_at (str | Unset): CompletedAt tracks when execution finished
        created_at (str | Unset):
        created_by (AppAccount | Unset):
        created_by_id (str | Unset):
        error_message (str | Unset): ErrorMessage stores any error that occurred during execution
        force (bool | Unset): Force indicates if this run was forced (bypassing change detection)
        id (str | Unset):
        log_stream (AppLogStream | Unset):
        log_stream_id (str | Unset): LogStreamID is the log stream created during this run for event tracking
        queue_signal (AppQueueSignal | Unset):
        started_at (str | Unset): StartedAt tracks when execution actually began
        status (str | Unset): Status tracks the current state of the run
            Values: pending, running, success, failed, cancelled
        updated_at (str | Unset):
        vcs_connection_commit (AppVCSConnectionCommit | Unset):
        workflow (AppWorkflow | Unset):
        workflow_id (str | Unset):
    """

    app_branch: AppAppBranch | Unset = UNSET
    app_branch_config: AppAppBranchConfig | Unset = UNSET
    app_config_id: str | Unset = UNSET
    commit_sha: str | Unset = UNSET
    completed_at: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by: AppAccount | Unset = UNSET
    created_by_id: str | Unset = UNSET
    error_message: str | Unset = UNSET
    force: bool | Unset = UNSET
    id: str | Unset = UNSET
    log_stream: AppLogStream | Unset = UNSET
    log_stream_id: str | Unset = UNSET
    queue_signal: AppQueueSignal | Unset = UNSET
    started_at: str | Unset = UNSET
    status: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    vcs_connection_commit: AppVCSConnectionCommit | Unset = UNSET
    workflow: AppWorkflow | Unset = UNSET
    workflow_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_branch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.app_branch, Unset):
            app_branch = self.app_branch.to_dict()

        app_branch_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.app_branch_config, Unset):
            app_branch_config = self.app_branch_config.to_dict()

        app_config_id = self.app_config_id

        commit_sha = self.commit_sha

        completed_at = self.completed_at

        created_at = self.created_at

        created_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        created_by_id = self.created_by_id

        error_message = self.error_message

        force = self.force

        id = self.id

        log_stream: dict[str, Any] | Unset = UNSET
        if not isinstance(self.log_stream, Unset):
            log_stream = self.log_stream.to_dict()

        log_stream_id = self.log_stream_id

        queue_signal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.queue_signal, Unset):
            queue_signal = self.queue_signal.to_dict()

        started_at = self.started_at

        status = self.status

        updated_at = self.updated_at

        vcs_connection_commit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vcs_connection_commit, Unset):
            vcs_connection_commit = self.vcs_connection_commit.to_dict()

        workflow: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

        workflow_id = self.workflow_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_branch is not UNSET:
            field_dict["app_branch"] = app_branch
        if app_branch_config is not UNSET:
            field_dict["app_branch_config"] = app_branch_config
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if commit_sha is not UNSET:
            field_dict["commit_sha"] = commit_sha
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if force is not UNSET:
            field_dict["force"] = force
        if id is not UNSET:
            field_dict["id"] = id
        if log_stream is not UNSET:
            field_dict["log_stream"] = log_stream
        if log_stream_id is not UNSET:
            field_dict["log_stream_id"] = log_stream_id
        if queue_signal is not UNSET:
            field_dict["queue_signal"] = queue_signal
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if vcs_connection_commit is not UNSET:
            field_dict["vcs_connection_commit"] = vcs_connection_commit
        if workflow is not UNSET:
            field_dict["workflow"] = workflow
        if workflow_id is not UNSET:
            field_dict["workflow_id"] = workflow_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_account import AppAccount
        from ..models.app_app_branch import AppAppBranch
        from ..models.app_app_branch_config import AppAppBranchConfig
        from ..models.app_log_stream import AppLogStream
        from ..models.app_queue_signal import AppQueueSignal
        from ..models.app_vcs_connection_commit import AppVCSConnectionCommit
        from ..models.app_workflow import AppWorkflow

        d = dict(src_dict)
        _app_branch = d.pop("app_branch", UNSET)
        app_branch: AppAppBranch | Unset
        if isinstance(_app_branch, Unset):
            app_branch = UNSET
        else:
            app_branch = AppAppBranch.from_dict(_app_branch)

        _app_branch_config = d.pop("app_branch_config", UNSET)
        app_branch_config: AppAppBranchConfig | Unset
        if isinstance(_app_branch_config, Unset):
            app_branch_config = UNSET
        else:
            app_branch_config = AppAppBranchConfig.from_dict(_app_branch_config)

        app_config_id = d.pop("app_config_id", UNSET)

        commit_sha = d.pop("commit_sha", UNSET)

        completed_at = d.pop("completed_at", UNSET)

        created_at = d.pop("created_at", UNSET)

        _created_by = d.pop("created_by", UNSET)
        created_by: AppAccount | Unset
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = AppAccount.from_dict(_created_by)

        created_by_id = d.pop("created_by_id", UNSET)

        error_message = d.pop("error_message", UNSET)

        force = d.pop("force", UNSET)

        id = d.pop("id", UNSET)

        _log_stream = d.pop("log_stream", UNSET)
        log_stream: AppLogStream | Unset
        if isinstance(_log_stream, Unset):
            log_stream = UNSET
        else:
            log_stream = AppLogStream.from_dict(_log_stream)

        log_stream_id = d.pop("log_stream_id", UNSET)

        _queue_signal = d.pop("queue_signal", UNSET)
        queue_signal: AppQueueSignal | Unset
        if isinstance(_queue_signal, Unset):
            queue_signal = UNSET
        else:
            queue_signal = AppQueueSignal.from_dict(_queue_signal)

        started_at = d.pop("started_at", UNSET)

        status = d.pop("status", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _vcs_connection_commit = d.pop("vcs_connection_commit", UNSET)
        vcs_connection_commit: AppVCSConnectionCommit | Unset
        if isinstance(_vcs_connection_commit, Unset):
            vcs_connection_commit = UNSET
        else:
            vcs_connection_commit = AppVCSConnectionCommit.from_dict(_vcs_connection_commit)

        _workflow = d.pop("workflow", UNSET)
        workflow: AppWorkflow | Unset
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = AppWorkflow.from_dict(_workflow)

        workflow_id = d.pop("workflow_id", UNSET)

        app_app_branch_run = cls(
            app_branch=app_branch,
            app_branch_config=app_branch_config,
            app_config_id=app_config_id,
            commit_sha=commit_sha,
            completed_at=completed_at,
            created_at=created_at,
            created_by=created_by,
            created_by_id=created_by_id,
            error_message=error_message,
            force=force,
            id=id,
            log_stream=log_stream,
            log_stream_id=log_stream_id,
            queue_signal=queue_signal,
            started_at=started_at,
            status=status,
            updated_at=updated_at,
            vcs_connection_commit=vcs_connection_commit,
            workflow=workflow,
            workflow_id=workflow_id,
        )

        app_app_branch_run.additional_properties = d
        return app_app_branch_run

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
