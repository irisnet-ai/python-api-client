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


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator

class ApiNotice(BaseModel):
    """
    ApiNotice
    """
    code: Optional[StrictInt] = Field(None, description="The status code of the response.")
    level: Optional[StrictStr] = Field(None, description="The severity level of the notice.")
    message: Optional[StrictStr] = Field(None, description="A hopefully detailed message describing what went wrong.")
    __properties = ["code", "level", "message"]

    @validator('level')
    def level_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('INFO', 'WARN', 'ERROR'):
            raise ValueError("must be one of enum values ('INFO', 'WARN', 'ERROR')")
        return value

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
    def from_json(cls, json_str: str) -> ApiNotice:
        """Create an instance of ApiNotice from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiNotice:
        """Create an instance of ApiNotice from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiNotice.parse_obj(obj)

        _obj = ApiNotice.parse_obj({
            "code": obj.get("code"),
            "level": obj.get("level"),
            "message": obj.get("message")
        })
        return _obj


