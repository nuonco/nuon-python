# coding: utf-8

"""
    Nuon

    API for managing nuon apps, components, and installs.

    The version of the OpenAPI document: 0.19.149
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
from nuon.models.app_token_type import AppTokenType
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AppUserToken(BaseModel):
    """
    AppUserToken
    """ # noqa: E501
    created_at: Optional[StrictStr] = None
    created_by_id: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    expires_at: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    issued_at: Optional[StrictStr] = None
    issuer: Optional[StrictStr] = None
    subject: Optional[StrictStr] = Field(default=None, description="claim data")
    token_type: Optional[AppTokenType] = None
    updated_at: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["created_at", "created_by_id", "email", "expires_at", "id", "issued_at", "issuer", "subject", "token_type", "updated_at"]

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
        """Create an instance of AppUserToken from a JSON string"""
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
        """Create an instance of AppUserToken from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "created_by_id": obj.get("created_by_id"),
            "email": obj.get("email"),
            "expires_at": obj.get("expires_at"),
            "id": obj.get("id"),
            "issued_at": obj.get("issued_at"),
            "issuer": obj.get("issuer"),
            "subject": obj.get("subject"),
            "token_type": obj.get("token_type"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


