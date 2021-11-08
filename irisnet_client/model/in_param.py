"""
    Irisnet API

    Artificial Intelligence (AI) for image- and video-processing in realtime. This is an interactive documentation meant to give a place were you can quickly look up the endpoints and their schemas, while also giving you the option to try things out yourself.  Listed below you'll see the available endpoints of the API that can be expanded by clicking on it. Each expanded endpoint lists the request parameter (if available) and the request body (if available). The request body can list some example bodies and the schema, explaining each model in detail. Additionally you'll find a 'Try it out' button where you can type in your custom parameters and custom body and execute that against the API. The responses section in the expanded endpoint lists the possible responses with their corresponding status codes. If you've executed an API call it will also show you the response from the server.  Underneath the endpoints you'll find the model schemas. These are the models used for the requests and responses. By clicking on the right arrow you can expand the model and it will show you a description of the model and the model parameters. For nested models you can keep clicking the right arrow to reveal further details on it.    # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from irisnet_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from irisnet_client.exceptions import ApiAttributeError



class INParam(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('in_class',): {
            'FACE': "face",
            'HAND': "hand",
            'FOOT': "foot",
            'FOOTWEAR': "footwear",
            'BREAST': "breast",
            'VULVA': "vulva",
            'PENIS': "penis",
            'VAGINA': "vagina",
            'BUTTOCKS': "buttocks",
            'ANUS': "anus",
            'ORAL': "oral",
            'PENETRATION': "penetration",
            'TOY': "toy",
            'CHILD': "child",
            'ADULT': "adult",
            'SENIOR': "senior",
            'POSE': "pose",
            'FEMALE': "female",
            'MALE': "male",
            'HAIR': "hair",
            'HAIRLESS': "hairless",
            'BEARD': "beard",
            'MOUSTACHE': "moustache",
            'HEADPIECE': "headpiece",
            'GLASSES': "glasses",
            'SUNGLASSES': "sunglasses",
            'MASK': "mask",
            'NUDITYCHECK': "nudityCheck",
            'AGEVERIFICATION': "ageVerification",
            'AGEESTIMATION': "ageEstimation",
            'ILLEGALSYMBOLS': "illegalSymbols",
            'TEXTRECOGNITION': "textRecognition",
            'ATTRIBUTESCHECK': "attributesCheck",
        },
    }

    validations = {
        ('severity',): {
            'inclusive_maximum': 1000,
            'inclusive_minimum': 0,
        },
        ('draw_mode',): {
            'inclusive_maximum': 7,
            'inclusive_minimum': 0,
        },
        ('grey',): {
            'inclusive_maximum': 255,
            'inclusive_minimum': 0,
        },
        ('scale',): {
            'inclusive_maximum': 2.0,
            'inclusive_minimum': 0.5,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'in_class': (str,),  # noqa: E501
            'min': (int,),  # noqa: E501
            'max': (int,),  # noqa: E501
            'severity': (int,),  # noqa: E501
            'draw_mode': (int,),  # noqa: E501
            'grey': (int,),  # noqa: E501
            'scale': (float,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'in_class': 'inClass',  # noqa: E501
        'min': 'min',  # noqa: E501
        'max': 'max',  # noqa: E501
        'severity': 'severity',  # noqa: E501
        'draw_mode': 'drawMode',  # noqa: E501
        'grey': 'grey',  # noqa: E501
        'scale': 'scale',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """INParam - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            in_class (str): The classification of the object, that the element refers to. Default parameter values are defined per classification object. The following list contains the default values for 'min', 'max' and 'drawMode' in order.  * _face_ _(1, 3, 0)_ - Classification for human faces. * _child (*)_ _(0, 0, 6)_ - Recognizes children's faces. * _adult (*)_ _(0, -1, 0)_ - Recognizes faces of adults that are not considered seniors. * _senior (*)_ _(0, -1, 0)_ - Recognizes faces of seniors. * _pose_ _(0, 0, 0)_ - The age can not be estimated, due to a pose that hides facial features. * _female (*)_ _(0, -1, 0)_ - Recognizes female faces.  * _male (*)_ _(0, -1, 0)_ - Recognizes male faces.  * _hand_ _(0, -1, 0)_ - Classification for recognizing hands. * _foot_ _(0, -1, 0)_ - Classification for recognizing feet. * _footwear_ _(0, -1, 0)_ - Classification for recognizing footwear. * _hair_ _(0, -1, 0)_ - Classification for recognizing hair.  * _hairless_ _(0, -1, 0)_ - Classification for recognizing no hair.  * _beard_ _(0, -1, 0)_ - Classification for recognizing beards.  * _moustache_ _(0, -1, 0)_ - Classification for recognizing moustaches.  * _headpiece_ _(0, -1, 0)_ - Classification for recognizing headpieces.  * _glasses_ _(0, -1, 0)_ - Classification for recognizing glasses.  * _sunglasses_ _(0, -1, 0)_ - Classification for recognizing sunglasses.  * _mask_ _(0, -1, 0)_ - Classification for recognizing medical masks.  * _breast_ _(0, 0, 2)_ - Object that recognizes female breasts. * _vulva_ _(0, 0, 2)_ - Object that recognizes vulvae. * _penis_ _(0, 0, 2)_ - Object that recognizes penises. * _vagina_ _(0, 0, 2)_ - Object that recognizes vaginae. * _buttocks_ _(0, 0, 2)_ - Object that recognizes buttocks. * _anus_ _(0, 0, 2)_ - Object that recognizes ani. * _toy_ _(0, -1, 0)_ - Object that recognizes sex toys. * _oral_ _(0, 0, 2)_ - Object that recognizes oral sex. * _penetration_ _(0, 0, 2)_ - Object that recognizes a sexual penetration penetration. * _illegalSymbols_ _(0, 0, 1)_ - Classification for symbols that are not permitted in Germany.  * _textRecognition_ _(0, 6, 6)_ - Classification for recognizing text occurrences.  _Classification objects that are marked with (*) are sub-classifications of face. Both face and the marked classification are affected by the given parameter values._  _Please be aware that the default values can be subject to change. This is due to the difficulty of recognizing certain objects e.g. objects that are classified as toy._. [optional]  # noqa: E501
            min (int): The minimum amount of objects allowed on the source media. Setting the value to -1 will cause the AI to ignore this rule.. [optional]  # noqa: E501
            max (int): The maximum amount of objects allowed on the source media. Setting the value to -1 will cause the AI to ignore this rule.. [optional]  # noqa: E501
            severity (int): Set a value to define the severity of a broken rule of the given classification object.. [optional] if omitted the server will use the default value of 100  # noqa: E501
            draw_mode (int): The draw mode that will be used for the creating the media.  * _0_ - will draw nothing, * _1_ - will draw a frame with class name surrounding the object, * _2_ - will draw a filled rectangle that will mask the object, * _3_ - is a combination between _1_ and _2_ (frame/name + mask), * _6_ - will blur the object and * _7_ - is a combination between _1_ and _6_ (frame/name + blur).. [optional]  # noqa: E501
            grey (int): A grey scale color to use for masking. '0' will represent black, while the maximum '255' will be white.. [optional] if omitted the server will use the default value of 127  # noqa: E501
            scale (float): Scale of the draw rectangle around the classification object. Specify a value to increase or decrease the size of the border.. [optional] if omitted the server will use the default value of 1.0  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """INParam - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            in_class (str): The classification of the object, that the element refers to. Default parameter values are defined per classification object. The following list contains the default values for 'min', 'max' and 'drawMode' in order.  * _face_ _(1, 3, 0)_ - Classification for human faces. * _child (*)_ _(0, 0, 6)_ - Recognizes children's faces. * _adult (*)_ _(0, -1, 0)_ - Recognizes faces of adults that are not considered seniors. * _senior (*)_ _(0, -1, 0)_ - Recognizes faces of seniors. * _pose_ _(0, 0, 0)_ - The age can not be estimated, due to a pose that hides facial features. * _female (*)_ _(0, -1, 0)_ - Recognizes female faces.  * _male (*)_ _(0, -1, 0)_ - Recognizes male faces.  * _hand_ _(0, -1, 0)_ - Classification for recognizing hands. * _foot_ _(0, -1, 0)_ - Classification for recognizing feet. * _footwear_ _(0, -1, 0)_ - Classification for recognizing footwear. * _hair_ _(0, -1, 0)_ - Classification for recognizing hair.  * _hairless_ _(0, -1, 0)_ - Classification for recognizing no hair.  * _beard_ _(0, -1, 0)_ - Classification for recognizing beards.  * _moustache_ _(0, -1, 0)_ - Classification for recognizing moustaches.  * _headpiece_ _(0, -1, 0)_ - Classification for recognizing headpieces.  * _glasses_ _(0, -1, 0)_ - Classification for recognizing glasses.  * _sunglasses_ _(0, -1, 0)_ - Classification for recognizing sunglasses.  * _mask_ _(0, -1, 0)_ - Classification for recognizing medical masks.  * _breast_ _(0, 0, 2)_ - Object that recognizes female breasts. * _vulva_ _(0, 0, 2)_ - Object that recognizes vulvae. * _penis_ _(0, 0, 2)_ - Object that recognizes penises. * _vagina_ _(0, 0, 2)_ - Object that recognizes vaginae. * _buttocks_ _(0, 0, 2)_ - Object that recognizes buttocks. * _anus_ _(0, 0, 2)_ - Object that recognizes ani. * _toy_ _(0, -1, 0)_ - Object that recognizes sex toys. * _oral_ _(0, 0, 2)_ - Object that recognizes oral sex. * _penetration_ _(0, 0, 2)_ - Object that recognizes a sexual penetration penetration. * _illegalSymbols_ _(0, 0, 1)_ - Classification for symbols that are not permitted in Germany.  * _textRecognition_ _(0, 6, 6)_ - Classification for recognizing text occurrences.  _Classification objects that are marked with (*) are sub-classifications of face. Both face and the marked classification are affected by the given parameter values._  _Please be aware that the default values can be subject to change. This is due to the difficulty of recognizing certain objects e.g. objects that are classified as toy._. [optional]  # noqa: E501
            min (int): The minimum amount of objects allowed on the source media. Setting the value to -1 will cause the AI to ignore this rule.. [optional]  # noqa: E501
            max (int): The maximum amount of objects allowed on the source media. Setting the value to -1 will cause the AI to ignore this rule.. [optional]  # noqa: E501
            severity (int): Set a value to define the severity of a broken rule of the given classification object.. [optional] if omitted the server will use the default value of 100  # noqa: E501
            draw_mode (int): The draw mode that will be used for the creating the media.  * _0_ - will draw nothing, * _1_ - will draw a frame with class name surrounding the object, * _2_ - will draw a filled rectangle that will mask the object, * _3_ - is a combination between _1_ and _2_ (frame/name + mask), * _6_ - will blur the object and * _7_ - is a combination between _1_ and _6_ (frame/name + blur).. [optional]  # noqa: E501
            grey (int): A grey scale color to use for masking. '0' will represent black, while the maximum '255' will be white.. [optional] if omitted the server will use the default value of 127  # noqa: E501
            scale (float): Scale of the draw rectangle around the classification object. Specify a value to increase or decrease the size of the border.. [optional] if omitted the server will use the default value of 1.0  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")