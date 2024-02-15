# coding: utf-8

"""
    Nuon

    API for managing nuon apps, components, and installs.

    The version of the OpenAPI document: 0.19.35
    Contact: support@nuon.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json




from pydantic import BaseModel, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from nuon.models.app_vcs_connection_commit import AppVCSConnectionCommit
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AppVCSConnection(BaseModel):
    """
    AppVCSConnection
    """ # noqa: E501
    created_at: Optional[StrictStr] = None
    created_by_id: Optional[StrictStr] = None
    github_install_id: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    vcs_connection_commit: Optional[List[AppVCSConnectionCommit]] = None
    __properties: ClassVar[List[str]] = ["created_at", "created_by_id", "github_install_id", "id", "updated_at", "vcs_connection_commit"]

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
        """Create an instance of AppVCSConnection from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in vcs_connection_commit (list)
        _items = []
        if self.vcs_connection_commit:
            for _item in self.vcs_connection_commit:
                if _item:
                    _items.append(_item.to_dict())
            _dict['vcs_connection_commit'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AppVCSConnection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "created_by_id": obj.get("created_by_id"),
            "github_install_id": obj.get("github_install_id"),
            "id": obj.get("id"),
            "updated_at": obj.get("updated_at"),
            "vcs_connection_commit": [AppVCSConnectionCommit.from_dict(_item) for _item in obj.get("vcs_connection_commit")] if obj.get("vcs_connection_commit") is not None else None
        })
        return _obj


