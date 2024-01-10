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

from pydantic import BaseModel, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class AppComponent(BaseModel):
    """
    AppComponent
    """ # noqa: E501
    app_id: Optional[StrictStr] = None
    config_versions: Optional[StrictInt] = None
    created_at: Optional[StrictStr] = None
    created_by_id: Optional[StrictStr] = None
    dependencies: Optional[List[StrictStr]] = None
    id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    status_description: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["app_id", "config_versions", "created_at", "created_by_id", "dependencies", "id", "name", "status", "status_description", "updated_at"]

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
        """Create an instance of AppComponent from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AppComponent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "app_id": obj.get("app_id"),
            "config_versions": obj.get("config_versions"),
            "created_at": obj.get("created_at"),
            "created_by_id": obj.get("created_by_id"),
            "dependencies": obj.get("dependencies"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "status": obj.get("status"),
            "status_description": obj.get("status_description"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


