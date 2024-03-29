# coding: utf-8

"""
    Irisnet API

    Artificial Intelligence (AI) for image- and video-processing in realtime. This is an interactive documentation meant to give a place were you can quickly look up the endpoints and their schemas, while also giving you the option to try things out yourself.  Listed below you'll see the available endpoints of the API that can be expanded by clicking on it. Each expanded endpoint lists the request parameter (if available) and the request body (if available). The request body can list some example bodies and the schema, explaining each model in detail. Additionally you'll find a 'Try it out' button where you can type in your custom parameters and custom body and execute that against the API. The responses section in the expanded endpoint lists the possible responses with their corresponding status codes. If you've executed an API call it will also show you the response from the server.  Underneath the endpoints you'll find the model schemas. These are the models used for the requests and responses. By clicking on the right arrow you can expand the model and it will show you a description of the model and the model parameters. For nested models you can keep clicking the right arrow to reveal further details on it.    # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from irisnet_client.configuration import Configuration


class INParam(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'in_class': 'str',
        'min': 'int',
        'max': 'int',
        'severity': 'int',
        'draw_mode': 'int',
        'grey': 'int',
        'scale': 'float'
    }

    attribute_map = {
        'in_class': 'inClass',
        'min': 'min',
        'max': 'max',
        'severity': 'severity',
        'draw_mode': 'drawMode',
        'grey': 'grey',
        'scale': 'scale'
    }

    def __init__(self, in_class=None, min=None, max=None, severity=100, draw_mode=None, grey=127, scale=1.0, local_vars_configuration=None):  # noqa: E501
        """INParam - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._in_class = None
        self._min = None
        self._max = None
        self._severity = None
        self._draw_mode = None
        self._grey = None
        self._scale = None
        self.discriminator = None

        if in_class is not None:
            self.in_class = in_class
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if severity is not None:
            self.severity = severity
        if draw_mode is not None:
            self.draw_mode = draw_mode
        if grey is not None:
            self.grey = grey
        if scale is not None:
            self.scale = scale

    @property
    def in_class(self):
        """Gets the in_class of this INParam.  # noqa: E501

        The classification of the object, that the element refers to. Default parameter values are defined per classification object. The following list contains the default values for 'min', 'max' and 'drawMode' in order.  * _face_ _(1, 3, 0)_ - Classification for human faces. * _child (*)_ _(0, 0, 6)_ - Recognizes children's faces. * _adult (*)_ _(0, -1, 0)_ - Recognizes faces of adults that are not considered seniors. * _senior (*)_ _(0, -1, 0)_ - Recognizes faces of seniors. * _pose_ _(0, 0, 0)_ - The age can not be estimated, due to a pose that hides facial features. * _female (*)_ _(0, -1, 0)_ - Recognizes female faces.  * _male (*)_ _(0, -1, 0)_ - Recognizes male faces.  * _hand_ _(0, -1, 0)_ - Classification for recognizing hands. * _foot_ _(0, -1, 0)_ - Classification for recognizing feet. * _footwear_ _(0, -1, 0)_ - Classification for recognizing footwear. * _hair_ _(0, -1, 0)_ - Classification for recognizing hair.  * _hairless_ _(0, -1, 0)_ - Classification for recognizing no hair.  * _beard_ _(0, -1, 0)_ - Classification for recognizing beards.  * _moustache_ _(0, -1, 0)_ - Classification for recognizing moustaches.  * _headpiece_ _(0, -1, 0)_ - Classification for recognizing headpieces.  * _glasses_ _(0, -1, 0)_ - Classification for recognizing glasses.  * _sunglasses_ _(0, -1, 0)_ - Classification for recognizing sunglasses.  * _mask_ _(0, -1, 0)_ - Classification for recognizing medical masks.  * _breast_ _(0, 0, 2)_ - Object that recognizes female breasts. * _vulva_ _(0, 0, 2)_ - Object that recognizes vulvae. * _penis_ _(0, 0, 2)_ - Object that recognizes penises. * _vagina_ _(0, 0, 2)_ - Object that recognizes vaginae. * _buttocks_ _(0, 0, 2)_ - Object that recognizes buttocks. * _anus_ _(0, 0, 2)_ - Object that recognizes ani. * _toy_ _(0, -1, 0)_ - Object that recognizes sex toys. * _oral_ _(0, 0, 2)_ - Object that recognizes oral sex. * _penetration_ _(0, 0, 2)_ - Object that recognizes a sexual penetration penetration. * _illegalSymbols_ _(0, 0, 1)_ - Classification for symbols that are not permitted in Germany.  * _textRecognition_ _(0, 6, 6)_ - Classification for recognizing text occurrences.  _Classification objects that are marked with (*) are sub-classifications of face. Both face and the marked classification are affected by the given parameter values._  _Please be aware that the default values can be subject to change. This is due to the difficulty of recognizing certain objects e.g. objects that are classified as toy._  # noqa: E501

        :return: The in_class of this INParam.  # noqa: E501
        :rtype: str
        """
        return self._in_class

    @in_class.setter
    def in_class(self, in_class):
        """Sets the in_class of this INParam.

        The classification of the object, that the element refers to. Default parameter values are defined per classification object. The following list contains the default values for 'min', 'max' and 'drawMode' in order.  * _face_ _(1, 3, 0)_ - Classification for human faces. * _child (*)_ _(0, 0, 6)_ - Recognizes children's faces. * _adult (*)_ _(0, -1, 0)_ - Recognizes faces of adults that are not considered seniors. * _senior (*)_ _(0, -1, 0)_ - Recognizes faces of seniors. * _pose_ _(0, 0, 0)_ - The age can not be estimated, due to a pose that hides facial features. * _female (*)_ _(0, -1, 0)_ - Recognizes female faces.  * _male (*)_ _(0, -1, 0)_ - Recognizes male faces.  * _hand_ _(0, -1, 0)_ - Classification for recognizing hands. * _foot_ _(0, -1, 0)_ - Classification for recognizing feet. * _footwear_ _(0, -1, 0)_ - Classification for recognizing footwear. * _hair_ _(0, -1, 0)_ - Classification for recognizing hair.  * _hairless_ _(0, -1, 0)_ - Classification for recognizing no hair.  * _beard_ _(0, -1, 0)_ - Classification for recognizing beards.  * _moustache_ _(0, -1, 0)_ - Classification for recognizing moustaches.  * _headpiece_ _(0, -1, 0)_ - Classification for recognizing headpieces.  * _glasses_ _(0, -1, 0)_ - Classification for recognizing glasses.  * _sunglasses_ _(0, -1, 0)_ - Classification for recognizing sunglasses.  * _mask_ _(0, -1, 0)_ - Classification for recognizing medical masks.  * _breast_ _(0, 0, 2)_ - Object that recognizes female breasts. * _vulva_ _(0, 0, 2)_ - Object that recognizes vulvae. * _penis_ _(0, 0, 2)_ - Object that recognizes penises. * _vagina_ _(0, 0, 2)_ - Object that recognizes vaginae. * _buttocks_ _(0, 0, 2)_ - Object that recognizes buttocks. * _anus_ _(0, 0, 2)_ - Object that recognizes ani. * _toy_ _(0, -1, 0)_ - Object that recognizes sex toys. * _oral_ _(0, 0, 2)_ - Object that recognizes oral sex. * _penetration_ _(0, 0, 2)_ - Object that recognizes a sexual penetration penetration. * _illegalSymbols_ _(0, 0, 1)_ - Classification for symbols that are not permitted in Germany.  * _textRecognition_ _(0, 6, 6)_ - Classification for recognizing text occurrences.  _Classification objects that are marked with (*) are sub-classifications of face. Both face and the marked classification are affected by the given parameter values._  _Please be aware that the default values can be subject to change. This is due to the difficulty of recognizing certain objects e.g. objects that are classified as toy._  # noqa: E501

        :param in_class: The in_class of this INParam.  # noqa: E501
        :type: str
        """
        allowed_values = ["face", "hand", "foot", "footwear", "breast", "vulva", "penis", "vagina", "buttocks", "anus", "oral", "penetration", "toy", "child", "adult", "senior", "pose", "female", "male", "hair", "hairless", "beard", "moustache", "headpiece", "glasses", "sunglasses", "mask", "nudityCheck", "ageVerification", "ageEstimation", "illegalSymbols", "textRecognition", "attributesCheck"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and in_class not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `in_class` ({0}), must be one of {1}"  # noqa: E501
                .format(in_class, allowed_values)
            )

        self._in_class = in_class

    @property
    def min(self):
        """Gets the min of this INParam.  # noqa: E501

        The minimum amount of objects allowed on the source media. Setting the value to -1 will cause the AI to ignore this rule.  # noqa: E501

        :return: The min of this INParam.  # noqa: E501
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this INParam.

        The minimum amount of objects allowed on the source media. Setting the value to -1 will cause the AI to ignore this rule.  # noqa: E501

        :param min: The min of this INParam.  # noqa: E501
        :type: int
        """

        self._min = min

    @property
    def max(self):
        """Gets the max of this INParam.  # noqa: E501

        The maximum amount of objects allowed on the source media. Setting the value to -1 will cause the AI to ignore this rule.  # noqa: E501

        :return: The max of this INParam.  # noqa: E501
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this INParam.

        The maximum amount of objects allowed on the source media. Setting the value to -1 will cause the AI to ignore this rule.  # noqa: E501

        :param max: The max of this INParam.  # noqa: E501
        :type: int
        """

        self._max = max

    @property
    def severity(self):
        """Gets the severity of this INParam.  # noqa: E501

        Set a value to define the severity of a broken rule of the given classification object.  # noqa: E501

        :return: The severity of this INParam.  # noqa: E501
        :rtype: int
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this INParam.

        Set a value to define the severity of a broken rule of the given classification object.  # noqa: E501

        :param severity: The severity of this INParam.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                severity is not None and severity > 1000):  # noqa: E501
            raise ValueError("Invalid value for `severity`, must be a value less than or equal to `1000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                severity is not None and severity < 0):  # noqa: E501
            raise ValueError("Invalid value for `severity`, must be a value greater than or equal to `0`")  # noqa: E501

        self._severity = severity

    @property
    def draw_mode(self):
        """Gets the draw_mode of this INParam.  # noqa: E501

        The draw mode that will be used for the creating the media.  * _0_ - will draw nothing, * _1_ - will draw a frame with class name surrounding the object, * _2_ - will draw a filled rectangle that will mask the object, * _3_ - is a combination between _1_ and _2_ (frame/name + mask), * _6_ - will blur the object and * _7_ - is a combination between _1_ and _6_ (frame/name + blur).  # noqa: E501

        :return: The draw_mode of this INParam.  # noqa: E501
        :rtype: int
        """
        return self._draw_mode

    @draw_mode.setter
    def draw_mode(self, draw_mode):
        """Sets the draw_mode of this INParam.

        The draw mode that will be used for the creating the media.  * _0_ - will draw nothing, * _1_ - will draw a frame with class name surrounding the object, * _2_ - will draw a filled rectangle that will mask the object, * _3_ - is a combination between _1_ and _2_ (frame/name + mask), * _6_ - will blur the object and * _7_ - is a combination between _1_ and _6_ (frame/name + blur).  # noqa: E501

        :param draw_mode: The draw_mode of this INParam.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                draw_mode is not None and draw_mode > 7):  # noqa: E501
            raise ValueError("Invalid value for `draw_mode`, must be a value less than or equal to `7`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                draw_mode is not None and draw_mode < 0):  # noqa: E501
            raise ValueError("Invalid value for `draw_mode`, must be a value greater than or equal to `0`")  # noqa: E501

        self._draw_mode = draw_mode

    @property
    def grey(self):
        """Gets the grey of this INParam.  # noqa: E501

        A grey scale color to use for masking. '0' will represent black, while the maximum '255' will be white.  # noqa: E501

        :return: The grey of this INParam.  # noqa: E501
        :rtype: int
        """
        return self._grey

    @grey.setter
    def grey(self, grey):
        """Sets the grey of this INParam.

        A grey scale color to use for masking. '0' will represent black, while the maximum '255' will be white.  # noqa: E501

        :param grey: The grey of this INParam.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                grey is not None and grey > 255):  # noqa: E501
            raise ValueError("Invalid value for `grey`, must be a value less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                grey is not None and grey < 0):  # noqa: E501
            raise ValueError("Invalid value for `grey`, must be a value greater than or equal to `0`")  # noqa: E501

        self._grey = grey

    @property
    def scale(self):
        """Gets the scale of this INParam.  # noqa: E501

        Scale of the draw rectangle around the classification object. Specify a value to increase or decrease the size of the border.  # noqa: E501

        :return: The scale of this INParam.  # noqa: E501
        :rtype: float
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """Sets the scale of this INParam.

        Scale of the draw rectangle around the classification object. Specify a value to increase or decrease the size of the border.  # noqa: E501

        :param scale: The scale of this INParam.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                scale is not None and scale > 2.0):  # noqa: E501
            raise ValueError("Invalid value for `scale`, must be a value less than or equal to `2.0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                scale is not None and scale < 0.5):  # noqa: E501
            raise ValueError("Invalid value for `scale`, must be a value greater than or equal to `0.5`")  # noqa: E501

        self._scale = scale

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, INParam):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, INParam):
            return True

        return self.to_dict() != other.to_dict()
