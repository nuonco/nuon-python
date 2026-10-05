from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_install_activity import ServiceInstallActivity


T = TypeVar("T", bound="ServiceGetInstallActivityResponse")


@_attrs_define
class ServiceGetInstallActivityResponse:
    """
    Attributes:
        activity (list[ServiceInstallActivity] | Unset):
        has_more (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):
        page (int | Unset):
    """

    activity: list[ServiceInstallActivity] | Unset = UNSET
    has_more: bool | Unset = UNSET
    limit: int | Unset = UNSET
    offset: int | Unset = UNSET
    page: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.activity, Unset):
            activity = []
            for activity_item_data in self.activity:
                activity_item = activity_item_data.to_dict()
                activity.append(activity_item)

        has_more = self.has_more

        limit = self.limit

        offset = self.offset

        page = self.page

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activity is not UNSET:
            field_dict["activity"] = activity
        if has_more is not UNSET:
            field_dict["has_more"] = has_more
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset
        if page is not UNSET:
            field_dict["page"] = page

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_install_activity import ServiceInstallActivity  # noqa: PLC0415

        d = dict(src_dict)
        _activity = d.pop("activity", UNSET)
        activity: list[ServiceInstallActivity] | Unset = UNSET
        if _activity is not UNSET:
            activity = []
            for activity_item_data in _activity:
                activity_item = ServiceInstallActivity.from_dict(activity_item_data)

                activity.append(activity_item)

        has_more = d.pop("has_more", UNSET)

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        page = d.pop("page", UNSET)

        service_get_install_activity_response = cls(
            activity=activity,
            has_more=has_more,
            limit=limit,
            offset=offset,
            page=page,
        )

        service_get_install_activity_response.additional_properties = d
        return service_get_install_activity_response

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
