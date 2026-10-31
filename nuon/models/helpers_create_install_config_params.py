from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_install_approval_option import AppInstallApprovalOption
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_custom_nested_stack import ConfigCustomNestedStack
    from ..models.config_install_telemetry import ConfigInstallTelemetry
    from ..models.helpers_create_install_config_params_labels import HelpersCreateInstallConfigParamsLabels


T = TypeVar("T", bound="HelpersCreateInstallConfigParams")


@_attrs_define
class HelpersCreateInstallConfigParams:
    """
    Attributes:
        action_timeout (int | None | Unset):
        approval_option (AppInstallApprovalOption | Unset):
        custom_nested_stacks (list[ConfigCustomNestedStack] | Unset):
        labels (HelpersCreateInstallConfigParamsLabels | Unset):
        runner_image_auto_update (bool | None | Unset):
        runner_image_id (str | Unset):
        runner_nested_template_url (str | Unset):
        telemetry (ConfigInstallTelemetry | Unset):
        vpc_nested_template_url (str | Unset):
    """

    action_timeout: int | None | Unset = UNSET
    approval_option: AppInstallApprovalOption | Unset = UNSET
    custom_nested_stacks: list[ConfigCustomNestedStack] | Unset = UNSET
    labels: HelpersCreateInstallConfigParamsLabels | Unset = UNSET
    runner_image_auto_update: bool | None | Unset = UNSET
    runner_image_id: str | Unset = UNSET
    runner_nested_template_url: str | Unset = UNSET
    telemetry: ConfigInstallTelemetry | Unset = UNSET
    vpc_nested_template_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_timeout: int | None | Unset
        if isinstance(self.action_timeout, Unset):
            action_timeout = UNSET
        else:
            action_timeout = self.action_timeout

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

        runner_image_auto_update: bool | None | Unset
        if isinstance(self.runner_image_auto_update, Unset):
            runner_image_auto_update = UNSET
        else:
            runner_image_auto_update = self.runner_image_auto_update

        runner_image_id = self.runner_image_id

        runner_nested_template_url = self.runner_nested_template_url

        telemetry: dict[str, Any] | Unset = UNSET
        if not isinstance(self.telemetry, Unset):
            telemetry = self.telemetry.to_dict()

        vpc_nested_template_url = self.vpc_nested_template_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action_timeout is not UNSET:
            field_dict["action_timeout"] = action_timeout
        if approval_option is not UNSET:
            field_dict["approval_option"] = approval_option
        if custom_nested_stacks is not UNSET:
            field_dict["custom_nested_stacks"] = custom_nested_stacks
        if labels is not UNSET:
            field_dict["labels"] = labels
        if runner_image_auto_update is not UNSET:
            field_dict["runner_image_auto_update"] = runner_image_auto_update
        if runner_image_id is not UNSET:
            field_dict["runner_image_id"] = runner_image_id
        if runner_nested_template_url is not UNSET:
            field_dict["runner_nested_template_url"] = runner_nested_template_url
        if telemetry is not UNSET:
            field_dict["telemetry"] = telemetry
        if vpc_nested_template_url is not UNSET:
            field_dict["vpc_nested_template_url"] = vpc_nested_template_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_custom_nested_stack import ConfigCustomNestedStack  # noqa: PLC0415
        from ..models.config_install_telemetry import ConfigInstallTelemetry  # noqa: PLC0415
        from ..models.helpers_create_install_config_params_labels import HelpersCreateInstallConfigParamsLabels  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_action_timeout(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        action_timeout = _parse_action_timeout(d.pop("action_timeout", UNSET))

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

        def _parse_runner_image_auto_update(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        runner_image_auto_update = _parse_runner_image_auto_update(d.pop("runner_image_auto_update", UNSET))

        runner_image_id = d.pop("runner_image_id", UNSET)

        runner_nested_template_url = d.pop("runner_nested_template_url", UNSET)

        _telemetry = d.pop("telemetry", UNSET)
        telemetry: ConfigInstallTelemetry | Unset
        if isinstance(_telemetry, Unset):
            telemetry = UNSET
        else:
            telemetry = ConfigInstallTelemetry.from_dict(_telemetry)

        vpc_nested_template_url = d.pop("vpc_nested_template_url", UNSET)

        helpers_create_install_config_params = cls(
            action_timeout=action_timeout,
            approval_option=approval_option,
            custom_nested_stacks=custom_nested_stacks,
            labels=labels,
            runner_image_auto_update=runner_image_auto_update,
            runner_image_id=runner_image_id,
            runner_nested_template_url=runner_nested_template_url,
            telemetry=telemetry,
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
