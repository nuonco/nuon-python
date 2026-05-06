from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_update_current_org_webhook_request_interests import (
        ServiceUpdateCurrentOrgWebhookRequestInterests,
    )


T = TypeVar("T", bound="ServiceUpdateCurrentOrgWebhookRequest")


@_attrs_define
class ServiceUpdateCurrentOrgWebhookRequest:
    """
    Attributes:
        interests (ServiceUpdateCurrentOrgWebhookRequestInterests | Unset):
        webhook_secret (str | Unset):
    """

    interests: ServiceUpdateCurrentOrgWebhookRequestInterests | Unset = UNSET
    webhook_secret: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interests: dict[str, Any] | Unset = UNSET
        if not isinstance(self.interests, Unset):
            interests = self.interests.to_dict()

        webhook_secret = self.webhook_secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interests is not UNSET:
            field_dict["interests"] = interests
        if webhook_secret is not UNSET:
            field_dict["webhook_secret"] = webhook_secret

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_update_current_org_webhook_request_interests import (
            ServiceUpdateCurrentOrgWebhookRequestInterests,
        )

        d = dict(src_dict)
        _interests = d.pop("interests", UNSET)
        interests: ServiceUpdateCurrentOrgWebhookRequestInterests | Unset
        if isinstance(_interests, Unset):
            interests = UNSET
        else:
            interests = ServiceUpdateCurrentOrgWebhookRequestInterests.from_dict(_interests)

        webhook_secret = d.pop("webhook_secret", UNSET)

        service_update_current_org_webhook_request = cls(
            interests=interests,
            webhook_secret=webhook_secret,
        )

        service_update_current_org_webhook_request.additional_properties = d
        return service_update_current_org_webhook_request

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
