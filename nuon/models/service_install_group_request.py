from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceInstallGroupRequest")


@_attrs_define
class ServiceInstallGroupRequest:
    """
    Attributes:
        name (str):
        install_ids (list[str] | Unset):
        max_parallel (int | Unset):
        order (int | Unset):
        requires_approval (bool | Unset):
        rollback_on_failure (bool | Unset):
    """

    name: str
    install_ids: list[str] | Unset = UNSET
    max_parallel: int | Unset = UNSET
    order: int | Unset = UNSET
    requires_approval: bool | Unset = UNSET
    rollback_on_failure: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        install_ids: list[str] | Unset = UNSET
        if not isinstance(self.install_ids, Unset):
            install_ids = self.install_ids

        max_parallel = self.max_parallel

        order = self.order

        requires_approval = self.requires_approval

        rollback_on_failure = self.rollback_on_failure

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if install_ids is not UNSET:
            field_dict["install_ids"] = install_ids
        if max_parallel is not UNSET:
            field_dict["max_parallel"] = max_parallel
        if order is not UNSET:
            field_dict["order"] = order
        if requires_approval is not UNSET:
            field_dict["requires_approval"] = requires_approval
        if rollback_on_failure is not UNSET:
            field_dict["rollback_on_failure"] = rollback_on_failure

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        install_ids = cast(list[str], d.pop("install_ids", UNSET))

        max_parallel = d.pop("max_parallel", UNSET)

        order = d.pop("order", UNSET)

        requires_approval = d.pop("requires_approval", UNSET)

        rollback_on_failure = d.pop("rollback_on_failure", UNSET)

        service_install_group_request = cls(
            name=name,
            install_ids=install_ids,
            max_parallel=max_parallel,
            order=order,
            requires_approval=requires_approval,
            rollback_on_failure=rollback_on_failure,
        )

        service_install_group_request.additional_properties = d
        return service_install_group_request

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
