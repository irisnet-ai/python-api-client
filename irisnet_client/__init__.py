# coding: utf-8

# flake8: noqa

"""
    Irisnet API

    Artificial Intelligence (AI) for image- and video-processing in realtime. This is an interactive documentation meant to give a place were you can quickly look up the endpoints and their schemas, while also giving you the option to try things out yourself.  Listed below you'll see the available endpoints of the API that can be expanded by clicking on it. Each expanded endpoint lists the request parameter (if available) and the request body (if available). The request body can list some example bodies and the schema, explaining each model in detail. Additionally you'll find a 'Try it out' button where you can type in your custom parameters and custom body and execute that against the API. The responses section in the expanded endpoint lists the possible responses with their corresponding status codes. If you've executed an API call it will also show you the response from the server.  Underneath the endpoints you'll find the model schemas. These are the models used for the requests and responses.By clicking on the right arrow you can expand the model and it will show you a description of the model and the model parameters. For nested models you can keep clicking the right arrow to reveal further details on it.    # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "2.2.2"

# import apis into sdk package
from irisnet_client.api.endpoints_for_ai_checks_api import EndpointsForAIChecksApi
from irisnet_client.api.endpoints_to_setup_the_ai_api import EndpointsToSetupTheAIApi
from irisnet_client.api.miscellaneous_operations_api import MiscellaneousOperationsApi

# import ApiClient
from irisnet_client.api_client import ApiClient
from irisnet_client.configuration import Configuration
from irisnet_client.exceptions import OpenApiException
from irisnet_client.exceptions import ApiTypeError
from irisnet_client.exceptions import ApiValueError
from irisnet_client.exceptions import ApiKeyError
from irisnet_client.exceptions import ApiException
# import models into sdk package
from irisnet_client.models.in_default import INDefault
from irisnet_client.models.in_define_ai import INDefineAI
from irisnet_client.models.in_error import INError
from irisnet_client.models.in_image import INImage
from irisnet_client.models.in_object import INObject
from irisnet_client.models.in_param import INParam
from irisnet_client.models.in_params import INParams
from irisnet_client.models.in_rule import INRule
from irisnet_client.models.inline_object import InlineObject
from irisnet_client.models.iris_net import IrisNet
from irisnet_client.models.license_info import LicenseInfo

