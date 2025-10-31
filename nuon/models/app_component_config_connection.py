from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_component_type import AppComponentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_docker_build_component_config import AppDockerBuildComponentConfig
    from ..models.app_external_image_component_config import AppExternalImageComponentConfig
    from ..models.app_helm_component_config import AppHelmComponentConfig
    from ..models.app_job_component_config import AppJobComponentConfig
    from ..models.app_kubernetes_manifest_component_config import AppKubernetesManifestComponentConfig
    from ..models.app_terraform_module_component_config import AppTerraformModuleComponentConfig
    from ..models.refs_ref import RefsRef


T = TypeVar("T", bound="AppComponentConfigConnection")


@_attrs_define
class AppComponentConfigConnection:
    """
    Attributes:
        app_config_id (str | Unset):
        app_config_version (int | Unset):
        checksum (str | Unset):
        component_dependency_ids (list[str] | Unset):
        component_id (str | Unset):
        component_name (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        docker_build (AppDockerBuildComponentConfig | Unset):
        drift_schedule (str | Unset):
        external_image (AppExternalImageComponentConfig | Unset):
        helm (AppHelmComponentConfig | Unset):
        id (str | Unset):
        job (AppJobComponentConfig | Unset):
        kubernetes_manifest (AppKubernetesManifestComponentConfig | Unset):
        references (list[str] | Unset):
        refs (list[RefsRef] | Unset):
        terraform_module (AppTerraformModuleComponentConfig | Unset):
        type_ (AppComponentType | Unset):
        updated_at (str | Unset):
        version (int | Unset):
    """

    app_config_id: str | Unset = UNSET
    app_config_version: int | Unset = UNSET
    checksum: str | Unset = UNSET
    component_dependency_ids: list[str] | Unset = UNSET
    component_id: str | Unset = UNSET
    component_name: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    docker_build: AppDockerBuildComponentConfig | Unset = UNSET
    drift_schedule: str | Unset = UNSET
    external_image: AppExternalImageComponentConfig | Unset = UNSET
    helm: AppHelmComponentConfig | Unset = UNSET
    id: str | Unset = UNSET
    job: AppJobComponentConfig | Unset = UNSET
    kubernetes_manifest: AppKubernetesManifestComponentConfig | Unset = UNSET
    references: list[str] | Unset = UNSET
    refs: list[RefsRef] | Unset = UNSET
    terraform_module: AppTerraformModuleComponentConfig | Unset = UNSET
    type_: AppComponentType | Unset = UNSET
    updated_at: str | Unset = UNSET
    version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config_id = self.app_config_id

        app_config_version = self.app_config_version

        checksum = self.checksum

        component_dependency_ids: list[str] | Unset = UNSET
        if not isinstance(self.component_dependency_ids, Unset):
            component_dependency_ids = self.component_dependency_ids

        component_id = self.component_id

        component_name = self.component_name

        created_at = self.created_at

        created_by_id = self.created_by_id

        docker_build: dict[str, Any] | Unset = UNSET
        if not isinstance(self.docker_build, Unset):
            docker_build = self.docker_build.to_dict()

        drift_schedule = self.drift_schedule

        external_image: dict[str, Any] | Unset = UNSET
        if not isinstance(self.external_image, Unset):
            external_image = self.external_image.to_dict()

        helm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.helm, Unset):
            helm = self.helm.to_dict()

        id = self.id

        job: dict[str, Any] | Unset = UNSET
        if not isinstance(self.job, Unset):
            job = self.job.to_dict()

        kubernetes_manifest: dict[str, Any] | Unset = UNSET
        if not isinstance(self.kubernetes_manifest, Unset):
            kubernetes_manifest = self.kubernetes_manifest.to_dict()

        references: list[str] | Unset = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        refs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.refs, Unset):
            refs = []
            for refs_item_data in self.refs:
                refs_item = refs_item_data.to_dict()
                refs.append(refs_item)

        terraform_module: dict[str, Any] | Unset = UNSET
        if not isinstance(self.terraform_module, Unset):
            terraform_module = self.terraform_module.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at = self.updated_at

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if app_config_version is not UNSET:
            field_dict["app_config_version"] = app_config_version
        if checksum is not UNSET:
            field_dict["checksum"] = checksum
        if component_dependency_ids is not UNSET:
            field_dict["component_dependency_ids"] = component_dependency_ids
        if component_id is not UNSET:
            field_dict["component_id"] = component_id
        if component_name is not UNSET:
            field_dict["component_name"] = component_name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if docker_build is not UNSET:
            field_dict["docker_build"] = docker_build
        if drift_schedule is not UNSET:
            field_dict["drift_schedule"] = drift_schedule
        if external_image is not UNSET:
            field_dict["external_image"] = external_image
        if helm is not UNSET:
            field_dict["helm"] = helm
        if id is not UNSET:
            field_dict["id"] = id
        if job is not UNSET:
            field_dict["job"] = job
        if kubernetes_manifest is not UNSET:
            field_dict["kubernetes_manifest"] = kubernetes_manifest
        if references is not UNSET:
            field_dict["references"] = references
        if refs is not UNSET:
            field_dict["refs"] = refs
        if terraform_module is not UNSET:
            field_dict["terraform_module"] = terraform_module
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_docker_build_component_config import AppDockerBuildComponentConfig
        from ..models.app_external_image_component_config import AppExternalImageComponentConfig
        from ..models.app_helm_component_config import AppHelmComponentConfig
        from ..models.app_job_component_config import AppJobComponentConfig
        from ..models.app_kubernetes_manifest_component_config import AppKubernetesManifestComponentConfig
        from ..models.app_terraform_module_component_config import AppTerraformModuleComponentConfig
        from ..models.refs_ref import RefsRef

        d = dict(src_dict)
        app_config_id = d.pop("app_config_id", UNSET)

        app_config_version = d.pop("app_config_version", UNSET)

        checksum = d.pop("checksum", UNSET)

        component_dependency_ids = cast(list[str], d.pop("component_dependency_ids", UNSET))

        component_id = d.pop("component_id", UNSET)

        component_name = d.pop("component_name", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        _docker_build = d.pop("docker_build", UNSET)
        docker_build: AppDockerBuildComponentConfig | Unset
        if isinstance(_docker_build, Unset):
            docker_build = UNSET
        else:
            docker_build = AppDockerBuildComponentConfig.from_dict(_docker_build)

        drift_schedule = d.pop("drift_schedule", UNSET)

        _external_image = d.pop("external_image", UNSET)
        external_image: AppExternalImageComponentConfig | Unset
        if isinstance(_external_image, Unset):
            external_image = UNSET
        else:
            external_image = AppExternalImageComponentConfig.from_dict(_external_image)

        _helm = d.pop("helm", UNSET)
        helm: AppHelmComponentConfig | Unset
        if isinstance(_helm, Unset):
            helm = UNSET
        else:
            helm = AppHelmComponentConfig.from_dict(_helm)

        id = d.pop("id", UNSET)

        _job = d.pop("job", UNSET)
        job: AppJobComponentConfig | Unset
        if isinstance(_job, Unset):
            job = UNSET
        else:
            job = AppJobComponentConfig.from_dict(_job)

        _kubernetes_manifest = d.pop("kubernetes_manifest", UNSET)
        kubernetes_manifest: AppKubernetesManifestComponentConfig | Unset
        if isinstance(_kubernetes_manifest, Unset):
            kubernetes_manifest = UNSET
        else:
            kubernetes_manifest = AppKubernetesManifestComponentConfig.from_dict(_kubernetes_manifest)

        references = cast(list[str], d.pop("references", UNSET))

        refs = []
        _refs = d.pop("refs", UNSET)
        for refs_item_data in _refs or []:
            refs_item = RefsRef.from_dict(refs_item_data)

            refs.append(refs_item)

        _terraform_module = d.pop("terraform_module", UNSET)
        terraform_module: AppTerraformModuleComponentConfig | Unset
        if isinstance(_terraform_module, Unset):
            terraform_module = UNSET
        else:
            terraform_module = AppTerraformModuleComponentConfig.from_dict(_terraform_module)

        _type_ = d.pop("type", UNSET)
        type_: AppComponentType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AppComponentType(_type_)

        updated_at = d.pop("updated_at", UNSET)

        version = d.pop("version", UNSET)

        app_component_config_connection = cls(
            app_config_id=app_config_id,
            app_config_version=app_config_version,
            checksum=checksum,
            component_dependency_ids=component_dependency_ids,
            component_id=component_id,
            component_name=component_name,
            created_at=created_at,
            created_by_id=created_by_id,
            docker_build=docker_build,
            drift_schedule=drift_schedule,
            external_image=external_image,
            helm=helm,
            id=id,
            job=job,
            kubernetes_manifest=kubernetes_manifest,
            references=references,
            refs=refs,
            terraform_module=terraform_module,
            type_=type_,
            updated_at=updated_at,
            version=version,
        )

        app_component_config_connection.additional_properties = d
        return app_component_config_connection

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
