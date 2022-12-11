<a name="__pageTop"></a>
# irisnet_client.apis.tags.ai_check_operations_api.AICheckOperationsApi

All URIs are relative to *https://api.irisnet.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_image**](#check_image) | **post** /v2/check-image/{configId} | Check an image with the AI.
[**check_stream**](#check_stream) | **post** /v2/check-stream/{configId} | Check a stream with the AI.
[**check_video**](#check_video) | **post** /v2/check-video/{configId} | Check a video with the AI.

# **check_image**
<a name="check_image"></a>
> CheckResult check_image(config_idurl)

Check an image with the AI.

The response (_CheckResult_ schema) is returned immediately after the request.

### Example

* Api Key Authentication (LICENSE-KEY):
```python
import irisnet_client
from irisnet_client.apis.tags import ai_check_operations_api
from irisnet_client.model.api_notice import ApiNotice
from irisnet_client.model.check_result import CheckResult
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
    api_instance = ai_check_operations_api.AICheckOperationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'configId': "configId_example",
    }
    query_params = {
        'url': "url_example",
    }
    try:
        # Check an image with the AI.
        api_response = api_instance.check_image(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except irisnet_client.ApiException as e:
        print("Exception when calling AICheckOperationsApi->check_image: %s\n" % e)

    # example passing only optional values
    path_params = {
        'configId': "configId_example",
    }
    query_params = {
        'url': "url_example",
        'detail': 1,
        'imageEncode': False,
    }
    try:
        # Check an image with the AI.
        api_response = api_instance.check_image(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except irisnet_client.ApiException as e:
        print("Exception when calling AICheckOperationsApi->check_image: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
url | UrlSchema | | 
detail | DetailSchema | | optional
imageEncode | ImageEncodeSchema | | optional


# UrlSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DetailSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 1value must be a 32 bit integer

# ImageEncodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

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
404 | [ApiResponseFor404](#check_image.ApiResponseFor404) | configId not found.
200 | [ApiResponseFor200](#check_image.ApiResponseFor200) | successful operation.
402 | [ApiResponseFor402](#check_image.ApiResponseFor402) | Not enough credits.

#### check_image.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiNotice**](../../models/ApiNotice.md) |  | 


#### check_image.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CheckResult**](../../models/CheckResult.md) |  | 


#### check_image.ApiResponseFor402
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor402ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor402ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiNotice**](../../models/ApiNotice.md) |  | 


### Authorization

[LICENSE-KEY](../../../README.md#LICENSE-KEY)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **check_stream**
<a name="check_stream"></a>
> [CheckResult] check_stream(config_idin_url)

Check a stream with the AI.

The body is continuously send per JSON stream until completion of the video stream. Only then the full _CheckResult_ schema will be shown (past _Events_ omitted).  <b>NOTICE: Depending on your configuration and parameters this operation can be quite expensive on your credit balance.<b>  <b>WARNING: Please do not use the 'Try it out' for this operation. The browser is not able to refresh the response preview until the completion of the video stream.<b>

### Example

* Api Key Authentication (LICENSE-KEY):
```python
import irisnet_client
from irisnet_client.apis.tags import ai_check_operations_api
from irisnet_client.model.api_notice import ApiNotice
from irisnet_client.model.check_result import CheckResult
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
    api_instance = ai_check_operations_api.AICheckOperationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'configId': "configId_example",
    }
    query_params = {
        'inUrl': "inUrl_example",
    }
    try:
        # Check a stream with the AI.
        api_response = api_instance.check_stream(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except irisnet_client.ApiException as e:
        print("Exception when calling AICheckOperationsApi->check_stream: %s\n" % e)

    # example passing only optional values
    path_params = {
        'configId': "configId_example",
    }
    query_params = {
        'inUrl': "inUrl_example",
        'outUrl': "outUrl_example",
        'cycleLength': 500,
        'checkRate': 0,
    }
    try:
        # Check a stream with the AI.
        api_response = api_instance.check_stream(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except irisnet_client.ApiException as e:
        print("Exception when calling AICheckOperationsApi->check_stream: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/x-ndjson', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
inUrl | InUrlSchema | | 
outUrl | OutUrlSchema | | optional
cycleLength | CycleLengthSchema | | optional
checkRate | CheckRateSchema | | optional


# InUrlSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OutUrlSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CycleLengthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 500value must be a 32 bit integer

# CheckRateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0value must be a 32 bit integer

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
404 | [ApiResponseFor404](#check_stream.ApiResponseFor404) | configId not found.
200 | [ApiResponseFor200](#check_stream.ApiResponseFor200) | successful operation.
402 | [ApiResponseFor402](#check_stream.ApiResponseFor402) | Not enough credits.

#### check_stream.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationXNdjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationXNdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiNotice**](../../models/ApiNotice.md) |  | 


#### check_stream.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationXNdjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationXNdjson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CheckResult**]({{complexTypePrefix}}CheckResult.md) | [**CheckResult**]({{complexTypePrefix}}CheckResult.md) | [**CheckResult**]({{complexTypePrefix}}CheckResult.md) |  | 

#### check_stream.ApiResponseFor402
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor402ResponseBodyApplicationXNdjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor402ResponseBodyApplicationXNdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiNotice**](../../models/ApiNotice.md) |  | 


### Authorization

[LICENSE-KEY](../../../README.md#LICENSE-KEY)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **check_video**
<a name="check_video"></a>
> check_video(config_idurlcallback)

Check a video with the AI.

An empty response is returned immediately. The actual body (_CheckResult_ schema) is send to the _callbackUrl_ after the AI has finished processing.  <b>NOTICE: Depending on your configuration and parameters this operation can be quite expensive on your credit balance.<b>

### Example

* Api Key Authentication (LICENSE-KEY):
```python
import irisnet_client
from irisnet_client.apis.tags import ai_check_operations_api
from irisnet_client.model.callback import Callback
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
    api_instance = ai_check_operations_api.AICheckOperationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'configId': "configId_example",
    }
    query_params = {
        'url': "url_example",
    }
    body = Callback(
        callback_url="callback_url_example",
        headers=dict(
            "key": "[\"Authorization\": \"Basic Rm9yemEgTmFwb2xpLCBzZW1wcmUh\"]",
        ),
    )
    try:
        # Check a video with the AI.
        api_response = api_instance.check_video(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
    except irisnet_client.ApiException as e:
        print("Exception when calling AICheckOperationsApi->check_video: %s\n" % e)

    # example passing only optional values
    path_params = {
        'configId': "configId_example",
    }
    query_params = {
        'url': "url_example",
        'detail': 1,
        'imageEncode': False,
        'checkRate': 0,
    }
    body = Callback(
        callback_url="callback_url_example",
        headers=dict(
            "key": "[\"Authorization\": \"Basic Rm9yemEgTmFwb2xpLCBzZW1wcmUh\"]",
        ),
    )
    try:
        # Check a video with the AI.
        api_response = api_instance.check_video(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
    except irisnet_client.ApiException as e:
        print("Exception when calling AICheckOperationsApi->check_video: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
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
[**Callback**](../../models/Callback.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
url | UrlSchema | | 
detail | DetailSchema | | optional
imageEncode | ImageEncodeSchema | | optional
checkRate | CheckRateSchema | | optional


# UrlSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DetailSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 1value must be a 32 bit integer

# ImageEncodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# CheckRateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0value must be a 32 bit integer

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
202 | [ApiResponseFor202](#check_video.ApiResponseFor202) | operation accepted: wait for callback.
404 | [ApiResponseFor404](#check_video.ApiResponseFor404) | configId not found.
402 | [ApiResponseFor402](#check_video.ApiResponseFor402) | Not enough credits.

#### check_video.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### check_video.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiNotice**](../../models/ApiNotice.md) |  | 


#### check_video.ApiResponseFor402
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor402ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor402ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiNotice**](../../models/ApiNotice.md) |  | 


### Authorization

[LICENSE-KEY](../../../README.md#LICENSE-KEY)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

