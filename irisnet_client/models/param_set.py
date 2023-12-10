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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel
from pydantic import Field
from typing_extensions import Annotated
from irisnet_client.models.param import Param
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ParamSet(BaseModel):
    """
    A set of parameters/rules that describe how the AI should behave.
    """ # noqa: E501
    thresh: Optional[Union[Annotated[float, Field(le=1.0, strict=True, ge=0.0)], Annotated[int, Field(le=1, strict=True, ge=0)]]] = Field(default=0.5, description="Threshold when an object can be recognized. Lowering the value will increase the probability of recognizing objects. A threshold of 0.5 would mean, that 50% of an object like a face must be visible, to be detected.Setting the value too low however, can cause false positives.")
    grey: Optional[Annotated[int, Field(le=255, strict=True, ge=0)]] = Field(default=127, description="A grey scale color to use for frame or masking. '0' will represent black, while the maximum '255' will be white.")
    min_duration: Optional[Annotated[int, Field(le=250, strict=True, ge=50)]] = Field(default=100, description="Set the overall minimum duration in milliseconds for a rule to be broken in moving images.", alias="minDuration")
    abort_on_severity: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=-1, description="Set a severity on which to automatically stop the check operation. Works with moving images.Use '-1' to ignore this option.", alias="abortOnSeverity")
    params: Optional[List[Param]] = Field(default=None, description="A list of parameter sets that describe the rules of the objects.")
    __properties: ClassVar[List[str]] = ["thresh", "grey", "minDuration", "abortOnSeverity", "params"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
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
        """Create an instance of ParamSet from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in params (list)
        _items = []
        if self.params:
            for _item in self.params:
                if _item:
                    _items.append(_item.to_dict())
            _dict['params'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ParamSet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "thresh": obj.get("thresh") if obj.get("thresh") is not None else 0.5,
            "grey": obj.get("grey") if obj.get("grey") is not None else 127,
            "minDuration": obj.get("minDuration") if obj.get("minDuration") is not None else 100,
            "abortOnSeverity": obj.get("abortOnSeverity") if obj.get("abortOnSeverity") is not None else -1,
            "params": [Param.from_dict(_item) for _item in obj.get("params")] if obj.get("params") is not None else None
        })
        return _obj


