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


class Param(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A single parameter set for one classification, for example face, describing the behaviour of the AI. Each classification has default parameters that are set if these are empty.
    """


    class MetaOapg:
        required = {
            "classification",
        }
        
        class properties:
            
            
            class classification(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "face": "FACE",
                        "hand": "HAND",
                        "foot": "FOOT",
                        "footwear": "FOOTWEAR",
                        "chest": "CHEST",
                        "breast": "BREAST",
                        "vulva": "VULVA",
                        "penis": "PENIS",
                        "vagina": "VAGINA",
                        "buttocks": "BUTTOCKS",
                        "anus": "ANUS",
                        "oral": "ORAL",
                        "penetration": "PENETRATION",
                        "toy": "TOY",
                        "child": "CHILD",
                        "adult": "ADULT",
                        "senior": "SENIOR",
                        "pose": "POSE",
                        "female": "FEMALE",
                        "male": "MALE",
                        "hair": "HAIR",
                        "hairless": "HAIRLESS",
                        "beard": "BEARD",
                        "moustache": "MOUSTACHE",
                        "headpiece": "HEADPIECE",
                        "glasses": "GLASSES",
                        "sunglasses": "SUNGLASSES",
                        "mask": "MASK",
                        "slimSizedFace": "SLIM_SIZED_FACE",
                        "realSizedFace": "REAL_SIZED_FACE",
                        "plusSizedFace": "PLUS_SIZED_FACE",
                        "slimSized": "SLIM_SIZED",
                        "realSized": "REAL_SIZED",
                        "plusSized": "PLUS_SIZED",
                        "noNipple": "NO_NIPPLE",
                        "hasNipple": "HAS_NIPPLE",
                        "beer": "BEER",
                        "beerBottle": "BEER_BOTTLE",
                        "beerCan": "BEER_CAN",
                        "wine": "WINE",
                        "wineBottle": "WINE_BOTTLE",
                        "cocktail": "COCKTAIL",
                        "alcohol": "ALCOHOL",
                        "cannabis": "CANNABIS",
                        "cigarette": "CIGARETTE",
                        "cocaine": "COCAINE",
                        "heroine": "HEROINE",
                        "coffee": "COFFEE",
                        "camouflage": "CAMOUFLAGE",
                        "club": "CLUB",
                        "knife": "KNIFE",
                        "sword": "SWORD",
                        "pistol": "PISTOL",
                        "rifle": "RIFLE",
                        "cannon": "CANNON",
                        "fire": "FIRE",
                        "nudityCheck": "NUDITY_CHECK",
                        "ageVerification": "AGE_VERIFICATION",
                        "ageEstimation": "AGE_ESTIMATION",
                        "illegalSymbols": "ILLEGAL_SYMBOLS",
                        "textRecognition": "TEXT_RECOGNITION",
                        "attributesCheck": "ATTRIBUTES_CHECK",
                        "bodyAttributes": "BODY_ATTRIBUTES",
                        "nippleCheck": "NIPPLE_CHECK",
                        "unwantedSubstances": "UNWANTED_SUBSTANCES",
                        "violenceCheck": "VIOLENCE_CHECK",
                    }
                
                @schemas.classproperty
                def FACE(cls):
                    return cls("face")
                
                @schemas.classproperty
                def HAND(cls):
                    return cls("hand")
                
                @schemas.classproperty
                def FOOT(cls):
                    return cls("foot")
                
                @schemas.classproperty
                def FOOTWEAR(cls):
                    return cls("footwear")
                
                @schemas.classproperty
                def CHEST(cls):
                    return cls("chest")
                
                @schemas.classproperty
                def BREAST(cls):
                    return cls("breast")
                
                @schemas.classproperty
                def VULVA(cls):
                    return cls("vulva")
                
                @schemas.classproperty
                def PENIS(cls):
                    return cls("penis")
                
                @schemas.classproperty
                def VAGINA(cls):
                    return cls("vagina")
                
                @schemas.classproperty
                def BUTTOCKS(cls):
                    return cls("buttocks")
                
                @schemas.classproperty
                def ANUS(cls):
                    return cls("anus")
                
                @schemas.classproperty
                def ORAL(cls):
                    return cls("oral")
                
                @schemas.classproperty
                def PENETRATION(cls):
                    return cls("penetration")
                
                @schemas.classproperty
                def TOY(cls):
                    return cls("toy")
                
                @schemas.classproperty
                def CHILD(cls):
                    return cls("child")
                
                @schemas.classproperty
                def ADULT(cls):
                    return cls("adult")
                
                @schemas.classproperty
                def SENIOR(cls):
                    return cls("senior")
                
                @schemas.classproperty
                def POSE(cls):
                    return cls("pose")
                
                @schemas.classproperty
                def FEMALE(cls):
                    return cls("female")
                
                @schemas.classproperty
                def MALE(cls):
                    return cls("male")
                
                @schemas.classproperty
                def HAIR(cls):
                    return cls("hair")
                
                @schemas.classproperty
                def HAIRLESS(cls):
                    return cls("hairless")
                
                @schemas.classproperty
                def BEARD(cls):
                    return cls("beard")
                
                @schemas.classproperty
                def MOUSTACHE(cls):
                    return cls("moustache")
                
                @schemas.classproperty
                def HEADPIECE(cls):
                    return cls("headpiece")
                
                @schemas.classproperty
                def GLASSES(cls):
                    return cls("glasses")
                
                @schemas.classproperty
                def SUNGLASSES(cls):
                    return cls("sunglasses")
                
                @schemas.classproperty
                def MASK(cls):
                    return cls("mask")
                
                @schemas.classproperty
                def SLIM_SIZED_FACE(cls):
                    return cls("slimSizedFace")
                
                @schemas.classproperty
                def REAL_SIZED_FACE(cls):
                    return cls("realSizedFace")
                
                @schemas.classproperty
                def PLUS_SIZED_FACE(cls):
                    return cls("plusSizedFace")
                
                @schemas.classproperty
                def SLIM_SIZED(cls):
                    return cls("slimSized")
                
                @schemas.classproperty
                def REAL_SIZED(cls):
                    return cls("realSized")
                
                @schemas.classproperty
                def PLUS_SIZED(cls):
                    return cls("plusSized")
                
                @schemas.classproperty
                def NO_NIPPLE(cls):
                    return cls("noNipple")
                
                @schemas.classproperty
                def HAS_NIPPLE(cls):
                    return cls("hasNipple")
                
                @schemas.classproperty
                def BEER(cls):
                    return cls("beer")
                
                @schemas.classproperty
                def BEER_BOTTLE(cls):
                    return cls("beerBottle")
                
                @schemas.classproperty
                def BEER_CAN(cls):
                    return cls("beerCan")
                
                @schemas.classproperty
                def WINE(cls):
                    return cls("wine")
                
                @schemas.classproperty
                def WINE_BOTTLE(cls):
                    return cls("wineBottle")
                
                @schemas.classproperty
                def COCKTAIL(cls):
                    return cls("cocktail")
                
                @schemas.classproperty
                def ALCOHOL(cls):
                    return cls("alcohol")
                
                @schemas.classproperty
                def CANNABIS(cls):
                    return cls("cannabis")
                
                @schemas.classproperty
                def CIGARETTE(cls):
                    return cls("cigarette")
                
                @schemas.classproperty
                def COCAINE(cls):
                    return cls("cocaine")
                
                @schemas.classproperty
                def HEROINE(cls):
                    return cls("heroine")
                
                @schemas.classproperty
                def COFFEE(cls):
                    return cls("coffee")
                
                @schemas.classproperty
                def CAMOUFLAGE(cls):
                    return cls("camouflage")
                
                @schemas.classproperty
                def CLUB(cls):
                    return cls("club")
                
                @schemas.classproperty
                def KNIFE(cls):
                    return cls("knife")
                
                @schemas.classproperty
                def SWORD(cls):
                    return cls("sword")
                
                @schemas.classproperty
                def PISTOL(cls):
                    return cls("pistol")
                
                @schemas.classproperty
                def RIFLE(cls):
                    return cls("rifle")
                
                @schemas.classproperty
                def CANNON(cls):
                    return cls("cannon")
                
                @schemas.classproperty
                def FIRE(cls):
                    return cls("fire")
                
                @schemas.classproperty
                def NUDITY_CHECK(cls):
                    return cls("nudityCheck")
                
                @schemas.classproperty
                def AGE_VERIFICATION(cls):
                    return cls("ageVerification")
                
                @schemas.classproperty
                def AGE_ESTIMATION(cls):
                    return cls("ageEstimation")
                
                @schemas.classproperty
                def ILLEGAL_SYMBOLS(cls):
                    return cls("illegalSymbols")
                
                @schemas.classproperty
                def TEXT_RECOGNITION(cls):
                    return cls("textRecognition")
                
                @schemas.classproperty
                def ATTRIBUTES_CHECK(cls):
                    return cls("attributesCheck")
                
                @schemas.classproperty
                def BODY_ATTRIBUTES(cls):
                    return cls("bodyAttributes")
                
                @schemas.classproperty
                def NIPPLE_CHECK(cls):
                    return cls("nippleCheck")
                
                @schemas.classproperty
                def UNWANTED_SUBSTANCES(cls):
                    return cls("unwantedSubstances")
                
                @schemas.classproperty
                def VIOLENCE_CHECK(cls):
                    return cls("violenceCheck")
            
            
            class min(
                schemas.Int32Schema
            ):
            
            
                class MetaOapg:
                    format = 'int32'
                    inclusive_minimum = -1
            
            
            class max(
                schemas.Int32Schema
            ):
            
            
                class MetaOapg:
                    format = 'int32'
                    inclusive_minimum = -1
            
            
            class severity(
                schemas.Int32Schema
            ):
            
            
                class MetaOapg:
                    format = 'int32'
                    inclusive_maximum = 999
                    inclusive_minimum = 0
            
            
            class drawMode(
                schemas.Int32Schema
            ):
            
            
                class MetaOapg:
                    format = 'int32'
                    inclusive_maximum = 7
                    inclusive_minimum = 0
            
            
            class grey(
                schemas.Int32Schema
            ):
            
            
                class MetaOapg:
                    format = 'int32'
                    inclusive_maximum = 255
                    inclusive_minimum = 0
            
            
            class scale(
                schemas.Float32Schema
            ):
            
            
                class MetaOapg:
                    format = 'float'
                    inclusive_maximum = 4.0
                    inclusive_minimum = 0.5
            ignore = schemas.BoolSchema
            __annotations__ = {
                "classification": classification,
                "min": min,
                "max": max,
                "severity": severity,
                "drawMode": drawMode,
                "grey": grey,
                "scale": scale,
                "ignore": ignore,
            }
    
    classification: MetaOapg.properties.classification
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["classification"]) -> MetaOapg.properties.classification: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["min"]) -> MetaOapg.properties.min: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["max"]) -> MetaOapg.properties.max: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["severity"]) -> MetaOapg.properties.severity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["drawMode"]) -> MetaOapg.properties.drawMode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["grey"]) -> MetaOapg.properties.grey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scale"]) -> MetaOapg.properties.scale: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ignore"]) -> MetaOapg.properties.ignore: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["classification", "min", "max", "severity", "drawMode", "grey", "scale", "ignore", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["classification"]) -> MetaOapg.properties.classification: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["min"]) -> typing.Union[MetaOapg.properties.min, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["max"]) -> typing.Union[MetaOapg.properties.max, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["severity"]) -> typing.Union[MetaOapg.properties.severity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["drawMode"]) -> typing.Union[MetaOapg.properties.drawMode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["grey"]) -> typing.Union[MetaOapg.properties.grey, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scale"]) -> typing.Union[MetaOapg.properties.scale, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ignore"]) -> typing.Union[MetaOapg.properties.ignore, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["classification", "min", "max", "severity", "drawMode", "grey", "scale", "ignore", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        classification: typing.Union[MetaOapg.properties.classification, str, ],
        min: typing.Union[MetaOapg.properties.min, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        max: typing.Union[MetaOapg.properties.max, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        severity: typing.Union[MetaOapg.properties.severity, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        drawMode: typing.Union[MetaOapg.properties.drawMode, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        grey: typing.Union[MetaOapg.properties.grey, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        scale: typing.Union[MetaOapg.properties.scale, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        ignore: typing.Union[MetaOapg.properties.ignore, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Param':
        return super().__new__(
            cls,
            *_args,
            classification=classification,
            min=min,
            max=max,
            severity=severity,
            drawMode=drawMode,
            grey=grey,
            scale=scale,
            ignore=ignore,
            _configuration=_configuration,
            **kwargs,
        )
