from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_complete_your_stack_step_request_app_type import ServiceCompleteYourStackStepRequestAppType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceCompleteYourStackStepRequest")


@_attrs_define
class ServiceCompleteYourStackStepRequest:
    """
    Attributes:
        app_type (ServiceCompleteYourStackStepRequestAppType):
        app_attributes (list[str] | Unset):
        cloud_provider (str | Unset):
        example_app_slug (str | Unset):
    """

    app_type: ServiceCompleteYourStackStepRequestAppType
    app_attributes: list[str] | Unset = UNSET
    cloud_provider: str | Unset = UNSET
    example_app_slug: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_type = self.app_type.value

        app_attributes: list[str] | Unset = UNSET
        if not isinstance(self.app_attributes, Unset):
            app_attributes = self.app_attributes

        cloud_provider = self.cloud_provider

        example_app_slug = self.example_app_slug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app_type": app_type,
            }
        )
        if app_attributes is not UNSET:
            field_dict["app_attributes"] = app_attributes
        if cloud_provider is not UNSET:
            field_dict["cloud_provider"] = cloud_provider
        if example_app_slug is not UNSET:
            field_dict["example_app_slug"] = example_app_slug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_type = ServiceCompleteYourStackStepRequestAppType(d.pop("app_type"))

        app_attributes = cast(list[str], d.pop("app_attributes", UNSET))

        cloud_provider = d.pop("cloud_provider", UNSET)

        example_app_slug = d.pop("example_app_slug", UNSET)

        service_complete_your_stack_step_request = cls(
            app_type=app_type,
            app_attributes=app_attributes,
            cloud_provider=cloud_provider,
            example_app_slug=example_app_slug,
        )

        service_complete_your_stack_step_request.additional_properties = d
        return service_complete_your_stack_step_request

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
