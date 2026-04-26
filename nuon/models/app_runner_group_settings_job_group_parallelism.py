from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AppRunnerGroupSettingsJobGroupParallelism")


@_attrs_define
class AppRunnerGroupSettingsJobGroupParallelism:
    """JobGroupParallelism maps RunnerJobGroup names to max-in-flight counts for queue-based job routing.
    e.g., {"build": "2", "deploy": "1"}. Only used when parallel-runner-jobs feature flag is on.

    """

    additional_properties: dict[str, str] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_runner_group_settings_job_group_parallelism = cls()

        app_runner_group_settings_job_group_parallelism.additional_properties = d
        return app_runner_group_settings_job_group_parallelism

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
