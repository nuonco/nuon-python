# coding: utf-8

"""
    Nuon

    API for managing nuon apps, components, and installs.

    The version of the OpenAPI document: 0.19.33
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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AppJobComponentConfig(BaseModel):
    """
    AppJobComponentConfig
    """ # noqa: E501
    args: Optional[List[StrictStr]] = None
    cmd: Optional[List[StrictStr]] = None
    component_config_connection_id: Optional[StrictStr] = Field(default=None, description="value")
    created_at: Optional[StrictStr] = None
    created_by_id: Optional[StrictStr] = None
    env_vars: Optional[Dict[str, StrictStr]] = None
    id: Optional[StrictStr] = None
    image_url: Optional[StrictStr] = Field(default=None, description="Image attributes, copied from a docker_buid or external_image component.")
    tag: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["args", "cmd", "component_config_connection_id", "created_at", "created_by_id", "env_vars", "id", "image_url", "tag", "updated_at"]

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
        """Create an instance of AppJobComponentConfig from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AppJobComponentConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "args": obj.get("args"),
            "cmd": obj.get("cmd"),
            "component_config_connection_id": obj.get("component_config_connection_id"),
            "created_at": obj.get("created_at"),
            "created_by_id": obj.get("created_by_id"),
            "env_vars": obj.get("env_vars"),
            "id": obj.get("id"),
            "image_url": obj.get("image_url"),
            "tag": obj.get("tag"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


