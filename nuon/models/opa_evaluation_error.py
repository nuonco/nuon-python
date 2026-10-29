from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpaEvaluationError")


@_attrs_define
class OpaEvaluationError:
    """
    Attributes:
        code (str | Unset):
        input_identity (str | Unset):
        input_index (int | Unset):
        message (str | Unset):
    """

    code: str | Unset = UNSET
    input_identity: str | Unset = UNSET
    input_index: int | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        input_identity = self.input_identity

        input_index = self.input_index

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if input_identity is not UNSET:
            field_dict["input_identity"] = input_identity
        if input_index is not UNSET:
            field_dict["input_index"] = input_index
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        input_identity = d.pop("input_identity", UNSET)

        input_index = d.pop("input_index", UNSET)

        message = d.pop("message", UNSET)

        opa_evaluation_error = cls(
            code=code,
            input_identity=input_identity,
            input_index=input_index,
            message=message,
        )

        opa_evaluation_error.additional_properties = d
        return opa_evaluation_error

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
