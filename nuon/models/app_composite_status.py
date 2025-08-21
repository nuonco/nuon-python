from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_status import AppStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_composite_status_metadata import AppCompositeStatusMetadata


T = TypeVar("T", bound="AppCompositeStatus")


@_attrs_define
class AppCompositeStatus:
    """
    Attributes:
        created_at_ts (Union[Unset, int]):
        created_by_id (Union[Unset, str]):
        history (Union[Unset, list['AppCompositeStatus']]):
        metadata (Union[Unset, AppCompositeStatusMetadata]):
        status (Union[Unset, AppStatus]):
        status_human_description (Union[Unset, str]):
    """

    created_at_ts: Union[Unset, int] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    history: Union[Unset, list["AppCompositeStatus"]] = UNSET
    metadata: Union[Unset, "AppCompositeStatusMetadata"] = UNSET
    status: Union[Unset, AppStatus] = UNSET
    status_human_description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at_ts = self.created_at_ts

        created_by_id = self.created_by_id

        history: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.history, Unset):
            history = []
            for history_item_data in self.history:
                history_item = history_item_data.to_dict()
                history.append(history_item)

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        status_human_description = self.status_human_description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at_ts is not UNSET:
            field_dict["created_at_ts"] = created_at_ts
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if history is not UNSET:
            field_dict["history"] = history
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if status is not UNSET:
            field_dict["status"] = status
        if status_human_description is not UNSET:
            field_dict["status_human_description"] = status_human_description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_composite_status_metadata import AppCompositeStatusMetadata

        d = dict(src_dict)
        created_at_ts = d.pop("created_at_ts", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        history = []
        _history = d.pop("history", UNSET)
        for history_item_data in _history or []:
            history_item = AppCompositeStatus.from_dict(history_item_data)

            history.append(history_item)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, AppCompositeStatusMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = AppCompositeStatusMetadata.from_dict(_metadata)

        _status = d.pop("status", UNSET)
        status: Union[Unset, AppStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppStatus(_status)

        status_human_description = d.pop("status_human_description", UNSET)

        app_composite_status = cls(
            created_at_ts=created_at_ts,
            created_by_id=created_by_id,
            history=history,
            metadata=metadata,
            status=status,
            status_human_description=status_human_description,
        )

        app_composite_status.additional_properties = d
        return app_composite_status

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
