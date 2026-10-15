from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_account import AppAccount


T = TypeVar("T", bound="AppActionRunTrigger")


@_attrs_define
class AppActionRunTrigger:
    """
    Attributes:
        actor (AppAccount | Unset):
        parent_id (str | Unset):
        parent_name (str | Unset):
        parent_type (str | Unset):
        type_ (str | Unset):
    """

    actor: AppAccount | Unset = UNSET
    parent_id: str | Unset = UNSET
    parent_name: str | Unset = UNSET
    parent_type: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        actor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actor, Unset):
            actor = self.actor.to_dict()

        parent_id = self.parent_id

        parent_name = self.parent_name

        parent_type = self.parent_type

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if actor is not UNSET:
            field_dict["actor"] = actor
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if parent_name is not UNSET:
            field_dict["parent_name"] = parent_name
        if parent_type is not UNSET:
            field_dict["parent_type"] = parent_type
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_account import AppAccount  # noqa: PLC0415

        d = dict(src_dict)
        _actor = d.pop("actor", UNSET)
        actor: AppAccount | Unset
        if isinstance(_actor, Unset):
            actor = UNSET
        else:
            actor = AppAccount.from_dict(_actor)

        parent_id = d.pop("parent_id", UNSET)

        parent_name = d.pop("parent_name", UNSET)

        parent_type = d.pop("parent_type", UNSET)

        type_ = d.pop("type", UNSET)

        app_action_run_trigger = cls(
            actor=actor,
            parent_id=parent_id,
            parent_name=parent_name,
            parent_type=parent_type,
            type_=type_,
        )

        app_action_run_trigger.additional_properties = d
        return app_action_run_trigger

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
