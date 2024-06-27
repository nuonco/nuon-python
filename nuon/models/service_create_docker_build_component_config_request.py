# coding: utf-8

"""
    Nuon

    API for managing nuon apps, components, and installs.

    The version of the OpenAPI document: 0.19.178
    Contact: support@nuon.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json




from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from nuon.models.service_connected_github_vcs_config_request import ServiceConnectedGithubVCSConfigRequest
from nuon.models.service_public_git_vcs_config_request import ServicePublicGitVCSConfigRequest
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ServiceCreateDockerBuildComponentConfigRequest(BaseModel):
    """
    ServiceCreateDockerBuildComponentConfigRequest
    """ # noqa: E501
    build_args: Optional[List[StrictStr]] = None
    connected_github_vcs_config: Optional[ServiceConnectedGithubVCSConfigRequest] = None
    dockerfile: StrictStr
    env_vars: Optional[Dict[str, StrictStr]] = None
    public_git_vcs_config: Optional[ServicePublicGitVCSConfigRequest] = None
    target: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["build_args", "connected_github_vcs_config", "dockerfile", "env_vars", "public_git_vcs_config", "target"]

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
        """Create an instance of ServiceCreateDockerBuildComponentConfigRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of connected_github_vcs_config
        if self.connected_github_vcs_config:
            _dict['connected_github_vcs_config'] = self.connected_github_vcs_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of public_git_vcs_config
        if self.public_git_vcs_config:
            _dict['public_git_vcs_config'] = self.public_git_vcs_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ServiceCreateDockerBuildComponentConfigRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "build_args": obj.get("build_args"),
            "connected_github_vcs_config": ServiceConnectedGithubVCSConfigRequest.from_dict(obj.get("connected_github_vcs_config")) if obj.get("connected_github_vcs_config") is not None else None,
            "dockerfile": obj.get("dockerfile"),
            "env_vars": obj.get("env_vars"),
            "public_git_vcs_config": ServicePublicGitVCSConfigRequest.from_dict(obj.get("public_git_vcs_config")) if obj.get("public_git_vcs_config") is not None else None,
            "target": obj.get("target")
        })
        return _obj


