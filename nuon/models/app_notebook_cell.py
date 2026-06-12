from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_notebook_cell_env_vars import AppNotebookCellEnvVars
    from ..models.app_notebook_cell_run import AppNotebookCellRun
    from ..models.sql_null_bool import SqlNullBool


T = TypeVar("T", bound="AppNotebookCell")


@_attrs_define
class AppNotebookCell:
    """
    Attributes:
        command (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        enable_kube_config (SqlNullBool | Unset):
        env_vars (AppNotebookCellEnvVars | Unset):
        id (str | Unset):
        inline_contents (str | Unset):
        latest_run (AppNotebookCellRun | Unset):
        name (str | Unset):
        notebook_id (str | Unset):
        position (int | Unset): Position is the 0-based ordering of this cell within the notebook.
        revision (int | Unset): Revision increments on every edit; runs snapshot the revision they ran.
        role (str | Unset):
        timeout (int | Unset):
        updated_at (str | Unset):
    """

    command: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    enable_kube_config: SqlNullBool | Unset = UNSET
    env_vars: AppNotebookCellEnvVars | Unset = UNSET
    id: str | Unset = UNSET
    inline_contents: str | Unset = UNSET
    latest_run: AppNotebookCellRun | Unset = UNSET
    name: str | Unset = UNSET
    notebook_id: str | Unset = UNSET
    position: int | Unset = UNSET
    revision: int | Unset = UNSET
    role: str | Unset = UNSET
    timeout: int | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        command = self.command

        created_at = self.created_at

        created_by_id = self.created_by_id

        enable_kube_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.enable_kube_config, Unset):
            enable_kube_config = self.enable_kube_config.to_dict()

        env_vars: dict[str, Any] | Unset = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        id = self.id

        inline_contents = self.inline_contents

        latest_run: dict[str, Any] | Unset = UNSET
        if not isinstance(self.latest_run, Unset):
            latest_run = self.latest_run.to_dict()

        name = self.name

        notebook_id = self.notebook_id

        position = self.position

        revision = self.revision

        role = self.role

        timeout = self.timeout

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if command is not UNSET:
            field_dict["command"] = command
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if enable_kube_config is not UNSET:
            field_dict["enable_kube_config"] = enable_kube_config
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if id is not UNSET:
            field_dict["id"] = id
        if inline_contents is not UNSET:
            field_dict["inline_contents"] = inline_contents
        if latest_run is not UNSET:
            field_dict["latest_run"] = latest_run
        if name is not UNSET:
            field_dict["name"] = name
        if notebook_id is not UNSET:
            field_dict["notebook_id"] = notebook_id
        if position is not UNSET:
            field_dict["position"] = position
        if revision is not UNSET:
            field_dict["revision"] = revision
        if role is not UNSET:
            field_dict["role"] = role
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_notebook_cell_env_vars import AppNotebookCellEnvVars
        from ..models.app_notebook_cell_run import AppNotebookCellRun
        from ..models.sql_null_bool import SqlNullBool

        d = dict(src_dict)
        command = d.pop("command", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        _enable_kube_config = d.pop("enable_kube_config", UNSET)
        enable_kube_config: SqlNullBool | Unset
        if isinstance(_enable_kube_config, Unset):
            enable_kube_config = UNSET
        else:
            enable_kube_config = SqlNullBool.from_dict(_enable_kube_config)

        _env_vars = d.pop("env_vars", UNSET)
        env_vars: AppNotebookCellEnvVars | Unset
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = AppNotebookCellEnvVars.from_dict(_env_vars)

        id = d.pop("id", UNSET)

        inline_contents = d.pop("inline_contents", UNSET)

        _latest_run = d.pop("latest_run", UNSET)
        latest_run: AppNotebookCellRun | Unset
        if isinstance(_latest_run, Unset):
            latest_run = UNSET
        else:
            latest_run = AppNotebookCellRun.from_dict(_latest_run)

        name = d.pop("name", UNSET)

        notebook_id = d.pop("notebook_id", UNSET)

        position = d.pop("position", UNSET)

        revision = d.pop("revision", UNSET)

        role = d.pop("role", UNSET)

        timeout = d.pop("timeout", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_notebook_cell = cls(
            command=command,
            created_at=created_at,
            created_by_id=created_by_id,
            enable_kube_config=enable_kube_config,
            env_vars=env_vars,
            id=id,
            inline_contents=inline_contents,
            latest_run=latest_run,
            name=name,
            notebook_id=notebook_id,
            position=position,
            revision=revision,
            role=role,
            timeout=timeout,
            updated_at=updated_at,
        )

        app_notebook_cell.additional_properties = d
        return app_notebook_cell

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
