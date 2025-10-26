# irisnet_client.AICheckOperationsApi

All URIs are relative to *https://api.irisnet.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**age_verification**](AICheckOperationsApi.md#age_verification) | **POST** /v2/age-verification/{configId} | Perform an age verfication check for a given selfie with the AI.
[**check_id_document**](AICheckOperationsApi.md#check_id_document) | **POST** /v2/check-id-document/{configId} | Check an id document with the AI.
[**check_image**](AICheckOperationsApi.md#check_image) | **POST** /v2/check-image/{configId} | Check an image with the AI.
[**check_poa_document**](AICheckOperationsApi.md#check_poa_document) | **POST** /v2/check-poa-document/{configId} | Perform an proof of address check with the AI.
[**check_stream**](AICheckOperationsApi.md#check_stream) | **POST** /v2/check-stream/{configId} | Check a stream with the AI.
[**check_text**](AICheckOperationsApi.md#check_text) | **POST** /v2/check-text/{configId} | Check a text with the AI.
[**check_video**](AICheckOperationsApi.md#check_video) | **POST** /v2/check-video/{configId} | Check a video with the AI.
[**face_authentication**](AICheckOperationsApi.md#face_authentication) | **POST** /v2/face-authentication/{configId} | Perform a face authentication for a given selfie with the AI.
[**live_document_check**](AICheckOperationsApi.md#live_document_check) | **POST** /v2/check-live-id-document/{configId} | Start a guided live id document check with the AI.


# **age_verification**
> CheckResult age_verification(config_id, biometric_check_request_data)

Perform an age verfication check for a given selfie with the AI.

The response (_CheckResult_ schema) containing only the checkId and possibly ApiNotices is returned immediately after the request. The actual body (_CheckResult_ schema) is sent to the _callbackUrl_ after the AI has finished processing.

### Example

* Api Key Authentication (LICENSE-KEY):

```python
import irisnet_client
from irisnet_client.models.biometric_check_request_data import BiometricCheckRequestData
from irisnet_client.models.check_result import CheckResult
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
    api_instance = irisnet_client.AICheckOperationsApi(api_client)
    config_id = 'config_id_example' # str | The configuration id from the Basic Configuration operations.
    biometric_check_request_data = {"callback":{"callbackUrl":"https://www.example.com/callback?ageestimation"},"selfieImage":"/9j/4AAQSkZJRgABAQEASABIAAD..."} # BiometricCheckRequestData | The BiometricCheckRequestData containing data needed for the age verification check.

    try:
        # Perform an age verfication check for a given selfie with the AI.
        api_response = api_instance.age_verification(config_id, biometric_check_request_data)
        print("The response of AICheckOperationsApi->age_verification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AICheckOperationsApi->age_verification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| The configuration id from the Basic Configuration operations. | 
 **biometric_check_request_data** | [**BiometricCheckRequestData**](BiometricCheckRequestData.md)| The BiometricCheckRequestData containing data needed for the age verification check. | 

### Return type

[**CheckResult**](CheckResult.md)

### Authorization

[LICENSE-KEY](../README.md#LICENSE-KEY)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Input accepted: Wait for callback. |  -  |
**402** | Not enough credits. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_id_document**
> CheckResult check_id_document(config_id, document_check_request_data)

Check an id document with the AI.

The response (_CheckResult_ schema) containing only the checkId and possibly ApiNotices is returned immediately after the request. The actual body (_CheckResult_ schema) is sent to the _callbackUrl_ after the AI has finished processing.

### Example

* Api Key Authentication (LICENSE-KEY):

```python
import irisnet_client
from irisnet_client.models.check_result import CheckResult
from irisnet_client.models.document_check_request_data import DocumentCheckRequestData
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
    api_instance = irisnet_client.AICheckOperationsApi(api_client)
    config_id = 'config_id_example' # str | The configuration id from the Basic Configuration operations.
    document_check_request_data = {"callback":{"callbackUrl":"https://www.example.com/callback?idcheck"},"documentCountry":"DE","documentType":"national_identity_card","frontImage":"/9j/4AAQSkZJRgABAQEASABIAAD...","backImage":"/9j/4AAQSkZJRgABAQEASABIAAD...","selfieImage":"/9j/4AAQSkZJRgABAQEASABIAAD..."} # DocumentCheckRequestData | The DocumentCheckRequestData containing data needed for the id document check.

    try:
        # Check an id document with the AI.
        api_response = api_instance.check_id_document(config_id, document_check_request_data)
        print("The response of AICheckOperationsApi->check_id_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AICheckOperationsApi->check_id_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| The configuration id from the Basic Configuration operations. | 
 **document_check_request_data** | [**DocumentCheckRequestData**](DocumentCheckRequestData.md)| The DocumentCheckRequestData containing data needed for the id document check. | 

### Return type

[**CheckResult**](CheckResult.md)

### Authorization

[LICENSE-KEY](../README.md#LICENSE-KEY)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Input accepted: Wait for callback. |  -  |
**402** | Not enough credits. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_image**
> CheckResult check_image(config_id, url=url, detail=detail, image_encode=image_encode, data=data)

Check an image with the AI.

The response (_CheckResult_ schema) is returned immediately after the request.

### Example

* Api Key Authentication (LICENSE-KEY):

```python
import irisnet_client
from irisnet_client.models.check_result import CheckResult
from irisnet_client.models.data import Data
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
    api_instance = irisnet_client.AICheckOperationsApi(api_client)
    config_id = 'config_id_example' # str | The configuration id from the Basic Configuration operations.
    url = 'url_example' # str | <s>The url to the image that needs to be checked.</s> Deprecated: Use request body instead. <b>This parameter will be removed in future releases.</b> (optional)
    detail = 1 # int | Set the detail level of the response.  * _1_ - The response only contains the _Summary_ and possibly the _Encoded_ schemas for basic information's (better API performance). * _2_ - Additionally lists all broken rules (_BrokenRule_ schema) according to the configuration parameters that were requested. * _3_ - Also shows detections (e.g. _BaseDetection_ schema) that contains extended features to each found object. (optional) (default to 1)
    image_encode = False # bool | Specifies whether or not to draw an output image that will be delivered in the response body as base64 encoded string. The _Encoded_ schema will be available in the response. (optional) (default to False)
    data = {"data":"https://example.com/path/to/your/image.png"} # Data | The http(s) url or base64 encoded body uri of the image that needs to be checked. (optional)

    try:
        # Check an image with the AI.
        api_response = api_instance.check_image(config_id, url=url, detail=detail, image_encode=image_encode, data=data)
        print("The response of AICheckOperationsApi->check_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AICheckOperationsApi->check_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| The configuration id from the Basic Configuration operations. | 
 **url** | **str**| &lt;s&gt;The url to the image that needs to be checked.&lt;/s&gt; Deprecated: Use request body instead. &lt;b&gt;This parameter will be removed in future releases.&lt;/b&gt; | [optional] 
 **detail** | **int**| Set the detail level of the response.  * _1_ - The response only contains the _Summary_ and possibly the _Encoded_ schemas for basic information&#39;s (better API performance). * _2_ - Additionally lists all broken rules (_BrokenRule_ schema) according to the configuration parameters that were requested. * _3_ - Also shows detections (e.g. _BaseDetection_ schema) that contains extended features to each found object. | [optional] [default to 1]
 **image_encode** | **bool**| Specifies whether or not to draw an output image that will be delivered in the response body as base64 encoded string. The _Encoded_ schema will be available in the response. | [optional] [default to False]
 **data** | [**Data**](Data.md)| The http(s) url or base64 encoded body uri of the image that needs to be checked. | [optional] 

### Return type

[**CheckResult**](CheckResult.md)

### Authorization

[LICENSE-KEY](../README.md#LICENSE-KEY)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation. |  -  |
**402** | Not enough credits. |  -  |
**404** | configId not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_poa_document**
> CheckResult check_poa_document(config_id, poa_check_request_data)

Perform an proof of address check with the AI.

The response (_CheckResult_ schema) containing only the checkId and possibly ApiNotices is returned immediately after the request. The actual body (_CheckResult_ schema) is sent to the _callbackUrl_ after the AI has finished processing.

### Example

* Api Key Authentication (LICENSE-KEY):

```python
import irisnet_client
from irisnet_client.models.check_result import CheckResult
from irisnet_client.models.poa_check_request_data import PoaCheckRequestData
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
    api_instance = irisnet_client.AICheckOperationsApi(api_client)
    config_id = 'config_id_example' # str | The configuration id from the Basic Configuration operations.
    poa_check_request_data = {"callback":{"callbackUrl":"https://www.example.com/callback?poacheck"},"documentType":"utility_bill","frontImage":"/9j/4AAQSkZJRgABAQEASABIAAD..."} # PoaCheckRequestData | The PoaCheckRequestData containing data needed for the proof of address check. The DocumentType in the request data must be either 'utility_bill' or 'bank_statement'.

    try:
        # Perform an proof of address check with the AI.
        api_response = api_instance.check_poa_document(config_id, poa_check_request_data)
        print("The response of AICheckOperationsApi->check_poa_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AICheckOperationsApi->check_poa_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| The configuration id from the Basic Configuration operations. | 
 **poa_check_request_data** | [**PoaCheckRequestData**](PoaCheckRequestData.md)| The PoaCheckRequestData containing data needed for the proof of address check. The DocumentType in the request data must be either &#39;utility_bill&#39; or &#39;bank_statement&#39;. | 

### Return type

[**CheckResult**](CheckResult.md)

### Authorization

[LICENSE-KEY](../README.md#LICENSE-KEY)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Input accepted: Wait for callback. |  -  |
**402** | Not enough credits. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_stream**
> List[CheckResult] check_stream(config_id, in_url, out_url=out_url, cycle_length=cycle_length, check_rate=check_rate)

Check a stream with the AI.

The body is continuously send per JSON stream until completion of the video stream. Only then the full _CheckResult_ schema will be shown (past _Events_ omitted).

<b>NOTICE: Depending on your configuration and parameters this operation can be quite expensive on your credit balance.<b>

<b>WARNING: Please do not use the 'Try it out' for this operation. The browser is not able to refresh the response preview until the completion of the video stream.<b>

### Example

* Api Key Authentication (LICENSE-KEY):

```python
import irisnet_client
from irisnet_client.models.check_result import CheckResult
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
    api_instance = irisnet_client.AICheckOperationsApi(api_client)
    config_id = 'config_id_example' # str | The configuration id from the Basic Configuration operations.
    in_url = 'in_url_example' # str | The URL of the video stream that the AI should check.
    out_url = 'out_url_example' # str | The URL of where the AI should send the encoded stream. (optional)
    cycle_length = 500 # int | Determine how often (value in milliseconds) the the AI should give a feedback. (optional) (default to 500)
    check_rate = 0 # int | The milliseconds between each AI check. E.g. The AI will check 1 frame per second when checkRate is set to '1000'. (optional) (default to 0)

    try:
        # Check a stream with the AI.
        api_response = api_instance.check_stream(config_id, in_url, out_url=out_url, cycle_length=cycle_length, check_rate=check_rate)
        print("The response of AICheckOperationsApi->check_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AICheckOperationsApi->check_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| The configuration id from the Basic Configuration operations. | 
 **in_url** | **str**| The URL of the video stream that the AI should check. | 
 **out_url** | **str**| The URL of where the AI should send the encoded stream. | [optional] 
 **cycle_length** | **int**| Determine how often (value in milliseconds) the the AI should give a feedback. | [optional] [default to 500]
 **check_rate** | **int**| The milliseconds between each AI check. E.g. The AI will check 1 frame per second when checkRate is set to &#39;1000&#39;. | [optional] [default to 0]

### Return type

[**List[CheckResult]**](CheckResult.md)

### Authorization

[LICENSE-KEY](../README.md#LICENSE-KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-ndjson

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation. |  -  |
**402** | Not enough credits. |  -  |
**404** | configId not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_text**
> CheckResult check_text(config_id, data, detail=detail)

Check a text with the AI.

The response (_CheckResult_ schema) is returned immediately after the request.

### Example

* Api Key Authentication (LICENSE-KEY):

```python
import irisnet_client
from irisnet_client.models.check_result import CheckResult
from irisnet_client.models.data import Data
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
    api_instance = irisnet_client.AICheckOperationsApi(api_client)
    config_id = 'config_id_example' # str | The configuration id from the Basic Configuration operations.
    data = {"data":"This is an example text."} # Data | The text that needs to be checked.
    detail = 1 # int | Set the detail level of the response.  * _1_ - The response only contains the _Summary_ and possibly the _Encoded_ schemas for basic information's (better API performance). * _2_ - Additionally lists all broken rules (_BrokenRule_ schema) according to the configuration parameters that were requested. * _3_ - Also shows detections (e.g. _BaseDetection_ schema) that contains extended features to each found object. (optional) (default to 1)

    try:
        # Check a text with the AI.
        api_response = api_instance.check_text(config_id, data, detail=detail)
        print("The response of AICheckOperationsApi->check_text:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AICheckOperationsApi->check_text: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| The configuration id from the Basic Configuration operations. | 
 **data** | [**Data**](Data.md)| The text that needs to be checked. | 
 **detail** | **int**| Set the detail level of the response.  * _1_ - The response only contains the _Summary_ and possibly the _Encoded_ schemas for basic information&#39;s (better API performance). * _2_ - Additionally lists all broken rules (_BrokenRule_ schema) according to the configuration parameters that were requested. * _3_ - Also shows detections (e.g. _BaseDetection_ schema) that contains extended features to each found object. | [optional] [default to 1]

### Return type

[**CheckResult**](CheckResult.md)

### Authorization

[LICENSE-KEY](../README.md#LICENSE-KEY)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation. |  -  |
**402** | Not enough credits. |  -  |
**404** | configId not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_video**
> check_video(config_id, url, callback, detail=detail, image_encode=image_encode, check_rate=check_rate)

Check a video with the AI.

An empty response is returned immediately. The actual body (_CheckResult_ schema) is send to the _callbackUrl_ after the AI has finished processing.

<b>NOTICE: Depending on your configuration and parameters this operation can be quite expensive on your credit balance.<b>

### Example

* Api Key Authentication (LICENSE-KEY):

```python
import irisnet_client
from irisnet_client.models.callback import Callback
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
    api_instance = irisnet_client.AICheckOperationsApi(api_client)
    config_id = 'config_id_example' # str | The configuration id from the Basic Configuration operations.
    url = 'url_example' # str | The url to the video that needs to be checked.
    callback = {"callbackUrl":"http://www.example.com/callback?video","headers":{"Authorization":"Basic Rm9yemEgTmFwb2xpLCBzZW1wcmUh"}} # Callback | 
    detail = 1 # int | Set the detail level of the response.  * _1_ - The response only contains the _Summary_ and possibly the _Encoded_ schemas for basic information's (better API performance). * _2_ - Additionally lists all broken rules (_BrokenRule_ schema) according to the configuration parameters that were requested. * _3_ - Also shows events (_Event_ schema) that contains extended features to each found object. (optional) (default to 1)
    image_encode = False # bool | Specifies whether or not to draw an output video that can be downloaded afterwards. The output video format will be MP4 containing H.264 encoding independent of the input format. The _Encoded_ schema will be available in the response. (optional) (default to False)
    check_rate = 0 # int | The milliseconds between each AI check. E.g. The AI will check 1 frame per second when checkRate is set to '1000'. (optional) (default to 0)

    try:
        # Check a video with the AI.
        api_instance.check_video(config_id, url, callback, detail=detail, image_encode=image_encode, check_rate=check_rate)
    except Exception as e:
        print("Exception when calling AICheckOperationsApi->check_video: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| The configuration id from the Basic Configuration operations. | 
 **url** | **str**| The url to the video that needs to be checked. | 
 **callback** | [**Callback**](Callback.md)|  | 
 **detail** | **int**| Set the detail level of the response.  * _1_ - The response only contains the _Summary_ and possibly the _Encoded_ schemas for basic information&#39;s (better API performance). * _2_ - Additionally lists all broken rules (_BrokenRule_ schema) according to the configuration parameters that were requested. * _3_ - Also shows events (_Event_ schema) that contains extended features to each found object. | [optional] [default to 1]
 **image_encode** | **bool**| Specifies whether or not to draw an output video that can be downloaded afterwards. The output video format will be MP4 containing H.264 encoding independent of the input format. The _Encoded_ schema will be available in the response. | [optional] [default to False]
 **check_rate** | **int**| The milliseconds between each AI check. E.g. The AI will check 1 frame per second when checkRate is set to &#39;1000&#39;. | [optional] [default to 0]

### Return type

void (empty response body)

### Authorization

[LICENSE-KEY](../README.md#LICENSE-KEY)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | operation accepted: wait for callback. |  -  |
**402** | Not enough credits. |  -  |
**404** | configId not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **face_authentication**
> CheckResult face_authentication(config_id, biometric_check_request_data)

Perform a face authentication for a given selfie with the AI.

The response (_CheckResult_ schema) containing only the checkId and possibly ApiNotices is returned immediately after the request. The actual body (_CheckResult_ schema) is sent to the _callbackUrl_ after the AI has finished processing.

### Example

* Api Key Authentication (LICENSE-KEY):

```python
import irisnet_client
from irisnet_client.models.biometric_check_request_data import BiometricCheckRequestData
from irisnet_client.models.check_result import CheckResult
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
    api_instance = irisnet_client.AICheckOperationsApi(api_client)
    config_id = 'config_id_example' # str | The configuration id from the Basic Configuration operations.
    biometric_check_request_data = {"callback":{"callbackUrl":"https://www.example.com/callback?ageestimation"},"selfieImage":"/9j/4AAQSkZJRgABAQEASABIAAD..."} # BiometricCheckRequestData | The BiometricCheckRequestData containing data needed for the face authentication.

    try:
        # Perform a face authentication for a given selfie with the AI.
        api_response = api_instance.face_authentication(config_id, biometric_check_request_data)
        print("The response of AICheckOperationsApi->face_authentication:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AICheckOperationsApi->face_authentication: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| The configuration id from the Basic Configuration operations. | 
 **biometric_check_request_data** | [**BiometricCheckRequestData**](BiometricCheckRequestData.md)| The BiometricCheckRequestData containing data needed for the face authentication. | 

### Return type

[**CheckResult**](CheckResult.md)

### Authorization

[LICENSE-KEY](../README.md#LICENSE-KEY)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Input accepted: Wait for callback. |  -  |
**402** | Not enough credits. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **live_document_check**
> LiveDocumentCheckResponseData live_document_check(config_id, live_document_check_request_data)

Start a guided live id document check with the AI.

The synchronous response (_LiveDocumentCheckResponseData_ schema) contains an eventId, possibly a token and an URL to send the enduser to. The actual result (_CheckResult_ schema) of the document check is sent to the provided _callbackUrl_ after the AI has finished processing.

### Example

* Api Key Authentication (LICENSE-KEY):

```python
import irisnet_client
from irisnet_client.models.live_document_check_request_data import LiveDocumentCheckRequestData
from irisnet_client.models.live_document_check_response_data import LiveDocumentCheckResponseData
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
    api_instance = irisnet_client.AICheckOperationsApi(api_client)
    config_id = 'config_id_example' # str | The configuration id from the Basic Configuration operations.
    live_document_check_request_data = {"callback":{"callbackUrl":"https://www.example.com/callback?liveident"},"endUserRedirectUrl":"https://www.example.com/user"} # LiveDocumentCheckRequestData | The LiveDocumentCheckRequestData containing data needed for the live id document check.

    try:
        # Start a guided live id document check with the AI.
        api_response = api_instance.live_document_check(config_id, live_document_check_request_data)
        print("The response of AICheckOperationsApi->live_document_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AICheckOperationsApi->live_document_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| The configuration id from the Basic Configuration operations. | 
 **live_document_check_request_data** | [**LiveDocumentCheckRequestData**](LiveDocumentCheckRequestData.md)| The LiveDocumentCheckRequestData containing data needed for the live id document check. | 

### Return type

[**LiveDocumentCheckResponseData**](LiveDocumentCheckResponseData.md)

### Authorization

[LICENSE-KEY](../README.md#LICENSE-KEY)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Input accepted: Send enduser to endUserIdentUrl and wait for status/callback. |  -  |
**402** | Not enough credits. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

