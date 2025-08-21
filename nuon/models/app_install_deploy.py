from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_install_deploy_type import AppInstallDeployType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_account import AppAccount
    from ..models.app_component_build import AppComponentBuild
    from ..models.app_composite_status import AppCompositeStatus
    from ..models.app_install_action_workflow_run import AppInstallActionWorkflowRun
    from ..models.app_install_deploy_outputs import AppInstallDeployOutputs
    from ..models.app_log_stream import AppLogStream
    from ..models.app_oci_artifact import AppOCIArtifact
    from ..models.app_runner_job import AppRunnerJob
    from ..models.app_workflow import AppWorkflow


T = TypeVar("T", bound="AppInstallDeploy")


@_attrs_define
class AppInstallDeploy:
    """
    Attributes:
        action_workflow_runs (Union[Unset, list['AppInstallActionWorkflowRun']]):
        build_id (Union[Unset, str]):
        component_build (Union[Unset, AppComponentBuild]):
        component_config_version (Union[Unset, int]):
        component_id (Union[Unset, str]):
        component_name (Union[Unset, str]):
        created_at (Union[Unset, str]):
        created_by (Union[Unset, AppAccount]):
        created_by_id (Union[Unset, str]):
        id (Union[Unset, str]):
        install_component_id (Union[Unset, str]):
        install_deploy_type (Union[Unset, AppInstallDeployType]):
        install_id (Union[Unset, str]): Fields that are de-nested at read time using AfterQuery
        install_workflow_id (Union[Unset, str]): DEPRECATED: use WorkflowID
        log_stream (Union[Unset, AppLogStream]):
        oci_artifact (Union[Unset, AppOCIArtifact]):
        outputs (Union[Unset, AppInstallDeployOutputs]):
        release_id (Union[Unset, str]):
        runner_jobs (Union[Unset, list['AppRunnerJob']]): runner details
        status (Union[Unset, str]):
        status_description (Union[Unset, str]):
        status_v2 (Union[Unset, AppCompositeStatus]):
        updated_at (Union[Unset, str]):
        workflow (Union[Unset, AppWorkflow]):
        workflow_id (Union[Unset, str]):
    """

    action_workflow_runs: Union[Unset, list["AppInstallActionWorkflowRun"]] = UNSET
    build_id: Union[Unset, str] = UNSET
    component_build: Union[Unset, "AppComponentBuild"] = UNSET
    component_config_version: Union[Unset, int] = UNSET
    component_id: Union[Unset, str] = UNSET
    component_name: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by: Union[Unset, "AppAccount"] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    install_component_id: Union[Unset, str] = UNSET
    install_deploy_type: Union[Unset, AppInstallDeployType] = UNSET
    install_id: Union[Unset, str] = UNSET
    install_workflow_id: Union[Unset, str] = UNSET
    log_stream: Union[Unset, "AppLogStream"] = UNSET
    oci_artifact: Union[Unset, "AppOCIArtifact"] = UNSET
    outputs: Union[Unset, "AppInstallDeployOutputs"] = UNSET
    release_id: Union[Unset, str] = UNSET
    runner_jobs: Union[Unset, list["AppRunnerJob"]] = UNSET
    status: Union[Unset, str] = UNSET
    status_description: Union[Unset, str] = UNSET
    status_v2: Union[Unset, "AppCompositeStatus"] = UNSET
    updated_at: Union[Unset, str] = UNSET
    workflow: Union[Unset, "AppWorkflow"] = UNSET
    workflow_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_workflow_runs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.action_workflow_runs, Unset):
            action_workflow_runs = []
            for action_workflow_runs_item_data in self.action_workflow_runs:
                action_workflow_runs_item = action_workflow_runs_item_data.to_dict()
                action_workflow_runs.append(action_workflow_runs_item)

        build_id = self.build_id

        component_build: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.component_build, Unset):
            component_build = self.component_build.to_dict()

        component_config_version = self.component_config_version

        component_id = self.component_id

        component_name = self.component_name

        created_at = self.created_at

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        created_by_id = self.created_by_id

        id = self.id

        install_component_id = self.install_component_id

        install_deploy_type: Union[Unset, str] = UNSET
        if not isinstance(self.install_deploy_type, Unset):
            install_deploy_type = self.install_deploy_type.value

        install_id = self.install_id

        install_workflow_id = self.install_workflow_id

        log_stream: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.log_stream, Unset):
            log_stream = self.log_stream.to_dict()

        oci_artifact: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.oci_artifact, Unset):
            oci_artifact = self.oci_artifact.to_dict()

        outputs: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.outputs, Unset):
            outputs = self.outputs.to_dict()

        release_id = self.release_id

        runner_jobs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.runner_jobs, Unset):
            runner_jobs = []
            for runner_jobs_item_data in self.runner_jobs:
                runner_jobs_item = runner_jobs_item_data.to_dict()
                runner_jobs.append(runner_jobs_item)

        status = self.status

        status_description = self.status_description

        status_v2: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status_v2, Unset):
            status_v2 = self.status_v2.to_dict()

        updated_at = self.updated_at

        workflow: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

        workflow_id = self.workflow_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action_workflow_runs is not UNSET:
            field_dict["action_workflow_runs"] = action_workflow_runs
        if build_id is not UNSET:
            field_dict["build_id"] = build_id
        if component_build is not UNSET:
            field_dict["component_build"] = component_build
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
        if id is not UNSET:
            field_dict["id"] = id
        if install_component_id is not UNSET:
            field_dict["install_component_id"] = install_component_id
        if install_deploy_type is not UNSET:
            field_dict["install_deploy_type"] = install_deploy_type
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if install_workflow_id is not UNSET:
            field_dict["install_workflow_id"] = install_workflow_id
        if log_stream is not UNSET:
            field_dict["log_stream"] = log_stream
        if oci_artifact is not UNSET:
            field_dict["oci_artifact"] = oci_artifact
        if outputs is not UNSET:
            field_dict["outputs"] = outputs
        if release_id is not UNSET:
            field_dict["release_id"] = release_id
        if runner_jobs is not UNSET:
            field_dict["runner_jobs"] = runner_jobs
        if status is not UNSET:
            field_dict["status"] = status
        if status_description is not UNSET:
            field_dict["status_description"] = status_description
        if status_v2 is not UNSET:
            field_dict["status_v2"] = status_v2
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if workflow is not UNSET:
            field_dict["workflow"] = workflow
        if workflow_id is not UNSET:
            field_dict["workflow_id"] = workflow_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_account import AppAccount
        from ..models.app_component_build import AppComponentBuild
        from ..models.app_composite_status import AppCompositeStatus
        from ..models.app_install_action_workflow_run import AppInstallActionWorkflowRun
        from ..models.app_install_deploy_outputs import AppInstallDeployOutputs
        from ..models.app_log_stream import AppLogStream
        from ..models.app_oci_artifact import AppOCIArtifact
        from ..models.app_runner_job import AppRunnerJob
        from ..models.app_workflow import AppWorkflow

        d = dict(src_dict)
        action_workflow_runs = []
        _action_workflow_runs = d.pop("action_workflow_runs", UNSET)
        for action_workflow_runs_item_data in _action_workflow_runs or []:
            action_workflow_runs_item = AppInstallActionWorkflowRun.from_dict(action_workflow_runs_item_data)

            action_workflow_runs.append(action_workflow_runs_item)

        build_id = d.pop("build_id", UNSET)

        _component_build = d.pop("component_build", UNSET)
        component_build: Union[Unset, AppComponentBuild]
        if isinstance(_component_build, Unset):
            component_build = UNSET
        else:
            component_build = AppComponentBuild.from_dict(_component_build)

        component_config_version = d.pop("component_config_version", UNSET)

        component_id = d.pop("component_id", UNSET)

        component_name = d.pop("component_name", UNSET)

        created_at = d.pop("created_at", UNSET)

        _created_by = d.pop("created_by", UNSET)
        created_by: Union[Unset, AppAccount]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = AppAccount.from_dict(_created_by)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        install_component_id = d.pop("install_component_id", UNSET)

        _install_deploy_type = d.pop("install_deploy_type", UNSET)
        install_deploy_type: Union[Unset, AppInstallDeployType]
        if isinstance(_install_deploy_type, Unset):
            install_deploy_type = UNSET
        else:
            install_deploy_type = AppInstallDeployType(_install_deploy_type)

        install_id = d.pop("install_id", UNSET)

        install_workflow_id = d.pop("install_workflow_id", UNSET)

        _log_stream = d.pop("log_stream", UNSET)
        log_stream: Union[Unset, AppLogStream]
        if isinstance(_log_stream, Unset):
            log_stream = UNSET
        else:
            log_stream = AppLogStream.from_dict(_log_stream)

        _oci_artifact = d.pop("oci_artifact", UNSET)
        oci_artifact: Union[Unset, AppOCIArtifact]
        if isinstance(_oci_artifact, Unset):
            oci_artifact = UNSET
        else:
            oci_artifact = AppOCIArtifact.from_dict(_oci_artifact)

        _outputs = d.pop("outputs", UNSET)
        outputs: Union[Unset, AppInstallDeployOutputs]
        if isinstance(_outputs, Unset):
            outputs = UNSET
        else:
            outputs = AppInstallDeployOutputs.from_dict(_outputs)

        release_id = d.pop("release_id", UNSET)

        runner_jobs = []
        _runner_jobs = d.pop("runner_jobs", UNSET)
        for runner_jobs_item_data in _runner_jobs or []:
            runner_jobs_item = AppRunnerJob.from_dict(runner_jobs_item_data)

            runner_jobs.append(runner_jobs_item)

        status = d.pop("status", UNSET)

        status_description = d.pop("status_description", UNSET)

        _status_v2 = d.pop("status_v2", UNSET)
        status_v2: Union[Unset, AppCompositeStatus]
        if isinstance(_status_v2, Unset):
            status_v2 = UNSET
        else:
            status_v2 = AppCompositeStatus.from_dict(_status_v2)

        updated_at = d.pop("updated_at", UNSET)

        _workflow = d.pop("workflow", UNSET)
        workflow: Union[Unset, AppWorkflow]
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = AppWorkflow.from_dict(_workflow)

        workflow_id = d.pop("workflow_id", UNSET)

        app_install_deploy = cls(
            action_workflow_runs=action_workflow_runs,
            build_id=build_id,
            component_build=component_build,
            component_config_version=component_config_version,
            component_id=component_id,
            component_name=component_name,
            created_at=created_at,
            created_by=created_by,
            created_by_id=created_by_id,
            id=id,
            install_component_id=install_component_id,
            install_deploy_type=install_deploy_type,
            install_id=install_id,
            install_workflow_id=install_workflow_id,
            log_stream=log_stream,
            oci_artifact=oci_artifact,
            outputs=outputs,
            release_id=release_id,
            runner_jobs=runner_jobs,
            status=status,
            status_description=status_description,
            status_v2=status_v2,
            updated_at=updated_at,
            workflow=workflow,
            workflow_id=workflow_id,
        )

        app_install_deploy.additional_properties = d
        return app_install_deploy

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
