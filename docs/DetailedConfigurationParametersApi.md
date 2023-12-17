# irisnet_client.DetailedConfigurationParametersApi

All URIs are relative to *https://api.irisnet.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_parameters**](DetailedConfigurationParametersApi.md#clear_parameters) | **DELETE** /v2/config/parameters/{configId} | Delete the parameters of the AI configuration.
[**get_parameters**](DetailedConfigurationParametersApi.md#get_parameters) | **GET** /v2/config/parameters/{configId} | Get the parameters of the AI configuration.
[**set_parameters**](DetailedConfigurationParametersApi.md#set_parameters) | **POST** /v2/config/parameters/{configId} | Set parameters to the given AI configuration.


# **clear_parameters**
> clear_parameters(config_id)

Delete the parameters of the AI configuration.

Clears the parameters and restores the defaults for all classifications.

### Example

* Api Key Authentication (LICENSE-KEY):
```python
import time
import os
import irisnet_client
from irisnet_client.rest import ApiException
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
configuration.api_key['LICENSE-KEY'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['LICENSE-KEY'] = 'Bearer'

# Enter a context with an instance of the API client
with irisnet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = irisnet_client.DetailedConfigurationParametersApi(api_client)
    config_id = 'config_id_example' # str | The id of the configuration where the parameters should be deleted.

    try:
        # Delete the parameters of the AI configuration.
        api_instance.clear_parameters(config_id)
    except Exception as e:
        print("Exception when calling DetailedConfigurationParametersApi->clear_parameters: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| The id of the configuration where the parameters should be deleted. | 

### Return type

void (empty response body)

### Authorization

[LICENSE-KEY](../README.md#LICENSE-KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | configId not found. |  -  |
**204** | successful operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parameters**
> ParamSet get_parameters(config_id)

Get the parameters of the AI configuration.

Returns the parameters stored in the given configuration.

### Example

* Api Key Authentication (LICENSE-KEY):
```python
import time
import os
import irisnet_client
from irisnet_client.models.param_set import ParamSet
from irisnet_client.rest import ApiException
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
configuration.api_key['LICENSE-KEY'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['LICENSE-KEY'] = 'Bearer'

# Enter a context with an instance of the API client
with irisnet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = irisnet_client.DetailedConfigurationParametersApi(api_client)
    config_id = 'config_id_example' # str | The id of the configuration for which the parameters are being requested.

    try:
        # Get the parameters of the AI configuration.
        api_response = api_instance.get_parameters(config_id)
        print("The response of DetailedConfigurationParametersApi->get_parameters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DetailedConfigurationParametersApi->get_parameters: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| The id of the configuration for which the parameters are being requested. | 

### Return type

[**ParamSet**](ParamSet.md)

### Authorization

[LICENSE-KEY](../README.md#LICENSE-KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | configuration with given id not found or parameters for configuration not found. |  -  |
**200** | successful operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_parameters**
> ParamSet set_parameters(config_id, param_set)

Set parameters to the given AI configuration.

Save or modify the parameters stored in the AI configuration.

### Example

* Api Key Authentication (LICENSE-KEY):
```python
import time
import os
import irisnet_client
from irisnet_client.models.param_set import ParamSet
from irisnet_client.rest import ApiException
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
configuration.api_key['LICENSE-KEY'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['LICENSE-KEY'] = 'Bearer'

# Enter a context with an instance of the API client
with irisnet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = irisnet_client.DetailedConfigurationParametersApi(api_client)
    config_id = 'config_id_example' # str | The id of the configuration where the parameters should be added.
    param_set = {"params":[{"classification":"breast","drawMode":3},{"classification":"vulva","drawMode":3},{"classification":"penis","drawMode":3},{"classification":"vagina","drawMode":3},{"classification":"buttocks","drawMode":3},{"classification":"anus","drawMode":3},{"classification":"toy","drawMode":3},{"classification":"oral","drawMode":3},{"classification":"penetration","drawMode":3}]} # ParamSet | Define the parameters to use for an AI check operation. View the _ParamSet_ and _Param_ schema to see the available parameters.

    try:
        # Set parameters to the given AI configuration.
        api_response = api_instance.set_parameters(config_id, param_set)
        print("The response of DetailedConfigurationParametersApi->set_parameters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DetailedConfigurationParametersApi->set_parameters: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| The id of the configuration where the parameters should be added. | 
 **param_set** | [**ParamSet**](ParamSet.md)| Define the parameters to use for an AI check operation. View the _ParamSet_ and _Param_ schema to see the available parameters. | 

### Return type

[**ParamSet**](ParamSet.md)

### Authorization

[LICENSE-KEY](../README.md#LICENSE-KEY)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | configId not found. |  -  |
**400** | Bad request. Check for badly formatted request body. |  -  |
**204** | successful operation. No previously configured parameters exist. |  -  |
**200** | successful operation. Previous user configured parameters are returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

