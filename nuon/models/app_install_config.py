from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_install_approval_option import AppInstallApprovalOption
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_custom_nested_stack import ConfigCustomNestedStack
    from ..models.github_com_nuonco_nuon_pkg_labels_labels import GithubComNuoncoNuonPkgLabelsLabels


T = TypeVar("T", bound="AppInstallConfig")


@_attrs_define
class AppInstallConfig:
    """
    Attributes:
        approval_option (AppInstallApprovalOption | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        custom_nested_stacks (list[ConfigCustomNestedStack] | Unset):
        id (str | Unset):
        install_id (str | Unset):
        labels (GithubComNuoncoNuonPkgLabelsLabels | Unset):
        org_id (str | Unset):
        runner_nested_template_url (str | Unset):
        updated_at (str | Unset):
        vpc_nested_template_url (str | Unset): Per-install stack template overrides (nil = use app config default)
    """

    approval_option: AppInstallApprovalOption | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    custom_nested_stacks: list[ConfigCustomNestedStack] | Unset = UNSET
    id: str | Unset = UNSET
    install_id: str | Unset = UNSET
    labels: GithubComNuoncoNuonPkgLabelsLabels | Unset = UNSET
    org_id: str | Unset = UNSET
    runner_nested_template_url: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    vpc_nested_template_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        approval_option: str | Unset = UNSET
        if not isinstance(self.approval_option, Unset):
            approval_option = self.approval_option.value

        created_at = self.created_at

        created_by_id = self.created_by_id

        custom_nested_stacks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_nested_stacks, Unset):
            custom_nested_stacks = []
            for custom_nested_stacks_item_data in self.custom_nested_stacks:
                custom_nested_stacks_item = custom_nested_stacks_item_data.to_dict()
                custom_nested_stacks.append(custom_nested_stacks_item)

        id = self.id

        install_id = self.install_id

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        org_id = self.org_id

        runner_nested_template_url = self.runner_nested_template_url

        updated_at = self.updated_at

        vpc_nested_template_url = self.vpc_nested_template_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if approval_option is not UNSET:
            field_dict["approval_option"] = approval_option
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if custom_nested_stacks is not UNSET:
            field_dict["custom_nested_stacks"] = custom_nested_stacks
        if id is not UNSET:
            field_dict["id"] = id
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if labels is not UNSET:
            field_dict["labels"] = labels
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if runner_nested_template_url is not UNSET:
            field_dict["runner_nested_template_url"] = runner_nested_template_url
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if vpc_nested_template_url is not UNSET:
            field_dict["vpc_nested_template_url"] = vpc_nested_template_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_custom_nested_stack import ConfigCustomNestedStack
        from ..models.github_com_nuonco_nuon_pkg_labels_labels import GithubComNuoncoNuonPkgLabelsLabels

        d = dict(src_dict)
        _approval_option = d.pop("approval_option", UNSET)
        approval_option: AppInstallApprovalOption | Unset
        if isinstance(_approval_option, Unset):
            approval_option = UNSET
        else:
            approval_option = AppInstallApprovalOption(_approval_option)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        _custom_nested_stacks = d.pop("custom_nested_stacks", UNSET)
        custom_nested_stacks: list[ConfigCustomNestedStack] | Unset = UNSET
        if _custom_nested_stacks is not UNSET:
            custom_nested_stacks = []
            for custom_nested_stacks_item_data in _custom_nested_stacks:
                custom_nested_stacks_item = ConfigCustomNestedStack.from_dict(custom_nested_stacks_item_data)

                custom_nested_stacks.append(custom_nested_stacks_item)

        id = d.pop("id", UNSET)

        install_id = d.pop("install_id", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: GithubComNuoncoNuonPkgLabelsLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = GithubComNuoncoNuonPkgLabelsLabels.from_dict(_labels)

        org_id = d.pop("org_id", UNSET)

        runner_nested_template_url = d.pop("runner_nested_template_url", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        vpc_nested_template_url = d.pop("vpc_nested_template_url", UNSET)

        app_install_config = cls(
            approval_option=approval_option,
            created_at=created_at,
            created_by_id=created_by_id,
            custom_nested_stacks=custom_nested_stacks,
            id=id,
            install_id=install_id,
            labels=labels,
            org_id=org_id,
            runner_nested_template_url=runner_nested_template_url,
            updated_at=updated_at,
            vpc_nested_template_url=vpc_nested_template_url,
        )

        app_install_config.additional_properties = d
        return app_install_config

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
