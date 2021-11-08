# irisnet_client.EndpointsForAIChecksApi

All URIs are relative to *https://api.irisnet.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_image**](EndpointsForAIChecksApi.md#check_image) | **POST** /v1/check-image/{licenseKey} | Upload and check image against previously chosen configuration.
[**check_image_url**](EndpointsForAIChecksApi.md#check_image_url) | **POST** /v1/check-url/{licenseKey} | Check image url against previously chosen configuration.


# **check_image**
> IrisNet check_image(license_key, file)

Upload and check image against previously chosen configuration.

### Example


```python
import time
import irisnet_client
from irisnet_client.api import endpoints_for_ai_checks_api
from irisnet_client.model.in_error import INError
from irisnet_client.model.iris_net import IrisNet
from pprint import pprint
# Defining the host is optional and defaults to https://api.irisnet.de
# See configuration.py for a list of all supported configuration parameters.
configuration = irisnet_client.Configuration(
    host = "https://api.irisnet.de"
)


# Enter a context with an instance of the API client
with irisnet_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = endpoints_for_ai_checks_api.EndpointsForAIChecksApi(api_client)
    license_key = "licenseKey_example" # str | License obtained from irisnet.de shop.
    file = open('/path/to/file', 'rb') # file_type | 
    detail = 1 # int | Sets the response details.  * _1_ - The response body informs you if the image is ok or not ok (better API performance) * _2_ - In addition the response body lists all broken rules. * _3_ - In addition to the first two options, this will show all objects with positional information. (optional) if omitted the server will use the default value of 1
    image_encode = False # bool | Specifies whether or not to draw an output image that can be downloaded afterwards. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Upload and check image against previously chosen configuration.
        api_response = api_instance.check_image(license_key, file)
        pprint(api_response)
    except irisnet_client.ApiException as e:
        print("Exception when calling EndpointsForAIChecksApi->check_image: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload and check image against previously chosen configuration.
        api_response = api_instance.check_image(license_key, file, detail=detail, image_encode=image_encode)
        pprint(api_response)
    except irisnet_client.ApiException as e:
        print("Exception when calling EndpointsForAIChecksApi->check_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_key** | **str**| License obtained from irisnet.de shop. |
 **file** | **file_type**|  |
 **detail** | **int**| Sets the response details.  * _1_ - The response body informs you if the image is ok or not ok (better API performance) * _2_ - In addition the response body lists all broken rules. * _3_ - In addition to the first two options, this will show all objects with positional information. | [optional] if omitted the server will use the default value of 1
 **image_encode** | **bool**| Specifies whether or not to draw an output image that can be downloaded afterwards. | [optional] if omitted the server will use the default value of False

### Return type

[**IrisNet**](IrisNet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/xml, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**402** | Not enough credits |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_image_url**
> IrisNet check_image_url(url, license_key)

Check image url against previously chosen configuration.

### Example


```python
import time
import irisnet_client
from irisnet_client.api import endpoints_for_ai_checks_api
from irisnet_client.model.in_error import INError
from irisnet_client.model.iris_net import IrisNet
from pprint import pprint
# Defining the host is optional and defaults to https://api.irisnet.de
# See configuration.py for a list of all supported configuration parameters.
configuration = irisnet_client.Configuration(
    host = "https://api.irisnet.de"
)


# Enter a context with an instance of the API client
with irisnet_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = endpoints_for_ai_checks_api.EndpointsForAIChecksApi(api_client)
    url = "url_example" # str | 
    license_key = "licenseKey_example" # str | License obtained from irisnet.de shop.
    detail = 1 # int | Sets the response details.  * _1_ - The response body informs you if the image is ok or not ok (better API performance) * _2_ - In addition the response body lists all broken rules. * _3_ - In addition to the first two options, this will show all objects with positional information. (optional) if omitted the server will use the default value of 1
    image_encode = False # bool | Specifies whether or not to draw an output image that can be downloaded afterwards. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Check image url against previously chosen configuration.
        api_response = api_instance.check_image_url(url, license_key)
        pprint(api_response)
    except irisnet_client.ApiException as e:
        print("Exception when calling EndpointsForAIChecksApi->check_image_url: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Check image url against previously chosen configuration.
        api_response = api_instance.check_image_url(url, license_key, detail=detail, image_encode=image_encode)
        pprint(api_response)
    except irisnet_client.ApiException as e:
        print("Exception when calling EndpointsForAIChecksApi->check_image_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**|  |
 **license_key** | **str**| License obtained from irisnet.de shop. |
 **detail** | **int**| Sets the response details.  * _1_ - The response body informs you if the image is ok or not ok (better API performance) * _2_ - In addition the response body lists all broken rules. * _3_ - In addition to the first two options, this will show all objects with positional information. | [optional] if omitted the server will use the default value of 1
 **image_encode** | **bool**| Specifies whether or not to draw an output image that can be downloaded afterwards. | [optional] if omitted the server will use the default value of False

### Return type

[**IrisNet**](IrisNet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**402** | Not enough credits |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

