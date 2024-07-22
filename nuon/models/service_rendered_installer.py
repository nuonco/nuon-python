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




from pydantic import BaseModel, ConfigDict, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from nuon.models.app_app import AppApp
from nuon.models.app_installer_metadata import AppInstallerMetadata
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ServiceRenderedInstaller(BaseModel):
    """
    ServiceRenderedInstaller
    """ # noqa: E501
    apps: Optional[List[AppApp]] = None
    metadata: Optional[AppInstallerMetadata] = None
    sandbox_mode: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["apps", "metadata", "sandbox_mode"]

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
        """Create an instance of ServiceRenderedInstaller from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in apps (list)
        _items = []
        if self.apps:
            for _item in self.apps:
                if _item:
                    _items.append(_item.to_dict())
            _dict['apps'] = _items
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ServiceRenderedInstaller from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "apps": [AppApp.from_dict(_item) for _item in obj.get("apps")] if obj.get("apps") is not None else None,
            "metadata": AppInstallerMetadata.from_dict(obj.get("metadata")) if obj.get("metadata") is not None else None,
            "sandbox_mode": obj.get("sandbox_mode")
        })
        return _obj


