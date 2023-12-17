# irisnet_client.AICheckOperationsApi

All URIs are relative to *https://api.irisnet.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_image**](AICheckOperationsApi.md#check_image) | **POST** /v2/check-image/{configId} | Check an image with the AI.
[**check_stream**](AICheckOperationsApi.md#check_stream) | **POST** /v2/check-stream/{configId} | Check a stream with the AI.
[**check_video**](AICheckOperationsApi.md#check_video) | **POST** /v2/check-video/{configId} | Check a video with the AI.


# **check_image**
> CheckResult check_image(config_id, url=url, data=data, detail=detail, image_encode=image_encode)

Check an image with the AI.

The response (_CheckResult_ schema) is returned immediately after the request.

### Example

* Api Key Authentication (LICENSE-KEY):
```python
import time
import os
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
    url = 'url_example' # str | <s>The url to the image that needs to be checked.</s> Deprecated: Use 'data' parameter instead. <b>This parameter will be removed in future releases.</b> (optional)
    data = 'data_example' # str | The http(s) url or base64 encoded data uri of the image that needs to be checked. (optional)
    detail = 1 # int | Set the detail level of the response.  * _1_ - The response only contains the _Summary_ and possibly the _Encoded_ schemas for basic information's (better API performance). * _2_ - Additionally lists all broken rules (_BrokenRule_ schema) according to the configuration parameters that were requested. * _3_ - Also shows detections (e.g. _BaseDetection_ schema) that contains extended features to each found object. (optional) (default to 1)
    image_encode = False # bool | Specifies whether or not to draw an output image that will be delivered in the response body as base64 encoded string. The _Encoded_ schema will be available in the response. (optional) (default to False)

    try:
        # Check an image with the AI.
        api_response = api_instance.check_image(config_id, url=url, data=data, detail=detail, image_encode=image_encode)
        print("The response of AICheckOperationsApi->check_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AICheckOperationsApi->check_image: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| The configuration id from the Basic Configuration operations. | 
 **url** | **str**| &lt;s&gt;The url to the image that needs to be checked.&lt;/s&gt; Deprecated: Use &#39;data&#39; parameter instead. &lt;b&gt;This parameter will be removed in future releases.&lt;/b&gt; | [optional] 
 **data** | **str**| The http(s) url or base64 encoded data uri of the image that needs to be checked. | [optional] 
 **detail** | **int**| Set the detail level of the response.  * _1_ - The response only contains the _Summary_ and possibly the _Encoded_ schemas for basic information&#39;s (better API performance). * _2_ - Additionally lists all broken rules (_BrokenRule_ schema) according to the configuration parameters that were requested. * _3_ - Also shows detections (e.g. _BaseDetection_ schema) that contains extended features to each found object. | [optional] [default to 1]
 **image_encode** | **bool**| Specifies whether or not to draw an output image that will be delivered in the response body as base64 encoded string. The _Encoded_ schema will be available in the response. | [optional] [default to False]

### Return type

[**CheckResult**](CheckResult.md)

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
**402** | Not enough credits. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_stream**
> List[CheckResult] check_stream(config_id, in_url, out_url=out_url, cycle_length=cycle_length, check_rate=check_rate)

Check a stream with the AI.

The body is continuously send per JSON stream until completion of the video stream. Only then the full _CheckResult_ schema will be shown (past _Events_ omitted).  <b>NOTICE: Depending on your configuration and parameters this operation can be quite expensive on your credit balance.<b>  <b>WARNING: Please do not use the 'Try it out' for this operation. The browser is not able to refresh the response preview until the completion of the video stream.<b>

### Example

* Api Key Authentication (LICENSE-KEY):
```python
import time
import os
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
**404** | configId not found. |  -  |
**200** | successful operation. |  -  |
**402** | Not enough credits. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_video**
> check_video(config_id, url, config, detail=detail, image_encode=image_encode, check_rate=check_rate)

Check a video with the AI.

An empty response is returned immediately. The actual body (_CheckResult_ schema) is send to the _callbackUrl_ after the AI has finished processing.  <b>NOTICE: Depending on your configuration and parameters this operation can be quite expensive on your credit balance.<b>

### Example

* Api Key Authentication (LICENSE-KEY):
```python
import time
import os
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
    api_instance = irisnet_client.AICheckOperationsApi(api_client)
    config_id = 'config_id_example' # str | The configuration id from the Basic Configuration operations.
    url = 'url_example' # str | The url to the video that needs to be checked.
    config = {"callbackUrl":"http://www.example.com/callback?video","headers":{"Authorization":"Basic Rm9yemEgTmFwb2xpLCBzZW1wcmUh"}} # Config | 
    detail = 1 # int | Set the detail level of the response.  * _1_ - The response only contains the _Summary_ and possibly the _Encoded_ schemas for basic information's (better API performance). * _2_ - Additionally lists all broken rules (_BrokenRule_ schema) according to the configuration parameters that were requested. * _3_ - Also shows events (_Event_ schema) that contains extended features to each found object. (optional) (default to 1)
    image_encode = False # bool | Specifies whether or not to draw an output video that can be downloaded afterwards. The _Encoded_ schema will be available in the response. (optional) (default to False)
    check_rate = 0 # int | The milliseconds between each AI check. E.g. The AI will check 1 frame per second when checkRate is set to '1000'. (optional) (default to 0)

    try:
        # Check a video with the AI.
        api_instance.check_video(config_id, url, config, detail=detail, image_encode=image_encode, check_rate=check_rate)
    except Exception as e:
        print("Exception when calling AICheckOperationsApi->check_video: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| The configuration id from the Basic Configuration operations. | 
 **url** | **str**| The url to the video that needs to be checked. | 
 **config** | [**Config**](Config.md)|  | 
 **detail** | **int**| Set the detail level of the response.  * _1_ - The response only contains the _Summary_ and possibly the _Encoded_ schemas for basic information&#39;s (better API performance). * _2_ - Additionally lists all broken rules (_BrokenRule_ schema) according to the configuration parameters that were requested. * _3_ - Also shows events (_Event_ schema) that contains extended features to each found object. | [optional] [default to 1]
 **image_encode** | **bool**| Specifies whether or not to draw an output video that can be downloaded afterwards. The _Encoded_ schema will be available in the response. | [optional] [default to False]
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
**404** | configId not found. |  -  |
**202** | operation accepted: wait for callback. |  -  |
**402** | Not enough credits. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

