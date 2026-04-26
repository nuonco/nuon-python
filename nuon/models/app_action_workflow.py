from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_action_workflow_config import AppActionWorkflowConfig
    from ..models.app_composite_status import AppCompositeStatus
    from ..models.github_com_nuonco_nuon_pkg_labels_labels import GithubComNuoncoNuonPkgLabelsLabels


T = TypeVar("T", bound="AppActionWorkflow")


@_attrs_define
class AppActionWorkflow:
    """
    Attributes:
        app_id (str | Unset):
        config_count (int | Unset):
        configs (list[AppActionWorkflowConfig] | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        labels (GithubComNuoncoNuonPkgLabelsLabels | Unset):
        name (str | Unset): metadata
        status (str | Unset): TODO: change to default null after migration & after initial pr
        status_description (str | Unset):
        status_v2 (AppCompositeStatus | Unset):
        updated_at (str | Unset):
    """

    app_id: str | Unset = UNSET
    config_count: int | Unset = UNSET
    configs: list[AppActionWorkflowConfig] | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    labels: GithubComNuoncoNuonPkgLabelsLabels | Unset = UNSET
    name: str | Unset = UNSET
    status: str | Unset = UNSET
    status_description: str | Unset = UNSET
    status_v2: AppCompositeStatus | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        config_count = self.config_count

        configs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.configs, Unset):
            configs = []
            for configs_item_data in self.configs:
                configs_item = configs_item_data.to_dict()
                configs.append(configs_item)

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        name = self.name

        status = self.status

        status_description = self.status_description

        status_v2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status_v2, Unset):
            status_v2 = self.status_v2.to_dict()

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if config_count is not UNSET:
            field_dict["config_count"] = config_count
        if configs is not UNSET:
            field_dict["configs"] = configs
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if labels is not UNSET:
            field_dict["labels"] = labels
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if status_description is not UNSET:
            field_dict["status_description"] = status_description
        if status_v2 is not UNSET:
            field_dict["status_v2"] = status_v2
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_action_workflow_config import AppActionWorkflowConfig
        from ..models.app_composite_status import AppCompositeStatus
        from ..models.github_com_nuonco_nuon_pkg_labels_labels import GithubComNuoncoNuonPkgLabelsLabels

        d = dict(src_dict)
        app_id = d.pop("app_id", UNSET)

        config_count = d.pop("config_count", UNSET)

        _configs = d.pop("configs", UNSET)
        configs: list[AppActionWorkflowConfig] | Unset = UNSET
        if _configs is not UNSET:
            configs = []
            for configs_item_data in _configs:
                configs_item = AppActionWorkflowConfig.from_dict(configs_item_data)

                configs.append(configs_item)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: GithubComNuoncoNuonPkgLabelsLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = GithubComNuoncoNuonPkgLabelsLabels.from_dict(_labels)

        name = d.pop("name", UNSET)

        status = d.pop("status", UNSET)

        status_description = d.pop("status_description", UNSET)

        _status_v2 = d.pop("status_v2", UNSET)
        status_v2: AppCompositeStatus | Unset
        if isinstance(_status_v2, Unset):
            status_v2 = UNSET
        else:
            status_v2 = AppCompositeStatus.from_dict(_status_v2)

        updated_at = d.pop("updated_at", UNSET)

        app_action_workflow = cls(
            app_id=app_id,
            config_count=config_count,
            configs=configs,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            labels=labels,
            name=name,
            status=status,
            status_description=status_description,
            status_v2=status_v2,
            updated_at=updated_at,
        )

        app_action_workflow.additional_properties = d
        return app_action_workflow

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
