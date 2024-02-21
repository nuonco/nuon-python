# coding: utf-8

"""
    Nuon

    API for managing nuon apps, components, and installs.

    The version of the OpenAPI document: 0.19.60
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
from nuon.models.app_app_runner_config import AppAppRunnerConfig
from nuon.models.app_app_sandbox_config import AppAppSandboxConfig
from nuon.models.app_aws_account import AppAWSAccount
from nuon.models.app_install_component import AppInstallComponent
from nuon.models.app_install_inputs import AppInstallInputs
from nuon.models.app_install_sandbox_run import AppInstallSandboxRun
from nuon.models.app_user_token import AppUserToken
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AppInstall(BaseModel):
    """
    AppInstall
    """ # noqa: E501
    app_id: Optional[StrictStr] = None
    app_runner_config: Optional[AppAppRunnerConfig] = None
    app_sandbox_config: Optional[AppAppSandboxConfig] = None
    aws_account: Optional[AppAWSAccount] = None
    created_at: Optional[StrictStr] = None
    created_by: Optional[AppUserToken] = None
    created_by_id: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    install_components: Optional[List[AppInstallComponent]] = None
    install_inputs: Optional[List[AppInstallInputs]] = None
    install_sandbox_runs: Optional[List[AppInstallSandboxRun]] = None
    name: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    status_description: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["app_id", "app_runner_config", "app_sandbox_config", "aws_account", "created_at", "created_by", "created_by_id", "id", "install_components", "install_inputs", "install_sandbox_runs", "name", "status", "status_description", "updated_at"]

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
        """Create an instance of AppInstall from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of app_runner_config
        if self.app_runner_config:
            _dict['app_runner_config'] = self.app_runner_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of app_sandbox_config
        if self.app_sandbox_config:
            _dict['app_sandbox_config'] = self.app_sandbox_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of aws_account
        if self.aws_account:
            _dict['aws_account'] = self.aws_account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['created_by'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in install_components (list)
        _items = []
        if self.install_components:
            for _item in self.install_components:
                if _item:
                    _items.append(_item.to_dict())
            _dict['install_components'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in install_inputs (list)
        _items = []
        if self.install_inputs:
            for _item in self.install_inputs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['install_inputs'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in install_sandbox_runs (list)
        _items = []
        if self.install_sandbox_runs:
            for _item in self.install_sandbox_runs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['install_sandbox_runs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AppInstall from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "app_id": obj.get("app_id"),
            "app_runner_config": AppAppRunnerConfig.from_dict(obj.get("app_runner_config")) if obj.get("app_runner_config") is not None else None,
            "app_sandbox_config": AppAppSandboxConfig.from_dict(obj.get("app_sandbox_config")) if obj.get("app_sandbox_config") is not None else None,
            "aws_account": AppAWSAccount.from_dict(obj.get("aws_account")) if obj.get("aws_account") is not None else None,
            "created_at": obj.get("created_at"),
            "created_by": AppUserToken.from_dict(obj.get("created_by")) if obj.get("created_by") is not None else None,
            "created_by_id": obj.get("created_by_id"),
            "id": obj.get("id"),
            "install_components": [AppInstallComponent.from_dict(_item) for _item in obj.get("install_components")] if obj.get("install_components") is not None else None,
            "install_inputs": [AppInstallInputs.from_dict(_item) for _item in obj.get("install_inputs")] if obj.get("install_inputs") is not None else None,
            "install_sandbox_runs": [AppInstallSandboxRun.from_dict(_item) for _item in obj.get("install_sandbox_runs")] if obj.get("install_sandbox_runs") is not None else None,
            "name": obj.get("name"),
            "status": obj.get("status"),
            "status_description": obj.get("status_description"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


