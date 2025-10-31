from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_account import AppAccount
    from ..models.app_component_config_connection import AppComponentConfigConnection
    from ..models.app_component_release import AppComponentRelease
    from ..models.app_composite_status import AppCompositeStatus
    from ..models.app_install_deploy import AppInstallDeploy
    from ..models.app_log_stream import AppLogStream
    from ..models.app_runner_job import AppRunnerJob
    from ..models.app_vcs_connection_commit import AppVCSConnectionCommit


T = TypeVar("T", bound="AppComponentBuild")


@_attrs_define
class AppComponentBuild:
    """
    Attributes:
        checksum (str | Unset): checksum of our intermediate component config
        component_config_connection (AppComponentConfigConnection | Unset):
        component_config_connection_id (str | Unset): DEPRECATED: will retain the field to connect against the last
            component config connection that set this build
        component_config_version (int | Unset):
        component_id (str | Unset): Read-only fields set on the object to de-nest data
        component_name (str | Unset):
        created_at (str | Unset):
        created_by (AppAccount | Unset):
        created_by_id (str | Unset):
        git_ref (str | Unset):
        id (str | Unset):
        install_deploys (list[AppInstallDeploy] | Unset):
        log_stream (AppLogStream | Unset):
        releases (list[AppComponentRelease] | Unset):
        runner_job (AppRunnerJob | Unset):
        status (str | Unset):
        status_description (str | Unset):
        status_v2 (AppCompositeStatus | Unset):
        updated_at (str | Unset):
        vcs_connection_commit (AppVCSConnectionCommit | Unset):
    """

    checksum: str | Unset = UNSET
    component_config_connection: AppComponentConfigConnection | Unset = UNSET
    component_config_connection_id: str | Unset = UNSET
    component_config_version: int | Unset = UNSET
    component_id: str | Unset = UNSET
    component_name: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by: AppAccount | Unset = UNSET
    created_by_id: str | Unset = UNSET
    git_ref: str | Unset = UNSET
    id: str | Unset = UNSET
    install_deploys: list[AppInstallDeploy] | Unset = UNSET
    log_stream: AppLogStream | Unset = UNSET
    releases: list[AppComponentRelease] | Unset = UNSET
    runner_job: AppRunnerJob | Unset = UNSET
    status: str | Unset = UNSET
    status_description: str | Unset = UNSET
    status_v2: AppCompositeStatus | Unset = UNSET
    updated_at: str | Unset = UNSET
    vcs_connection_commit: AppVCSConnectionCommit | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        checksum = self.checksum

        component_config_connection: dict[str, Any] | Unset = UNSET
        if not isinstance(self.component_config_connection, Unset):
            component_config_connection = self.component_config_connection.to_dict()

        component_config_connection_id = self.component_config_connection_id

        component_config_version = self.component_config_version

        component_id = self.component_id

        component_name = self.component_name

        created_at = self.created_at

        created_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        created_by_id = self.created_by_id

        git_ref = self.git_ref

        id = self.id

        install_deploys: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.install_deploys, Unset):
            install_deploys = []
            for install_deploys_item_data in self.install_deploys:
                install_deploys_item = install_deploys_item_data.to_dict()
                install_deploys.append(install_deploys_item)

        log_stream: dict[str, Any] | Unset = UNSET
        if not isinstance(self.log_stream, Unset):
            log_stream = self.log_stream.to_dict()

        releases: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.releases, Unset):
            releases = []
            for releases_item_data in self.releases:
                releases_item = releases_item_data.to_dict()
                releases.append(releases_item)

        runner_job: dict[str, Any] | Unset = UNSET
        if not isinstance(self.runner_job, Unset):
            runner_job = self.runner_job.to_dict()

        status = self.status

        status_description = self.status_description

        status_v2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status_v2, Unset):
            status_v2 = self.status_v2.to_dict()

        updated_at = self.updated_at

        vcs_connection_commit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vcs_connection_commit, Unset):
            vcs_connection_commit = self.vcs_connection_commit.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if checksum is not UNSET:
            field_dict["checksum"] = checksum
        if component_config_connection is not UNSET:
            field_dict["component_config_connection"] = component_config_connection
        if component_config_connection_id is not UNSET:
            field_dict["component_config_connection_id"] = component_config_connection_id
        if component_config_version is not UNSET:
            field_dict["component_config_version"] = component_config_version
        if component_id is not UNSET:
            field_dict["component_id"] = component_id
        if component_name is not UNSET:
            field_dict["component_name"] = component_name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if git_ref is not UNSET:
            field_dict["git_ref"] = git_ref
        if id is not UNSET:
            field_dict["id"] = id
        if install_deploys is not UNSET:
            field_dict["install_deploys"] = install_deploys
        if log_stream is not UNSET:
            field_dict["log_stream"] = log_stream
        if releases is not UNSET:
            field_dict["releases"] = releases
        if runner_job is not UNSET:
            field_dict["runner_job"] = runner_job
        if status is not UNSET:
            field_dict["status"] = status
        if status_description is not UNSET:
            field_dict["status_description"] = status_description
        if status_v2 is not UNSET:
            field_dict["status_v2"] = status_v2
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if vcs_connection_commit is not UNSET:
            field_dict["vcs_connection_commit"] = vcs_connection_commit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_account import AppAccount
        from ..models.app_component_config_connection import AppComponentConfigConnection
        from ..models.app_component_release import AppComponentRelease
        from ..models.app_composite_status import AppCompositeStatus
        from ..models.app_install_deploy import AppInstallDeploy
        from ..models.app_log_stream import AppLogStream
        from ..models.app_runner_job import AppRunnerJob
        from ..models.app_vcs_connection_commit import AppVCSConnectionCommit

        d = dict(src_dict)
        checksum = d.pop("checksum", UNSET)

        _component_config_connection = d.pop("component_config_connection", UNSET)
        component_config_connection: AppComponentConfigConnection | Unset
        if isinstance(_component_config_connection, Unset):
            component_config_connection = UNSET
        else:
            component_config_connection = AppComponentConfigConnection.from_dict(_component_config_connection)

        component_config_connection_id = d.pop("component_config_connection_id", UNSET)

        component_config_version = d.pop("component_config_version", UNSET)

        component_id = d.pop("component_id", UNSET)

        component_name = d.pop("component_name", UNSET)

        created_at = d.pop("created_at", UNSET)

        _created_by = d.pop("created_by", UNSET)
        created_by: AppAccount | Unset
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = AppAccount.from_dict(_created_by)

        created_by_id = d.pop("created_by_id", UNSET)

        git_ref = d.pop("git_ref", UNSET)

        id = d.pop("id", UNSET)

        install_deploys = []
        _install_deploys = d.pop("install_deploys", UNSET)
        for install_deploys_item_data in _install_deploys or []:
            install_deploys_item = AppInstallDeploy.from_dict(install_deploys_item_data)

            install_deploys.append(install_deploys_item)

        _log_stream = d.pop("log_stream", UNSET)
        log_stream: AppLogStream | Unset
        if isinstance(_log_stream, Unset):
            log_stream = UNSET
        else:
            log_stream = AppLogStream.from_dict(_log_stream)

        releases = []
        _releases = d.pop("releases", UNSET)
        for releases_item_data in _releases or []:
            releases_item = AppComponentRelease.from_dict(releases_item_data)

            releases.append(releases_item)

        _runner_job = d.pop("runner_job", UNSET)
        runner_job: AppRunnerJob | Unset
        if isinstance(_runner_job, Unset):
            runner_job = UNSET
        else:
            runner_job = AppRunnerJob.from_dict(_runner_job)

        status = d.pop("status", UNSET)

        status_description = d.pop("status_description", UNSET)

        _status_v2 = d.pop("status_v2", UNSET)
        status_v2: AppCompositeStatus | Unset
        if isinstance(_status_v2, Unset):
            status_v2 = UNSET
        else:
            status_v2 = AppCompositeStatus.from_dict(_status_v2)

        updated_at = d.pop("updated_at", UNSET)

        _vcs_connection_commit = d.pop("vcs_connection_commit", UNSET)
        vcs_connection_commit: AppVCSConnectionCommit | Unset
        if isinstance(_vcs_connection_commit, Unset):
            vcs_connection_commit = UNSET
        else:
            vcs_connection_commit = AppVCSConnectionCommit.from_dict(_vcs_connection_commit)

        app_component_build = cls(
            checksum=checksum,
            component_config_connection=component_config_connection,
            component_config_connection_id=component_config_connection_id,
            component_config_version=component_config_version,
            component_id=component_id,
            component_name=component_name,
            created_at=created_at,
            created_by=created_by,
            created_by_id=created_by_id,
            git_ref=git_ref,
            id=id,
            install_deploys=install_deploys,
            log_stream=log_stream,
            releases=releases,
            runner_job=runner_job,
            status=status,
            status_description=status_description,
            status_v2=status_v2,
            updated_at=updated_at,
            vcs_connection_commit=vcs_connection_commit,
        )

        app_component_build.additional_properties = d
        return app_component_build

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
