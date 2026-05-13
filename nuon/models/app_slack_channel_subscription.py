from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_slack_channel_subscription_interests import AppSlackChannelSubscriptionInterests
    from ..models.app_slack_channel_subscription_match import AppSlackChannelSubscriptionMatch


T = TypeVar("T", bound="AppSlackChannelSubscription")


@_attrs_define
class AppSlackChannelSubscription:
    """
    Attributes:
        channel_id (str | Unset):
        channel_name (str | Unset):
        created_at (str | Unset):
        created_by_account_id (str | Unset):
        created_by_id (str | Unset):
        created_by_slack_user_id (str | Unset):
        id (str | Unset):
        interests (AppSlackChannelSubscriptionInterests | Unset): Interests is the per-subscription event filter. Stored
            as JSONB; one
            shape is shared with webhooks (see internal/pkg/interests). New rows
            default to AllEvents=true via the create handler when the request omits
            the field.
        match (AppSlackChannelSubscriptionMatch | Unset): Match is the per-subscription routing predicate. Nil = match
            every
            event in the org. Non-nil = evaluated by labels.SubscriptionMatch
            against the dispatch-time labels.EventTargets. swaggertype:"object"
            keeps the SDK from materialising the full nested type tree.
        org_id (str | Unset): OrgID is denormalized from OrgLink for query convenience.
        org_link_id (str | Unset):
        team_id (str | Unset):
        updated_at (str | Unset):
    """

    channel_id: str | Unset = UNSET
    channel_name: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_account_id: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    created_by_slack_user_id: str | Unset = UNSET
    id: str | Unset = UNSET
    interests: AppSlackChannelSubscriptionInterests | Unset = UNSET
    match: AppSlackChannelSubscriptionMatch | Unset = UNSET
    org_id: str | Unset = UNSET
    org_link_id: str | Unset = UNSET
    team_id: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_id = self.channel_id

        channel_name = self.channel_name

        created_at = self.created_at

        created_by_account_id = self.created_by_account_id

        created_by_id = self.created_by_id

        created_by_slack_user_id = self.created_by_slack_user_id

        id = self.id

        interests: dict[str, Any] | Unset = UNSET
        if not isinstance(self.interests, Unset):
            interests = self.interests.to_dict()

        match: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match, Unset):
            match = self.match.to_dict()

        org_id = self.org_id

        org_link_id = self.org_link_id

        team_id = self.team_id

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if channel_name is not UNSET:
            field_dict["channel_name"] = channel_name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_account_id is not UNSET:
            field_dict["created_by_account_id"] = created_by_account_id
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if created_by_slack_user_id is not UNSET:
            field_dict["created_by_slack_user_id"] = created_by_slack_user_id
        if id is not UNSET:
            field_dict["id"] = id
        if interests is not UNSET:
            field_dict["interests"] = interests
        if match is not UNSET:
            field_dict["match"] = match
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if org_link_id is not UNSET:
            field_dict["org_link_id"] = org_link_id
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_slack_channel_subscription_interests import AppSlackChannelSubscriptionInterests
        from ..models.app_slack_channel_subscription_match import AppSlackChannelSubscriptionMatch

        d = dict(src_dict)
        channel_id = d.pop("channel_id", UNSET)

        channel_name = d.pop("channel_name", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_account_id = d.pop("created_by_account_id", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        created_by_slack_user_id = d.pop("created_by_slack_user_id", UNSET)

        id = d.pop("id", UNSET)

        _interests = d.pop("interests", UNSET)
        interests: AppSlackChannelSubscriptionInterests | Unset
        if isinstance(_interests, Unset):
            interests = UNSET
        else:
            interests = AppSlackChannelSubscriptionInterests.from_dict(_interests)

        _match = d.pop("match", UNSET)
        match: AppSlackChannelSubscriptionMatch | Unset
        if isinstance(_match, Unset):
            match = UNSET
        else:
            match = AppSlackChannelSubscriptionMatch.from_dict(_match)

        org_id = d.pop("org_id", UNSET)

        org_link_id = d.pop("org_link_id", UNSET)

        team_id = d.pop("team_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_slack_channel_subscription = cls(
            channel_id=channel_id,
            channel_name=channel_name,
            created_at=created_at,
            created_by_account_id=created_by_account_id,
            created_by_id=created_by_id,
            created_by_slack_user_id=created_by_slack_user_id,
            id=id,
            interests=interests,
            match=match,
            org_id=org_id,
            org_link_id=org_link_id,
            team_id=team_id,
            updated_at=updated_at,
        )

        app_slack_channel_subscription.additional_properties = d
        return app_slack_channel_subscription

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
