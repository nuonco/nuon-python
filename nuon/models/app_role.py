from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_role_type import AppRoleType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_account import AppAccount
    from ..models.app_policy import AppPolicy


T = TypeVar("T", bound="AppRole")


@_attrs_define
class AppRole:
    """
    Attributes:
        created_by (Union[Unset, AppAccount]):
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        id (Union[Unset, str]):
        policies (Union[Unset, list['AppPolicy']]):
        role_type (Union[Unset, AppRoleType]):
        updated_at (Union[Unset, str]):
    """

    created_by: Union[Unset, "AppAccount"] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    policies: Union[Unset, list["AppPolicy"]] = UNSET
    role_type: Union[Unset, AppRoleType] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        policies: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.policies, Unset):
            policies = []
            for policies_item_data in self.policies:
                policies_item = policies_item_data.to_dict()
                policies.append(policies_item)

        role_type: Union[Unset, str] = UNSET
        if not isinstance(self.role_type, Unset):
            role_type = self.role_type.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if policies is not UNSET:
            field_dict["policies"] = policies
        if role_type is not UNSET:
            field_dict["role_type"] = role_type
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_account import AppAccount
        from ..models.app_policy import AppPolicy

        d = dict(src_dict)
        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, AppAccount]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = AppAccount.from_dict(_created_by)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        policies = []
        _policies = d.pop("policies", UNSET)
        for policies_item_data in _policies or []:
            policies_item = AppPolicy.from_dict(policies_item_data)

            policies.append(policies_item)

        _role_type = d.pop("role_type", UNSET)
        role_type: Union[Unset, AppRoleType]
        if isinstance(_role_type, Unset):
            role_type = UNSET
        else:
            role_type = AppRoleType(_role_type)

        updated_at = d.pop("updated_at", UNSET)

        app_role = cls(
            created_by=created_by,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            policies=policies,
            role_type=role_type,
            updated_at=updated_at,
        )

        app_role.additional_properties = d
        return app_role

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
