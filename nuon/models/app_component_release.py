from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_component_release_step import AppComponentReleaseStep


T = TypeVar("T", bound="AppComponentRelease")


@_attrs_define
class AppComponentRelease:
    """
    Attributes:
        build_id (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        release_steps (list[AppComponentReleaseStep] | Unset):
        status (str | Unset):
        status_description (str | Unset):
        total_release_steps (int | Unset):
        updated_at (str | Unset):
    """

    build_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    release_steps: list[AppComponentReleaseStep] | Unset = UNSET
    status: str | Unset = UNSET
    status_description: str | Unset = UNSET
    total_release_steps: int | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        build_id = self.build_id

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        release_steps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.release_steps, Unset):
            release_steps = []
            for release_steps_item_data in self.release_steps:
                release_steps_item = release_steps_item_data.to_dict()
                release_steps.append(release_steps_item)

        status = self.status

        status_description = self.status_description

        total_release_steps = self.total_release_steps

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if build_id is not UNSET:
            field_dict["build_id"] = build_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if release_steps is not UNSET:
            field_dict["release_steps"] = release_steps
        if status is not UNSET:
            field_dict["status"] = status
        if status_description is not UNSET:
            field_dict["status_description"] = status_description
        if total_release_steps is not UNSET:
            field_dict["total_release_steps"] = total_release_steps
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_component_release_step import AppComponentReleaseStep

        d = dict(src_dict)
        build_id = d.pop("build_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        release_steps = []
        _release_steps = d.pop("release_steps", UNSET)
        for release_steps_item_data in _release_steps or []:
            release_steps_item = AppComponentReleaseStep.from_dict(release_steps_item_data)

            release_steps.append(release_steps_item)

        status = d.pop("status", UNSET)

        status_description = d.pop("status_description", UNSET)

        total_release_steps = d.pop("total_release_steps", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_component_release = cls(
            build_id=build_id,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            release_steps=release_steps,
            status=status,
            status_description=status_description,
            total_release_steps=total_release_steps,
            updated_at=updated_at,
        )

        app_component_release.additional_properties = d
        return app_component_release

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
