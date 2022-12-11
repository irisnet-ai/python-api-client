<a name="__pageTop"></a>
# irisnet_client.apis.tags.detailed_configuration_parameters_api.DetailedConfigurationParametersApi

All URIs are relative to *https://api.irisnet.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_parameters**](#clear_parameters) | **delete** /v2/config/parameters/{configId} | Delete the parameters of the AI configuration.
[**get_parameters**](#get_parameters) | **get** /v2/config/parameters/{configId} | Get the parameters of the AI configuration.
[**set_parameters**](#set_parameters) | **post** /v2/config/parameters/{configId} | Set parameters to the given AI configuration.

# **clear_parameters**
<a name="clear_parameters"></a>
> clear_parameters(config_id)

Delete the parameters of the AI configuration.

Clears the parameters and restores the defaults for all classifications.

### Example

* Api Key Authentication (LICENSE-KEY):
```python
import irisnet_client
from irisnet_client.apis.tags import detailed_configuration_parameters_api
from irisnet_client.model.api_notice import ApiNotice
from pprint import pprint
# Defining the host is optional and defaults to https://api.irisnet.de
# See configuration.py for a list of all supported configuration parameters.
configuration = irisnet_client.Configuration(
    host = "https://api.irisnet.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: LICENSE-KEY
configuration.api_key['LICENSE-KEY'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['LICENSE-KEY'] = 'Bearer'
# Enter a context with an instance of the API client
with irisnet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = detailed_configuration_parameters_api.DetailedConfigurationParametersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'configId': "configId_example",
    }
    try:
        # Delete the parameters of the AI configuration.
        api_response = api_instance.clear_parameters(
            path_params=path_params,
        )
    except irisnet_client.ApiException as e:
        print("Exception when calling DetailedConfigurationParametersApi->clear_parameters: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
configId | ConfigIdSchema | | 

# ConfigIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#clear_parameters.ApiResponseFor204) | successful operation.
404 | [ApiResponseFor404](#clear_parameters.ApiResponseFor404) | configId not found.

#### clear_parameters.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### clear_parameters.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiNotice**](../../models/ApiNotice.md) |  | 


### Authorization

[LICENSE-KEY](../../../README.md#LICENSE-KEY)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_parameters**
<a name="get_parameters"></a>
> ParamSet get_parameters(config_id)

Get the parameters of the AI configuration.

Returns the parameters stored in the given configuration.

### Example

* Api Key Authentication (LICENSE-KEY):
```python
import irisnet_client
from irisnet_client.apis.tags import detailed_configuration_parameters_api
from irisnet_client.model.api_notice import ApiNotice
from irisnet_client.model.param_set import ParamSet
from pprint import pprint
# Defining the host is optional and defaults to https://api.irisnet.de
# See configuration.py for a list of all supported configuration parameters.
configuration = irisnet_client.Configuration(
    host = "https://api.irisnet.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: LICENSE-KEY
configuration.api_key['LICENSE-KEY'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['LICENSE-KEY'] = 'Bearer'
# Enter a context with an instance of the API client
with irisnet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = detailed_configuration_parameters_api.DetailedConfigurationParametersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'configId': "configId_example",
    }
    try:
        # Get the parameters of the AI configuration.
        api_response = api_instance.get_parameters(
            path_params=path_params,
        )
        pprint(api_response)
    except irisnet_client.ApiException as e:
        print("Exception when calling DetailedConfigurationParametersApi->get_parameters: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
configId | ConfigIdSchema | | 

# ConfigIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_parameters.ApiResponseFor200) | successful operation.
404 | [ApiResponseFor404](#get_parameters.ApiResponseFor404) | configuration with given id not found or parameters for configuration not found.

#### get_parameters.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ParamSet**](../../models/ParamSet.md) |  | 


#### get_parameters.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiNotice**](../../models/ApiNotice.md) |  | 


### Authorization

[LICENSE-KEY](../../../README.md#LICENSE-KEY)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **set_parameters**
<a name="set_parameters"></a>
> ParamSet set_parameters(config_idparam_set)

Set parameters to the given AI configuration.

Save or modify the parameters stored in the AI configuration.

### Example

* Api Key Authentication (LICENSE-KEY):
```python
import irisnet_client
from irisnet_client.apis.tags import detailed_configuration_parameters_api
from irisnet_client.model.api_notice import ApiNotice
from irisnet_client.model.param_set import ParamSet
from pprint import pprint
# Defining the host is optional and defaults to https://api.irisnet.de
# See configuration.py for a list of all supported configuration parameters.
configuration = irisnet_client.Configuration(
    host = "https://api.irisnet.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: LICENSE-KEY
configuration.api_key['LICENSE-KEY'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['LICENSE-KEY'] = 'Bearer'
# Enter a context with an instance of the API client
with irisnet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = detailed_configuration_parameters_api.DetailedConfigurationParametersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'configId': "configId_example",
    }
    body = ParamSet(
        thresh=0.5,
        grey=127,
        min_duration=100,
        abort_on_severity=-1,
        params=[
            Param(
                classification="face",
                min=-1,
                max=-1,
                severity=100,
                draw_mode=0,
                grey=127,
                scale=1.0,
                ignore=False,
            )
        ],
    )
    try:
        # Set parameters to the given AI configuration.
        api_response = api_instance.set_parameters(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except irisnet_client.ApiException as e:
        print("Exception when calling DetailedConfigurationParametersApi->set_parameters: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ParamSet**](../../models/ParamSet.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
configId | ConfigIdSchema | | 

# ConfigIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
400 | [ApiResponseFor400](#set_parameters.ApiResponseFor400) | Bad request. Check for badly formatted request body.
204 | [ApiResponseFor204](#set_parameters.ApiResponseFor204) | successful operation. No previously configured parameters exist.
404 | [ApiResponseFor404](#set_parameters.ApiResponseFor404) | configId not found.
200 | [ApiResponseFor200](#set_parameters.ApiResponseFor200) | successful operation. Previous user configured parameters are returned.

#### set_parameters.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiNotice**](../../models/ApiNotice.md) |  | 


#### set_parameters.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### set_parameters.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiNotice**](../../models/ApiNotice.md) |  | 


#### set_parameters.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ParamSet**](../../models/ParamSet.md) |  | 


### Authorization

[LICENSE-KEY](../../../README.md#LICENSE-KEY)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

