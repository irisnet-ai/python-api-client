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


class INDefineAI(object):
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
        'in_image': 'list[INImage]'
    }

    attribute_map = {
        'in_image': 'inImage'
    }

    def __init__(self, in_image=None, local_vars_configuration=None):  # noqa: E501
        """INDefineAI - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._in_image = None
        self.discriminator = None

        if in_image is not None:
            self.in_image = in_image

    @property
    def in_image(self):
        """Gets the in_image of this INDefineAI.  # noqa: E501

        Configures your detection. As there are literally hundreds of parameters, INDefine uses prototypes to get usefull behaviour. This includes a default setting for parameters and rules that should be applied to images. You can combine multiple detections by using more than 1 prototype  # noqa: E501

        :return: The in_image of this INDefineAI.  # noqa: E501
        :rtype: list[INImage]
        """
        return self._in_image

    @in_image.setter
    def in_image(self, in_image):
        """Sets the in_image of this INDefineAI.

        Configures your detection. As there are literally hundreds of parameters, INDefine uses prototypes to get usefull behaviour. This includes a default setting for parameters and rules that should be applied to images. You can combine multiple detections by using more than 1 prototype  # noqa: E501

        :param in_image: The in_image of this INDefineAI.  # noqa: E501
        :type: list[INImage]
        """

        self._in_image = in_image

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
        if not isinstance(other, INDefineAI):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, INDefineAI):
            return True

        return self.to_dict() != other.to_dict()
