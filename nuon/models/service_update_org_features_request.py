from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.service_update_org_features_request_features import ServiceUpdateOrgFeaturesRequestFeatures


T = TypeVar("T", bound="ServiceUpdateOrgFeaturesRequest")


@_attrs_define
class ServiceUpdateOrgFeaturesRequest:
    """
    Attributes:
        features (ServiceUpdateOrgFeaturesRequestFeatures):
    """

    features: ServiceUpdateOrgFeaturesRequestFeatures
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        features = self.features.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "features": features,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_update_org_features_request_features import ServiceUpdateOrgFeaturesRequestFeatures

        d = dict(src_dict)
        features = ServiceUpdateOrgFeaturesRequestFeatures.from_dict(d.pop("features"))

        service_update_org_features_request = cls(
            features=features,
        )

        service_update_org_features_request.additional_properties = d
        return service_update_org_features_request

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
