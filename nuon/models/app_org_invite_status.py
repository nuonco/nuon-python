# coding: utf-8

"""
    Nuon

    API for managing nuon apps, components, and installs.

    The version of the OpenAPI document: 0.19.108
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


class AppOrgInviteStatus(str, Enum):
    """
    AppOrgInviteStatus
    """

    """
    allowed enum values
    """
    PENDING = 'pending'
    ACCEPTED = 'accepted'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AppOrgInviteStatus from a JSON string"""
        return cls(json.loads(json_str))


