from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_app_config_status import AppAppConfigStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceUpdateAppConfigRequest")


@_attrs_define
class ServiceUpdateAppConfigRequest:
    """
    Attributes:
        component_ids (Union[Unset, list[str]]):
        state (Union[Unset, str]):
        status (Union[Unset, AppAppConfigStatus]):
        status_description (Union[Unset, str]):
    """

    component_ids: Union[Unset, list[str]] = UNSET
    state: Union[Unset, str] = UNSET
    status: Union[Unset, AppAppConfigStatus] = UNSET
    status_description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.component_ids, Unset):
            component_ids = self.component_ids

        state = self.state

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        status_description = self.status_description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if component_ids is not UNSET:
            field_dict["component_ids"] = component_ids
        if state is not UNSET:
            field_dict["state"] = state
        if status is not UNSET:
            field_dict["status"] = status
        if status_description is not UNSET:
            field_dict["status_description"] = status_description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        component_ids = cast(list[str], d.pop("component_ids", UNSET))

        state = d.pop("state", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, AppAppConfigStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppAppConfigStatus(_status)

        status_description = d.pop("status_description", UNSET)

        service_update_app_config_request = cls(
            component_ids=component_ids,
            state=state,
            status=status,
            status_description=status_description,
        )

        service_update_app_config_request.additional_properties = d
        return service_update_app_config_request

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
