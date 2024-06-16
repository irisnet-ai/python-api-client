# coding: utf-8

# flake8: noqa
"""
    Irisnet API

    Artificial Intelligence (AI) for image- and video-processing in real-time. This is an interactive documentation where you can quickly look up the endpoints and their schemas, while having the opportunity to try things out for yourself.  In the list below, you can see the available endpoints of the API, which can be expanded by clicking on them. Each expanded endpoint lists the request parameters (if available) and the request body (if available). The request body can list some example bodies and the schema, explaining each model in detail.  Additionally you'll find a 'Try it out' button that allows you to enter your custom parameters and custom body and execute that against the API. <b>Be sure to enter your license key to authorize the requests before using this documentation interactively.</b>  The responses section in the expanded endpoint lists the possible responses with their corresponding status codes. If you've executed an API call it will also show you the response from the server.  Underneath the endpoints you'll find the model schemas. These are the models used for the requests and responses. If you click on the right arrow, you can expand the model and get a description of the model and the model parameters. For nested models, you can keep clicking the right arrow for further details.  Clicking the link below the title at the top of this page opens the [OpenAPI specification](https://swagger.io/specification/) (OAS3) in JSON format. The OAS3 Spec allows the generation of clients in many programming languages. There are several free client generators available that can be used to get started easily.

    The version of the OpenAPI document: v2
    Contact: info@irisnet.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from irisnet_client.models.age_estimation_attribute import AgeEstimationAttribute
from irisnet_client.models.age_estimation_detection import AgeEstimationDetection
from irisnet_client.models.age_estimation_sub_checks import AgeEstimationSubChecks
from irisnet_client.models.api_notice import ApiNotice
from irisnet_client.models.base_attribute import BaseAttribute
from irisnet_client.models.base_detection import BaseDetection
from irisnet_client.models.breast_detection import BreastDetection
from irisnet_client.models.broken_rule import BrokenRule
from irisnet_client.models.callback import Callback
from irisnet_client.models.check_result import CheckResult
from irisnet_client.models.config import Config
from irisnet_client.models.data import Data
from irisnet_client.models.document_check_request_data import DocumentCheckRequestData
from irisnet_client.models.encoded import Encoded
from irisnet_client.models.event import Event
from irisnet_client.models.face_detection import FaceDetection
from irisnet_client.models.hair_attribute import HairAttribute
from irisnet_client.models.hair_detection import HairDetection
from irisnet_client.models.id_document_attribute import IdDocumentAttribute
from irisnet_client.models.id_document_detection import IdDocumentDetection
from irisnet_client.models.id_document_sub_checks import IdDocumentSubChecks
from irisnet_client.models.license_info import LicenseInfo
from irisnet_client.models.param import Param
from irisnet_client.models.param_set import ParamSet
from irisnet_client.models.pricing import Pricing
from irisnet_client.models.summary import Summary
