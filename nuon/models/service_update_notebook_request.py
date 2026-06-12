from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_update_notebook_request_status import ServiceUpdateNotebookRequestStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceUpdateNotebookRequest")


@_attrs_define
class ServiceUpdateNotebookRequest:
    """
    Attributes:
        description (str | Unset):
        name (str | Unset):
        status (ServiceUpdateNotebookRequestStatus | Unset):
    """

    description: str | Unset = UNSET
    name: str | Unset = UNSET
    status: ServiceUpdateNotebookRequestStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        name = self.name

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        _status = d.pop("status", UNSET)
        status: ServiceUpdateNotebookRequestStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ServiceUpdateNotebookRequestStatus(_status)

        service_update_notebook_request = cls(
            description=description,
            name=name,
            status=status,
        )

        service_update_notebook_request.additional_properties = d
        return service_update_notebook_request

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
