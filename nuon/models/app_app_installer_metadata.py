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




from pydantic import BaseModel, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AppAppInstallerMetadata(BaseModel):
    """
    AppAppInstallerMetadata
    """ # noqa: E501
    app_installer_id: Optional[StrictStr] = None
    community_url: Optional[StrictStr] = None
    created_at: Optional[StrictStr] = None
    created_by_id: Optional[StrictStr] = None
    demo_url: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    documentation_url: Optional[StrictStr] = None
    github_url: Optional[StrictStr] = None
    homepage_url: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    logo_url: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["app_installer_id", "community_url", "created_at", "created_by_id", "demo_url", "description", "documentation_url", "github_url", "homepage_url", "id", "logo_url", "name", "updated_at"]

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
        """Create an instance of AppAppInstallerMetadata from a JSON string"""
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
        """Create an instance of AppAppInstallerMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "app_installer_id": obj.get("app_installer_id"),
            "community_url": obj.get("community_url"),
            "created_at": obj.get("created_at"),
            "created_by_id": obj.get("created_by_id"),
            "demo_url": obj.get("demo_url"),
            "description": obj.get("description"),
            "documentation_url": obj.get("documentation_url"),
            "github_url": obj.get("github_url"),
            "homepage_url": obj.get("homepage_url"),
            "id": obj.get("id"),
            "logo_url": obj.get("logo_url"),
            "name": obj.get("name"),
            "updated_at": obj.get("updated_at")
        })
        return _obj

