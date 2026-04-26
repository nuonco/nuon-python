from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_queue_emitter import AppQueueEmitter
    from ..models.app_queue_metadata import AppQueueMetadata
    from ..models.app_queue_signal import AppQueueSignal
    from ..models.signaldb_workflow_ref import SignaldbWorkflowRef


T = TypeVar("T", bound="AppQueue")


@_attrs_define
class AppQueue:
    """
    Attributes:
        created_at (str | Unset):
        created_by_id (str | Unset):
        emitters (list[AppQueueEmitter] | Unset):
        id (str | Unset):
        idle_timeout (int | Unset):
        max_depth (int | Unset):
        max_in_flight (int | Unset):
        metadata (AppQueueMetadata | Unset):
        name (str | Unset):
        org_id (str | Unset):
        owner_id (str | Unset):
        owner_type (str | Unset):
        queue_signal (list[AppQueueSignal] | Unset):
        updated_at (str | Unset):
        workflow (SignaldbWorkflowRef | Unset):
    """

    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    emitters: list[AppQueueEmitter] | Unset = UNSET
    id: str | Unset = UNSET
    idle_timeout: int | Unset = UNSET
    max_depth: int | Unset = UNSET
    max_in_flight: int | Unset = UNSET
    metadata: AppQueueMetadata | Unset = UNSET
    name: str | Unset = UNSET
    org_id: str | Unset = UNSET
    owner_id: str | Unset = UNSET
    owner_type: str | Unset = UNSET
    queue_signal: list[AppQueueSignal] | Unset = UNSET
    updated_at: str | Unset = UNSET
    workflow: SignaldbWorkflowRef | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        emitters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.emitters, Unset):
            emitters = []
            for emitters_item_data in self.emitters:
                emitters_item = emitters_item_data.to_dict()
                emitters.append(emitters_item)

        id = self.id

        idle_timeout = self.idle_timeout

        max_depth = self.max_depth

        max_in_flight = self.max_in_flight

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        name = self.name

        org_id = self.org_id

        owner_id = self.owner_id

        owner_type = self.owner_type

        queue_signal: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.queue_signal, Unset):
            queue_signal = []
            for queue_signal_item_data in self.queue_signal:
                queue_signal_item = queue_signal_item_data.to_dict()
                queue_signal.append(queue_signal_item)

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
        if emitters is not UNSET:
            field_dict["emitters"] = emitters
        if id is not UNSET:
            field_dict["id"] = id
        if idle_timeout is not UNSET:
            field_dict["idle_timeout"] = idle_timeout
        if max_depth is not UNSET:
            field_dict["max_depth"] = max_depth
        if max_in_flight is not UNSET:
            field_dict["max_in_flight"] = max_in_flight
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if owner_type is not UNSET:
            field_dict["owner_type"] = owner_type
        if queue_signal is not UNSET:
            field_dict["queue_signal"] = queue_signal
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if workflow is not UNSET:
            field_dict["workflow"] = workflow

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_queue_emitter import AppQueueEmitter
        from ..models.app_queue_metadata import AppQueueMetadata
        from ..models.app_queue_signal import AppQueueSignal
        from ..models.signaldb_workflow_ref import SignaldbWorkflowRef

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        _emitters = d.pop("emitters", UNSET)
        emitters: list[AppQueueEmitter] | Unset = UNSET
        if _emitters is not UNSET:
            emitters = []
            for emitters_item_data in _emitters:
                emitters_item = AppQueueEmitter.from_dict(emitters_item_data)

                emitters.append(emitters_item)

        id = d.pop("id", UNSET)

        idle_timeout = d.pop("idle_timeout", UNSET)

        max_depth = d.pop("max_depth", UNSET)

        max_in_flight = d.pop("max_in_flight", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: AppQueueMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = AppQueueMetadata.from_dict(_metadata)

        name = d.pop("name", UNSET)

        org_id = d.pop("org_id", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        owner_type = d.pop("owner_type", UNSET)

        _queue_signal = d.pop("queue_signal", UNSET)
        queue_signal: list[AppQueueSignal] | Unset = UNSET
        if _queue_signal is not UNSET:
            queue_signal = []
            for queue_signal_item_data in _queue_signal:
                queue_signal_item = AppQueueSignal.from_dict(queue_signal_item_data)

                queue_signal.append(queue_signal_item)

        updated_at = d.pop("updated_at", UNSET)

        _workflow = d.pop("workflow", UNSET)
        workflow: SignaldbWorkflowRef | Unset
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = SignaldbWorkflowRef.from_dict(_workflow)

        app_queue = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            emitters=emitters,
            id=id,
            idle_timeout=idle_timeout,
            max_depth=max_depth,
            max_in_flight=max_in_flight,
            metadata=metadata,
            name=name,
            org_id=org_id,
            owner_id=owner_id,
            owner_type=owner_type,
            queue_signal=queue_signal,
            updated_at=updated_at,
            workflow=workflow,
        )

        app_queue.additional_properties = d
        return app_queue

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
