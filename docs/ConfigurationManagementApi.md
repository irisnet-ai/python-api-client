# irisnet_client.ConfigurationManagementApi

All URIs are relative to *https://api.irisnet.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_config**](ConfigurationManagementApi.md#delete_config) | **DELETE** /v2/config/{configId} | Delete an AI configuration.
[**get_all_configs**](ConfigurationManagementApi.md#get_all_configs) | **GET** /v2/config/ | List all saved AI configurations.
[**get_config**](ConfigurationManagementApi.md#get_config) | **GET** /v2/config/{configId} | Get a specific AI configuration.
[**set_config**](ConfigurationManagementApi.md#set_config) | **POST** /v2/config/ | Create a new AI configuration.


# **delete_config**
> delete_config(config_id)

Delete an AI configuration.

Deletes the AI configuration with the given id.

### Example

* Api Key Authentication (LICENSE-KEY):

```python
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
    api_instance = irisnet_client.ConfigurationManagementApi(api_client)
    config_id = 'config_id_example' # str | The id of the configuration that should be deleted.

    try:
        # Delete an AI configuration.
        api_instance.delete_config(config_id)
    except Exception as e:
        print("Exception when calling ConfigurationManagementApi->delete_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| The id of the configuration that should be deleted. | 

### Return type

void (empty response body)

### Authorization

[LICENSE-KEY](../README.md#LICENSE-KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | successful operation. |  -  |
**404** | configId not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_configs**
> List[Config] get_all_configs()

List all saved AI configurations.

Returns a list of all configurations with its id's and configured prototypes. There is a limit on how many configurations can be stored per license key. You can find this limit in the response of the info operation.

### Example

* Api Key Authentication (LICENSE-KEY):

```python
import irisnet_client
from irisnet_client.models.config import Config
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
    api_instance = irisnet_client.ConfigurationManagementApi(api_client)

    try:
        # List all saved AI configurations.
        api_response = api_instance.get_all_configs()
        print("The response of ConfigurationManagementApi->get_all_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationManagementApi->get_all_configs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Config]**](Config.md)

### Authorization

[LICENSE-KEY](../README.md#LICENSE-KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config**
> Config get_config(config_id)

Get a specific AI configuration.

Returns a specific AI configuration for the requested id.

### Example

* Api Key Authentication (LICENSE-KEY):

```python
import irisnet_client
from irisnet_client.models.config import Config
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
    api_instance = irisnet_client.ConfigurationManagementApi(api_client)
    config_id = 'config_id_example' # str | The id of the configuration that is being requested.

    try:
        # Get a specific AI configuration.
        api_response = api_instance.get_config(config_id)
        print("The response of ConfigurationManagementApi->get_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationManagementApi->get_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| The id of the configuration that is being requested. | 

### Return type

[**Config**](Config.md)

### Authorization

[LICENSE-KEY](../README.md#LICENSE-KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | configId not found. |  -  |
**200** | successful operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_config**
> Config set_config(config)

Create a new AI configuration.

Create a new AI configuration with the desired prototypes.

### Example

* Api Key Authentication (LICENSE-KEY):

```python
import irisnet_client
from irisnet_client.models.config import Config
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
    api_instance = irisnet_client.ConfigurationManagementApi(api_client)
    config = {"prototypes":["nudityCheck","ageEstimation","illegalSymbols","attributesCheck","nippleCheck","textRecognition","bodyAttributes","unwantedSubstances","violenceCheck","selfieCheck"]} # Config | Define the prototypes to use for an AI check operation. View the _Config_ schema to see the available prototypes.

    try:
        # Create a new AI configuration.
        api_response = api_instance.set_config(config)
        print("The response of ConfigurationManagementApi->set_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationManagementApi->set_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config** | [**Config**](Config.md)| Define the prototypes to use for an AI check operation. View the _Config_ schema to see the available prototypes. | 

### Return type

[**Config**](Config.md)

### Authorization

[LICENSE-KEY](../README.md#LICENSE-KEY)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Maximum number of stored AI configurations reached. |  -  |
**400** | Bad request. Check for badly formatted request body. |  -  |
**200** | successful operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

