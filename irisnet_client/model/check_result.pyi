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


class CheckResult(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The root object returned after a check operation.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def summary() -> typing.Type['Summary']:
                return Summary
            
            
            class encodings(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Encoded']:
                        return Encoded
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Encoded'], typing.List['Encoded']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'encodings':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Encoded':
                    return super().__getitem__(i)
            
            
            class brokenRules(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['BrokenRule']:
                        return BrokenRule
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['BrokenRule'], typing.List['BrokenRule']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'brokenRules':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'BrokenRule':
                    return super().__getitem__(i)
            
            
            class detections(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.ComposedSchema,
                    ):
                    
                    
                        class MetaOapg:
                            
                            @classmethod
                            @functools.lru_cache()
                            def one_of(cls):
                                # we need this here to make our import statements work
                                # we must store _composed_schemas in here so the code is only run
                                # when we invoke this method. If we kept this at the class
                                # level we would get an error because the class level
                                # code would be run when this module is imported, and these composed
                                # classes don't exist yet because their module has not finished
                                # loading
                                return [
                                    BaseDetection,
                                    BreastDetection,
                                    FaceDetection,
                                    HairDetection,
                                ]
                    
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'detections':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class events(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Event']:
                        return Event
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Event'], typing.List['Event']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'events':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Event':
                    return super().__getitem__(i)
            
            
            class notifications(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ApiNotice']:
                        return ApiNotice
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ApiNotice'], typing.List['ApiNotice']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'notifications':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ApiNotice':
                    return super().__getitem__(i)
            __annotations__ = {
                "summary": summary,
                "encodings": encodings,
                "brokenRules": brokenRules,
                "detections": detections,
                "events": events,
                "notifications": notifications,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["summary"]) -> 'Summary': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["encodings"]) -> MetaOapg.properties.encodings: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["brokenRules"]) -> MetaOapg.properties.brokenRules: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["detections"]) -> MetaOapg.properties.detections: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["events"]) -> MetaOapg.properties.events: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notifications"]) -> MetaOapg.properties.notifications: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["summary", "encodings", "brokenRules", "detections", "events", "notifications", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["summary"]) -> typing.Union['Summary', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["encodings"]) -> typing.Union[MetaOapg.properties.encodings, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["brokenRules"]) -> typing.Union[MetaOapg.properties.brokenRules, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["detections"]) -> typing.Union[MetaOapg.properties.detections, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["events"]) -> typing.Union[MetaOapg.properties.events, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notifications"]) -> typing.Union[MetaOapg.properties.notifications, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["summary", "encodings", "brokenRules", "detections", "events", "notifications", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        summary: typing.Union['Summary', schemas.Unset] = schemas.unset,
        encodings: typing.Union[MetaOapg.properties.encodings, list, tuple, schemas.Unset] = schemas.unset,
        brokenRules: typing.Union[MetaOapg.properties.brokenRules, list, tuple, schemas.Unset] = schemas.unset,
        detections: typing.Union[MetaOapg.properties.detections, list, tuple, schemas.Unset] = schemas.unset,
        events: typing.Union[MetaOapg.properties.events, list, tuple, schemas.Unset] = schemas.unset,
        notifications: typing.Union[MetaOapg.properties.notifications, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CheckResult':
        return super().__new__(
            cls,
            *_args,
            summary=summary,
            encodings=encodings,
            brokenRules=brokenRules,
            detections=detections,
            events=events,
            notifications=notifications,
            _configuration=_configuration,
            **kwargs,
        )

from irisnet_client.model.api_notice import ApiNotice
from irisnet_client.model.base_detection import BaseDetection
from irisnet_client.model.breast_detection import BreastDetection
from irisnet_client.model.broken_rule import BrokenRule
from irisnet_client.model.encoded import Encoded
from irisnet_client.model.event import Event
from irisnet_client.model.face_detection import FaceDetection
from irisnet_client.model.hair_detection import HairDetection
from irisnet_client.model.summary import Summary
