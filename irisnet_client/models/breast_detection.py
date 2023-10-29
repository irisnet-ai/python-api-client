# coding: utf-8

"""
    Irisnet API

    Artificial Intelligence (AI) for image- and video-processing in real-time. This is an interactive documentation where you can quickly look up the endpoints and their schemas, while having the opportunity to try things out for yourself.  In the list below, you can see the available endpoints of the API, which can be expanded by clicking on them. Each expanded endpoint lists the request parameters (if available) and the request body (if available). The request body can list some example bodies and the schema, explaining each model in detail.  Additionally you'll find a 'Try it out' button that allows you to enter your custom parameters and custom body and execute that against the API. <b>Be sure to enter your license key to authorize the requests before using this documentation interactively.</b>  The responses section in the expanded endpoint lists the possible responses with their corresponding status codes. If you've executed an API call it will also show you the response from the server.  Underneath the endpoints you'll find the model schemas. These are the models used for the requests and responses. If you click on the right arrow, you can expand the model and get a description of the model and the model parameters. For nested models, you can keep clicking the right arrow for further details.  Clicking the link below the title at the top of this page opens the [OpenAPI specification](https://swagger.io/specification/) (OAS3) in JSON format. The OAS3 Spec allows the generation of clients in many programming languages. There are several free client generators available that can be used to get started easily.

    The version of the OpenAPI document: v2
    Contact: info@irisnet.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import Field, conlist
from irisnet_client.models.base_attribute import BaseAttribute
from irisnet_client.models.base_detection import BaseDetection
from irisnet_client.models.coordinates import Coordinates

class BreastDetection(BaseDetection):
    """
    Contains further characteristics particular to _breast_ detection.  # noqa: E501
    """
    attributes: Optional[conlist(BaseAttribute)] = Field(None, description="Attributes characterizing the _breast_ detection. Mainly contains attributes that were activated with the _nippleCheck_ prototype.")
    __properties = ["classification", "group", "id", "probability", "coordinates", "type", "attributes"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> BreastDetection:
        """Create an instance of BreastDetection from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of coordinates
        if self.coordinates:
            _dict['coordinates'] = self.coordinates.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in attributes (list)
        _items = []
        if self.attributes:
            for _item in self.attributes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['attributes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BreastDetection:
        """Create an instance of BreastDetection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BreastDetection.parse_obj(obj)

        _obj = BreastDetection.parse_obj({
            "classification": obj.get("classification"),
            "group": obj.get("group"),
            "id": obj.get("id"),
            "probability": obj.get("probability"),
            "coordinates": Coordinates.from_dict(obj.get("coordinates")) if obj.get("coordinates") is not None else None,
            "type": obj.get("type"),
            "attributes": [BaseAttribute.from_dict(_item) for _item in obj.get("attributes")] if obj.get("attributes") is not None else None
        })
        return _obj

