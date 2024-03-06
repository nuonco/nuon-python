# coding: utf-8

"""
    Nuon

    API for managing nuon apps, components, and installs.

    The version of the OpenAPI document: 0.19.84
    Contact: support@nuon.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json




from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from nuon.models.app_user_token import AppUserToken
from nuon.models.app_vcs_connection import AppVCSConnection
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AppConnectedGithubVCSConfig(BaseModel):
    """
    AppConnectedGithubVCSConfig
    """ # noqa: E501
    branch: Optional[StrictStr] = None
    component_config_id: Optional[StrictStr] = Field(default=None, description="parent component")
    component_config_type: Optional[StrictStr] = None
    created_at: Optional[StrictStr] = None
    created_by: Optional[AppUserToken] = None
    created_by_id: Optional[StrictStr] = None
    directory: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    repo: Optional[StrictStr] = None
    repo_name: Optional[StrictStr] = None
    repo_owner: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    vcs_connection: Optional[AppVCSConnection] = None
    vcs_connection_id: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["branch", "component_config_id", "component_config_type", "created_at", "created_by", "created_by_id", "directory", "id", "repo", "repo_name", "repo_owner", "updated_at", "vcs_connection", "vcs_connection_id"]

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
        """Create an instance of AppConnectedGithubVCSConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of vcs_connection
        if self.vcs_connection:
            _dict['vcs_connection'] = self.vcs_connection.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AppConnectedGithubVCSConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "branch": obj.get("branch"),
            "component_config_id": obj.get("component_config_id"),
            "component_config_type": obj.get("component_config_type"),
            "created_at": obj.get("created_at"),
            "created_by": AppUserToken.from_dict(obj.get("created_by")) if obj.get("created_by") is not None else None,
            "created_by_id": obj.get("created_by_id"),
            "directory": obj.get("directory"),
            "id": obj.get("id"),
            "repo": obj.get("repo"),
            "repo_name": obj.get("repo_name"),
            "repo_owner": obj.get("repo_owner"),
            "updated_at": obj.get("updated_at"),
            "vcs_connection": AppVCSConnection.from_dict(obj.get("vcs_connection")) if obj.get("vcs_connection") is not None else None,
            "vcs_connection_id": obj.get("vcs_connection_id")
        })
        return _obj


