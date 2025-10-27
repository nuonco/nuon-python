from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_install_approval_option import AppInstallApprovalOption
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServicePatchInstallConfigParams")


@_attrs_define
class ServicePatchInstallConfigParams:
    """
    Attributes:
        approval_option (Union[Unset, AppInstallApprovalOption]):
    """

    approval_option: Union[Unset, AppInstallApprovalOption] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        approval_option: Union[Unset, str] = UNSET
        if not isinstance(self.approval_option, Unset):
            approval_option = self.approval_option.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if approval_option is not UNSET:
            field_dict["approval_option"] = approval_option

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _approval_option = d.pop("approval_option", UNSET)
        approval_option: Union[Unset, AppInstallApprovalOption]
        if isinstance(_approval_option, Unset):
            approval_option = UNSET
        else:
            approval_option = AppInstallApprovalOption(_approval_option)

        service_patch_install_config_params = cls(
            approval_option=approval_option,
        )

        service_patch_install_config_params.additional_properties = d
        return service_patch_install_config_params

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
