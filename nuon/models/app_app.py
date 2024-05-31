# coding: utf-8

"""
    Nuon

    API for managing nuon apps, components, and installs.

    The version of the OpenAPI document: 0.19.150
    Contact: support@nuon.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json




from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from nuon.models.app_app_input_config import AppAppInputConfig
from nuon.models.app_app_runner_config import AppAppRunnerConfig
from nuon.models.app_app_sandbox_config import AppAppSandboxConfig
from nuon.models.app_cloud_platform import AppCloudPlatform
from nuon.models.app_notifications_config import AppNotificationsConfig
from nuon.models.app_user_token import AppUserToken
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AppApp(BaseModel):
    """
    AppApp
    """ # noqa: E501
    cloud_platform: Optional[AppCloudPlatform] = None
    created_at: Optional[StrictStr] = None
    created_by: Optional[AppUserToken] = None
    created_by_id: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    display_name: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    input_config: Optional[AppAppInputConfig] = Field(default=None, description="fields set via after query")
    name: Optional[StrictStr] = None
    notifications_config: Optional[AppNotificationsConfig] = None
    org_id: Optional[StrictStr] = None
    runner_config: Optional[AppAppRunnerConfig] = None
    sandbox_config: Optional[AppAppSandboxConfig] = None
    slack_webhook_url: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    status_description: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["cloud_platform", "created_at", "created_by", "created_by_id", "description", "display_name", "id", "input_config", "name", "notifications_config", "org_id", "runner_config", "sandbox_config", "slack_webhook_url", "status", "status_description", "updated_at"]

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
        """Create an instance of AppApp from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of input_config
        if self.input_config:
            _dict['input_config'] = self.input_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of notifications_config
        if self.notifications_config:
            _dict['notifications_config'] = self.notifications_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of runner_config
        if self.runner_config:
            _dict['runner_config'] = self.runner_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sandbox_config
        if self.sandbox_config:
            _dict['sandbox_config'] = self.sandbox_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AppApp from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cloud_platform": obj.get("cloud_platform"),
            "created_at": obj.get("created_at"),
            "created_by": AppUserToken.from_dict(obj.get("created_by")) if obj.get("created_by") is not None else None,
            "created_by_id": obj.get("created_by_id"),
            "description": obj.get("description"),
            "display_name": obj.get("display_name"),
            "id": obj.get("id"),
            "input_config": AppAppInputConfig.from_dict(obj.get("input_config")) if obj.get("input_config") is not None else None,
            "name": obj.get("name"),
            "notifications_config": AppNotificationsConfig.from_dict(obj.get("notifications_config")) if obj.get("notifications_config") is not None else None,
            "org_id": obj.get("org_id"),
            "runner_config": AppAppRunnerConfig.from_dict(obj.get("runner_config")) if obj.get("runner_config") is not None else None,
            "sandbox_config": AppAppSandboxConfig.from_dict(obj.get("sandbox_config")) if obj.get("sandbox_config") is not None else None,
            "slack_webhook_url": obj.get("slack_webhook_url"),
            "status": obj.get("status"),
            "status_description": obj.get("status_description"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


