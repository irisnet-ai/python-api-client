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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class IdDocumentAttribute(BaseModel):
    """
    Attributes qualifying the _idDocument_ classification.
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="Used as a type discriminator for json to object conversion.")
    document_type: Optional[StrictStr] = Field(default=None, description="The type of the document", alias="documentType")
    document_number: Optional[StrictStr] = Field(default=None, description="The number of the document", alias="documentNumber")
    is_two_sided: Optional[StrictBool] = Field(default=None, description="Indicates whether the document is two-sided", alias="isTwoSided")
    issuing_authority: Optional[StrictStr] = Field(default=None, description="The issuing authority", alias="issuingAuthority")
    issuing_date: Optional[date] = Field(default=None, description="The issuing date", alias="issuingDate")
    issuing_country: Optional[StrictStr] = Field(default=None, description="The document's country in ISO 3166-1 alpha-2 format", alias="issuingCountry")
    expiration_date: Optional[date] = Field(default=None, description="The expiration date", alias="expirationDate")
    access_number: Optional[StrictStr] = Field(default=None, description="The access number", alias="accessNumber")
    first_names: Optional[List[StrictStr]] = Field(default=None, description="The document holder's first name(s)", alias="firstNames")
    last_names: Optional[List[StrictStr]] = Field(default=None, description="The document holder's last name(s)", alias="lastNames")
    birth_name: Optional[StrictStr] = Field(default=None, description="The document holder's birth name", alias="birthName")
    date_of_birth: Optional[date] = Field(default=None, description="The document holder's date of birth", alias="dateOfBirth")
    place_of_birth: Optional[StrictStr] = Field(default=None, description="The document holder's place of birth", alias="placeOfBirth")
    nationality: Optional[StrictStr] = Field(default=None, description="The document holder's nationality in ISO 3166-1 alpha-2 format")
    gender: Optional[StrictStr] = Field(default=None, description="The document holder's gender")
    height: Optional[StrictStr] = Field(default=None, description="The document holder's height")
    address: Optional[StrictStr] = Field(default=None, description="The document holder's address")
    machine_readable_zone: Optional[List[StrictStr]] = Field(default=None, description="The document's machine readable zone (MRZ), at most 3 lines", alias="machineReadableZone")
    __properties: ClassVar[List[str]] = ["type", "documentType", "documentNumber", "isTwoSided", "issuingAuthority", "issuingDate", "issuingCountry", "expirationDate", "accessNumber", "firstNames", "lastNames", "birthName", "dateOfBirth", "placeOfBirth", "nationality", "gender", "height", "address", "machineReadableZone"]

    @field_validator('document_type')
    def document_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['passport', 'driving_license', 'national_identity_card', 'residence_permit', 'visa', 'unknown']):
            raise ValueError("must be one of enum values ('passport', 'driving_license', 'national_identity_card', 'residence_permit', 'visa', 'unknown')")
        return value

    @field_validator('gender')
    def gender_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['male', 'female', 'other']):
            raise ValueError("must be one of enum values ('male', 'female', 'other')")
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
        """Create an instance of IdDocumentAttribute from a JSON string"""
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
        """Create an instance of IdDocumentAttribute from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "documentType": obj.get("documentType"),
            "documentNumber": obj.get("documentNumber"),
            "isTwoSided": obj.get("isTwoSided"),
            "issuingAuthority": obj.get("issuingAuthority"),
            "issuingDate": obj.get("issuingDate"),
            "issuingCountry": obj.get("issuingCountry"),
            "expirationDate": obj.get("expirationDate"),
            "accessNumber": obj.get("accessNumber"),
            "firstNames": obj.get("firstNames"),
            "lastNames": obj.get("lastNames"),
            "birthName": obj.get("birthName"),
            "dateOfBirth": obj.get("dateOfBirth"),
            "placeOfBirth": obj.get("placeOfBirth"),
            "nationality": obj.get("nationality"),
            "gender": obj.get("gender"),
            "height": obj.get("height"),
            "address": obj.get("address"),
            "machineReadableZone": obj.get("machineReadableZone")
        })
        return _obj


