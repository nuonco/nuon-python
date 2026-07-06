from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_composite_status import AppCompositeStatus
    from ..models.app_install_app_config_version_metadata import AppInstallAppConfigVersionMetadata
    from ..models.app_workflow import AppWorkflow
    from ..models.blobstore_blob import BlobstoreBlob


T = TypeVar("T", bound="AppInstallAppConfigVersion")


@_attrs_define
class AppInstallAppConfigVersion:
    """
    Attributes:
        app_branch_run_id (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        diff (BlobstoreBlob | Unset):
        id (str | Unset):
        install_group_id (str | Unset):
        install_id (str | Unset):
        metadata (AppInstallAppConfigVersionMetadata | Unset):
        new_app_config_id (str | Unset):
        old_app_config_id (str | Unset):
        org_id (str | Unset):
        status (AppCompositeStatus | Unset):
        updated_at (str | Unset):
        workflow (AppWorkflow | Unset):
        workflow_id (str | Unset):
    """

    app_branch_run_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    diff: BlobstoreBlob | Unset = UNSET
    id: str | Unset = UNSET
    install_group_id: str | Unset = UNSET
    install_id: str | Unset = UNSET
    metadata: AppInstallAppConfigVersionMetadata | Unset = UNSET
    new_app_config_id: str | Unset = UNSET
    old_app_config_id: str | Unset = UNSET
    org_id: str | Unset = UNSET
    status: AppCompositeStatus | Unset = UNSET
    updated_at: str | Unset = UNSET
    workflow: AppWorkflow | Unset = UNSET
    workflow_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_branch_run_id = self.app_branch_run_id

        created_at = self.created_at

        created_by_id = self.created_by_id

        diff: dict[str, Any] | Unset = UNSET
        if not isinstance(self.diff, Unset):
            diff = self.diff.to_dict()

        id = self.id

        install_group_id = self.install_group_id

        install_id = self.install_id

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        new_app_config_id = self.new_app_config_id

        old_app_config_id = self.old_app_config_id

        org_id = self.org_id

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        updated_at = self.updated_at

        workflow: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

        workflow_id = self.workflow_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_branch_run_id is not UNSET:
            field_dict["app_branch_run_id"] = app_branch_run_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if diff is not UNSET:
            field_dict["diff"] = diff
        if id is not UNSET:
            field_dict["id"] = id
        if install_group_id is not UNSET:
            field_dict["install_group_id"] = install_group_id
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if new_app_config_id is not UNSET:
            field_dict["new_app_config_id"] = new_app_config_id
        if old_app_config_id is not UNSET:
            field_dict["old_app_config_id"] = old_app_config_id
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if workflow is not UNSET:
            field_dict["workflow"] = workflow
        if workflow_id is not UNSET:
            field_dict["workflow_id"] = workflow_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_composite_status import AppCompositeStatus
        from ..models.app_install_app_config_version_metadata import AppInstallAppConfigVersionMetadata
        from ..models.app_workflow import AppWorkflow
        from ..models.blobstore_blob import BlobstoreBlob

        d = dict(src_dict)
        app_branch_run_id = d.pop("app_branch_run_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        _diff = d.pop("diff", UNSET)
        diff: BlobstoreBlob | Unset
        if isinstance(_diff, Unset):
            diff = UNSET
        else:
            diff = BlobstoreBlob.from_dict(_diff)

        id = d.pop("id", UNSET)

        install_group_id = d.pop("install_group_id", UNSET)

        install_id = d.pop("install_id", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: AppInstallAppConfigVersionMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = AppInstallAppConfigVersionMetadata.from_dict(_metadata)

        new_app_config_id = d.pop("new_app_config_id", UNSET)

        old_app_config_id = d.pop("old_app_config_id", UNSET)

        org_id = d.pop("org_id", UNSET)

        _status = d.pop("status", UNSET)
        status: AppCompositeStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppCompositeStatus.from_dict(_status)

        updated_at = d.pop("updated_at", UNSET)

        _workflow = d.pop("workflow", UNSET)
        workflow: AppWorkflow | Unset
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = AppWorkflow.from_dict(_workflow)

        workflow_id = d.pop("workflow_id", UNSET)

        app_install_app_config_version = cls(
            app_branch_run_id=app_branch_run_id,
            created_at=created_at,
            created_by_id=created_by_id,
            diff=diff,
            id=id,
            install_group_id=install_group_id,
            install_id=install_id,
            metadata=metadata,
            new_app_config_id=new_app_config_id,
            old_app_config_id=old_app_config_id,
            org_id=org_id,
            status=status,
            updated_at=updated_at,
            workflow=workflow,
            workflow_id=workflow_id,
        )

        app_install_app_config_version.additional_properties = d
        return app_install_app_config_version

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
