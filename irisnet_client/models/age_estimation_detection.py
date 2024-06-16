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

from pydantic import ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from irisnet_client.models.age_estimation_attribute import AgeEstimationAttribute
from irisnet_client.models.age_estimation_sub_checks import AgeEstimationSubChecks
from irisnet_client.models.base_detection import BaseDetection
from typing import Optional, Set
from typing_extensions import Self

class AgeEstimationDetection(BaseDetection):
    """
    Contains further characteristics particular to _ageEstimation_ detection.
    """ # noqa: E501
    check_id: Optional[StrictStr] = Field(default=None, description="The id of the check that lead to the detection", alias="checkId")
    face_similarity: Optional[StrictInt] = Field(default=None, description="Indicates the similarity-level of whether two faces belong to the same person", alias="faceSimilarity")
    face_liveness_check_score: Optional[StrictInt] = Field(default=None, description="Indicates the liveness score of the selfie image", alias="faceLivenessCheckScore")
    processed_checks: Optional[AgeEstimationSubChecks] = Field(default=None, alias="processedChecks")
    attributes: Optional[List[AgeEstimationAttribute]] = Field(default=None, description="Attributes of the _idDocument_ detection.")
    __properties: ClassVar[List[str]] = ["type", "attributes", "subDetections", "checkId", "hasOfficialDocument", "comparable", "faceSimilarity", "faceLivenessCheckScore", "documentFrontLivenessScore", "documentBackLivenessScore", "processedChecks", "documentHolderId"]

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
        """Create an instance of AgeEstimationDetection from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in attributes (list)
        _items = []
        if self.attributes:
            for _item in self.attributes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['attributes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in sub_detections (list)
        _items = []
        if self.sub_detections:
            for _item in self.sub_detections:
                if _item:
                    _items.append(_item.to_dict())
            _dict['subDetections'] = _items
        # override the default output from pydantic by calling `to_dict()` of processed_checks
        if self.processed_checks:
            _dict['processedChecks'] = self.processed_checks.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AgeEstimationDetection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "attributes": [AgeEstimationAttribute.from_dict(_item) for _item in obj["attributes"]] if obj.get("attributes") is not None else None,
            "subDetections": [BaseDetection.from_dict(_item) for _item in obj["subDetections"]] if obj.get("subDetections") is not None else None,
            "checkId": obj.get("checkId"),
            "hasOfficialDocument": obj.get("hasOfficialDocument"),
            "comparable": obj.get("comparable"),
            "faceSimilarity": obj.get("faceSimilarity"),
            "faceLivenessCheckScore": obj.get("faceLivenessCheckScore"),
            "documentFrontLivenessScore": obj.get("documentFrontLivenessScore"),
            "documentBackLivenessScore": obj.get("documentBackLivenessScore"),
            "processedChecks": AgeEstimationSubChecks.from_dict(obj["processedChecks"]) if obj.get("processedChecks") is not None else None,
            "documentHolderId": obj.get("documentHolderId")
        })
        return _obj

