from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.service_add_action_labels_request_labels import ServiceAddActionLabelsRequestLabels


T = TypeVar("T", bound="ServiceAddActionLabelsRequest")


@_attrs_define
class ServiceAddActionLabelsRequest:
    """
    Attributes:
        labels (ServiceAddActionLabelsRequestLabels):
    """

    labels: ServiceAddActionLabelsRequestLabels
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        labels = self.labels.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "labels": labels,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_add_action_labels_request_labels import ServiceAddActionLabelsRequestLabels

        d = dict(src_dict)
        labels = ServiceAddActionLabelsRequestLabels.from_dict(d.pop("labels"))

        service_add_action_labels_request = cls(
            labels=labels,
        )

        service_add_action_labels_request.additional_properties = d
        return service_add_action_labels_request

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
