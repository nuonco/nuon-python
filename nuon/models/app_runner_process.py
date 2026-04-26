from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_runner_process_type import AppRunnerProcessType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_composite_status import AppCompositeStatus
    from ..models.app_runner_process_shutdown import AppRunnerProcessShutdown


T = TypeVar("T", bound="AppRunnerProcess")


@_attrs_define
class AppRunnerProcess:
    """
    Attributes:
        composite_status (AppCompositeStatus | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        initial_health_check (bool | Unset):
        labels (list[str] | Unset): Labels are computed server-side and not persisted.
        log_stream_id (str | Unset):
        org_id (str | Unset):
        runner_id (str | Unset):
        shutdowns (list[AppRunnerProcessShutdown] | Unset):
        started_at (str | Unset):
        type_ (AppRunnerProcessType | Unset):
        updated_at (str | Unset):
        uptime (int | Unset):
        version (str | Unset):
        warnings (list[str] | Unset): Warnings are computed server-side and not persisted.
    """

    composite_status: AppCompositeStatus | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    initial_health_check: bool | Unset = UNSET
    labels: list[str] | Unset = UNSET
    log_stream_id: str | Unset = UNSET
    org_id: str | Unset = UNSET
    runner_id: str | Unset = UNSET
    shutdowns: list[AppRunnerProcessShutdown] | Unset = UNSET
    started_at: str | Unset = UNSET
    type_: AppRunnerProcessType | Unset = UNSET
    updated_at: str | Unset = UNSET
    uptime: int | Unset = UNSET
    version: str | Unset = UNSET
    warnings: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        composite_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.composite_status, Unset):
            composite_status = self.composite_status.to_dict()

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        initial_health_check = self.initial_health_check

        labels: list[str] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        log_stream_id = self.log_stream_id

        org_id = self.org_id

        runner_id = self.runner_id

        shutdowns: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.shutdowns, Unset):
            shutdowns = []
            for shutdowns_item_data in self.shutdowns:
                shutdowns_item = shutdowns_item_data.to_dict()
                shutdowns.append(shutdowns_item)

        started_at = self.started_at

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at = self.updated_at

        uptime = self.uptime

        version = self.version

        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

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
        if initial_health_check is not UNSET:
            field_dict["initial_health_check"] = initial_health_check
        if labels is not UNSET:
            field_dict["labels"] = labels
        if log_stream_id is not UNSET:
            field_dict["log_stream_id"] = log_stream_id
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if runner_id is not UNSET:
            field_dict["runner_id"] = runner_id
        if shutdowns is not UNSET:
            field_dict["shutdowns"] = shutdowns
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if uptime is not UNSET:
            field_dict["uptime"] = uptime
        if version is not UNSET:
            field_dict["version"] = version
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_composite_status import AppCompositeStatus
        from ..models.app_runner_process_shutdown import AppRunnerProcessShutdown

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

        initial_health_check = d.pop("initial_health_check", UNSET)

        labels = cast(list[str], d.pop("labels", UNSET))

        log_stream_id = d.pop("log_stream_id", UNSET)

        org_id = d.pop("org_id", UNSET)

        runner_id = d.pop("runner_id", UNSET)

        _shutdowns = d.pop("shutdowns", UNSET)
        shutdowns: list[AppRunnerProcessShutdown] | Unset = UNSET
        if _shutdowns is not UNSET:
            shutdowns = []
            for shutdowns_item_data in _shutdowns:
                shutdowns_item = AppRunnerProcessShutdown.from_dict(shutdowns_item_data)

                shutdowns.append(shutdowns_item)

        started_at = d.pop("started_at", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: AppRunnerProcessType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AppRunnerProcessType(_type_)

        updated_at = d.pop("updated_at", UNSET)

        uptime = d.pop("uptime", UNSET)

        version = d.pop("version", UNSET)

        warnings = cast(list[str], d.pop("warnings", UNSET))

        app_runner_process = cls(
            composite_status=composite_status,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            initial_health_check=initial_health_check,
            labels=labels,
            log_stream_id=log_stream_id,
            org_id=org_id,
            runner_id=runner_id,
            shutdowns=shutdowns,
            started_at=started_at,
            type_=type_,
            updated_at=updated_at,
            uptime=uptime,
            version=version,
            warnings=warnings,
        )

        app_runner_process.additional_properties = d
        return app_runner_process

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
