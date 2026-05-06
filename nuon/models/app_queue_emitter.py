from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_queue_emitter_mode import AppQueueEmitterMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_composite_status import AppCompositeStatus
    from ..models.signaldb_signal_data import SignaldbSignalData
    from ..models.signaldb_workflow_ref import SignaldbWorkflowRef


T = TypeVar("T", bound="AppQueueEmitter")


@_attrs_define
class AppQueueEmitter:
    """
    Attributes:
        created_at (str | Unset):
        created_by_id (str | Unset):
        cron_schedule (str | Unset): Schedule configuration
            For cron mode: cron expression (e.g., "0 * * * *")
        description (str | Unset):
        emit_count (int | Unset):
        fired (bool | Unset): For scheduled mode: whether the signal has been fired
        id (str | Unset):
        jitter_window (int | Unset): For cron mode: spread emitter ticks deterministically across this window
            to avoid thundering-herd when many emitters share a schedule. A hash of the
            emitter ID determines each emitter's static offset within the window. Zero
            disables jitter (default).
        last_emitted_at (str | Unset):
        mode (AppQueueEmitterMode | Unset):
        name (str | Unset): Emitter identity
        next_emit_at (str | Unset):
        org_id (str | Unset):
        queue_id (str | Unset): Many-to-one: each emitter belongs to exactly one queue
        scheduled_at (str | Unset): For scheduled mode: the time to fire the signal
        signal_template (SignaldbSignalData | Unset):
        signal_type (str | Unset): Signal template - the signal to emit on each tick
        status (AppCompositeStatus | Unset):
        updated_at (str | Unset):
        workflow (SignaldbWorkflowRef | Unset):
    """

    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    cron_schedule: str | Unset = UNSET
    description: str | Unset = UNSET
    emit_count: int | Unset = UNSET
    fired: bool | Unset = UNSET
    id: str | Unset = UNSET
    jitter_window: int | Unset = UNSET
    last_emitted_at: str | Unset = UNSET
    mode: AppQueueEmitterMode | Unset = UNSET
    name: str | Unset = UNSET
    next_emit_at: str | Unset = UNSET
    org_id: str | Unset = UNSET
    queue_id: str | Unset = UNSET
    scheduled_at: str | Unset = UNSET
    signal_template: SignaldbSignalData | Unset = UNSET
    signal_type: str | Unset = UNSET
    status: AppCompositeStatus | Unset = UNSET
    updated_at: str | Unset = UNSET
    workflow: SignaldbWorkflowRef | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        cron_schedule = self.cron_schedule

        description = self.description

        emit_count = self.emit_count

        fired = self.fired

        id = self.id

        jitter_window = self.jitter_window

        last_emitted_at = self.last_emitted_at

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        name = self.name

        next_emit_at = self.next_emit_at

        org_id = self.org_id

        queue_id = self.queue_id

        scheduled_at = self.scheduled_at

        signal_template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.signal_template, Unset):
            signal_template = self.signal_template.to_dict()

        signal_type = self.signal_type

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

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
        if cron_schedule is not UNSET:
            field_dict["cron_schedule"] = cron_schedule
        if description is not UNSET:
            field_dict["description"] = description
        if emit_count is not UNSET:
            field_dict["emit_count"] = emit_count
        if fired is not UNSET:
            field_dict["fired"] = fired
        if id is not UNSET:
            field_dict["id"] = id
        if jitter_window is not UNSET:
            field_dict["jitter_window"] = jitter_window
        if last_emitted_at is not UNSET:
            field_dict["last_emitted_at"] = last_emitted_at
        if mode is not UNSET:
            field_dict["mode"] = mode
        if name is not UNSET:
            field_dict["name"] = name
        if next_emit_at is not UNSET:
            field_dict["next_emit_at"] = next_emit_at
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if queue_id is not UNSET:
            field_dict["queue_id"] = queue_id
        if scheduled_at is not UNSET:
            field_dict["scheduled_at"] = scheduled_at
        if signal_template is not UNSET:
            field_dict["signal_template"] = signal_template
        if signal_type is not UNSET:
            field_dict["signal_type"] = signal_type
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if workflow is not UNSET:
            field_dict["workflow"] = workflow

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_composite_status import AppCompositeStatus
        from ..models.signaldb_signal_data import SignaldbSignalData
        from ..models.signaldb_workflow_ref import SignaldbWorkflowRef

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        cron_schedule = d.pop("cron_schedule", UNSET)

        description = d.pop("description", UNSET)

        emit_count = d.pop("emit_count", UNSET)

        fired = d.pop("fired", UNSET)

        id = d.pop("id", UNSET)

        jitter_window = d.pop("jitter_window", UNSET)

        last_emitted_at = d.pop("last_emitted_at", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: AppQueueEmitterMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = AppQueueEmitterMode(_mode)

        name = d.pop("name", UNSET)

        next_emit_at = d.pop("next_emit_at", UNSET)

        org_id = d.pop("org_id", UNSET)

        queue_id = d.pop("queue_id", UNSET)

        scheduled_at = d.pop("scheduled_at", UNSET)

        _signal_template = d.pop("signal_template", UNSET)
        signal_template: SignaldbSignalData | Unset
        if isinstance(_signal_template, Unset):
            signal_template = UNSET
        else:
            signal_template = SignaldbSignalData.from_dict(_signal_template)

        signal_type = d.pop("signal_type", UNSET)

        _status = d.pop("status", UNSET)
        status: AppCompositeStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppCompositeStatus.from_dict(_status)

        updated_at = d.pop("updated_at", UNSET)

        _workflow = d.pop("workflow", UNSET)
        workflow: SignaldbWorkflowRef | Unset
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = SignaldbWorkflowRef.from_dict(_workflow)

        app_queue_emitter = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            cron_schedule=cron_schedule,
            description=description,
            emit_count=emit_count,
            fired=fired,
            id=id,
            jitter_window=jitter_window,
            last_emitted_at=last_emitted_at,
            mode=mode,
            name=name,
            next_emit_at=next_emit_at,
            org_id=org_id,
            queue_id=queue_id,
            scheduled_at=scheduled_at,
            signal_template=signal_template,
            signal_type=signal_type,
            status=status,
            updated_at=updated_at,
            workflow=workflow,
        )

        app_queue_emitter.additional_properties = d
        return app_queue_emitter

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
