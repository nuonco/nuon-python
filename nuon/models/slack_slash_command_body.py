from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SlackSlashCommandBody")


@_attrs_define
class SlackSlashCommandBody:
    """
    Attributes:
        channel_id (str): Channel ID the command was invoked in
        command (str): The slash command itself (e.g. /nuon)
        team_id (str): Slack team (workspace) ID
        user_id (str): Slack user ID who invoked the command
        channel_name (str | Unset): Channel name
        text (str | Unset): Subcommand text
    """

    channel_id: str
    command: str
    team_id: str
    user_id: str
    channel_name: str | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_id = self.channel_id

        command = self.command

        team_id = self.team_id

        user_id = self.user_id

        channel_name = self.channel_name

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channel_id": channel_id,
                "command": command,
                "team_id": team_id,
                "user_id": user_id,
            }
        )
        if channel_name is not UNSET:
            field_dict["channel_name"] = channel_name
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        channel_id = d.pop("channel_id")

        command = d.pop("command")

        team_id = d.pop("team_id")

        user_id = d.pop("user_id")

        channel_name = d.pop("channel_name", UNSET)

        text = d.pop("text", UNSET)

        slack_slash_command_body = cls(
            channel_id=channel_id,
            command=command,
            team_id=team_id,
            user_id=user_id,
            channel_name=channel_name,
            text=text,
        )

        slack_slash_command_body.additional_properties = d
        return slack_slash_command_body

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
