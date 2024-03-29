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
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, field_validator
from irisnet_client.models.base_detection import BaseDetection
from irisnet_client.models.breast_detection import BreastDetection
from irisnet_client.models.face_detection import FaceDetection
from irisnet_client.models.hair_detection import HairDetection
from typing import Union, Any, List, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal
from pydantic import StrictStr, Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

CHECKRESULTDETECTIONSINNER_ONE_OF_SCHEMAS = ["BaseDetection", "BreastDetection", "FaceDetection", "HairDetection"]

class CheckResultDetectionsInner(BaseModel):
    """
    CheckResultDetectionsInner
    """
    # data type: BaseDetection
    oneof_schema_1_validator: Optional[BaseDetection] = None
    # data type: BreastDetection
    oneof_schema_2_validator: Optional[BreastDetection] = None
    # data type: FaceDetection
    oneof_schema_3_validator: Optional[FaceDetection] = None
    # data type: HairDetection
    oneof_schema_4_validator: Optional[HairDetection] = None
    actual_instance: Optional[Union[BaseDetection, BreastDetection, FaceDetection, HairDetection]] = None
    one_of_schemas: List[str] = Literal["BaseDetection", "BreastDetection", "FaceDetection", "HairDetection"]

    model_config = {
        "validate_assignment": True
    }


    discriminator_value_class_map: Dict[str, str] = {
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = CheckResultDetectionsInner.model_construct()
        error_messages = []
        match = 0
        # validate data type: BaseDetection
        if not isinstance(v, BaseDetection):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BaseDetection`")
        else:
            match += 1
        # validate data type: BreastDetection
        if not isinstance(v, BreastDetection):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BreastDetection`")
        else:
            match += 1
        # validate data type: FaceDetection
        if not isinstance(v, FaceDetection):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FaceDetection`")
        else:
            match += 1
        # validate data type: HairDetection
        if not isinstance(v, HairDetection):
            error_messages.append(f"Error! Input type `{type(v)}` is not `HairDetection`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in CheckResultDetectionsInner with oneOf schemas: BaseDetection, BreastDetection, FaceDetection, HairDetection. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in CheckResultDetectionsInner with oneOf schemas: BaseDetection, BreastDetection, FaceDetection, HairDetection. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into BaseDetection
        try:
            instance.actual_instance = BaseDetection.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BreastDetection
        try:
            instance.actual_instance = BreastDetection.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into FaceDetection
        try:
            instance.actual_instance = FaceDetection.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into HairDetection
        try:
            instance.actual_instance = HairDetection.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into CheckResultDetectionsInner with oneOf schemas: BaseDetection, BreastDetection, FaceDetection, HairDetection. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into CheckResultDetectionsInner with oneOf schemas: BaseDetection, BreastDetection, FaceDetection, HairDetection. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


