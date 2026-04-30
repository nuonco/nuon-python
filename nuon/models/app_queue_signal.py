from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_composite_status import AppCompositeStatus
    from ..models.app_queue import AppQueue
    from ..models.cctx_signal_context import CctxSignalContext
    from ..models.signaldb_signal_data import SignaldbSignalData
    from ..models.signaldb_workflow_ref import SignaldbWorkflowRef


T = TypeVar("T", bound="AppQueueSignal")


@_attrs_define
class AppQueueSignal:
    """
    Attributes:
        created_at (str | Unset):
        created_by_id (str | Unset):
        emitter_id (str | Unset): Optional: if this signal was emitted by an emitter
        enqueued (bool | Unset):
        execution_count (int | Unset):
        id (str | Unset):
        org_id (str | Unset):
        owner_id (str | Unset):
        owner_type (str | Unset):
        queue (AppQueue | Unset):
        queue_id (str | Unset):
        signal (SignaldbSignalData | Unset):
        signal_context (CctxSignalContext | Unset):
        status (AppCompositeStatus | Unset):
        type_ (str | Unset):
        updated_at (str | Unset):
        workflow (SignaldbWorkflowRef | Unset):
    """

    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    emitter_id: str | Unset = UNSET
    enqueued: bool | Unset = UNSET
    execution_count: int | Unset = UNSET
    id: str | Unset = UNSET
    org_id: str | Unset = UNSET
    owner_id: str | Unset = UNSET
    owner_type: str | Unset = UNSET
    queue: AppQueue | Unset = UNSET
    queue_id: str | Unset = UNSET
    signal: SignaldbSignalData | Unset = UNSET
    signal_context: CctxSignalContext | Unset = UNSET
    status: AppCompositeStatus | Unset = UNSET
    type_: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    workflow: SignaldbWorkflowRef | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        emitter_id = self.emitter_id

        enqueued = self.enqueued

        execution_count = self.execution_count

        id = self.id

        org_id = self.org_id

        owner_id = self.owner_id

        owner_type = self.owner_type

        queue: dict[str, Any] | Unset = UNSET
        if not isinstance(self.queue, Unset):
            queue = self.queue.to_dict()

        queue_id = self.queue_id

        signal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.signal, Unset):
            signal = self.signal.to_dict()

        signal_context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.signal_context, Unset):
            signal_context = self.signal_context.to_dict()

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        type_ = self.type_

        updated_at = self.updated_at

        workflow: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if emitter_id is not UNSET:
            field_dict["emitter_id"] = emitter_id
        if enqueued is not UNSET:
            field_dict["enqueued"] = enqueued
        if execution_count is not UNSET:
            field_dict["execution_count"] = execution_count
        if id is not UNSET:
            field_dict["id"] = id
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if owner_type is not UNSET:
            field_dict["owner_type"] = owner_type
        if queue is not UNSET:
            field_dict["queue"] = queue
        if queue_id is not UNSET:
            field_dict["queue_id"] = queue_id
        if signal is not UNSET:
            field_dict["signal"] = signal
        if signal_context is not UNSET:
            field_dict["signal_context"] = signal_context
        if status is not UNSET:
            field_dict["status"] = status
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if workflow is not UNSET:
            field_dict["workflow"] = workflow

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_composite_status import AppCompositeStatus
        from ..models.app_queue import AppQueue
        from ..models.cctx_signal_context import CctxSignalContext
        from ..models.signaldb_signal_data import SignaldbSignalData
        from ..models.signaldb_workflow_ref import SignaldbWorkflowRef

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        emitter_id = d.pop("emitter_id", UNSET)

        enqueued = d.pop("enqueued", UNSET)

        execution_count = d.pop("execution_count", UNSET)

        id = d.pop("id", UNSET)

        org_id = d.pop("org_id", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        owner_type = d.pop("owner_type", UNSET)

        _queue = d.pop("queue", UNSET)
        queue: AppQueue | Unset
        if isinstance(_queue, Unset):
            queue = UNSET
        else:
            queue = AppQueue.from_dict(_queue)

        queue_id = d.pop("queue_id", UNSET)

        _signal = d.pop("signal", UNSET)
        signal: SignaldbSignalData | Unset
        if isinstance(_signal, Unset):
            signal = UNSET
        else:
            signal = SignaldbSignalData.from_dict(_signal)

        _signal_context = d.pop("signal_context", UNSET)
        signal_context: CctxSignalContext | Unset
        if isinstance(_signal_context, Unset):
            signal_context = UNSET
        else:
            signal_context = CctxSignalContext.from_dict(_signal_context)

        _status = d.pop("status", UNSET)
        status: AppCompositeStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppCompositeStatus.from_dict(_status)

        type_ = d.pop("type", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _workflow = d.pop("workflow", UNSET)
        workflow: SignaldbWorkflowRef | Unset
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = SignaldbWorkflowRef.from_dict(_workflow)

        app_queue_signal = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            emitter_id=emitter_id,
            enqueued=enqueued,
            execution_count=execution_count,
            id=id,
            org_id=org_id,
            owner_id=owner_id,
            owner_type=owner_type,
            queue=queue,
            queue_id=queue_id,
            signal=signal,
            signal_context=signal_context,
            status=status,
            type_=type_,
            updated_at=updated_at,
            workflow=workflow,
        )

        app_queue_signal.additional_properties = d
        return app_queue_signal

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
