# coding: utf-8

"""
    Nuon

    API for managing nuon apps, components, and installs.

    The version of the OpenAPI document: 0.19.191
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

class AppInstallerMetadata(BaseModel):
    """
    AppInstallerMetadata
    """ # noqa: E501
    community_url: Optional[StrictStr] = None
    copyright_markdown: Optional[StrictStr] = None
    created_at: Optional[StrictStr] = None
    created_by: Optional[AppAccount] = None
    created_by_id: Optional[StrictStr] = None
    demo_url: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    documentation_url: Optional[StrictStr] = None
    favicon_url: Optional[StrictStr] = None
    footer_markdown: Optional[StrictStr] = None
    formatted_demo_url: Optional[StrictStr] = None
    github_url: Optional[StrictStr] = None
    homepage_url: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    installer_id: Optional[StrictStr] = None
    logo_url: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    og_image_url: Optional[StrictStr] = None
    post_install_markdown: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["community_url", "copyright_markdown", "created_at", "created_by", "created_by_id", "demo_url", "description", "documentation_url", "favicon_url", "footer_markdown", "formatted_demo_url", "github_url", "homepage_url", "id", "installer_id", "logo_url", "name", "og_image_url", "post_install_markdown", "updated_at"]

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
        """Create an instance of AppInstallerMetadata from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AppInstallerMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "community_url": obj.get("community_url"),
            "copyright_markdown": obj.get("copyright_markdown"),
            "created_at": obj.get("created_at"),
            "created_by": AppAccount.from_dict(obj.get("created_by")) if obj.get("created_by") is not None else None,
            "created_by_id": obj.get("created_by_id"),
            "demo_url": obj.get("demo_url"),
            "description": obj.get("description"),
            "documentation_url": obj.get("documentation_url"),
            "favicon_url": obj.get("favicon_url"),
            "footer_markdown": obj.get("footer_markdown"),
            "formatted_demo_url": obj.get("formatted_demo_url"),
            "github_url": obj.get("github_url"),
            "homepage_url": obj.get("homepage_url"),
            "id": obj.get("id"),
            "installer_id": obj.get("installer_id"),
            "logo_url": obj.get("logo_url"),
            "name": obj.get("name"),
            "og_image_url": obj.get("og_image_url"),
            "post_install_markdown": obj.get("post_install_markdown"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


