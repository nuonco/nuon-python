from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_nuonco_nuon_pkg_labels_labels import GithubComNuoncoNuonPkgLabelsLabels


T = TypeVar("T", bound="ServiceAppFleetInstall")


@_attrs_define
class ServiceAppFleetInstall:
    """
    Attributes:
        app_branch_group (str | Unset):
        app_branch_id (str | Unset):
        app_config_id (str | Unset):
        applied_config_id (str | Unset):
        health (str | Unset):
        id (str | Unset):
        labels (GithubComNuoncoNuonPkgLabelsLabels | Unset):
        name (str | Unset):
        rollout (str | Unset):
        runner_status (str | Unset):
    """

    app_branch_group: str | Unset = UNSET
    app_branch_id: str | Unset = UNSET
    app_config_id: str | Unset = UNSET
    applied_config_id: str | Unset = UNSET
    health: str | Unset = UNSET
    id: str | Unset = UNSET
    labels: GithubComNuoncoNuonPkgLabelsLabels | Unset = UNSET
    name: str | Unset = UNSET
    rollout: str | Unset = UNSET
    runner_status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_branch_group = self.app_branch_group

        app_branch_id = self.app_branch_id

        app_config_id = self.app_config_id

        applied_config_id = self.applied_config_id

        health = self.health

        id = self.id

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        name = self.name

        rollout = self.rollout

        runner_status = self.runner_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_branch_group is not UNSET:
            field_dict["app_branch_group"] = app_branch_group
        if app_branch_id is not UNSET:
            field_dict["app_branch_id"] = app_branch_id
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if applied_config_id is not UNSET:
            field_dict["applied_config_id"] = applied_config_id
        if health is not UNSET:
            field_dict["health"] = health
        if id is not UNSET:
            field_dict["id"] = id
        if labels is not UNSET:
            field_dict["labels"] = labels
        if name is not UNSET:
            field_dict["name"] = name
        if rollout is not UNSET:
            field_dict["rollout"] = rollout
        if runner_status is not UNSET:
            field_dict["runner_status"] = runner_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_nuonco_nuon_pkg_labels_labels import GithubComNuoncoNuonPkgLabelsLabels  # noqa: PLC0415

        d = dict(src_dict)
        app_branch_group = d.pop("app_branch_group", UNSET)

        app_branch_id = d.pop("app_branch_id", UNSET)

        app_config_id = d.pop("app_config_id", UNSET)

        applied_config_id = d.pop("applied_config_id", UNSET)

        health = d.pop("health", UNSET)

        id = d.pop("id", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: GithubComNuoncoNuonPkgLabelsLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = GithubComNuoncoNuonPkgLabelsLabels.from_dict(_labels)

        name = d.pop("name", UNSET)

        rollout = d.pop("rollout", UNSET)

        runner_status = d.pop("runner_status", UNSET)

        service_app_fleet_install = cls(
            app_branch_group=app_branch_group,
            app_branch_id=app_branch_id,
            app_config_id=app_config_id,
            applied_config_id=applied_config_id,
            health=health,
            id=id,
            labels=labels,
            name=name,
            rollout=rollout,
            runner_status=runner_status,
        )

        service_app_fleet_install.additional_properties = d
        return service_app_fleet_install

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
