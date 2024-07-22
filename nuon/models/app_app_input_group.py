# coding: utf-8

"""
    Nuon

    API for managing nuon apps, components, and installs.

    The version of the OpenAPI document: 0.19.195
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
from nuon.models.app_account import AppAccount
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AppAppInputGroup(BaseModel):
    """
    AppAppInputGroup
    """ # noqa: E501
    app_input_id: Optional[StrictStr] = None
    app_inputs: Optional[List[AppAppInput]] = None
    created_at: Optional[StrictStr] = None
    created_by: Optional[AppAccount] = None
    created_by_id: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    display_name: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    org_id: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["app_input_id", "app_inputs", "created_at", "created_by", "created_by_id", "description", "display_name", "id", "name", "org_id", "updated_at"]

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
        """Create an instance of AppAppInputGroup from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in app_inputs (list)
        _items = []
        if self.app_inputs:
            for _item in self.app_inputs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['app_inputs'] = _items
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['created_by'] = self.created_by.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AppAppInputGroup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "app_input_id": obj.get("app_input_id"),
            "app_inputs": [AppAppInput.from_dict(_item) for _item in obj.get("app_inputs")] if obj.get("app_inputs") is not None else None,
            "created_at": obj.get("created_at"),
            "created_by": AppAccount.from_dict(obj.get("created_by")) if obj.get("created_by") is not None else None,
            "created_by_id": obj.get("created_by_id"),
            "description": obj.get("description"),
            "display_name": obj.get("display_name"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "org_id": obj.get("org_id"),
            "updated_at": obj.get("updated_at")
        })
        return _obj

from nuon.models.app_app_input import AppAppInput
# TODO: Rewrite to not use raise_errors
AppAppInputGroup.model_rebuild(raise_errors=False)

