# coding: utf-8

"""
    Nuon

    API for managing nuon apps, components, and installs.

    The version of the OpenAPI document: 0.19.191
    Contact: support@nuon.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json




from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from nuon.models.app_account import AppAccount
from nuon.models.app_docker_build_component_config import AppDockerBuildComponentConfig
from nuon.models.app_external_image_component_config import AppExternalImageComponentConfig
from nuon.models.app_helm_component_config import AppHelmComponentConfig
from nuon.models.app_job_component_config import AppJobComponentConfig
from nuon.models.app_terraform_module_component_config import AppTerraformModuleComponentConfig
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AppComponentConfigConnection(BaseModel):
    """
    AppComponentConfigConnection
    """ # noqa: E501
    component_id: Optional[StrictStr] = None
    created_at: Optional[StrictStr] = None
    created_by: Optional[AppAccount] = None
    created_by_id: Optional[StrictStr] = None
    docker_build: Optional[AppDockerBuildComponentConfig] = None
    external_image: Optional[AppExternalImageComponentConfig] = None
    helm: Optional[AppHelmComponentConfig] = None
    id: Optional[StrictStr] = None
    job: Optional[AppJobComponentConfig] = None
    terraform_module: Optional[AppTerraformModuleComponentConfig] = None
    updated_at: Optional[StrictStr] = None
    version: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["component_id", "created_at", "created_by", "created_by_id", "docker_build", "external_image", "helm", "id", "job", "terraform_module", "updated_at", "version"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AppComponentConfigConnection from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['created_by'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of docker_build
        if self.docker_build:
            _dict['docker_build'] = self.docker_build.to_dict()
        # override the default output from pydantic by calling `to_dict()` of external_image
        if self.external_image:
            _dict['external_image'] = self.external_image.to_dict()
        # override the default output from pydantic by calling `to_dict()` of helm
        if self.helm:
            _dict['helm'] = self.helm.to_dict()
        # override the default output from pydantic by calling `to_dict()` of job
        if self.job:
            _dict['job'] = self.job.to_dict()
        # override the default output from pydantic by calling `to_dict()` of terraform_module
        if self.terraform_module:
            _dict['terraform_module'] = self.terraform_module.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AppComponentConfigConnection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "component_id": obj.get("component_id"),
            "created_at": obj.get("created_at"),
            "created_by": AppAccount.from_dict(obj.get("created_by")) if obj.get("created_by") is not None else None,
            "created_by_id": obj.get("created_by_id"),
            "docker_build": AppDockerBuildComponentConfig.from_dict(obj.get("docker_build")) if obj.get("docker_build") is not None else None,
            "external_image": AppExternalImageComponentConfig.from_dict(obj.get("external_image")) if obj.get("external_image") is not None else None,
            "helm": AppHelmComponentConfig.from_dict(obj.get("helm")) if obj.get("helm") is not None else None,
            "id": obj.get("id"),
            "job": AppJobComponentConfig.from_dict(obj.get("job")) if obj.get("job") is not None else None,
            "terraform_module": AppTerraformModuleComponentConfig.from_dict(obj.get("terraform_module")) if obj.get("terraform_module") is not None else None,
            "updated_at": obj.get("updated_at"),
            "version": obj.get("version")
        })
        return _obj


