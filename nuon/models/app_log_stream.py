from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_log_stream_attrs import AppLogStreamAttrs


T = TypeVar("T", bound="AppLogStream")


@_attrs_define
class AppLogStream:
    """
    Attributes:
        attrs (Union[Unset, AppLogStreamAttrs]):
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        id (Union[Unset, str]):
        open_ (Union[Unset, bool]):
        org_id (Union[Unset, str]):
        owner_id (Union[Unset, str]):
        owner_type (Union[Unset, str]):
        runner_api_url (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        write_token (Union[Unset, str]):
    """

    attrs: Union[Unset, "AppLogStreamAttrs"] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    open_: Union[Unset, bool] = UNSET
    org_id: Union[Unset, str] = UNSET
    owner_id: Union[Unset, str] = UNSET
    owner_type: Union[Unset, str] = UNSET
    runner_api_url: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    write_token: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attrs: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.attrs, Unset):
            attrs = self.attrs.to_dict()

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        open_ = self.open_

        org_id = self.org_id

        owner_id = self.owner_id

        owner_type = self.owner_type

        runner_api_url = self.runner_api_url

        updated_at = self.updated_at

        write_token = self.write_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attrs is not UNSET:
            field_dict["attrs"] = attrs
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if open_ is not UNSET:
            field_dict["open"] = open_
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if owner_type is not UNSET:
            field_dict["owner_type"] = owner_type
        if runner_api_url is not UNSET:
            field_dict["runner_api_url"] = runner_api_url
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if write_token is not UNSET:
            field_dict["write_token"] = write_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_log_stream_attrs import AppLogStreamAttrs

        d = dict(src_dict)
        _attrs = d.pop("attrs", UNSET)
        attrs: Union[Unset, AppLogStreamAttrs]
        if isinstance(_attrs, Unset):
            attrs = UNSET
        else:
            attrs = AppLogStreamAttrs.from_dict(_attrs)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        open_ = d.pop("open", UNSET)

        org_id = d.pop("org_id", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        owner_type = d.pop("owner_type", UNSET)

        runner_api_url = d.pop("runner_api_url", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        write_token = d.pop("write_token", UNSET)

        app_log_stream = cls(
            attrs=attrs,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            open_=open_,
            org_id=org_id,
            owner_id=owner_id,
            owner_type=owner_type,
            runner_api_url=runner_api_url,
            updated_at=updated_at,
            write_token=write_token,
        )

        app_log_stream.additional_properties = d
        return app_log_stream

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
