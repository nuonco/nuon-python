# coding: utf-8

"""
    Nuon

    API for managing nuon apps, components, and installs.

    The version of the OpenAPI document: 0.19.43
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
from nuon.models.app_install_deploy import AppInstallDeploy
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AppComponentReleaseStep(BaseModel):
    """
    AppComponentReleaseStep
    """ # noqa: E501
    component_release_id: Optional[StrictStr] = Field(default=None, description="parent release ID")
    created_at: Optional[StrictStr] = None
    created_by_id: Optional[StrictStr] = None
    delay: Optional[StrictStr] = Field(default=None, description="fields to control the delay of the individual step, as this is set based on the parent strategy")
    id: Optional[StrictStr] = None
    install_deploys: Optional[List[AppInstallDeploy]] = None
    requested_install_ids: Optional[List[StrictStr]] = Field(default=None, description="When a step is created, a set of installs are targeted. However, by the time the release step goes out, the install might have been setup in any order of ways.")
    status: Optional[StrictStr] = None
    status_description: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["component_release_id", "created_at", "created_by_id", "delay", "id", "install_deploys", "requested_install_ids", "status", "status_description", "updated_at"]

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
        """Create an instance of AppComponentReleaseStep from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in install_deploys (list)
        _items = []
        if self.install_deploys:
            for _item in self.install_deploys:
                if _item:
                    _items.append(_item.to_dict())
            _dict['install_deploys'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AppComponentReleaseStep from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "component_release_id": obj.get("component_release_id"),
            "created_at": obj.get("created_at"),
            "created_by_id": obj.get("created_by_id"),
            "delay": obj.get("delay"),
            "id": obj.get("id"),
            "install_deploys": [AppInstallDeploy.from_dict(_item) for _item in obj.get("install_deploys")] if obj.get("install_deploys") is not None else None,
            "requested_install_ids": obj.get("requested_install_ids"),
            "status": obj.get("status"),
            "status_description": obj.get("status_description"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


