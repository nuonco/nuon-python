from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_app_label_key_summary import ServiceAppLabelKeySummary
    from ..models.service_app_labels_response_label_colors import ServiceAppLabelsResponseLabelColors


T = TypeVar("T", bound="ServiceAppLabelsResponse")


@_attrs_define
class ServiceAppLabelsResponse:
    """
    Attributes:
        default_colors (list[str] | Unset):
        label_colors (ServiceAppLabelsResponseLabelColors | Unset):
        labels (list[ServiceAppLabelKeySummary] | Unset):
    """

    default_colors: list[str] | Unset = UNSET
    label_colors: ServiceAppLabelsResponseLabelColors | Unset = UNSET
    labels: list[ServiceAppLabelKeySummary] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_colors: list[str] | Unset = UNSET
        if not isinstance(self.default_colors, Unset):
            default_colors = self.default_colors

        label_colors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.label_colors, Unset):
            label_colors = self.label_colors.to_dict()

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_colors is not UNSET:
            field_dict["default_colors"] = default_colors
        if label_colors is not UNSET:
            field_dict["label_colors"] = label_colors
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_app_label_key_summary import ServiceAppLabelKeySummary
        from ..models.service_app_labels_response_label_colors import ServiceAppLabelsResponseLabelColors

        d = dict(src_dict)
        default_colors = cast(list[str], d.pop("default_colors", UNSET))

        _label_colors = d.pop("label_colors", UNSET)
        label_colors: ServiceAppLabelsResponseLabelColors | Unset
        if isinstance(_label_colors, Unset):
            label_colors = UNSET
        else:
            label_colors = ServiceAppLabelsResponseLabelColors.from_dict(_label_colors)

        _labels = d.pop("labels", UNSET)
        labels: list[ServiceAppLabelKeySummary] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = ServiceAppLabelKeySummary.from_dict(labels_item_data)

                labels.append(labels_item)

        service_app_labels_response = cls(
            default_colors=default_colors,
            label_colors=label_colors,
            labels=labels,
        )

        service_app_labels_response.additional_properties = d
        return service_app_labels_response

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
