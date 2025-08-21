from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceCreateComponentBuildRequest")


@_attrs_define
class ServiceCreateComponentBuildRequest:
    """
    Attributes:
        git_ref (Union[Unset, str]):
        use_latest (Union[Unset, bool]):
    """

    git_ref: Union[Unset, str] = UNSET
    use_latest: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        git_ref = self.git_ref

        use_latest = self.use_latest

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if git_ref is not UNSET:
            field_dict["git_ref"] = git_ref
        if use_latest is not UNSET:
            field_dict["use_latest"] = use_latest

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        git_ref = d.pop("git_ref", UNSET)

        use_latest = d.pop("use_latest", UNSET)

        service_create_component_build_request = cls(
            git_ref=git_ref,
            use_latest=use_latest,
        )

        service_create_component_build_request.additional_properties = d
        return service_create_component_build_request

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
