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


class LicenseInfo(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Describes the current balance of the given license key. A key has a certain amount of credits that can be used for any kind of AI recognition. The license key is invalid, when all of the credits have been used, the license was disabled or expired.
    """


    class MetaOapg:
        
        class properties:
            creditsUsed = schemas.Int32Schema
            creditsRemaining = schemas.Int32Schema
            totalCredits = schemas.Int32Schema
            licenseKey = schemas.StrSchema
            
            
            class privileges(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.StrSchema
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, str, ],
                ) -> 'privileges':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "creditsUsed": creditsUsed,
                "creditsRemaining": creditsRemaining,
                "totalCredits": totalCredits,
                "licenseKey": licenseKey,
                "privileges": privileges,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creditsUsed"]) -> MetaOapg.properties.creditsUsed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creditsRemaining"]) -> MetaOapg.properties.creditsRemaining: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalCredits"]) -> MetaOapg.properties.totalCredits: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["licenseKey"]) -> MetaOapg.properties.licenseKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["privileges"]) -> MetaOapg.properties.privileges: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["creditsUsed", "creditsRemaining", "totalCredits", "licenseKey", "privileges", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creditsUsed"]) -> typing.Union[MetaOapg.properties.creditsUsed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creditsRemaining"]) -> typing.Union[MetaOapg.properties.creditsRemaining, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalCredits"]) -> typing.Union[MetaOapg.properties.totalCredits, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["licenseKey"]) -> typing.Union[MetaOapg.properties.licenseKey, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["privileges"]) -> typing.Union[MetaOapg.properties.privileges, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["creditsUsed", "creditsRemaining", "totalCredits", "licenseKey", "privileges", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        creditsUsed: typing.Union[MetaOapg.properties.creditsUsed, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        creditsRemaining: typing.Union[MetaOapg.properties.creditsRemaining, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        totalCredits: typing.Union[MetaOapg.properties.totalCredits, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        licenseKey: typing.Union[MetaOapg.properties.licenseKey, str, schemas.Unset] = schemas.unset,
        privileges: typing.Union[MetaOapg.properties.privileges, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LicenseInfo':
        return super().__new__(
            cls,
            *_args,
            creditsUsed=creditsUsed,
            creditsRemaining=creditsRemaining,
            totalCredits=totalCredits,
            licenseKey=licenseKey,
            privileges=privileges,
            _configuration=_configuration,
            **kwargs,
        )
