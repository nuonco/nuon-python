from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceInstallDeploymentSourceBuild")


@_attrs_define
class ServiceInstallDeploymentSourceBuild:
    """
    Attributes:
        commit (str | Unset):
        coverage (str | Unset):
        digest (str | Unset):
        id (str | Unset):
        repository (str | Unset):
        root (str | Unset):
    """

    commit: str | Unset = UNSET
    coverage: str | Unset = UNSET
    digest: str | Unset = UNSET
    id: str | Unset = UNSET
    repository: str | Unset = UNSET
    root: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        commit = self.commit

        coverage = self.coverage

        digest = self.digest

        id = self.id

        repository = self.repository

        root = self.root

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if commit is not UNSET:
            field_dict["commit"] = commit
        if coverage is not UNSET:
            field_dict["coverage"] = coverage
        if digest is not UNSET:
            field_dict["digest"] = digest
        if id is not UNSET:
            field_dict["id"] = id
        if repository is not UNSET:
            field_dict["repository"] = repository
        if root is not UNSET:
            field_dict["root"] = root

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        commit = d.pop("commit", UNSET)

        coverage = d.pop("coverage", UNSET)

        digest = d.pop("digest", UNSET)

        id = d.pop("id", UNSET)

        repository = d.pop("repository", UNSET)

        root = d.pop("root", UNSET)

        service_install_deployment_source_build = cls(
            commit=commit,
            coverage=coverage,
            digest=digest,
            id=id,
            repository=repository,
            root=root,
        )

        service_install_deployment_source_build.additional_properties = d
        return service_install_deployment_source_build

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
