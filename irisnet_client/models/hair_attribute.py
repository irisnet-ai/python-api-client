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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class HairAttribute(BaseModel):
    """
    Attributes qualifying the _hair_ classification.
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="Used as a type discriminator for json to object conversion.")
    color: Optional[StrictStr] = Field(default=None, description="The color of the hair.")
    style: Optional[StrictStr] = Field(default=None, description="The hair style.")
    __properties: ClassVar[List[str]] = ["type", "color", "style"]

    @field_validator('color')
    def color_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['black', 'darkBrown', 'brown', 'lightBrown', 'darkBlonde', 'blonde', 'darkGrey', 'grey', 'red', 'white', 'other']):
            raise ValueError("must be one of enum values ('black', 'darkBrown', 'brown', 'lightBrown', 'darkBlonde', 'blonde', 'darkGrey', 'grey', 'red', 'white', 'other')")
        return value

    @field_validator('style')
    def style_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['longHaired', 'shortHaired']):
            raise ValueError("must be one of enum values ('longHaired', 'shortHaired')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of HairAttribute from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HairAttribute from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "color": obj.get("color"),
            "style": obj.get("style")
        })
        return _obj


