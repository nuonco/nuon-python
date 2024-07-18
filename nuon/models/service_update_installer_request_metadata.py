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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ServiceUpdateInstallerRequestMetadata(BaseModel):
    """
    ServiceUpdateInstallerRequestMetadata
    """ # noqa: E501
    community_url: StrictStr
    copyright_markdown: Optional[StrictStr] = None
    demo_url: Optional[StrictStr] = None
    description: StrictStr
    documentation_url: StrictStr
    favicon_url: Optional[StrictStr] = None
    footer_markdown: Optional[StrictStr] = None
    github_url: StrictStr
    homepage_url: StrictStr
    logo_url: StrictStr
    og_image_url: Optional[StrictStr] = None
    post_install_markdown: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["community_url", "copyright_markdown", "demo_url", "description", "documentation_url", "favicon_url", "footer_markdown", "github_url", "homepage_url", "logo_url", "og_image_url", "post_install_markdown"]

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
        """Create an instance of ServiceUpdateInstallerRequestMetadata from a JSON string"""
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
        """Create an instance of ServiceUpdateInstallerRequestMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "community_url": obj.get("community_url"),
            "copyright_markdown": obj.get("copyright_markdown"),
            "demo_url": obj.get("demo_url"),
            "description": obj.get("description"),
            "documentation_url": obj.get("documentation_url"),
            "favicon_url": obj.get("favicon_url"),
            "footer_markdown": obj.get("footer_markdown"),
            "github_url": obj.get("github_url"),
            "homepage_url": obj.get("homepage_url"),
            "logo_url": obj.get("logo_url"),
            "og_image_url": obj.get("og_image_url"),
            "post_install_markdown": obj.get("post_install_markdown")
        })
        return _obj


