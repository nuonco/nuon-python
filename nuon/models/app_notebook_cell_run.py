from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_account import AppAccount
    from ..models.app_composite_status import AppCompositeStatus
    from ..models.app_notebook_cell_run_env_vars import AppNotebookCellRunEnvVars


T = TypeVar("T", bound="AppNotebookCellRun")


@_attrs_define
class AppNotebookCellRun:
    """
    Attributes:
        cell_id (str | Unset):
        cell_revision (int | Unset): CellRevision records which revision of the cell this run executed.
        command (str | Unset):
        created_at (str | Unset):
        created_by (AppAccount | Unset):
        created_by_id (str | Unset):
        env_vars (AppNotebookCellRunEnvVars | Unset):
        id (str | Unset):
        idempotency_key (str | Unset): IdempotencyKey deduplicates run requests (HTTP retries / update retries).
            A server-side key is always generated, so the composite unique index on
            (notebook_id, idempotency_key) in Indexes() never sees an empty key.
        inline_contents (str | Unset):
        install_action_workflow_run_id (str | Unset): Link to the existing execution/audit artifacts.
        install_id (str | Unset):
        log_stream_id (str | Unset):
        name (str | Unset): Cell config snapshot at run time.
        notebook_id (str | Unset):
        runner_job_id (str | Unset):
        status (str | Unset):
        status_description (str | Unset):
        status_v2 (AppCompositeStatus | Unset):
        triggered_by_id (str | Unset):
        triggered_by_type (str | Unset):
        updated_at (str | Unset):
    """

    cell_id: str | Unset = UNSET
    cell_revision: int | Unset = UNSET
    command: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by: AppAccount | Unset = UNSET
    created_by_id: str | Unset = UNSET
    env_vars: AppNotebookCellRunEnvVars | Unset = UNSET
    id: str | Unset = UNSET
    idempotency_key: str | Unset = UNSET
    inline_contents: str | Unset = UNSET
    install_action_workflow_run_id: str | Unset = UNSET
    install_id: str | Unset = UNSET
    log_stream_id: str | Unset = UNSET
    name: str | Unset = UNSET
    notebook_id: str | Unset = UNSET
    runner_job_id: str | Unset = UNSET
    status: str | Unset = UNSET
    status_description: str | Unset = UNSET
    status_v2: AppCompositeStatus | Unset = UNSET
    triggered_by_id: str | Unset = UNSET
    triggered_by_type: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cell_id = self.cell_id

        cell_revision = self.cell_revision

        command = self.command

        created_at = self.created_at

        created_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        created_by_id = self.created_by_id

        env_vars: dict[str, Any] | Unset = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        id = self.id

        idempotency_key = self.idempotency_key

        inline_contents = self.inline_contents

        install_action_workflow_run_id = self.install_action_workflow_run_id

        install_id = self.install_id

        log_stream_id = self.log_stream_id

        name = self.name

        notebook_id = self.notebook_id

        runner_job_id = self.runner_job_id

        status = self.status

        status_description = self.status_description

        status_v2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status_v2, Unset):
            status_v2 = self.status_v2.to_dict()

        triggered_by_id = self.triggered_by_id

        triggered_by_type = self.triggered_by_type

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cell_id is not UNSET:
            field_dict["cell_id"] = cell_id
        if cell_revision is not UNSET:
            field_dict["cell_revision"] = cell_revision
        if command is not UNSET:
            field_dict["command"] = command
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if id is not UNSET:
            field_dict["id"] = id
        if idempotency_key is not UNSET:
            field_dict["idempotency_key"] = idempotency_key
        if inline_contents is not UNSET:
            field_dict["inline_contents"] = inline_contents
        if install_action_workflow_run_id is not UNSET:
            field_dict["install_action_workflow_run_id"] = install_action_workflow_run_id
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if log_stream_id is not UNSET:
            field_dict["log_stream_id"] = log_stream_id
        if name is not UNSET:
            field_dict["name"] = name
        if notebook_id is not UNSET:
            field_dict["notebook_id"] = notebook_id
        if runner_job_id is not UNSET:
            field_dict["runner_job_id"] = runner_job_id
        if status is not UNSET:
            field_dict["status"] = status
        if status_description is not UNSET:
            field_dict["status_description"] = status_description
        if status_v2 is not UNSET:
            field_dict["status_v2"] = status_v2
        if triggered_by_id is not UNSET:
            field_dict["triggered_by_id"] = triggered_by_id
        if triggered_by_type is not UNSET:
            field_dict["triggered_by_type"] = triggered_by_type
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_account import AppAccount
        from ..models.app_composite_status import AppCompositeStatus
        from ..models.app_notebook_cell_run_env_vars import AppNotebookCellRunEnvVars

        d = dict(src_dict)
        cell_id = d.pop("cell_id", UNSET)

        cell_revision = d.pop("cell_revision", UNSET)

        command = d.pop("command", UNSET)

        created_at = d.pop("created_at", UNSET)

        _created_by = d.pop("created_by", UNSET)
        created_by: AppAccount | Unset
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = AppAccount.from_dict(_created_by)

        created_by_id = d.pop("created_by_id", UNSET)

        _env_vars = d.pop("env_vars", UNSET)
        env_vars: AppNotebookCellRunEnvVars | Unset
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = AppNotebookCellRunEnvVars.from_dict(_env_vars)

        id = d.pop("id", UNSET)

        idempotency_key = d.pop("idempotency_key", UNSET)

        inline_contents = d.pop("inline_contents", UNSET)

        install_action_workflow_run_id = d.pop("install_action_workflow_run_id", UNSET)

        install_id = d.pop("install_id", UNSET)

        log_stream_id = d.pop("log_stream_id", UNSET)

        name = d.pop("name", UNSET)

        notebook_id = d.pop("notebook_id", UNSET)

        runner_job_id = d.pop("runner_job_id", UNSET)

        status = d.pop("status", UNSET)

        status_description = d.pop("status_description", UNSET)

        _status_v2 = d.pop("status_v2", UNSET)
        status_v2: AppCompositeStatus | Unset
        if isinstance(_status_v2, Unset):
            status_v2 = UNSET
        else:
            status_v2 = AppCompositeStatus.from_dict(_status_v2)

        triggered_by_id = d.pop("triggered_by_id", UNSET)

        triggered_by_type = d.pop("triggered_by_type", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_notebook_cell_run = cls(
            cell_id=cell_id,
            cell_revision=cell_revision,
            command=command,
            created_at=created_at,
            created_by=created_by,
            created_by_id=created_by_id,
            env_vars=env_vars,
            id=id,
            idempotency_key=idempotency_key,
            inline_contents=inline_contents,
            install_action_workflow_run_id=install_action_workflow_run_id,
            install_id=install_id,
            log_stream_id=log_stream_id,
            name=name,
            notebook_id=notebook_id,
            runner_job_id=runner_job_id,
            status=status,
            status_description=status_description,
            status_v2=status_v2,
            triggered_by_id=triggered_by_id,
            triggered_by_type=triggered_by_type,
            updated_at=updated_at,
        )

        app_notebook_cell_run.additional_properties = d
        return app_notebook_cell_run

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
