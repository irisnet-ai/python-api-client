# coding: utf-8

"""
    Irisnet API

    Artificial Intelligence (AI) for image- and video-processing in real-time. This is an interactive documentation where you can quickly look up the endpoints and their schemas, while having the opportunity to try things out for yourself.  In the list below, you can see the available endpoints of the API, which can be expanded by clicking on them. Each expanded endpoint lists the request parameters (if available) and the request body (if available). The request body can list some example bodies and the schema, explaining each model in detail.  Additionally you'll find a 'Try it out' button that allows you to enter your custom parameters and custom body and execute that against the API. <b>Be sure to enter your license key to authorize the requests before using this documentation interactively.</b>  The responses section in the expanded endpoint lists the possible responses with their corresponding status codes. If you've executed an API call it will also show you the response from the server.  Underneath the endpoints you'll find the model schemas. These are the models used for the requests and responses. If you click on the right arrow, you can expand the model and get a description of the model and the model parameters. For nested models, you can keep clicking the right arrow for further details.  Clicking the link below the title at the top of this page opens the [OpenAPI specification](https://swagger.io/specification/) (OAS3) in JSON format. The OAS3 Spec allows the generation of clients in many programming languages. There are several free client generators available that can be used to get started easily.

    The version of the OpenAPI document: v2
    Contact: info@irisnet.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from pydantic import Field, StrictBool, StrictStr, conint

from typing import List, Optional

from irisnet_client.models.check_result import CheckResult
from irisnet_client.models.config import Config

from irisnet_client.api_client import ApiClient
from irisnet_client.api_response import ApiResponse
from irisnet_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class AICheckOperationsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def check_image(self, config_id : Annotated[StrictStr, Field(..., description="The configuration id from the Basic Configuration operations.")], url : Annotated[Optional[StrictStr], Field(description="<s>The url to the image that needs to be checked.</s> Deprecated: Use 'data' parameter instead. <b>This parameter will be removed in future releases.</b>")] = None, data : Annotated[Optional[StrictStr], Field(description="The http(s) url or base64 encoded data uri of the image that needs to be checked.")] = None, detail : Annotated[Optional[conint(strict=True, le=3, ge=0)], Field(description="Set the detail level of the response.  * _1_ - The response only contains the _Summary_ and possibly the _Encoded_ schemas for basic information's (better API performance). * _2_ - Additionally lists all broken rules (_BrokenRule_ schema) according to the configuration parameters that were requested. * _3_ - Also shows detections (e.g. _BaseDetection_ schema) that contains extended features to each found object.")] = None, image_encode : Annotated[Optional[StrictBool], Field(description="Specifies whether or not to draw an output image that will be delivered in the response body as base64 encoded string. The _Encoded_ schema will be available in the response.")] = None, **kwargs) -> CheckResult:  # noqa: E501
        """Check an image with the AI.  # noqa: E501

        The response (_CheckResult_ schema) is returned immediately after the request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.check_image(config_id, url, data, detail, image_encode, async_req=True)
        >>> result = thread.get()

        :param config_id: The configuration id from the Basic Configuration operations. (required)
        :type config_id: str
        :param url: <s>The url to the image that needs to be checked.</s> Deprecated: Use 'data' parameter instead. <b>This parameter will be removed in future releases.</b>
        :type url: str
        :param data: The http(s) url or base64 encoded data uri of the image that needs to be checked.
        :type data: str
        :param detail: Set the detail level of the response.  * _1_ - The response only contains the _Summary_ and possibly the _Encoded_ schemas for basic information's (better API performance). * _2_ - Additionally lists all broken rules (_BrokenRule_ schema) according to the configuration parameters that were requested. * _3_ - Also shows detections (e.g. _BaseDetection_ schema) that contains extended features to each found object.
        :type detail: int
        :param image_encode: Specifies whether or not to draw an output image that will be delivered in the response body as base64 encoded string. The _Encoded_ schema will be available in the response.
        :type image_encode: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CheckResult
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the check_image_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.check_image_with_http_info(config_id, url, data, detail, image_encode, **kwargs)  # noqa: E501

    @validate_arguments
    def check_image_with_http_info(self, config_id : Annotated[StrictStr, Field(..., description="The configuration id from the Basic Configuration operations.")], url : Annotated[Optional[StrictStr], Field(description="<s>The url to the image that needs to be checked.</s> Deprecated: Use 'data' parameter instead. <b>This parameter will be removed in future releases.</b>")] = None, data : Annotated[Optional[StrictStr], Field(description="The http(s) url or base64 encoded data uri of the image that needs to be checked.")] = None, detail : Annotated[Optional[conint(strict=True, le=3, ge=0)], Field(description="Set the detail level of the response.  * _1_ - The response only contains the _Summary_ and possibly the _Encoded_ schemas for basic information's (better API performance). * _2_ - Additionally lists all broken rules (_BrokenRule_ schema) according to the configuration parameters that were requested. * _3_ - Also shows detections (e.g. _BaseDetection_ schema) that contains extended features to each found object.")] = None, image_encode : Annotated[Optional[StrictBool], Field(description="Specifies whether or not to draw an output image that will be delivered in the response body as base64 encoded string. The _Encoded_ schema will be available in the response.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Check an image with the AI.  # noqa: E501

        The response (_CheckResult_ schema) is returned immediately after the request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.check_image_with_http_info(config_id, url, data, detail, image_encode, async_req=True)
        >>> result = thread.get()

        :param config_id: The configuration id from the Basic Configuration operations. (required)
        :type config_id: str
        :param url: <s>The url to the image that needs to be checked.</s> Deprecated: Use 'data' parameter instead. <b>This parameter will be removed in future releases.</b>
        :type url: str
        :param data: The http(s) url or base64 encoded data uri of the image that needs to be checked.
        :type data: str
        :param detail: Set the detail level of the response.  * _1_ - The response only contains the _Summary_ and possibly the _Encoded_ schemas for basic information's (better API performance). * _2_ - Additionally lists all broken rules (_BrokenRule_ schema) according to the configuration parameters that were requested. * _3_ - Also shows detections (e.g. _BaseDetection_ schema) that contains extended features to each found object.
        :type detail: int
        :param image_encode: Specifies whether or not to draw an output image that will be delivered in the response body as base64 encoded string. The _Encoded_ schema will be available in the response.
        :type image_encode: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CheckResult, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'config_id',
            'url',
            'data',
            'detail',
            'image_encode'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method check_image" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['config_id']:
            _path_params['configId'] = _params['config_id']


        # process the query parameters
        _query_params = []
        if _params.get('url') is not None:  # noqa: E501
            _query_params.append(('url', _params['url']))

        if _params.get('data') is not None:  # noqa: E501
            _query_params.append(('data', _params['data']))

        if _params.get('detail') is not None:  # noqa: E501
            _query_params.append(('detail', _params['detail']))

        if _params.get('image_encode') is not None:  # noqa: E501
            _query_params.append(('imageEncode', _params['image_encode']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['LICENSE-KEY']  # noqa: E501

        _response_types_map = {
            '404': "ApiNotice",
            '200': "CheckResult",
            '402': "ApiNotice",
        }

        return self.api_client.call_api(
            '/v2/check-image/{configId}', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def check_stream(self, config_id : Annotated[StrictStr, Field(..., description="The configuration id from the Basic Configuration operations.")], in_url : Annotated[StrictStr, Field(..., description="The URL of the video stream that the AI should check.")], out_url : Annotated[Optional[StrictStr], Field(description="The URL of where the AI should send the encoded stream.")] = None, cycle_length : Annotated[Optional[conint(strict=True, ge=100)], Field(description="Determine how often (value in milliseconds) the the AI should give a feedback.")] = None, check_rate : Annotated[Optional[conint(strict=True, ge=0)], Field(description="The milliseconds between each AI check. E.g. The AI will check 1 frame per second when checkRate is set to '1000'.")] = None, **kwargs) -> List[CheckResult]:  # noqa: E501
        """Check a stream with the AI.  # noqa: E501

        The body is continuously send per JSON stream until completion of the video stream. Only then the full _CheckResult_ schema will be shown (past _Events_ omitted).  <b>NOTICE: Depending on your configuration and parameters this operation can be quite expensive on your credit balance.<b>  <b>WARNING: Please do not use the 'Try it out' for this operation. The browser is not able to refresh the response preview until the completion of the video stream.<b>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.check_stream(config_id, in_url, out_url, cycle_length, check_rate, async_req=True)
        >>> result = thread.get()

        :param config_id: The configuration id from the Basic Configuration operations. (required)
        :type config_id: str
        :param in_url: The URL of the video stream that the AI should check. (required)
        :type in_url: str
        :param out_url: The URL of where the AI should send the encoded stream.
        :type out_url: str
        :param cycle_length: Determine how often (value in milliseconds) the the AI should give a feedback.
        :type cycle_length: int
        :param check_rate: The milliseconds between each AI check. E.g. The AI will check 1 frame per second when checkRate is set to '1000'.
        :type check_rate: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[CheckResult]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the check_stream_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.check_stream_with_http_info(config_id, in_url, out_url, cycle_length, check_rate, **kwargs)  # noqa: E501

    @validate_arguments
    def check_stream_with_http_info(self, config_id : Annotated[StrictStr, Field(..., description="The configuration id from the Basic Configuration operations.")], in_url : Annotated[StrictStr, Field(..., description="The URL of the video stream that the AI should check.")], out_url : Annotated[Optional[StrictStr], Field(description="The URL of where the AI should send the encoded stream.")] = None, cycle_length : Annotated[Optional[conint(strict=True, ge=100)], Field(description="Determine how often (value in milliseconds) the the AI should give a feedback.")] = None, check_rate : Annotated[Optional[conint(strict=True, ge=0)], Field(description="The milliseconds between each AI check. E.g. The AI will check 1 frame per second when checkRate is set to '1000'.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Check a stream with the AI.  # noqa: E501

        The body is continuously send per JSON stream until completion of the video stream. Only then the full _CheckResult_ schema will be shown (past _Events_ omitted).  <b>NOTICE: Depending on your configuration and parameters this operation can be quite expensive on your credit balance.<b>  <b>WARNING: Please do not use the 'Try it out' for this operation. The browser is not able to refresh the response preview until the completion of the video stream.<b>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.check_stream_with_http_info(config_id, in_url, out_url, cycle_length, check_rate, async_req=True)
        >>> result = thread.get()

        :param config_id: The configuration id from the Basic Configuration operations. (required)
        :type config_id: str
        :param in_url: The URL of the video stream that the AI should check. (required)
        :type in_url: str
        :param out_url: The URL of where the AI should send the encoded stream.
        :type out_url: str
        :param cycle_length: Determine how often (value in milliseconds) the the AI should give a feedback.
        :type cycle_length: int
        :param check_rate: The milliseconds between each AI check. E.g. The AI will check 1 frame per second when checkRate is set to '1000'.
        :type check_rate: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(List[CheckResult], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'config_id',
            'in_url',
            'out_url',
            'cycle_length',
            'check_rate'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method check_stream" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['config_id']:
            _path_params['configId'] = _params['config_id']


        # process the query parameters
        _query_params = []
        if _params.get('in_url') is not None:  # noqa: E501
            _query_params.append(('inUrl', _params['in_url']))

        if _params.get('out_url') is not None:  # noqa: E501
            _query_params.append(('outUrl', _params['out_url']))

        if _params.get('cycle_length') is not None:  # noqa: E501
            _query_params.append(('cycleLength', _params['cycle_length']))

        if _params.get('check_rate') is not None:  # noqa: E501
            _query_params.append(('checkRate', _params['check_rate']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/x-ndjson'])  # noqa: E501

        # authentication setting
        _auth_settings = ['LICENSE-KEY']  # noqa: E501

        _response_types_map = {
            '404': "ApiNotice",
            '200': "List[CheckResult]",
            '402': "ApiNotice",
        }

        return self.api_client.call_api(
            '/v2/check-stream/{configId}', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def check_video(self, config_id : Annotated[StrictStr, Field(..., description="The configuration id from the Basic Configuration operations.")], url : Annotated[StrictStr, Field(..., description="The url to the video that needs to be checked.")], config : Config, detail : Annotated[Optional[conint(strict=True, le=3, ge=0)], Field(description="Set the detail level of the response.  * _1_ - The response only contains the _Summary_ and possibly the _Encoded_ schemas for basic information's (better API performance). * _2_ - Additionally lists all broken rules (_BrokenRule_ schema) according to the configuration parameters that were requested. * _3_ - Also shows events (_Event_ schema) that contains extended features to each found object.")] = None, image_encode : Annotated[Optional[StrictBool], Field(description="Specifies whether or not to draw an output video that can be downloaded afterwards. The _Encoded_ schema will be available in the response.")] = None, check_rate : Annotated[Optional[conint(strict=True, ge=0)], Field(description="The milliseconds between each AI check. E.g. The AI will check 1 frame per second when checkRate is set to '1000'.")] = None, **kwargs) -> None:  # noqa: E501
        """Check a video with the AI.  # noqa: E501

        An empty response is returned immediately. The actual body (_CheckResult_ schema) is send to the _callbackUrl_ after the AI has finished processing.  <b>NOTICE: Depending on your configuration and parameters this operation can be quite expensive on your credit balance.<b>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.check_video(config_id, url, config, detail, image_encode, check_rate, async_req=True)
        >>> result = thread.get()

        :param config_id: The configuration id from the Basic Configuration operations. (required)
        :type config_id: str
        :param url: The url to the video that needs to be checked. (required)
        :type url: str
        :param config: (required)
        :type config: Config
        :param detail: Set the detail level of the response.  * _1_ - The response only contains the _Summary_ and possibly the _Encoded_ schemas for basic information's (better API performance). * _2_ - Additionally lists all broken rules (_BrokenRule_ schema) according to the configuration parameters that were requested. * _3_ - Also shows events (_Event_ schema) that contains extended features to each found object.
        :type detail: int
        :param image_encode: Specifies whether or not to draw an output video that can be downloaded afterwards. The _Encoded_ schema will be available in the response.
        :type image_encode: bool
        :param check_rate: The milliseconds between each AI check. E.g. The AI will check 1 frame per second when checkRate is set to '1000'.
        :type check_rate: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the check_video_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.check_video_with_http_info(config_id, url, config, detail, image_encode, check_rate, **kwargs)  # noqa: E501

    @validate_arguments
    def check_video_with_http_info(self, config_id : Annotated[StrictStr, Field(..., description="The configuration id from the Basic Configuration operations.")], url : Annotated[StrictStr, Field(..., description="The url to the video that needs to be checked.")], config : Config, detail : Annotated[Optional[conint(strict=True, le=3, ge=0)], Field(description="Set the detail level of the response.  * _1_ - The response only contains the _Summary_ and possibly the _Encoded_ schemas for basic information's (better API performance). * _2_ - Additionally lists all broken rules (_BrokenRule_ schema) according to the configuration parameters that were requested. * _3_ - Also shows events (_Event_ schema) that contains extended features to each found object.")] = None, image_encode : Annotated[Optional[StrictBool], Field(description="Specifies whether or not to draw an output video that can be downloaded afterwards. The _Encoded_ schema will be available in the response.")] = None, check_rate : Annotated[Optional[conint(strict=True, ge=0)], Field(description="The milliseconds between each AI check. E.g. The AI will check 1 frame per second when checkRate is set to '1000'.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Check a video with the AI.  # noqa: E501

        An empty response is returned immediately. The actual body (_CheckResult_ schema) is send to the _callbackUrl_ after the AI has finished processing.  <b>NOTICE: Depending on your configuration and parameters this operation can be quite expensive on your credit balance.<b>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.check_video_with_http_info(config_id, url, config, detail, image_encode, check_rate, async_req=True)
        >>> result = thread.get()

        :param config_id: The configuration id from the Basic Configuration operations. (required)
        :type config_id: str
        :param url: The url to the video that needs to be checked. (required)
        :type url: str
        :param config: (required)
        :type config: Config
        :param detail: Set the detail level of the response.  * _1_ - The response only contains the _Summary_ and possibly the _Encoded_ schemas for basic information's (better API performance). * _2_ - Additionally lists all broken rules (_BrokenRule_ schema) according to the configuration parameters that were requested. * _3_ - Also shows events (_Event_ schema) that contains extended features to each found object.
        :type detail: int
        :param image_encode: Specifies whether or not to draw an output video that can be downloaded afterwards. The _Encoded_ schema will be available in the response.
        :type image_encode: bool
        :param check_rate: The milliseconds between each AI check. E.g. The AI will check 1 frame per second when checkRate is set to '1000'.
        :type check_rate: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'config_id',
            'url',
            'config',
            'detail',
            'image_encode',
            'check_rate'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method check_video" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['config_id']:
            _path_params['configId'] = _params['config_id']


        # process the query parameters
        _query_params = []
        if _params.get('url') is not None:  # noqa: E501
            _query_params.append(('url', _params['url']))

        if _params.get('detail') is not None:  # noqa: E501
            _query_params.append(('detail', _params['detail']))

        if _params.get('image_encode') is not None:  # noqa: E501
            _query_params.append(('imageEncode', _params['image_encode']))

        if _params.get('check_rate') is not None:  # noqa: E501
            _query_params.append(('checkRate', _params['check_rate']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['config'] is not None:
            _body_params = _params['config']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['LICENSE-KEY']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/v2/check-video/{configId}', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))