from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_create_channel_subscription_request_interests import (
        ServiceCreateChannelSubscriptionRequestInterests,
    )
    from ..models.service_create_channel_subscription_request_match import ServiceCreateChannelSubscriptionRequestMatch


T = TypeVar("T", bound="ServiceCreateChannelSubscriptionRequest")


@_attrs_define
class ServiceCreateChannelSubscriptionRequest:
    """
    Attributes:
        channel_id (str):
        org_link_id (str):
        channel_name (str | Unset):
        interests (ServiceCreateChannelSubscriptionRequestInterests | Unset):
        match (ServiceCreateChannelSubscriptionRequestMatch | Unset):
    """

    channel_id: str
    org_link_id: str
    channel_name: str | Unset = UNSET
    interests: ServiceCreateChannelSubscriptionRequestInterests | Unset = UNSET
    match: ServiceCreateChannelSubscriptionRequestMatch | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_id = self.channel_id

        org_link_id = self.org_link_id

        channel_name = self.channel_name

        interests: dict[str, Any] | Unset = UNSET
        if not isinstance(self.interests, Unset):
            interests = self.interests.to_dict()

        match: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match, Unset):
            match = self.match.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channel_id": channel_id,
                "org_link_id": org_link_id,
            }
        )
        if channel_name is not UNSET:
            field_dict["channel_name"] = channel_name
        if interests is not UNSET:
            field_dict["interests"] = interests
        if match is not UNSET:
            field_dict["match"] = match

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_create_channel_subscription_request_interests import (
            ServiceCreateChannelSubscriptionRequestInterests,
        )
        from ..models.service_create_channel_subscription_request_match import (
            ServiceCreateChannelSubscriptionRequestMatch,
        )

        d = dict(src_dict)
        channel_id = d.pop("channel_id")

        org_link_id = d.pop("org_link_id")

        channel_name = d.pop("channel_name", UNSET)

        _interests = d.pop("interests", UNSET)
        interests: ServiceCreateChannelSubscriptionRequestInterests | Unset
        if isinstance(_interests, Unset):
            interests = UNSET
        else:
            interests = ServiceCreateChannelSubscriptionRequestInterests.from_dict(_interests)

        _match = d.pop("match", UNSET)
        match: ServiceCreateChannelSubscriptionRequestMatch | Unset
        if isinstance(_match, Unset):
            match = UNSET
        else:
            match = ServiceCreateChannelSubscriptionRequestMatch.from_dict(_match)

        service_create_channel_subscription_request = cls(
            channel_id=channel_id,
            org_link_id=org_link_id,
            channel_name=channel_name,
            interests=interests,
            match=match,
        )

        service_create_channel_subscription_request.additional_properties = d
        return service_create_channel_subscription_request

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
