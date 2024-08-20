# coding: utf-8

"""
    Nuon

    API for managing nuon apps, components, and installs.

    The version of the OpenAPI document: 0.19.206
    Contact: support@nuon.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class AppPolicyName(str, Enum):
    """
    AppPolicyName
    """

    """
    allowed enum values
    """
    ORG_ADMIN = 'org_admin'
    INSTALLER = 'installer'
    RUNNER = 'runner'
    HOSTED_INSTALLER = 'hosted_installer'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AppPolicyName from a JSON string"""
        return cls(json.loads(json_str))


