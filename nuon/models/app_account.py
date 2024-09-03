# coding: utf-8

"""
    Nuon

    API for managing nuon apps, components, and installs.

    The version of the OpenAPI document: 0.19.215
    Contact: support@nuon.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json




from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from nuon.models.app_account_type import AppAccountType
from nuon.models.permissions_permission import PermissionsPermission
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AppAccount(BaseModel):
    """
    AppAccount
    """ # noqa: E501
    account_type: Optional[AppAccountType] = None
    created_at: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    org_ids: Optional[List[StrictStr]] = Field(default=None, description="ReadOnly Fields")
    permissions: Optional[Dict[str, PermissionsPermission]] = None
    roles: Optional[List[AppRole]] = None
    subject: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["account_type", "created_at", "email", "id", "org_ids", "permissions", "roles", "subject", "updated_at"]

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
        """Create an instance of AppAccount from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in roles (list)
        _items = []
        if self.roles:
            for _item in self.roles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['roles'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AppAccount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "account_type": obj.get("account_type"),
            "created_at": obj.get("created_at"),
            "email": obj.get("email"),
            "id": obj.get("id"),
            "org_ids": obj.get("org_ids"),
            "permissions": dict((_k, _v) for _k, _v in obj.get("permissions").items()),
            "roles": [AppRole.from_dict(_item) for _item in obj.get("roles")] if obj.get("roles") is not None else None,
            "subject": obj.get("subject"),
            "updated_at": obj.get("updated_at")
        })
        return _obj

from nuon.models.app_role import AppRole
# TODO: Rewrite to not use raise_errors
AppAccount.model_rebuild(raise_errors=False)

