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
from pydantic import Field, StrictStr

from irisnet_client.models.param_set import ParamSet

from irisnet_client.api_client import ApiClient
from irisnet_client.api_response import ApiResponse
from irisnet_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class DetailedConfigurationParametersApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def clear_parameters(self, config_id : Annotated[StrictStr, Field(..., description="The id of the configuration where the parameters should be deleted.")], **kwargs) -> None:  # noqa: E501
        """Delete the parameters of the AI configuration.  # noqa: E501

        Clears the parameters and restores the defaults for all classifications.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.clear_parameters(config_id, async_req=True)
        >>> result = thread.get()

        :param config_id: The id of the configuration where the parameters should be deleted. (required)
        :type config_id: str
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
            message = "Error! Please call the clear_parameters_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.clear_parameters_with_http_info(config_id, **kwargs)  # noqa: E501

    @validate_arguments
    def clear_parameters_with_http_info(self, config_id : Annotated[StrictStr, Field(..., description="The id of the configuration where the parameters should be deleted.")], **kwargs) -> ApiResponse:  # noqa: E501
        """Delete the parameters of the AI configuration.  # noqa: E501

        Clears the parameters and restores the defaults for all classifications.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.clear_parameters_with_http_info(config_id, async_req=True)
        >>> result = thread.get()

        :param config_id: The id of the configuration where the parameters should be deleted. (required)
        :type config_id: str
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
            'config_id'
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
                    " to method clear_parameters" % _key
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

        _response_types_map = {}

        return self.api_client.call_api(
            '/v2/config/parameters/{configId}', 'DELETE',
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
    def get_parameters(self, config_id : Annotated[StrictStr, Field(..., description="The id of the configuration for which the parameters are being requested.")], **kwargs) -> ParamSet:  # noqa: E501
        """Get the parameters of the AI configuration.  # noqa: E501

        Returns the parameters stored in the given configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_parameters(config_id, async_req=True)
        >>> result = thread.get()

        :param config_id: The id of the configuration for which the parameters are being requested. (required)
        :type config_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ParamSet
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_parameters_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_parameters_with_http_info(config_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_parameters_with_http_info(self, config_id : Annotated[StrictStr, Field(..., description="The id of the configuration for which the parameters are being requested.")], **kwargs) -> ApiResponse:  # noqa: E501
        """Get the parameters of the AI configuration.  # noqa: E501

        Returns the parameters stored in the given configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_parameters_with_http_info(config_id, async_req=True)
        >>> result = thread.get()

        :param config_id: The id of the configuration for which the parameters are being requested. (required)
        :type config_id: str
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
        :rtype: tuple(ParamSet, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'config_id'
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
                    " to method get_parameters" % _key
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
            '200': "ParamSet",
        }

        return self.api_client.call_api(
            '/v2/config/parameters/{configId}', 'GET',
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
    def set_parameters(self, config_id : Annotated[StrictStr, Field(..., description="The id of the configuration where the parameters should be added.")], param_set : Annotated[ParamSet, Field(..., description="Define the parameters to use for an AI check operation. View the _ParamSet_ and _Param_ schema to see the available parameters.")], **kwargs) -> ParamSet:  # noqa: E501
        """Set parameters to the given AI configuration.  # noqa: E501

        Save or modify the parameters stored in the AI configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.set_parameters(config_id, param_set, async_req=True)
        >>> result = thread.get()

        :param config_id: The id of the configuration where the parameters should be added. (required)
        :type config_id: str
        :param param_set: Define the parameters to use for an AI check operation. View the _ParamSet_ and _Param_ schema to see the available parameters. (required)
        :type param_set: ParamSet
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ParamSet
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the set_parameters_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.set_parameters_with_http_info(config_id, param_set, **kwargs)  # noqa: E501

    @validate_arguments
    def set_parameters_with_http_info(self, config_id : Annotated[StrictStr, Field(..., description="The id of the configuration where the parameters should be added.")], param_set : Annotated[ParamSet, Field(..., description="Define the parameters to use for an AI check operation. View the _ParamSet_ and _Param_ schema to see the available parameters.")], **kwargs) -> ApiResponse:  # noqa: E501
        """Set parameters to the given AI configuration.  # noqa: E501

        Save or modify the parameters stored in the AI configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.set_parameters_with_http_info(config_id, param_set, async_req=True)
        >>> result = thread.get()

        :param config_id: The id of the configuration where the parameters should be added. (required)
        :type config_id: str
        :param param_set: Define the parameters to use for an AI check operation. View the _ParamSet_ and _Param_ schema to see the available parameters. (required)
        :type param_set: ParamSet
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
        :rtype: tuple(ParamSet, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'config_id',
            'param_set'
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
                    " to method set_parameters" % _key
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
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['param_set'] is not None:
            _body_params = _params['param_set']

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

        _response_types_map = {
            '204': None,
            '404': "ApiNotice",
            '400': "ApiNotice",
            '200': "ParamSet",
        }

        return self.api_client.call_api(
            '/v2/config/parameters/{configId}', 'POST',
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