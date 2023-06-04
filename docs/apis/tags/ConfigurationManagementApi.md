<a id="__pageTop"></a>
# irisnet_client.apis.tags.configuration_management_api.ConfigurationManagementApi

All URIs are relative to *https://api.irisnet.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_config**](#delete_config) | **delete** /v2/config/{configId} | Delete an AI configuration.
[**get_all_configs**](#get_all_configs) | **get** /v2/config/ | List all saved AI configurations.
[**get_config**](#get_config) | **get** /v2/config/{configId} | Get a specific AI configuration.
[**set_config**](#set_config) | **post** /v2/config/ | Create a new AI configuration.

# **delete_config**
<a id="delete_config"></a>
> delete_config(config_id)

Delete an AI configuration.

Deletes the AI configuration with the given id.

### Example

* Api Key Authentication (LICENSE-KEY):
```python
import irisnet_client
from irisnet_client.apis.tags import configuration_management_api
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
    api_instance = configuration_management_api.ConfigurationManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'configId': "configId_example",
    }
    try:
        # Delete an AI configuration.
        api_response = api_instance.delete_config(
            path_params=path_params,
        )
    except irisnet_client.ApiException as e:
        print("Exception when calling ConfigurationManagementApi->delete_config: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('*/*', ) | Tells the server the content type(s) that are accepted by the client
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
204 | [ApiResponseFor204](#delete_config.ApiResponseFor204) | successful operation.
404 | [ApiResponseFor404](#delete_config.ApiResponseFor404) | configId not found.

#### delete_config.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_config.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBody, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiNotice**](../../models/ApiNotice.md) |  | 


### Authorization

[LICENSE-KEY](../../../README.md#LICENSE-KEY)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_all_configs**
<a id="get_all_configs"></a>
> [Config] get_all_configs()

List all saved AI configurations.

Returns a list of all configurations with its id's and configured prototypes. There is a limit on how many configurations can be stored per license key. You can find this limit in the response of the info operation.

### Example

* Api Key Authentication (LICENSE-KEY):
```python
import irisnet_client
from irisnet_client.apis.tags import configuration_management_api
from irisnet_client.model.config import Config
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
    api_instance = configuration_management_api.ConfigurationManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List all saved AI configurations.
        api_response = api_instance.get_all_configs()
        pprint(api_response)
    except irisnet_client.ApiException as e:
        print("Exception when calling ConfigurationManagementApi->get_all_configs: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_all_configs.ApiResponseFor200) | successful operation.

#### get_all_configs.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Config**]({{complexTypePrefix}}Config.md) | [**Config**]({{complexTypePrefix}}Config.md) | [**Config**]({{complexTypePrefix}}Config.md) |  | 

### Authorization

[LICENSE-KEY](../../../README.md#LICENSE-KEY)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_config**
<a id="get_config"></a>
> Config get_config(config_id)

Get a specific AI configuration.

Returns a specific AI configuration for the requested id.

### Example

* Api Key Authentication (LICENSE-KEY):
```python
import irisnet_client
from irisnet_client.apis.tags import configuration_management_api
from irisnet_client.model.config import Config
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
    api_instance = configuration_management_api.ConfigurationManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'configId': "configId_example",
    }
    try:
        # Get a specific AI configuration.
        api_response = api_instance.get_config(
            path_params=path_params,
        )
        pprint(api_response)
    except irisnet_client.ApiException as e:
        print("Exception when calling ConfigurationManagementApi->get_config: %s\n" % e)
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
404 | [ApiResponseFor404](#get_config.ApiResponseFor404) | configId not found.
200 | [ApiResponseFor200](#get_config.ApiResponseFor200) | successful operation.

#### get_config.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiNotice**](../../models/ApiNotice.md) |  | 


#### get_config.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Config**](../../models/Config.md) |  | 


### Authorization

[LICENSE-KEY](../../../README.md#LICENSE-KEY)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **set_config**
<a id="set_config"></a>
> Config set_config(config)

Create a new AI configuration.

Create a new AI configuration with the desired prototypes.

### Example

* Api Key Authentication (LICENSE-KEY):
```python
import irisnet_client
from irisnet_client.apis.tags import configuration_management_api
from irisnet_client.model.config import Config
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
    api_instance = configuration_management_api.ConfigurationManagementApi(api_client)

    # example passing only required values which don't have defaults set
    body = Config(
        id="id_example",
        prototypes=[
            "nudityCheck"
        ],
    )
    try:
        # Create a new AI configuration.
        api_response = api_instance.set_config(
            body=body,
        )
        pprint(api_response)
    except irisnet_client.ApiException as e:
        print("Exception when calling ConfigurationManagementApi->set_config: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Config**](../../models/Config.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
400 | [ApiResponseFor400](#set_config.ApiResponseFor400) | Bad request. Check for badly formatted request body.
403 | [ApiResponseFor403](#set_config.ApiResponseFor403) | Maximum number of stored AI configurations reached.
200 | [ApiResponseFor200](#set_config.ApiResponseFor200) | successful operation.

#### set_config.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiNotice**](../../models/ApiNotice.md) |  | 


#### set_config.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiNotice**](../../models/ApiNotice.md) |  | 


#### set_config.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Config**](../../models/Config.md) |  | 


### Authorization

[LICENSE-KEY](../../../README.md#LICENSE-KEY)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

