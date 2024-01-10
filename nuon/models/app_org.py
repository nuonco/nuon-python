# coding: utf-8

"""
    Nuon

    API for managing nuon apps, components, and installs.

    The version of the OpenAPI document: 0.19.15
    Contact: support@nuon.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from nuon.models.app_user_org import AppUserOrg
from nuon.models.app_vcs_connection import AppVCSConnection
from typing import Optional, Set
from typing_extensions import Self

class AppOrg(BaseModel):
    """
    AppOrg
    """ # noqa: E501
    created_at: Optional[StrictStr] = None
    created_by_id: Optional[StrictStr] = None
    custom_cert: Optional[StrictBool] = None
    id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    sandbox_mode: Optional[StrictBool] = Field(default=None, description="These fields are used to control the behaviour of the org NOTE: these are starting as nullable, so we can update stage/prod before resetting locally.")
    status: Optional[StrictStr] = None
    status_description: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    users: Optional[List[AppUserOrg]] = None
    vcs_connections: Optional[List[AppVCSConnection]] = None
    __properties: ClassVar[List[str]] = ["created_at", "created_by_id", "custom_cert", "id", "name", "sandbox_mode", "status", "status_description", "updated_at", "users", "vcs_connections"]

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
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AppOrg from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in users (list)
        _items = []
        if self.users:
            for _item in self.users:
                if _item:
                    _items.append(_item.to_dict())
            _dict['users'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in vcs_connections (list)
        _items = []
        if self.vcs_connections:
            for _item in self.vcs_connections:
                if _item:
                    _items.append(_item.to_dict())
            _dict['vcs_connections'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AppOrg from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "created_by_id": obj.get("created_by_id"),
            "custom_cert": obj.get("custom_cert"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "sandbox_mode": obj.get("sandbox_mode"),
            "status": obj.get("status"),
            "status_description": obj.get("status_description"),
            "updated_at": obj.get("updated_at"),
            "users": [AppUserOrg.from_dict(_item) for _item in obj["users"]] if obj.get("users") is not None else None,
            "vcs_connections": [AppVCSConnection.from_dict(_item) for _item in obj["vcs_connections"]] if obj.get("vcs_connections") is not None else None
        })
        return _obj


