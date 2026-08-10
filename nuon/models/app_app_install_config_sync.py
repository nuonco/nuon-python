from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_composite_status import AppCompositeStatus
    from ..models.app_install_config_sync import AppInstallConfigSync
    from ..models.app_install_creation_approval import AppInstallCreationApproval
    from ..models.app_vcs_connection_commit import AppVCSConnectionCommit
    from ..models.app_workflow import AppWorkflow


T = TypeVar("T", bound="AppAppInstallConfigSync")


@_attrs_define
class AppAppInstallConfigSync:
    """
    Attributes:
        app_id (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        install_config_syncs (list[AppInstallConfigSync] | Unset):
        install_creation_approval (AppInstallCreationApproval | Unset):
        org_id (str | Unset):
        queue_id (str | Unset):
        queue_signal_id (str | Unset):
        status (AppCompositeStatus | Unset):
        triggered_by (str | Unset):
        updated_at (str | Unset):
        vcs_connection_commit (AppVCSConnectionCommit | Unset):
        workflow (AppWorkflow | Unset):
        workflow_id (str | Unset):
    """

    app_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    install_config_syncs: list[AppInstallConfigSync] | Unset = UNSET
    install_creation_approval: AppInstallCreationApproval | Unset = UNSET
    org_id: str | Unset = UNSET
    queue_id: str | Unset = UNSET
    queue_signal_id: str | Unset = UNSET
    status: AppCompositeStatus | Unset = UNSET
    triggered_by: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    vcs_connection_commit: AppVCSConnectionCommit | Unset = UNSET
    workflow: AppWorkflow | Unset = UNSET
    workflow_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        install_config_syncs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.install_config_syncs, Unset):
            install_config_syncs = []
            for install_config_syncs_item_data in self.install_config_syncs:
                install_config_syncs_item = install_config_syncs_item_data.to_dict()
                install_config_syncs.append(install_config_syncs_item)

        install_creation_approval: dict[str, Any] | Unset = UNSET
        if not isinstance(self.install_creation_approval, Unset):
            install_creation_approval = self.install_creation_approval.to_dict()

        org_id = self.org_id

        queue_id = self.queue_id

        queue_signal_id = self.queue_signal_id

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        triggered_by = self.triggered_by

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
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if install_config_syncs is not UNSET:
            field_dict["install_config_syncs"] = install_config_syncs
        if install_creation_approval is not UNSET:
            field_dict["install_creation_approval"] = install_creation_approval
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if queue_id is not UNSET:
            field_dict["queue_id"] = queue_id
        if queue_signal_id is not UNSET:
            field_dict["queue_signal_id"] = queue_signal_id
        if status is not UNSET:
            field_dict["status"] = status
        if triggered_by is not UNSET:
            field_dict["triggered_by"] = triggered_by
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
        from ..models.app_composite_status import AppCompositeStatus
        from ..models.app_install_config_sync import AppInstallConfigSync
        from ..models.app_install_creation_approval import AppInstallCreationApproval
        from ..models.app_vcs_connection_commit import AppVCSConnectionCommit
        from ..models.app_workflow import AppWorkflow

        d = dict(src_dict)
        app_id = d.pop("app_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        _install_config_syncs = d.pop("install_config_syncs", UNSET)
        install_config_syncs: list[AppInstallConfigSync] | Unset = UNSET
        if _install_config_syncs is not UNSET:
            install_config_syncs = []
            for install_config_syncs_item_data in _install_config_syncs:
                install_config_syncs_item = AppInstallConfigSync.from_dict(install_config_syncs_item_data)

                install_config_syncs.append(install_config_syncs_item)

        _install_creation_approval = d.pop("install_creation_approval", UNSET)
        install_creation_approval: AppInstallCreationApproval | Unset
        if isinstance(_install_creation_approval, Unset):
            install_creation_approval = UNSET
        else:
            install_creation_approval = AppInstallCreationApproval.from_dict(_install_creation_approval)

        org_id = d.pop("org_id", UNSET)

        queue_id = d.pop("queue_id", UNSET)

        queue_signal_id = d.pop("queue_signal_id", UNSET)

        _status = d.pop("status", UNSET)
        status: AppCompositeStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppCompositeStatus.from_dict(_status)

        triggered_by = d.pop("triggered_by", UNSET)

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

        app_app_install_config_sync = cls(
            app_id=app_id,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            install_config_syncs=install_config_syncs,
            install_creation_approval=install_creation_approval,
            org_id=org_id,
            queue_id=queue_id,
            queue_signal_id=queue_signal_id,
            status=status,
            triggered_by=triggered_by,
            updated_at=updated_at,
            vcs_connection_commit=vcs_connection_commit,
            workflow=workflow,
            workflow_id=workflow_id,
        )

        app_app_install_config_sync.additional_properties = d
        return app_app_install_config_sync

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
