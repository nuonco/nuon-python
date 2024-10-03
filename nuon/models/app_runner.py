# coding: utf-8

"""
    Nuon

    API for managing nuon apps, components, and installs.

    The version of the OpenAPI document: 0.19.216
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
from nuon.models.app_org import AppOrg
from nuon.models.app_runner_job import AppRunnerJob
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AppRunner(BaseModel):
    """
    AppRunner
    """ # noqa: E501
    created_at: Optional[StrictStr] = None
    created_by: Optional[AppAccount] = None
    created_by_id: Optional[StrictStr] = None
    display_name: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    jobs: Optional[List[AppRunnerJob]] = None
    name: Optional[StrictStr] = None
    org: Optional[AppOrg] = None
    org_id: Optional[StrictStr] = None
    runner_id: Optional[StrictStr] = None
    runner_job: Optional[AppRunnerJob] = None
    status: Optional[StrictStr] = None
    status_description: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["created_at", "created_by", "created_by_id", "display_name", "id", "jobs", "name", "org", "org_id", "runner_id", "runner_job", "status", "status_description", "updated_at"]

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
        """Create an instance of AppRunner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in jobs (list)
        _items = []
        if self.jobs:
            for _item in self.jobs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['jobs'] = _items
        # override the default output from pydantic by calling `to_dict()` of org
        if self.org:
            _dict['org'] = self.org.to_dict()
        # override the default output from pydantic by calling `to_dict()` of runner_job
        if self.runner_job:
            _dict['runner_job'] = self.runner_job.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AppRunner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "created_by": AppAccount.from_dict(obj.get("created_by")) if obj.get("created_by") is not None else None,
            "created_by_id": obj.get("created_by_id"),
            "display_name": obj.get("display_name"),
            "id": obj.get("id"),
            "jobs": [AppRunnerJob.from_dict(_item) for _item in obj.get("jobs")] if obj.get("jobs") is not None else None,
            "name": obj.get("name"),
            "org": AppOrg.from_dict(obj.get("org")) if obj.get("org") is not None else None,
            "org_id": obj.get("org_id"),
            "runner_id": obj.get("runner_id"),
            "runner_job": AppRunnerJob.from_dict(obj.get("runner_job")) if obj.get("runner_job") is not None else None,
            "status": obj.get("status"),
            "status_description": obj.get("status_description"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


