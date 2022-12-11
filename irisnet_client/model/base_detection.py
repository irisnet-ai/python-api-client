# coding: utf-8

"""
    Irisnet API

    Artificial Intelligence (AI) for image- and video-processing in real-time. This is an interactive documentation where you can quickly look up the endpoints and their schemas, while having the opportunity to try things out for yourself.  In the list below, you can see the available endpoints of the API, which can be expanded by clicking on them. Each expanded endpoint lists the request parameters (if available) and the request body (if available). The request body can list some example bodies and the schema, explaining each model in detail.  Additionally you'll find a 'Try it out' button that allows you to enter your custom parameters and custom body and execute that against the API. <b>Be sure to enter your license key to authorize the requests before using this documentation interactively.</b>  The responses section in the expanded endpoint lists the possible responses with their corresponding status codes. If you've executed an API call it will also show you the response from the server.  Underneath the endpoints you'll find the model schemas. These are the models used for the requests and responses. If you click on the right arrow, you can expand the model and get a description of the model and the model parameters. For nested models, you can keep clicking the right arrow for further details.  Clicking the link below the title at the top of this page opens the [OpenAPI specification](https://swagger.io/specification/) (OAS3) in JSON format. The OAS3 Spec allows the generation of clients in many programming languages. There are several free client generators available that can be used to get started easily.  # noqa: E501

    The version of the OpenAPI document: v2
    Contact: info@irisnet.de
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from irisnet_client import schemas  # noqa: F401


class BaseDetection(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A detection describes the object found with all its details.
    """


    class MetaOapg:
        
        @staticmethod
        def discriminator():
            return {
                'type': {
                    'BreastDetection': BreastDetection,
                    'FaceDetection': FaceDetection,
                    'HairDetection': HairDetection,
                }
            }
        
        class properties:
            classification = schemas.StrSchema
            group = schemas.StrSchema
            id = schemas.Int32Schema
            probability = schemas.Int32Schema
        
            @staticmethod
            def coordinates() -> typing.Type['Coordinates']:
                return Coordinates
            type = schemas.StrSchema
            __annotations__ = {
                "classification": classification,
                "group": group,
                "id": id,
                "probability": probability,
                "coordinates": coordinates,
                "type": type,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["classification"]) -> MetaOapg.properties.classification: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["group"]) -> MetaOapg.properties.group: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["probability"]) -> MetaOapg.properties.probability: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coordinates"]) -> 'Coordinates': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["classification", "group", "id", "probability", "coordinates", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["classification"]) -> typing.Union[MetaOapg.properties.classification, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["group"]) -> typing.Union[MetaOapg.properties.group, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["probability"]) -> typing.Union[MetaOapg.properties.probability, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coordinates"]) -> typing.Union['Coordinates', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["classification", "group", "id", "probability", "coordinates", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        classification: typing.Union[MetaOapg.properties.classification, str, schemas.Unset] = schemas.unset,
        group: typing.Union[MetaOapg.properties.group, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        probability: typing.Union[MetaOapg.properties.probability, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        coordinates: typing.Union['Coordinates', schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BaseDetection':
        return super().__new__(
            cls,
            *args,
            classification=classification,
            group=group,
            id=id,
            probability=probability,
            coordinates=coordinates,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )

from irisnet_client.model.breast_detection import BreastDetection
from irisnet_client.model.coordinates import Coordinates
from irisnet_client.model.face_detection import FaceDetection
from irisnet_client.model.hair_detection import HairDetection
