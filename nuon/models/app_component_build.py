# coding: utf-8

"""
    Nuon

    API for managing nuon apps, components, and installs.

    The version of the OpenAPI document: 0.19.214
    Contact: support@nuon.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json




from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from nuon.models.app_account import AppAccount
from nuon.models.app_component_release import AppComponentRelease
from nuon.models.app_install_deploy import AppInstallDeploy
from nuon.models.app_vcs_connection_commit import AppVCSConnectionCommit
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AppComponentBuild(BaseModel):
    """
    AppComponentBuild
    """ # noqa: E501
    component_config_connection_id: Optional[StrictStr] = None
    component_config_version: Optional[StrictInt] = None
    component_id: Optional[StrictStr] = Field(default=None, description="Read-only fields set on the object to de-nest data")
    component_name: Optional[StrictStr] = None
    created_at: Optional[StrictStr] = None
    created_by: Optional[AppAccount] = None
    created_by_id: Optional[StrictStr] = None
    git_ref: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    install_deploys: Optional[List[AppInstallDeploy]] = None
    releases: Optional[List[AppComponentRelease]] = None
    status: Optional[StrictStr] = None
    status_description: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    vcs_connection_commit: Optional[AppVCSConnectionCommit] = None
    __properties: ClassVar[List[str]] = ["component_config_connection_id", "component_config_version", "component_id", "component_name", "created_at", "created_by", "created_by_id", "git_ref", "id", "install_deploys", "releases", "status", "status_description", "updated_at", "vcs_connection_commit"]

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
        """Create an instance of AppComponentBuild from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in install_deploys (list)
        _items = []
        if self.install_deploys:
            for _item in self.install_deploys:
                if _item:
                    _items.append(_item.to_dict())
            _dict['install_deploys'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in releases (list)
        _items = []
        if self.releases:
            for _item in self.releases:
                if _item:
                    _items.append(_item.to_dict())
            _dict['releases'] = _items
        # override the default output from pydantic by calling `to_dict()` of vcs_connection_commit
        if self.vcs_connection_commit:
            _dict['vcs_connection_commit'] = self.vcs_connection_commit.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AppComponentBuild from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "component_config_connection_id": obj.get("component_config_connection_id"),
            "component_config_version": obj.get("component_config_version"),
            "component_id": obj.get("component_id"),
            "component_name": obj.get("component_name"),
            "created_at": obj.get("created_at"),
            "created_by": AppAccount.from_dict(obj.get("created_by")) if obj.get("created_by") is not None else None,
            "created_by_id": obj.get("created_by_id"),
            "git_ref": obj.get("git_ref"),
            "id": obj.get("id"),
            "install_deploys": [AppInstallDeploy.from_dict(_item) for _item in obj.get("install_deploys")] if obj.get("install_deploys") is not None else None,
            "releases": [AppComponentRelease.from_dict(_item) for _item in obj.get("releases")] if obj.get("releases") is not None else None,
            "status": obj.get("status"),
            "status_description": obj.get("status_description"),
            "updated_at": obj.get("updated_at"),
            "vcs_connection_commit": AppVCSConnectionCommit.from_dict(obj.get("vcs_connection_commit")) if obj.get("vcs_connection_commit") is not None else None
        })
        return _obj


