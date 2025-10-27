from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppLatestRunnerHeartBeat")


@_attrs_define
class AppLatestRunnerHeartBeat:
    """
    Attributes:
        alive_time (Union[Unset, int]):
        created_at (Union[Unset, str]):
        process (Union[Unset, str]):
        runner_id (Union[Unset, str]):
        started_at (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    alive_time: Union[Unset, int] = UNSET
    created_at: Union[Unset, str] = UNSET
    process: Union[Unset, str] = UNSET
    runner_id: Union[Unset, str] = UNSET
    started_at: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alive_time = self.alive_time

        created_at = self.created_at

        process = self.process

        runner_id = self.runner_id

        started_at = self.started_at

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alive_time is not UNSET:
            field_dict["alive_time"] = alive_time
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if process is not UNSET:
            field_dict["process"] = process
        if runner_id is not UNSET:
            field_dict["runner_id"] = runner_id
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        alive_time = d.pop("alive_time", UNSET)

        created_at = d.pop("created_at", UNSET)

        process = d.pop("process", UNSET)

        runner_id = d.pop("runner_id", UNSET)

        started_at = d.pop("started_at", UNSET)

        version = d.pop("version", UNSET)

        app_latest_runner_heart_beat = cls(
            alive_time=alive_time,
            created_at=created_at,
            process=process,
            runner_id=runner_id,
            started_at=started_at,
            version=version,
        )

        app_latest_runner_heart_beat.additional_properties = d
        return app_latest_runner_heart_beat

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
