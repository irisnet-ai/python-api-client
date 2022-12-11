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


class Summary(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Summarizing the result of the AI.
    """


    class MetaOapg:
        
        class properties:
            status = schemas.StrSchema
            brokenRulesCount = schemas.Int32Schema
            helpSuggested = schemas.Int32Schema
            severity = schemas.Int32Schema
            creditsConsumed = schemas.Int32Schema
            
            
            class tags(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    unique_items = True
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tags':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class rejectTags(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    unique_items = True
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'rejectTags':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class rejectReasons(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    unique_items = True
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'rejectReasons':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "status": status,
                "brokenRulesCount": brokenRulesCount,
                "helpSuggested": helpSuggested,
                "severity": severity,
                "creditsConsumed": creditsConsumed,
                "tags": tags,
                "rejectTags": rejectTags,
                "rejectReasons": rejectReasons,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["brokenRulesCount"]) -> MetaOapg.properties.brokenRulesCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["helpSuggested"]) -> MetaOapg.properties.helpSuggested: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["severity"]) -> MetaOapg.properties.severity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creditsConsumed"]) -> MetaOapg.properties.creditsConsumed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> MetaOapg.properties.tags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rejectTags"]) -> MetaOapg.properties.rejectTags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rejectReasons"]) -> MetaOapg.properties.rejectReasons: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["status", "brokenRulesCount", "helpSuggested", "severity", "creditsConsumed", "tags", "rejectTags", "rejectReasons", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["brokenRulesCount"]) -> typing.Union[MetaOapg.properties.brokenRulesCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["helpSuggested"]) -> typing.Union[MetaOapg.properties.helpSuggested, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["severity"]) -> typing.Union[MetaOapg.properties.severity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creditsConsumed"]) -> typing.Union[MetaOapg.properties.creditsConsumed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> typing.Union[MetaOapg.properties.tags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rejectTags"]) -> typing.Union[MetaOapg.properties.rejectTags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rejectReasons"]) -> typing.Union[MetaOapg.properties.rejectReasons, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["status", "brokenRulesCount", "helpSuggested", "severity", "creditsConsumed", "tags", "rejectTags", "rejectReasons", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        brokenRulesCount: typing.Union[MetaOapg.properties.brokenRulesCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        helpSuggested: typing.Union[MetaOapg.properties.helpSuggested, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        severity: typing.Union[MetaOapg.properties.severity, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        creditsConsumed: typing.Union[MetaOapg.properties.creditsConsumed, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        tags: typing.Union[MetaOapg.properties.tags, list, tuple, schemas.Unset] = schemas.unset,
        rejectTags: typing.Union[MetaOapg.properties.rejectTags, list, tuple, schemas.Unset] = schemas.unset,
        rejectReasons: typing.Union[MetaOapg.properties.rejectReasons, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Summary':
        return super().__new__(
            cls,
            *args,
            status=status,
            brokenRulesCount=brokenRulesCount,
            helpSuggested=helpSuggested,
            severity=severity,
            creditsConsumed=creditsConsumed,
            tags=tags,
            rejectTags=rejectTags,
            rejectReasons=rejectReasons,
            _configuration=_configuration,
            **kwargs,
        )