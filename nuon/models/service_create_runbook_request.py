from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_create_runbook_request_labels import ServiceCreateRunbookRequestLabels


T = TypeVar("T", bound="ServiceCreateRunbookRequest")


@_attrs_define
class ServiceCreateRunbookRequest:
    """
    Attributes:
        name (str):
        description (str | Unset):
        labels (ServiceCreateRunbookRequestLabels | Unset):
    """

    name: str
    description: str | Unset = UNSET
    labels: ServiceCreateRunbookRequestLabels | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_create_runbook_request_labels import ServiceCreateRunbookRequestLabels

        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: ServiceCreateRunbookRequestLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = ServiceCreateRunbookRequestLabels.from_dict(_labels)

        service_create_runbook_request = cls(
            name=name,
            description=description,
            labels=labels,
        )

        service_create_runbook_request.additional_properties = d
        return service_create_runbook_request

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
