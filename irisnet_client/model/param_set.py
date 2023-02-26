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


class ParamSet(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A set of parameters/rules that describe how the AI should behave.
    """


    class MetaOapg:
        
        class properties:
            
            
            class thresh(
                schemas.Float32Schema
            ):
            
            
                class MetaOapg:
                    format = 'float'
                    inclusive_maximum = 1.0
                    inclusive_minimum = 0.0
            
            
            class grey(
                schemas.Int32Schema
            ):
            
            
                class MetaOapg:
                    format = 'int32'
                    inclusive_maximum = 255
                    inclusive_minimum = 0
            
            
            class minDuration(
                schemas.Int32Schema
            ):
            
            
                class MetaOapg:
                    format = 'int32'
                    inclusive_maximum = 250
                    inclusive_minimum = 50
            
            
            class abortOnSeverity(
                schemas.Int32Schema
            ):
            
            
                class MetaOapg:
                    format = 'int32'
                    inclusive_minimum = -1
            
            
            class params(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Param']:
                        return Param
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Param'], typing.List['Param']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'params':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Param':
                    return super().__getitem__(i)
            __annotations__ = {
                "thresh": thresh,
                "grey": grey,
                "minDuration": minDuration,
                "abortOnSeverity": abortOnSeverity,
                "params": params,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thresh"]) -> MetaOapg.properties.thresh: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["grey"]) -> MetaOapg.properties.grey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minDuration"]) -> MetaOapg.properties.minDuration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["abortOnSeverity"]) -> MetaOapg.properties.abortOnSeverity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["params"]) -> MetaOapg.properties.params: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["thresh", "grey", "minDuration", "abortOnSeverity", "params", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thresh"]) -> typing.Union[MetaOapg.properties.thresh, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["grey"]) -> typing.Union[MetaOapg.properties.grey, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minDuration"]) -> typing.Union[MetaOapg.properties.minDuration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["abortOnSeverity"]) -> typing.Union[MetaOapg.properties.abortOnSeverity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["params"]) -> typing.Union[MetaOapg.properties.params, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["thresh", "grey", "minDuration", "abortOnSeverity", "params", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        thresh: typing.Union[MetaOapg.properties.thresh, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        grey: typing.Union[MetaOapg.properties.grey, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        minDuration: typing.Union[MetaOapg.properties.minDuration, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        abortOnSeverity: typing.Union[MetaOapg.properties.abortOnSeverity, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        params: typing.Union[MetaOapg.properties.params, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ParamSet':
        return super().__new__(
            cls,
            *_args,
            thresh=thresh,
            grey=grey,
            minDuration=minDuration,
            abortOnSeverity=abortOnSeverity,
            params=params,
            _configuration=_configuration,
            **kwargs,
        )

from irisnet_client.model.param import Param
