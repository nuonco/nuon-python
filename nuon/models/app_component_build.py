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
    from ..models.app_policy_report import AppPolicyReport
    from ..models.app_queue_signal import AppQueueSignal
    from ..models.app_runner_job import AppRunnerJob
    from ..models.app_vcs_connection_commit import AppVCSConnectionCommit


T = TypeVar("T", bound="AppComponentBuild")


@_attrs_define
class AppComponentBuild:
    """
    Attributes:
        app_branch_run_id (str | Unset):
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
        no_op (bool | Unset): NoOp is true when the runner detected SourceDigest matches the previous
            build's SourceDigest and skipped the artifact push.

            Downstream contract:
              - The build is still marked Active because the bytes it represents
                are deployable (they live in the install registry under the prior
                build that pushed them).
              - No new install deploys are auto-queued for a NoOp build; the
                dep-aware deploy path handles fan-out for installs that depend
                on the underlying image.
              - pollForDeployableBuild treats NoOp builds as Active without any
                special-casing because the deployable artifact at the same
                SourceDigest is already present in the install registry from the
                prior build.
        policy_reports (list[AppPolicyReport] | Unset):
        queue_signal (AppQueueSignal | Unset):
        releases (list[AppComponentRelease] | Unset):
        resolved_at (str | Unset): ResolvedAt is when the runner resolved SourceRef to SourceDigest.
        resolved_tag (str | Unset): ResolvedTag is the tag the runner actually pulled from. For digest-pinned
            refs this is empty. For mutable/semver refs this is the concrete tag the
            runner selected (e.g. "1.25.5" even if SourceRef pinned "1.25.3" with a
            "~1.25.0" update_policy constraint).
        runner_job (AppRunnerJob | Unset):
        source_checksum (str | Unset): checksum of the component's source directory at build time
        source_digest (str | Unset): SourceDigest is the manifest list digest of the resolved source ref,
            e.g. "sha256:abc...". This is the canonical content address of what was
            pulled and is used for build dedup.
        source_image (str | Unset): SourceImage is the repository portion of SourceRef without tag/digest, e.g. "nginx".
        source_media_type (str | Unset): SourceMediaType records the media type of the resolved manifest (image,
            image index, OCI artifact, etc.) for downstream rendering decisions.
        source_ref (str | Unset): Source identity for image-type builds.

            SourceRef is what the user wrote in the spec, e.g. "nginx:1.25.3" or
            "myimage@sha256:...". Always populated for image-type builds so we have a
            permanent record of what was requested at build time.
        status (str | Unset):
        status_description (str | Unset):
        status_v2 (AppCompositeStatus | Unset):
        updated_at (str | Unset):
        vcs_connection_commit (AppVCSConnectionCommit | Unset):
    """

    app_branch_run_id: str | Unset = UNSET
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
    no_op: bool | Unset = UNSET
    policy_reports: list[AppPolicyReport] | Unset = UNSET
    queue_signal: AppQueueSignal | Unset = UNSET
    releases: list[AppComponentRelease] | Unset = UNSET
    resolved_at: str | Unset = UNSET
    resolved_tag: str | Unset = UNSET
    runner_job: AppRunnerJob | Unset = UNSET
    source_checksum: str | Unset = UNSET
    source_digest: str | Unset = UNSET
    source_image: str | Unset = UNSET
    source_media_type: str | Unset = UNSET
    source_ref: str | Unset = UNSET
    status: str | Unset = UNSET
    status_description: str | Unset = UNSET
    status_v2: AppCompositeStatus | Unset = UNSET
    updated_at: str | Unset = UNSET
    vcs_connection_commit: AppVCSConnectionCommit | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_branch_run_id = self.app_branch_run_id

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

        no_op = self.no_op

        policy_reports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.policy_reports, Unset):
            policy_reports = []
            for policy_reports_item_data in self.policy_reports:
                policy_reports_item = policy_reports_item_data.to_dict()
                policy_reports.append(policy_reports_item)

        queue_signal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.queue_signal, Unset):
            queue_signal = self.queue_signal.to_dict()

        releases: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.releases, Unset):
            releases = []
            for releases_item_data in self.releases:
                releases_item = releases_item_data.to_dict()
                releases.append(releases_item)

        resolved_at = self.resolved_at

        resolved_tag = self.resolved_tag

        runner_job: dict[str, Any] | Unset = UNSET
        if not isinstance(self.runner_job, Unset):
            runner_job = self.runner_job.to_dict()

        source_checksum = self.source_checksum

        source_digest = self.source_digest

        source_image = self.source_image

        source_media_type = self.source_media_type

        source_ref = self.source_ref

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
        if app_branch_run_id is not UNSET:
            field_dict["app_branch_run_id"] = app_branch_run_id
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
        if no_op is not UNSET:
            field_dict["no_op"] = no_op
        if policy_reports is not UNSET:
            field_dict["policy_reports"] = policy_reports
        if queue_signal is not UNSET:
            field_dict["queue_signal"] = queue_signal
        if releases is not UNSET:
            field_dict["releases"] = releases
        if resolved_at is not UNSET:
            field_dict["resolved_at"] = resolved_at
        if resolved_tag is not UNSET:
            field_dict["resolved_tag"] = resolved_tag
        if runner_job is not UNSET:
            field_dict["runner_job"] = runner_job
        if source_checksum is not UNSET:
            field_dict["source_checksum"] = source_checksum
        if source_digest is not UNSET:
            field_dict["source_digest"] = source_digest
        if source_image is not UNSET:
            field_dict["source_image"] = source_image
        if source_media_type is not UNSET:
            field_dict["source_media_type"] = source_media_type
        if source_ref is not UNSET:
            field_dict["source_ref"] = source_ref
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
        from ..models.app_policy_report import AppPolicyReport
        from ..models.app_queue_signal import AppQueueSignal
        from ..models.app_runner_job import AppRunnerJob
        from ..models.app_vcs_connection_commit import AppVCSConnectionCommit

        d = dict(src_dict)
        app_branch_run_id = d.pop("app_branch_run_id", UNSET)

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

        _install_deploys = d.pop("install_deploys", UNSET)
        install_deploys: list[AppInstallDeploy] | Unset = UNSET
        if _install_deploys is not UNSET:
            install_deploys = []
            for install_deploys_item_data in _install_deploys:
                install_deploys_item = AppInstallDeploy.from_dict(install_deploys_item_data)

                install_deploys.append(install_deploys_item)

        _log_stream = d.pop("log_stream", UNSET)
        log_stream: AppLogStream | Unset
        if isinstance(_log_stream, Unset):
            log_stream = UNSET
        else:
            log_stream = AppLogStream.from_dict(_log_stream)

        no_op = d.pop("no_op", UNSET)

        _policy_reports = d.pop("policy_reports", UNSET)
        policy_reports: list[AppPolicyReport] | Unset = UNSET
        if _policy_reports is not UNSET:
            policy_reports = []
            for policy_reports_item_data in _policy_reports:
                policy_reports_item = AppPolicyReport.from_dict(policy_reports_item_data)

                policy_reports.append(policy_reports_item)

        _queue_signal = d.pop("queue_signal", UNSET)
        queue_signal: AppQueueSignal | Unset
        if isinstance(_queue_signal, Unset):
            queue_signal = UNSET
        else:
            queue_signal = AppQueueSignal.from_dict(_queue_signal)

        _releases = d.pop("releases", UNSET)
        releases: list[AppComponentRelease] | Unset = UNSET
        if _releases is not UNSET:
            releases = []
            for releases_item_data in _releases:
                releases_item = AppComponentRelease.from_dict(releases_item_data)

                releases.append(releases_item)

        resolved_at = d.pop("resolved_at", UNSET)

        resolved_tag = d.pop("resolved_tag", UNSET)

        _runner_job = d.pop("runner_job", UNSET)
        runner_job: AppRunnerJob | Unset
        if isinstance(_runner_job, Unset):
            runner_job = UNSET
        else:
            runner_job = AppRunnerJob.from_dict(_runner_job)

        source_checksum = d.pop("source_checksum", UNSET)

        source_digest = d.pop("source_digest", UNSET)

        source_image = d.pop("source_image", UNSET)

        source_media_type = d.pop("source_media_type", UNSET)

        source_ref = d.pop("source_ref", UNSET)

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
            app_branch_run_id=app_branch_run_id,
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
            no_op=no_op,
            policy_reports=policy_reports,
            queue_signal=queue_signal,
            releases=releases,
            resolved_at=resolved_at,
            resolved_tag=resolved_tag,
            runner_job=runner_job,
            source_checksum=source_checksum,
            source_digest=source_digest,
            source_image=source_image,
            source_media_type=source_media_type,
            source_ref=source_ref,
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
