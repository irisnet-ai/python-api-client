<a id="__pageTop"></a>
# irisnet_client.apis.tags.balance_endpoints_api.BalanceEndpointsApi

All URIs are relative to *https://api.irisnet.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cost**](#get_cost) | **get** /v2/cost/{configId} | Get the cost of the configuration for a single image.
[**get_license_info**](#get_license_info) | **get** /v2/info/ | Get information for the given license key.
[**get_video_cost**](#get_video_cost) | **get** /v2/cost/{configId}/{frames} | Get the cost of the configuration for moving images.
[**get_video_cost1**](#get_video_cost1) | **get** /v2/cost/{configId}/{fps}/{duration} | Get the cost of the configuration for moving images.

# **get_cost**
<a id="get_cost"></a>
> Pricing get_cost(config_id)

Get the cost of the configuration for a single image.

The cost is subtracted from the license key after a successful check-image operation.

### Example

* Api Key Authentication (LICENSE-KEY):
```python
import irisnet_client
from irisnet_client.apis.tags import balance_endpoints_api
from irisnet_client.model.pricing import Pricing
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
    api_instance = balance_endpoints_api.BalanceEndpointsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'configId': "configId_example",
    }
    try:
        # Get the cost of the configuration for a single image.
        api_response = api_instance.get_cost(
            path_params=path_params,
        )
        pprint(api_response)
    except irisnet_client.ApiException as e:
        print("Exception when calling BalanceEndpointsApi->get_cost: %s\n" % e)
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
404 | [ApiResponseFor404](#get_cost.ApiResponseFor404) | configId not found.
200 | [ApiResponseFor200](#get_cost.ApiResponseFor200) | The cost of the given configuration.
429 | [ApiResponseFor429](#get_cost.ApiResponseFor429) | The ai could not handle the request because it is either overloaded or currently down for maintenance. This is a temporary state. A &#x27;Retry-After&#x27; Header is included in the response to signal the client to retry after a certain amount of seconds.

#### get_cost.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiNotice**](../../models/ApiNotice.md) |  | 


#### get_cost.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Pricing**](../../models/Pricing.md) |  | 


#### get_cost.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiNotice**](../../models/ApiNotice.md) |  | 


### Authorization

[LICENSE-KEY](../../../README.md#LICENSE-KEY)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_license_info**
<a id="get_license_info"></a>
> LicenseInfo get_license_info()

Get information for the given license key.

Get the LicenseInfo schema for the given license key in the authorization header.

### Example

* Api Key Authentication (LICENSE-KEY):
```python
import irisnet_client
from irisnet_client.apis.tags import balance_endpoints_api
from irisnet_client.model.license_info import LicenseInfo
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
    api_instance = balance_endpoints_api.BalanceEndpointsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get information for the given license key.
        api_response = api_instance.get_license_info()
        pprint(api_response)
    except irisnet_client.ApiException as e:
        print("Exception when calling BalanceEndpointsApi->get_license_info: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
404 | [ApiResponseFor404](#get_license_info.ApiResponseFor404) | The entered license key was not found.
200 | [ApiResponseFor200](#get_license_info.ApiResponseFor200) | successful operation.

#### get_license_info.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiNotice**](../../models/ApiNotice.md) |  | 


#### get_license_info.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LicenseInfo**](../../models/LicenseInfo.md) |  | 


### Authorization

[LICENSE-KEY](../../../README.md#LICENSE-KEY)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_video_cost**
<a id="get_video_cost"></a>
> Pricing get_video_cost(config_idframes)

Get the cost of the configuration for moving images.

The cost is subtracted from the license key after a successful check operation for moving images.  <b>NOTICE: The returned cost is an approximation. The exact cost can only be determined during the check operation.<b>

### Example

* Api Key Authentication (LICENSE-KEY):
```python
import irisnet_client
from irisnet_client.apis.tags import balance_endpoints_api
from irisnet_client.model.pricing import Pricing
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
    api_instance = balance_endpoints_api.BalanceEndpointsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'configId': "configId_example",
        'frames': 1,
    }
    try:
        # Get the cost of the configuration for moving images.
        api_response = api_instance.get_video_cost(
            path_params=path_params,
        )
        pprint(api_response)
    except irisnet_client.ApiException as e:
        print("Exception when calling BalanceEndpointsApi->get_video_cost: %s\n" % e)
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
frames | FramesSchema | | 

# ConfigIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# FramesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
404 | [ApiResponseFor404](#get_video_cost.ApiResponseFor404) | configId not found.
429 | [ApiResponseFor429](#get_video_cost.ApiResponseFor429) | The ai could not handle the request because it is either overloaded or currently down for maintenance. This is a temporary state. A &#x27;Retry-After&#x27; Header is included in the response to signal the client to retry after a certain amount of seconds.
200 | [ApiResponseFor200](#get_video_cost.ApiResponseFor200) | The cost of the given configuration

#### get_video_cost.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiNotice**](../../models/ApiNotice.md) |  | 


#### get_video_cost.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiNotice**](../../models/ApiNotice.md) |  | 


#### get_video_cost.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Pricing**](../../models/Pricing.md) |  | 


### Authorization

[LICENSE-KEY](../../../README.md#LICENSE-KEY)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_video_cost1**
<a id="get_video_cost1"></a>
> Pricing get_video_cost1(config_idfpsduration)

Get the cost of the configuration for moving images.

The cost is subtracted from the license key after a successful check operation for moving images.  <b>NOTICE: The returned cost is an approximation. The exact cost can only be determined during the check operation.<b>

### Example

* Api Key Authentication (LICENSE-KEY):
```python
import irisnet_client
from irisnet_client.apis.tags import balance_endpoints_api
from irisnet_client.model.pricing import Pricing
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
    api_instance = balance_endpoints_api.BalanceEndpointsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'configId': "configId_example",
        'fps': 1,
        'duration': 1,
    }
    try:
        # Get the cost of the configuration for moving images.
        api_response = api_instance.get_video_cost1(
            path_params=path_params,
        )
        pprint(api_response)
    except irisnet_client.ApiException as e:
        print("Exception when calling BalanceEndpointsApi->get_video_cost1: %s\n" % e)
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
fps | FpsSchema | | 
duration | DurationSchema | | 

# ConfigIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# FpsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# DurationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
404 | [ApiResponseFor404](#get_video_cost1.ApiResponseFor404) | configId not found.
200 | [ApiResponseFor200](#get_video_cost1.ApiResponseFor200) | The cost of the given configuration.
429 | [ApiResponseFor429](#get_video_cost1.ApiResponseFor429) | The ai could not handle the request because it is either overloaded or currently down for maintenance. This is a temporary state. A &#x27;Retry-After&#x27; Header is included in the response to signal the client to retry after a certain amount of seconds.

#### get_video_cost1.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiNotice**](../../models/ApiNotice.md) |  | 


#### get_video_cost1.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Pricing**](../../models/Pricing.md) |  | 


#### get_video_cost1.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiNotice**](../../models/ApiNotice.md) |  | 


### Authorization

[LICENSE-KEY](../../../README.md#LICENSE-KEY)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

