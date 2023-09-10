# irisnet_client.BalanceEndpointsApi

All URIs are relative to *https://api.irisnet.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cost**](BalanceEndpointsApi.md#get_cost) | **GET** /v2/cost/{configId} | Get the cost of the configuration for a single image.
[**get_license_info**](BalanceEndpointsApi.md#get_license_info) | **GET** /v2/info/ | Get information for the given license key.
[**get_video_cost**](BalanceEndpointsApi.md#get_video_cost) | **GET** /v2/cost/{configId}/{frames} | Get the cost of the configuration for moving images.
[**get_video_cost1**](BalanceEndpointsApi.md#get_video_cost1) | **GET** /v2/cost/{configId}/{fps}/{duration} | Get the cost of the configuration for moving images.


# **get_cost**
> Pricing get_cost(config_id)

Get the cost of the configuration for a single image.

The cost is subtracted from the license key after a successful check-image operation.

### Example

* Api Key Authentication (LICENSE-KEY):
```python
import time
import os
import irisnet_client
from irisnet_client.models.pricing import Pricing
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
    api_instance = irisnet_client.BalanceEndpointsApi(api_client)
    config_id = 'config_id_example' # str | The configuration id from the Basic Configuration operations.

    try:
        # Get the cost of the configuration for a single image.
        api_response = api_instance.get_cost(config_id)
        print("The response of BalanceEndpointsApi->get_cost:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BalanceEndpointsApi->get_cost: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| The configuration id from the Basic Configuration operations. | 

### Return type

[**Pricing**](Pricing.md)

### Authorization

[LICENSE-KEY](../README.md#LICENSE-KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | configId not found. |  -  |
**429** | The ai could not handle the request because it is either overloaded or currently down for maintenance. This is a temporary state. A &#39;Retry-After&#39; Header is included in the response to signal the client to retry after a certain amount of seconds. |  -  |
**200** | The cost of the given configuration. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_info**
> LicenseInfo get_license_info()

Get information for the given license key.

Get the LicenseInfo schema for the given license key in the authorization header.

### Example

* Api Key Authentication (LICENSE-KEY):
```python
import time
import os
import irisnet_client
from irisnet_client.models.license_info import LicenseInfo
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
    api_instance = irisnet_client.BalanceEndpointsApi(api_client)

    try:
        # Get information for the given license key.
        api_response = api_instance.get_license_info()
        print("The response of BalanceEndpointsApi->get_license_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BalanceEndpointsApi->get_license_info: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**LicenseInfo**](LicenseInfo.md)

### Authorization

[LICENSE-KEY](../README.md#LICENSE-KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | The entered license key was not found. |  -  |
**200** | successful operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video_cost**
> Pricing get_video_cost(config_id, frames)

Get the cost of the configuration for moving images.

The cost is subtracted from the license key after a successful check operation for moving images.  <b>NOTICE: The returned cost is an approximation. The exact cost can only be determined during the check operation.<b>

### Example

* Api Key Authentication (LICENSE-KEY):
```python
import time
import os
import irisnet_client
from irisnet_client.models.pricing import Pricing
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
    api_instance = irisnet_client.BalanceEndpointsApi(api_client)
    config_id = 'config_id_example' # str | The configuration id from the Basic Configuration operations.
    frames = 56 # int | The number of frames that the AI should check.

    try:
        # Get the cost of the configuration for moving images.
        api_response = api_instance.get_video_cost(config_id, frames)
        print("The response of BalanceEndpointsApi->get_video_cost:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BalanceEndpointsApi->get_video_cost: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| The configuration id from the Basic Configuration operations. | 
 **frames** | **int**| The number of frames that the AI should check. | 

### Return type

[**Pricing**](Pricing.md)

### Authorization

[LICENSE-KEY](../README.md#LICENSE-KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | configId not found. |  -  |
**200** | The cost of the given configuration |  -  |
**429** | The ai could not handle the request because it is either overloaded or currently down for maintenance. This is a temporary state. A &#39;Retry-After&#39; Header is included in the response to signal the client to retry after a certain amount of seconds. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video_cost1**
> Pricing get_video_cost1(config_id, fps, duration)

Get the cost of the configuration for moving images.

The cost is subtracted from the license key after a successful check operation for moving images.  <b>NOTICE: The returned cost is an approximation. The exact cost can only be determined during the check operation.<b>

### Example

* Api Key Authentication (LICENSE-KEY):
```python
import time
import os
import irisnet_client
from irisnet_client.models.pricing import Pricing
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
    api_instance = irisnet_client.BalanceEndpointsApi(api_client)
    config_id = 'config_id_example' # str | The configuration id from the Basic Configuration operations.
    fps = 56 # int | The frames per second of the video or stream.
    duration = 56 # int | The duration in seconds of the video or stream.

    try:
        # Get the cost of the configuration for moving images.
        api_response = api_instance.get_video_cost1(config_id, fps, duration)
        print("The response of BalanceEndpointsApi->get_video_cost1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BalanceEndpointsApi->get_video_cost1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| The configuration id from the Basic Configuration operations. | 
 **fps** | **int**| The frames per second of the video or stream. | 
 **duration** | **int**| The duration in seconds of the video or stream. | 

### Return type

[**Pricing**](Pricing.md)

### Authorization

[LICENSE-KEY](../README.md#LICENSE-KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | configId not found. |  -  |
**429** | The ai could not handle the request because it is either overloaded or currently down for maintenance. This is a temporary state. A &#39;Retry-After&#39; Header is included in the response to signal the client to retry after a certain amount of seconds. |  -  |
**200** | The cost of the given configuration. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

