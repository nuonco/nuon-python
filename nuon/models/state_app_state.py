from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.state_app_state_secrets import StateAppStateSecrets


T = TypeVar("T", bound="StateAppState")


@_attrs_define
class StateAppState:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        populated (Union[Unset, bool]):
        secrets (Union[Unset, StateAppStateSecrets]):
        status (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    populated: Union[Unset, bool] = UNSET
    secrets: Union[Unset, "StateAppStateSecrets"] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        populated = self.populated

        secrets: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.secrets, Unset):
            secrets = self.secrets.to_dict()

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if populated is not UNSET:
            field_dict["populated"] = populated
        if secrets is not UNSET:
            field_dict["secrets"] = secrets
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.state_app_state_secrets import StateAppStateSecrets

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        populated = d.pop("populated", UNSET)

        _secrets = d.pop("secrets", UNSET)
        secrets: Union[Unset, StateAppStateSecrets]
        if isinstance(_secrets, Unset):
            secrets = UNSET
        else:
            secrets = StateAppStateSecrets.from_dict(_secrets)

        status = d.pop("status", UNSET)

        state_app_state = cls(
            id=id,
            name=name,
            populated=populated,
            secrets=secrets,
            status=status,
        )

        state_app_state.additional_properties = d
        return state_app_state

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
