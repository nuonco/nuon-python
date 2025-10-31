from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_app_runner_type import AppAppRunnerType
from ..models.app_runner_group_type import AppRunnerGroupType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_runner import AppRunner
    from ..models.app_runner_group_settings import AppRunnerGroupSettings


T = TypeVar("T", bound="AppRunnerGroup")


@_attrs_define
class AppRunnerGroup:
    """
    Attributes:
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        org_id (str | Unset):
        owner_id (str | Unset): parent can org, install or in the future, builtin runner group
        owner_type (str | Unset):
        platform (AppAppRunnerType | Unset):
        runners (list[AppRunner] | Unset):
        settings (AppRunnerGroupSettings | Unset):
        type_ (AppRunnerGroupType | Unset):
        updated_at (str | Unset):
    """

    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    org_id: str | Unset = UNSET
    owner_id: str | Unset = UNSET
    owner_type: str | Unset = UNSET
    platform: AppAppRunnerType | Unset = UNSET
    runners: list[AppRunner] | Unset = UNSET
    settings: AppRunnerGroupSettings | Unset = UNSET
    type_: AppRunnerGroupType | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        org_id = self.org_id

        owner_id = self.owner_id

        owner_type = self.owner_type

        platform: str | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        runners: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.runners, Unset):
            runners = []
            for runners_item_data in self.runners:
                runners_item = runners_item_data.to_dict()
                runners.append(runners_item)

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if owner_type is not UNSET:
            field_dict["owner_type"] = owner_type
        if platform is not UNSET:
            field_dict["platform"] = platform
        if runners is not UNSET:
            field_dict["runners"] = runners
        if settings is not UNSET:
            field_dict["settings"] = settings
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_runner import AppRunner
        from ..models.app_runner_group_settings import AppRunnerGroupSettings

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        org_id = d.pop("org_id", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        owner_type = d.pop("owner_type", UNSET)

        _platform = d.pop("platform", UNSET)
        platform: AppAppRunnerType | Unset
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = AppAppRunnerType(_platform)

        runners = []
        _runners = d.pop("runners", UNSET)
        for runners_item_data in _runners or []:
            runners_item = AppRunner.from_dict(runners_item_data)

            runners.append(runners_item)

        _settings = d.pop("settings", UNSET)
        settings: AppRunnerGroupSettings | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = AppRunnerGroupSettings.from_dict(_settings)

        _type_ = d.pop("type", UNSET)
        type_: AppRunnerGroupType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AppRunnerGroupType(_type_)

        updated_at = d.pop("updated_at", UNSET)

        app_runner_group = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            org_id=org_id,
            owner_id=owner_id,
            owner_type=owner_type,
            platform=platform,
            runners=runners,
            settings=settings,
            type_=type_,
            updated_at=updated_at,
        )

        app_runner_group.additional_properties = d
        return app_runner_group

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
