# coding: utf-8

"""
    Nuon

    API for managing nuon apps, components, and installs.

    The version of the OpenAPI document: 0.19.162
    Contact: support@nuon.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json




from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from nuon.models.metrics_decr import MetricsDecr
from nuon.models.metrics_event import MetricsEvent
from nuon.models.metrics_incr import MetricsIncr
from nuon.models.metrics_timing import MetricsTiming
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ServicePublishMetricInput(BaseModel):
    """
    ServicePublishMetricInput
    """ # noqa: E501
    decr: Optional[MetricsDecr] = None
    event: Optional[MetricsEvent] = None
    incr: Optional[MetricsIncr] = None
    timing: Optional[MetricsTiming] = None
    __properties: ClassVar[List[str]] = ["decr", "event", "incr", "timing"]

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
        """Create an instance of ServicePublishMetricInput from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of decr
        if self.decr:
            _dict['decr'] = self.decr.to_dict()
        # override the default output from pydantic by calling `to_dict()` of event
        if self.event:
            _dict['event'] = self.event.to_dict()
        # override the default output from pydantic by calling `to_dict()` of incr
        if self.incr:
            _dict['incr'] = self.incr.to_dict()
        # override the default output from pydantic by calling `to_dict()` of timing
        if self.timing:
            _dict['timing'] = self.timing.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ServicePublishMetricInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "decr": MetricsDecr.from_dict(obj.get("decr")) if obj.get("decr") is not None else None,
            "event": MetricsEvent.from_dict(obj.get("event")) if obj.get("event") is not None else None,
            "incr": MetricsIncr.from_dict(obj.get("incr")) if obj.get("incr") is not None else None,
            "timing": MetricsTiming.from_dict(obj.get("timing")) if obj.get("timing") is not None else None
        })
        return _obj


