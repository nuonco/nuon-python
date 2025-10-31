from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_user_journey_step_metadata import AppUserJourneyStepMetadata


T = TypeVar("T", bound="AppUserJourneyStep")


@_attrs_define
class AppUserJourneyStep:
    """
    Attributes:
        complete (bool | Unset):
        completed_at (str | Unset): Top-level completion tracking fields
        completion_method (str | Unset):
        completion_source (str | Unset):
        metadata (AppUserJourneyStepMetadata | Unset): Flexible metadata for business data
        name (str | Unset):
        title (str | Unset):
    """

    complete: bool | Unset = UNSET
    completed_at: str | Unset = UNSET
    completion_method: str | Unset = UNSET
    completion_source: str | Unset = UNSET
    metadata: AppUserJourneyStepMetadata | Unset = UNSET
    name: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        complete = self.complete

        completed_at = self.completed_at

        completion_method = self.completion_method

        completion_source = self.completion_source

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        name = self.name

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if complete is not UNSET:
            field_dict["complete"] = complete
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if completion_method is not UNSET:
            field_dict["completion_method"] = completion_method
        if completion_source is not UNSET:
            field_dict["completion_source"] = completion_source
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_user_journey_step_metadata import AppUserJourneyStepMetadata

        d = dict(src_dict)
        complete = d.pop("complete", UNSET)

        completed_at = d.pop("completed_at", UNSET)

        completion_method = d.pop("completion_method", UNSET)

        completion_source = d.pop("completion_source", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: AppUserJourneyStepMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = AppUserJourneyStepMetadata.from_dict(_metadata)

        name = d.pop("name", UNSET)

        title = d.pop("title", UNSET)

        app_user_journey_step = cls(
            complete=complete,
            completed_at=completed_at,
            completion_method=completion_method,
            completion_source=completion_source,
            metadata=metadata,
            name=name,
            title=title,
        )

        app_user_journey_step.additional_properties = d
        return app_user_journey_step

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
