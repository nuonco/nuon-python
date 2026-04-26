from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_runner_process_shutdown_type import AppRunnerProcessShutdownType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_composite_status import AppCompositeStatus
    from ..models.pgtype_hstore import PgtypeHstore


T = TypeVar("T", bound="AppRunnerProcessShutdown")


@_attrs_define
class AppRunnerProcessShutdown:
    """
    Attributes:
        composite_status (AppCompositeStatus | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        metadata (PgtypeHstore | Unset):
        org_id (str | Unset):
        runner_process_id (str | Unset):
        status (str | Unset): Status and StatusDescription are computed from CompositeStatus via AfterQuery.
        status_description (str | Unset):
        type_ (AppRunnerProcessShutdownType | Unset):
        updated_at (str | Unset):
    """

    composite_status: AppCompositeStatus | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    metadata: PgtypeHstore | Unset = UNSET
    org_id: str | Unset = UNSET
    runner_process_id: str | Unset = UNSET
    status: str | Unset = UNSET
    status_description: str | Unset = UNSET
    type_: AppRunnerProcessShutdownType | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        composite_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.composite_status, Unset):
            composite_status = self.composite_status.to_dict()

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        org_id = self.org_id

        runner_process_id = self.runner_process_id

        status = self.status

        status_description = self.status_description

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if composite_status is not UNSET:
            field_dict["composite_status"] = composite_status
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if runner_process_id is not UNSET:
            field_dict["runner_process_id"] = runner_process_id
        if status is not UNSET:
            field_dict["status"] = status
        if status_description is not UNSET:
            field_dict["status_description"] = status_description
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_composite_status import AppCompositeStatus
        from ..models.pgtype_hstore import PgtypeHstore

        d = dict(src_dict)
        _composite_status = d.pop("composite_status", UNSET)
        composite_status: AppCompositeStatus | Unset
        if isinstance(_composite_status, Unset):
            composite_status = UNSET
        else:
            composite_status = AppCompositeStatus.from_dict(_composite_status)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: PgtypeHstore | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PgtypeHstore.from_dict(_metadata)

        org_id = d.pop("org_id", UNSET)

        runner_process_id = d.pop("runner_process_id", UNSET)

        status = d.pop("status", UNSET)

        status_description = d.pop("status_description", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: AppRunnerProcessShutdownType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AppRunnerProcessShutdownType(_type_)

        updated_at = d.pop("updated_at", UNSET)

        app_runner_process_shutdown = cls(
            composite_status=composite_status,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            metadata=metadata,
            org_id=org_id,
            runner_process_id=runner_process_id,
            status=status,
            status_description=status_description,
            type_=type_,
            updated_at=updated_at,
        )

        app_runner_process_shutdown.additional_properties = d
        return app_runner_process_shutdown

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
