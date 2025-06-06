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
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class Config(BaseModel):
    """
    Can be used to set a multitude of pre-defined commonly used rules without the need of specifying each parameter set.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="The unique identifier for the AI configuration. Use this for any check operation to tell the AI how to behave.")
    name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The name of the AI configuration.")
    kyc_check_parameters: Optional[List[StrictStr]] = Field(default=None, description="Configures your kyc checks. You can combine certain parameters to customize a single check operation.", alias="kycCheckParameters")
    prototypes: Optional[List[StrictStr]] = Field(default=None, description="Configures your detection. As there are literally hundreds of parameters, prototypes can be used to get useful behaviour. This includes a default setting for parameters and rules that should be applied to the check operations. You can use multiple prototypes for a single check operation.")
    __properties: ClassVar[List[str]] = ["id", "name", "kycCheckParameters", "prototypes"]

    @field_validator('name')
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9a-zA-Z _-]{0,100}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-zA-Z _-]{0,100}$/")
        return value

    @field_validator('kyc_check_parameters')
    def kyc_check_parameters_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['identityDocumentCheck', 'automatedDocumentRecognition', 'biometricCheck', 'formAutofill', 'ageVerificationCheck', 'proofOfAddressCheck', 'faceAuthentication', 'liveIdentification', 'liveIdentityDocumentCheck', 'liveSelfie', 'liveProofOfAddressCheck', 'liveAgeVerificationCheck', 'liveFaceAuthentication', 'videoUploadIdentification', 'considerKnownFaces', 'addEncodingsToResult', 'iFrameFlow', 'redirectFlow']):
                raise ValueError("each list item must be one of ('identityDocumentCheck', 'automatedDocumentRecognition', 'biometricCheck', 'formAutofill', 'ageVerificationCheck', 'proofOfAddressCheck', 'faceAuthentication', 'liveIdentification', 'liveIdentityDocumentCheck', 'liveSelfie', 'liveProofOfAddressCheck', 'liveAgeVerificationCheck', 'liveFaceAuthentication', 'videoUploadIdentification', 'considerKnownFaces', 'addEncodingsToResult', 'iFrameFlow', 'redirectFlow')")
        return value

    @field_validator('prototypes')
    def prototypes_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['nudityCheck', 'ageEstimation', 'illegalSymbols', 'textRecognition', 'attributesCheck', 'bodyAttributes', 'nippleCheck', 'unwantedSubstances', 'violenceCheck', 'selfieCheck']):
                raise ValueError("each list item must be one of ('nudityCheck', 'ageEstimation', 'illegalSymbols', 'textRecognition', 'attributesCheck', 'bodyAttributes', 'nippleCheck', 'unwantedSubstances', 'violenceCheck', 'selfieCheck')")
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
        """Create an instance of Config from a JSON string"""
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
        """Create an instance of Config from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "kycCheckParameters": obj.get("kycCheckParameters"),
            "prototypes": obj.get("prototypes")
        })
        return _obj


