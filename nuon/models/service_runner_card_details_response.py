from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_runner import AppRunner
    from ..models.app_runner_heart_beat import AppRunnerHeartBeat


T = TypeVar("T", bound="ServiceRunnerCardDetailsResponse")


@_attrs_define
class ServiceRunnerCardDetailsResponse:
    """
    Attributes:
        latest_heart_beat (AppRunnerHeartBeat | Unset):
        runner (AppRunner | Unset):
    """

    latest_heart_beat: AppRunnerHeartBeat | Unset = UNSET
    runner: AppRunner | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        latest_heart_beat: dict[str, Any] | Unset = UNSET
        if not isinstance(self.latest_heart_beat, Unset):
            latest_heart_beat = self.latest_heart_beat.to_dict()

        runner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.runner, Unset):
            runner = self.runner.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if latest_heart_beat is not UNSET:
            field_dict["latest_heart_beat"] = latest_heart_beat
        if runner is not UNSET:
            field_dict["runner"] = runner

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_runner import AppRunner
        from ..models.app_runner_heart_beat import AppRunnerHeartBeat

        d = dict(src_dict)
        _latest_heart_beat = d.pop("latest_heart_beat", UNSET)
        latest_heart_beat: AppRunnerHeartBeat | Unset
        if isinstance(_latest_heart_beat, Unset):
            latest_heart_beat = UNSET
        else:
            latest_heart_beat = AppRunnerHeartBeat.from_dict(_latest_heart_beat)

        _runner = d.pop("runner", UNSET)
        runner: AppRunner | Unset
        if isinstance(_runner, Unset):
            runner = UNSET
        else:
            runner = AppRunner.from_dict(_runner)

        service_runner_card_details_response = cls(
            latest_heart_beat=latest_heart_beat,
            runner=runner,
        )

        service_runner_card_details_response.additional_properties = d
        return service_runner_card_details_response

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
