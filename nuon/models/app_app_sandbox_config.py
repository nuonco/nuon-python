# coding: utf-8

"""
    Nuon

    API for managing nuon apps, components, and installs.

    The version of the OpenAPI document: 0.19.24
    Contact: support@nuon.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from nuon.models.app_connected_github_vcs_config import AppConnectedGithubVCSConfig
from nuon.models.app_public_git_vcs_config import AppPublicGitVCSConfig
from nuon.models.app_sandbox_release import AppSandboxRelease
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AppAppSandboxConfig(BaseModel):
    """
    AppAppSandboxConfig
    """ # noqa: E501
    app_id: Optional[StrictStr] = Field(default=None, description="TODO(jm): add this back, once we have migrated all existing app sandbox configs `gorm:\"not null;default null\"`")
    connected_github_vcs_config: Optional[AppConnectedGithubVCSConfig] = None
    created_at: Optional[StrictStr] = None
    created_by_id: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    org_id: Optional[StrictStr] = None
    public_git_vcs_config: Optional[AppPublicGitVCSConfig] = None
    sandbox_release: Optional[AppSandboxRelease] = None
    sandbox_release_id: Optional[StrictStr] = None
    terraform_version: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    variables: Optional[Dict[str, StrictStr]] = None
    __properties: ClassVar[List[str]] = ["app_id", "connected_github_vcs_config", "created_at", "created_by_id", "id", "org_id", "public_git_vcs_config", "sandbox_release", "sandbox_release_id", "terraform_version", "updated_at", "variables"]

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
        """Create an instance of AppAppSandboxConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of sandbox_release
        if self.sandbox_release:
            _dict['sandbox_release'] = self.sandbox_release.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AppAppSandboxConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "app_id": obj.get("app_id"),
            "connected_github_vcs_config": AppConnectedGithubVCSConfig.from_dict(obj.get("connected_github_vcs_config")) if obj.get("connected_github_vcs_config") is not None else None,
            "created_at": obj.get("created_at"),
            "created_by_id": obj.get("created_by_id"),
            "id": obj.get("id"),
            "org_id": obj.get("org_id"),
            "public_git_vcs_config": AppPublicGitVCSConfig.from_dict(obj.get("public_git_vcs_config")) if obj.get("public_git_vcs_config") is not None else None,
            "sandbox_release": AppSandboxRelease.from_dict(obj.get("sandbox_release")) if obj.get("sandbox_release") is not None else None,
            "sandbox_release_id": obj.get("sandbox_release_id"),
            "terraform_version": obj.get("terraform_version"),
            "updated_at": obj.get("updated_at"),
            "variables": obj.get("variables")
        })
        return _obj


