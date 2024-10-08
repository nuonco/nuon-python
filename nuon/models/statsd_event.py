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




from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from nuon.models.statsd_event_alert_type import StatsdEventAlertType
from nuon.models.statsd_event_priority import StatsdEventPriority
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class StatsdEvent(BaseModel):
    """
    StatsdEvent
    """ # noqa: E501
    aggregation_key: Optional[StrictStr] = Field(default=None, description="AggregationKey groups this event with others of the same key.", alias="aggregationKey")
    alert_type: Optional[StatsdEventAlertType] = Field(default=None, description="AlertType can be statsd.Info, statsd.Error, statsd.Warning, or statsd.Success. If absent, the default value applied by the dogstatsd server is Info.", alias="alertType")
    hostname: Optional[StrictStr] = Field(default=None, description="Hostname for the event.")
    priority: Optional[StatsdEventPriority] = Field(default=None, description="Priority of the event.  Can be statsd.Low or statsd.Normal.")
    source_type_name: Optional[StrictStr] = Field(default=None, description="SourceTypeName is a source type for the event.", alias="sourceTypeName")
    tags: Optional[List[StrictStr]] = Field(default=None, description="Tags for the event.")
    text: Optional[StrictStr] = Field(default=None, description="Text is the description of the event.")
    timestamp: Optional[StrictStr] = Field(default=None, description="Timestamp is a timestamp for the event.  If not provided, the dogstatsd server will set this to the current time.")
    title: Optional[StrictStr] = Field(default=None, description="Title of the event.  Required.")
    __properties: ClassVar[List[str]] = ["aggregationKey", "alertType", "hostname", "priority", "sourceTypeName", "tags", "text", "timestamp", "title"]

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
        """Create an instance of StatsdEvent from a JSON string"""
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
        """Create an instance of StatsdEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "aggregationKey": obj.get("aggregationKey"),
            "alertType": obj.get("alertType"),
            "hostname": obj.get("hostname"),
            "priority": obj.get("priority"),
            "sourceTypeName": obj.get("sourceTypeName"),
            "tags": obj.get("tags"),
            "text": obj.get("text"),
            "timestamp": obj.get("timestamp"),
            "title": obj.get("title")
        })
        return _obj


