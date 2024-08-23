# coding: utf-8

"""
    Nuon

    API for managing nuon apps, components, and installs.

    The version of the OpenAPI document: 0.19.210
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
from nuon.models.app_component_release_step import AppComponentReleaseStep
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AppComponentRelease(BaseModel):
    """
    AppComponentRelease
    """ # noqa: E501
    build_id: Optional[StrictStr] = None
    created_at: Optional[StrictStr] = None
    created_by: Optional[AppAccount] = None
    created_by_id: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    release_steps: Optional[List[AppComponentReleaseStep]] = None
    status: Optional[StrictStr] = None
    status_description: Optional[StrictStr] = None
    total_release_steps: Optional[StrictInt] = None
    updated_at: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["build_id", "created_at", "created_by", "created_by_id", "id", "release_steps", "status", "status_description", "total_release_steps", "updated_at"]

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
        """Create an instance of AppComponentRelease from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in release_steps (list)
        _items = []
        if self.release_steps:
            for _item in self.release_steps:
                if _item:
                    _items.append(_item.to_dict())
            _dict['release_steps'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AppComponentRelease from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "build_id": obj.get("build_id"),
            "created_at": obj.get("created_at"),
            "created_by": AppAccount.from_dict(obj.get("created_by")) if obj.get("created_by") is not None else None,
            "created_by_id": obj.get("created_by_id"),
            "id": obj.get("id"),
            "release_steps": [AppComponentReleaseStep.from_dict(_item) for _item in obj.get("release_steps")] if obj.get("release_steps") is not None else None,
            "status": obj.get("status"),
            "status_description": obj.get("status_description"),
            "total_release_steps": obj.get("total_release_steps"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


