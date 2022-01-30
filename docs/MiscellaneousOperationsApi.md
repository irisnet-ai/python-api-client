# irisnet_client.MiscellaneousOperationsApi

All URIs are relative to *https://api.irisnet.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_processed**](MiscellaneousOperationsApi.md#download_processed) | **GET** /v1/download/{filename} | Get the resulting media file.
[**get_ai_cost**](MiscellaneousOperationsApi.md#get_ai_cost) | **GET** /v1/cost | Get the cost per image check of the previously set parameters. The cost of the configuration is subtracted from the license key during each check.
[**get_license_info**](MiscellaneousOperationsApi.md#get_license_info) | **GET** /v1/info/{licenseKey} | Get information from given license key.


# **download_processed**
> file_type download_processed(filename)

Get the resulting media file.

### Example


```python
import time
import irisnet_client
from irisnet_client.api import miscellaneous_operations_api
from irisnet_client.model.in_error import INError
from pprint import pprint
# Defining the host is optional and defaults to https://api.irisnet.de
# See configuration.py for a list of all supported configuration parameters.
configuration = irisnet_client.Configuration(
    host = "https://api.irisnet.de"
)


# Enter a context with an instance of the API client
with irisnet_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = miscellaneous_operations_api.MiscellaneousOperationsApi(api_client)
    filename = "filename_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get the resulting media file.
        api_response = api_instance.download_processed(filename)
        pprint(api_response)
    except irisnet_client.ApiException as e:
        print("Exception when calling MiscellaneousOperationsApi->download_processed: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**|  |

### Return type

**file_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Specified file was not found. |  -  |
**200** | Returns the file AI produced file with masking or blurring, depending on given AI parameters. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_cost**
> int get_ai_cost()

Get the cost per image check of the previously set parameters. The cost of the configuration is subtracted from the license key during each check.

### Example


```python
import time
import irisnet_client
from irisnet_client.api import miscellaneous_operations_api
from irisnet_client.model.in_error import INError
from pprint import pprint
# Defining the host is optional and defaults to https://api.irisnet.de
# See configuration.py for a list of all supported configuration parameters.
configuration = irisnet_client.Configuration(
    host = "https://api.irisnet.de"
)


# Enter a context with an instance of the API client
with irisnet_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = miscellaneous_operations_api.MiscellaneousOperationsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the cost per image check of the previously set parameters. The cost of the configuration is subtracted from the license key during each check.
        api_response = api_instance.get_ai_cost()
        pprint(api_response)
    except irisnet_client.ApiException as e:
        print("Exception when calling MiscellaneousOperationsApi->get_ai_cost: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**429** | The ai could not handle the request because it is either overloaded or currently down for maintenance. This is a temporary state. A &#39;Retry-After&#39; Header is included in the response to signal the client to retry after a certain amount of seconds. |  -  |
**200** | Contains the cost of the AI check with the current set of parameters. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_info**
> LicenseInfo get_license_info(license_key)

Get information from given license key.

### Example


```python
import time
import irisnet_client
from irisnet_client.api import miscellaneous_operations_api
from irisnet_client.model.license_info import LicenseInfo
from irisnet_client.model.in_error import INError
from pprint import pprint
# Defining the host is optional and defaults to https://api.irisnet.de
# See configuration.py for a list of all supported configuration parameters.
configuration = irisnet_client.Configuration(
    host = "https://api.irisnet.de"
)


# Enter a context with an instance of the API client
with irisnet_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = miscellaneous_operations_api.MiscellaneousOperationsApi(api_client)
    license_key = "licenseKey_example" # str | License obtained from the https://irisnet.de/subscribe shop.

    # example passing only required values which don't have defaults set
    try:
        # Get information from given license key.
        api_response = api_instance.get_license_info(license_key)
        pprint(api_response)
    except irisnet_client.ApiException as e:
        print("Exception when calling MiscellaneousOperationsApi->get_license_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_key** | **str**| License obtained from the https://irisnet.de/subscribe shop. |

### Return type

[**LicenseInfo**](LicenseInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | The entered license key was not found. |  -  |
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

