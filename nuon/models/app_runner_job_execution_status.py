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
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class AppRunnerJobExecutionStatus(str, Enum):
    """
    AppRunnerJobExecutionStatus
    """

    """
    allowed enum values
    """
    PENDING = 'pending'
    INITIALIZING = 'initializing'
    IN_MINUS_PROGRESS = 'in-progress'
    CLEANING_MINUS_UP = 'cleaning-up'
    FINISHED = 'finished'
    FAILED = 'failed'
    TIMED_MINUS_OUT = 'timed-out'
    NOT_MINUS_ATTEMPTED = 'not-attempted'
    CANCELLED = 'cancelled'
    UNKNOWN = 'unknown'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AppRunnerJobExecutionStatus from a JSON string"""
        return cls(json.loads(json_str))


