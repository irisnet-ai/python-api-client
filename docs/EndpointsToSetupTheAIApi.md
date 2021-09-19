# irisnet_client.EndpointsToSetupTheAIApi

All URIs are relative to *https://api.irisnet.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**set_in_define**](EndpointsToSetupTheAIApi.md#set_in_define) | **POST** /v1/set-definition | Set definitions via pre-defined prototypes.
[**set_in_params**](EndpointsToSetupTheAIApi.md#set_in_params) | **POST** /v1/set-parameters | Set the behaviour parameters for one object class.


# **set_in_define**
> set_in_define(in_define_ai)

Set definitions via pre-defined prototypes.

Each available prototype groups together a pre-defined set of parameters that will define the behaviour of the AI. This allows to configure multiple AI-checks per image. The image upload is only required once. Set the definition context with your needs in mind, credits are subtracted accordingly. See 'cost' endpoint for further information. Additionally you can overwrite specific parameters using 'set-parameters'. Any prior request to 'set-parameters' are invalidated when calling this request. This can also be used to reset the AI configuration.

### Example

```python
from __future__ import print_function
import time
import irisnet_client
from irisnet_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.irisnet.de
# See configuration.py for a list of all supported configuration parameters.
configuration = irisnet_client.Configuration(
    host = "https://api.irisnet.de"
)


# Enter a context with an instance of the API client
with irisnet_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = irisnet_client.EndpointsToSetupTheAIApi(api_client)
    in_define_ai = <?xml version="1.0" encoding="UTF-8"?>
<inDefineAI>
	<inImage proto="nudityCheck"/>
	<inImage proto="ageEstimation"/>
	<inImage proto="illegalSymbols"/>
	<inImage proto="attributesCheck"/>
	<inImage proto="textRecognition"/>
</inDefineAI> # INDefineAI | 

    try:
        # Set definitions via pre-defined prototypes.
        api_instance.set_in_define(in_define_ai)
    except ApiException as e:
        print("Exception when calling EndpointsToSetupTheAIApi->set_in_define: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **in_define_ai** | [**INDefineAI**](INDefineAI.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad request. Check for badly formatted request body. |  -  |
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_in_params**
> set_in_params(in_params)

Set the behaviour parameters for one object class.

Overwrites or extends the default configuration of the AI. By setting precise behaviour parameters, the AI can be fine tuned for specific use cases. To reset the parameters to their default values, make a post request to 'set-definition'.

### Example

```python
from __future__ import print_function
import time
import irisnet_client
from irisnet_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.irisnet.de
# See configuration.py for a list of all supported configuration parameters.
configuration = irisnet_client.Configuration(
    host = "https://api.irisnet.de"
)


# Enter a context with an instance of the API client
with irisnet_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = irisnet_client.EndpointsToSetupTheAIApi(api_client)
    in_params = <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<inParams>
	<inDefault thresh="0.5" grey="127"/>
	<inParam inClass="face" min="-1" max="-1" drawMode="0" grey="127"/>
	<inParam inClass="hand" min="-1" max="-1" drawMode="0" grey="127"/>
	<inParam inClass="breast" min="0" max="0" drawMode="2" grey="127"/>
	<inParam inClass="vulva" min="0" max="0" drawMode="2" grey="127"/>
	<inParam inClass="penis" min="0" max="0" drawMode="2" grey="127"/>
	<inParam inClass="vagina" min="0" max="0" drawMode="2" grey="127"/>
	<inParam inClass="buttocks" min="0" max="0" drawMode="2" grey="127"/>
	<inParam inClass="anus" min="0" max="0" drawMode="2" grey="127"/>
	<inParam inClass="toy" min="0" max="0" drawMode="2" grey="127"/>
	<inParam inClass="oral" min="0" max="0" drawMode="2" grey="127"/>
	<inParam inClass="penetration" min="0" max="0" drawMode="2" grey="127"/>
</inParams> # INParams | 

    try:
        # Set the behaviour parameters for one object class.
        api_instance.set_in_params(in_params)
    except ApiException as e:
        print("Exception when calling EndpointsToSetupTheAIApi->set_in_params: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **in_params** | [**INParams**](INParams.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad request. Check for badly formatted request body. |  -  |
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

