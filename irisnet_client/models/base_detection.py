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
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Optional
from irisnet_client.models.breast_detection import BreastDetection
from irisnet_client.models.hair_detection import HairDetection
from irisnet_client.models.id_document_detection import IdDocumentDetection
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field

BASEDETECTION_ANY_OF_SCHEMAS = ["BaseDetection", "BreastDetection", "FaceDetection", "HairDetection", "IdDocumentDetection"]

class BaseDetection(BaseModel):
    """
    A detection describes the object found with all its details.
    """

    # data type: BaseDetection
    anyof_schema_1_validator: Optional[BaseDetection] = None
    # data type: FaceDetection
    anyof_schema_2_validator: Optional[FaceDetection] = None
    # data type: BreastDetection
    anyof_schema_3_validator: Optional[BreastDetection] = None
    # data type: HairDetection
    anyof_schema_4_validator: Optional[HairDetection] = None
    # data type: IdDocumentDetection
    anyof_schema_5_validator: Optional[IdDocumentDetection] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[BaseDetection, BreastDetection, FaceDetection, HairDetection, IdDocumentDetection]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: Set[str] = { "BaseDetection", "BreastDetection", "FaceDetection", "HairDetection", "IdDocumentDetection" }

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    discriminator_value_class_map: Dict[str, str] = {
        'BreastDetection': 'BreastDetection',
        'FaceDetection': 'FaceDetection',
        'HairDetection': 'HairDetection',
        'IdDocumentDetection': 'IdDocumentDetection'
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
    def actual_instance_must_validate_anyof(cls, v):
        instance = BaseDetection.model_construct()
        error_messages = []
        # validate data type: BaseDetection
        if not isinstance(v, BaseDetection):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BaseDetection`")
        else:
            return v

        # validate data type: FaceDetection
        if not isinstance(v, FaceDetection):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FaceDetection`")
        else:
            return v

        # validate data type: BreastDetection
        if not isinstance(v, BreastDetection):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BreastDetection`")
        else:
            return v

        # validate data type: HairDetection
        if not isinstance(v, HairDetection):
            error_messages.append(f"Error! Input type `{type(v)}` is not `HairDetection`")
        else:
            return v

        # validate data type: IdDocumentDetection
        if not isinstance(v, IdDocumentDetection):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IdDocumentDetection`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in BaseDetection with anyOf schemas: BaseDetection, BreastDetection, FaceDetection, HairDetection, IdDocumentDetection. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[BaseDetection] = None
        try:
            instance.actual_instance = BaseDetection.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[FaceDetection] = None
        try:
            instance.actual_instance = FaceDetection.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_3_validator: Optional[BreastDetection] = None
        try:
            instance.actual_instance = BreastDetection.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_4_validator: Optional[HairDetection] = None
        try:
            instance.actual_instance = HairDetection.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_5_validator: Optional[IdDocumentDetection] = None
        try:
            instance.actual_instance = IdDocumentDetection.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into BaseDetection with anyOf schemas: BaseDetection, BreastDetection, FaceDetection, HairDetection, IdDocumentDetection. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], BaseDetection, BreastDetection, FaceDetection, HairDetection, IdDocumentDetection]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())

from irisnet_client.models.face_detection import FaceDetection
# TODO: Rewrite to not use raise_errors
BaseDetection.model_rebuild(raise_errors=False)

