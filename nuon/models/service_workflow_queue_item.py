from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_status import AppStatus
from ..models.app_workflow_type import AppWorkflowType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_workflow_queue_item_metadata import ServiceWorkflowQueueItemMetadata


T = TypeVar("T", bound="ServiceWorkflowQueueItem")


@_attrs_define
class ServiceWorkflowQueueItem:
    """
    Attributes:
        created_at (str | Unset):
        metadata (ServiceWorkflowQueueItemMetadata | Unset):
        status (AppStatus | Unset):
        workflow_id (str | Unset):
        workflow_type (AppWorkflowType | Unset):
    """

    created_at: str | Unset = UNSET
    metadata: ServiceWorkflowQueueItemMetadata | Unset = UNSET
    status: AppStatus | Unset = UNSET
    workflow_id: str | Unset = UNSET
    workflow_type: AppWorkflowType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        workflow_id = self.workflow_id

        workflow_type: str | Unset = UNSET
        if not isinstance(self.workflow_type, Unset):
            workflow_type = self.workflow_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if status is not UNSET:
            field_dict["status"] = status
        if workflow_id is not UNSET:
            field_dict["workflow_id"] = workflow_id
        if workflow_type is not UNSET:
            field_dict["workflow_type"] = workflow_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_workflow_queue_item_metadata import ServiceWorkflowQueueItemMetadata

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: ServiceWorkflowQueueItemMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ServiceWorkflowQueueItemMetadata.from_dict(_metadata)

        _status = d.pop("status", UNSET)
        status: AppStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppStatus(_status)

        workflow_id = d.pop("workflow_id", UNSET)

        _workflow_type = d.pop("workflow_type", UNSET)
        workflow_type: AppWorkflowType | Unset
        if isinstance(_workflow_type, Unset):
            workflow_type = UNSET
        else:
            workflow_type = AppWorkflowType(_workflow_type)

        service_workflow_queue_item = cls(
            created_at=created_at,
            metadata=metadata,
            status=status,
            workflow_id=workflow_id,
            workflow_type=workflow_type,
        )

        service_workflow_queue_item.additional_properties = d
        return service_workflow_queue_item

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
