from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceCreateOrgRequest")


@_attrs_define
class ServiceCreateOrgRequest:
    """
    Attributes:
        name (str):
        use_sandbox_mode (Union[Unset, bool]): These fields are used to control the behaviour of the org.
    """

    name: str
    use_sandbox_mode: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        use_sandbox_mode = self.use_sandbox_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if use_sandbox_mode is not UNSET:
            field_dict["use_sandbox_mode"] = use_sandbox_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        use_sandbox_mode = d.pop("use_sandbox_mode", UNSET)

        service_create_org_request = cls(
            name=name,
            use_sandbox_mode=use_sandbox_mode,
        )

        service_create_org_request.additional_properties = d
        return service_create_org_request

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
