from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_workflow import AppWorkflow


T = TypeVar("T", bound="AppAppBranch")


@_attrs_define
class AppAppBranch:
    """
    Attributes:
        app_id (str | Unset):
        connected_github_vcs_config_id (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        name (str | Unset):
        org_id (str | Unset):
        updated_at (str | Unset):
        workflows (list[AppWorkflow] | Unset):
    """

    app_id: str | Unset = UNSET
    connected_github_vcs_config_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    org_id: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    workflows: list[AppWorkflow] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        connected_github_vcs_config_id = self.connected_github_vcs_config_id

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        name = self.name

        org_id = self.org_id

        updated_at = self.updated_at

        workflows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.workflows, Unset):
            workflows = []
            for workflows_item_data in self.workflows:
                workflows_item = workflows_item_data.to_dict()
                workflows.append(workflows_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if connected_github_vcs_config_id is not UNSET:
            field_dict["connected_github_vcs_config_id"] = connected_github_vcs_config_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if workflows is not UNSET:
            field_dict["workflows"] = workflows

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_workflow import AppWorkflow

        d = dict(src_dict)
        app_id = d.pop("app_id", UNSET)

        connected_github_vcs_config_id = d.pop("connected_github_vcs_config_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        org_id = d.pop("org_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _workflows = d.pop("workflows", UNSET)
        workflows: list[AppWorkflow] | Unset = UNSET
        if _workflows is not UNSET:
            workflows = []
            for workflows_item_data in _workflows:
                workflows_item = AppWorkflow.from_dict(workflows_item_data)

                workflows.append(workflows_item)

        app_app_branch = cls(
            app_id=app_id,
            connected_github_vcs_config_id=connected_github_vcs_config_id,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            name=name,
            org_id=org_id,
            updated_at=updated_at,
            workflows=workflows,
        )

        app_app_branch.additional_properties = d
        return app_app_branch

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
