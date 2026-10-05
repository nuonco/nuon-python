from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_install_deployment_config_change import ServiceInstallDeploymentConfigChange


T = TypeVar("T", bound="ServiceInstallDeploymentChangeGroup")


@_attrs_define
class ServiceInstallDeploymentChangeGroup:
    """
    Attributes:
        changes (list[ServiceInstallDeploymentConfigChange] | Unset):
        diff_language (str | Unset):
        file_diff (str | Unset):
        id (str | Unset):
        label (str | Unset):
        resource_name (str | Unset):
        scope (str | Unset):
        summary (str | Unset):
    """

    changes: list[ServiceInstallDeploymentConfigChange] | Unset = UNSET
    diff_language: str | Unset = UNSET
    file_diff: str | Unset = UNSET
    id: str | Unset = UNSET
    label: str | Unset = UNSET
    resource_name: str | Unset = UNSET
    scope: str | Unset = UNSET
    summary: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        changes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.changes, Unset):
            changes = []
            for changes_item_data in self.changes:
                changes_item = changes_item_data.to_dict()
                changes.append(changes_item)

        diff_language = self.diff_language

        file_diff = self.file_diff

        id = self.id

        label = self.label

        resource_name = self.resource_name

        scope = self.scope

        summary = self.summary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if changes is not UNSET:
            field_dict["changes"] = changes
        if diff_language is not UNSET:
            field_dict["diff_language"] = diff_language
        if file_diff is not UNSET:
            field_dict["file_diff"] = file_diff
        if id is not UNSET:
            field_dict["id"] = id
        if label is not UNSET:
            field_dict["label"] = label
        if resource_name is not UNSET:
            field_dict["resource_name"] = resource_name
        if scope is not UNSET:
            field_dict["scope"] = scope
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_install_deployment_config_change import (
            ServiceInstallDeploymentConfigChange,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _changes = d.pop("changes", UNSET)
        changes: list[ServiceInstallDeploymentConfigChange] | Unset = UNSET
        if _changes is not UNSET:
            changes = []
            for changes_item_data in _changes:
                changes_item = ServiceInstallDeploymentConfigChange.from_dict(changes_item_data)

                changes.append(changes_item)

        diff_language = d.pop("diff_language", UNSET)

        file_diff = d.pop("file_diff", UNSET)

        id = d.pop("id", UNSET)

        label = d.pop("label", UNSET)

        resource_name = d.pop("resource_name", UNSET)

        scope = d.pop("scope", UNSET)

        summary = d.pop("summary", UNSET)

        service_install_deployment_change_group = cls(
            changes=changes,
            diff_language=diff_language,
            file_diff=file_diff,
            id=id,
            label=label,
            resource_name=resource_name,
            scope=scope,
            summary=summary,
        )

        service_install_deployment_change_group.additional_properties = d
        return service_install_deployment_change_group

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
