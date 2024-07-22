# coding: utf-8

"""
    Nuon

    API for managing nuon apps, components, and installs.

    The version of the OpenAPI document: 0.19.196
    Contact: support@nuon.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json




from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from nuon.models.app_account import AppAccount
from nuon.models.app_notifications_config import AppNotificationsConfig
from nuon.models.app_org_health_check import AppOrgHealthCheck
from nuon.models.app_vcs_connection import AppVCSConnection
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AppOrg(BaseModel):
    """
    AppOrg
    """ # noqa: E501
    created_at: Optional[StrictStr] = None
    created_by: Optional[AppAccount] = None
    created_by_id: Optional[StrictStr] = None
    custom_cert: Optional[StrictBool] = None
    health_checks: Optional[List[AppOrgHealthCheck]] = None
    id: Optional[StrictStr] = None
    latest_health_check: Optional[AppOrgHealthCheck] = Field(default=None, description="Filled in at read time")
    name: Optional[StrictStr] = None
    notifications_config: Optional[AppNotificationsConfig] = None
    sandbox_mode: Optional[StrictBool] = Field(default=None, description="These fields are used to control the behaviour of the org NOTE: these are starting as nullable, so we can update stage/prod before resetting locally.")
    status: Optional[StrictStr] = None
    status_description: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    vcs_connections: Optional[List[AppVCSConnection]] = None
    __properties: ClassVar[List[str]] = ["created_at", "created_by", "created_by_id", "custom_cert", "health_checks", "id", "latest_health_check", "name", "notifications_config", "sandbox_mode", "status", "status_description", "updated_at", "vcs_connections"]

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
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['created_by'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in health_checks (list)
        _items = []
        if self.health_checks:
            for _item in self.health_checks:
                if _item:
                    _items.append(_item.to_dict())
            _dict['health_checks'] = _items
        # override the default output from pydantic by calling `to_dict()` of latest_health_check
        if self.latest_health_check:
            _dict['latest_health_check'] = self.latest_health_check.to_dict()
        # override the default output from pydantic by calling `to_dict()` of notifications_config
        if self.notifications_config:
            _dict['notifications_config'] = self.notifications_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in vcs_connections (list)
        _items = []
        if self.vcs_connections:
            for _item in self.vcs_connections:
                if _item:
                    _items.append(_item.to_dict())
            _dict['vcs_connections'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AppOrg from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "created_by": AppAccount.from_dict(obj.get("created_by")) if obj.get("created_by") is not None else None,
            "created_by_id": obj.get("created_by_id"),
            "custom_cert": obj.get("custom_cert"),
            "health_checks": [AppOrgHealthCheck.from_dict(_item) for _item in obj.get("health_checks")] if obj.get("health_checks") is not None else None,
            "id": obj.get("id"),
            "latest_health_check": AppOrgHealthCheck.from_dict(obj.get("latest_health_check")) if obj.get("latest_health_check") is not None else None,
            "name": obj.get("name"),
            "notifications_config": AppNotificationsConfig.from_dict(obj.get("notifications_config")) if obj.get("notifications_config") is not None else None,
            "sandbox_mode": obj.get("sandbox_mode"),
            "status": obj.get("status"),
            "status_description": obj.get("status_description"),
            "updated_at": obj.get("updated_at"),
            "vcs_connections": [AppVCSConnection.from_dict(_item) for _item in obj.get("vcs_connections")] if obj.get("vcs_connections") is not None else None
        })
        return _obj


