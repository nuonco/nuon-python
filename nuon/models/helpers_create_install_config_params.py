from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_install_approval_option import AppInstallApprovalOption
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_custom_nested_stack import ConfigCustomNestedStack
    from ..models.helpers_create_install_config_params_labels import HelpersCreateInstallConfigParamsLabels


T = TypeVar("T", bound="HelpersCreateInstallConfigParams")


@_attrs_define
class HelpersCreateInstallConfigParams:
    """
    Attributes:
        approval_option (AppInstallApprovalOption | Unset):
        custom_nested_stacks (list[ConfigCustomNestedStack] | Unset):
        labels (HelpersCreateInstallConfigParamsLabels | Unset):
        runner_nested_template_url (str | Unset):
        vpc_nested_template_url (str | Unset):
    """

    approval_option: AppInstallApprovalOption | Unset = UNSET
    custom_nested_stacks: list[ConfigCustomNestedStack] | Unset = UNSET
    labels: HelpersCreateInstallConfigParamsLabels | Unset = UNSET
    runner_nested_template_url: str | Unset = UNSET
    vpc_nested_template_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        approval_option: str | Unset = UNSET
        if not isinstance(self.approval_option, Unset):
            approval_option = self.approval_option.value

        custom_nested_stacks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_nested_stacks, Unset):
            custom_nested_stacks = []
            for custom_nested_stacks_item_data in self.custom_nested_stacks:
                custom_nested_stacks_item = custom_nested_stacks_item_data.to_dict()
                custom_nested_stacks.append(custom_nested_stacks_item)

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        runner_nested_template_url = self.runner_nested_template_url

        vpc_nested_template_url = self.vpc_nested_template_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if approval_option is not UNSET:
            field_dict["approval_option"] = approval_option
        if custom_nested_stacks is not UNSET:
            field_dict["custom_nested_stacks"] = custom_nested_stacks
        if labels is not UNSET:
            field_dict["labels"] = labels
        if runner_nested_template_url is not UNSET:
            field_dict["runner_nested_template_url"] = runner_nested_template_url
        if vpc_nested_template_url is not UNSET:
            field_dict["vpc_nested_template_url"] = vpc_nested_template_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_custom_nested_stack import ConfigCustomNestedStack
        from ..models.helpers_create_install_config_params_labels import HelpersCreateInstallConfigParamsLabels

        d = dict(src_dict)
        _approval_option = d.pop("approval_option", UNSET)
        approval_option: AppInstallApprovalOption | Unset
        if isinstance(_approval_option, Unset):
            approval_option = UNSET
        else:
            approval_option = AppInstallApprovalOption(_approval_option)

        _custom_nested_stacks = d.pop("custom_nested_stacks", UNSET)
        custom_nested_stacks: list[ConfigCustomNestedStack] | Unset = UNSET
        if _custom_nested_stacks is not UNSET:
            custom_nested_stacks = []
            for custom_nested_stacks_item_data in _custom_nested_stacks:
                custom_nested_stacks_item = ConfigCustomNestedStack.from_dict(custom_nested_stacks_item_data)

                custom_nested_stacks.append(custom_nested_stacks_item)

        _labels = d.pop("labels", UNSET)
        labels: HelpersCreateInstallConfigParamsLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = HelpersCreateInstallConfigParamsLabels.from_dict(_labels)

        runner_nested_template_url = d.pop("runner_nested_template_url", UNSET)

        vpc_nested_template_url = d.pop("vpc_nested_template_url", UNSET)

        helpers_create_install_config_params = cls(
            approval_option=approval_option,
            custom_nested_stacks=custom_nested_stacks,
            labels=labels,
            runner_nested_template_url=runner_nested_template_url,
            vpc_nested_template_url=vpc_nested_template_url,
        )

        helpers_create_install_config_params.additional_properties = d
        return helpers_create_install_config_params

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
