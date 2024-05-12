# irisnet-client
Artificial Intelligence (AI) for image- and video-processing in real-time. This is an interactive documentation where you can quickly look up the endpoints and their schemas, while having the opportunity to try things out for yourself.

In the list below, you can see the available endpoints of the API, which can be expanded by clicking on them. Each expanded endpoint lists the request parameters (if available) and the request body (if available). The request body can list some example bodies and the schema, explaining each model in detail.

Additionally you'll find a 'Try it out' button that allows you to enter your custom parameters and custom body and execute that against the API. <b>Be sure to enter your license key to authorize the requests before using this documentation interactively.</b>

The responses section in the expanded endpoint lists the possible responses with their corresponding status codes. If you've executed an API call it will also show you the response from the server.

Underneath the endpoints you'll find the model schemas. These are the models used for the requests and responses. If you click on the right arrow, you can expand the model and get a description of the model and the model parameters. For nested models, you can keep clicking the right arrow for further details.

Clicking the link below the title at the top of this page opens the [OpenAPI specification](https://swagger.io/specification/) (OAS3) in JSON format. The OAS3 Spec allows the generation of clients in many programming languages. There are several free client generators available that can be used to get started easily.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v2
- Package version: 3.5.5
- Generator version: 7.5.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://shop.airisprotect.com](https://shop.airisprotect.com)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import irisnet_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import irisnet_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    except ApiException as e:
        print("Exception when calling AICheckOperationsApi->check_image: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.irisnet.de*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AICheckOperationsApi* | [**check_image**](docs/AICheckOperationsApi.md#check_image) | **POST** /v2/check-image/{configId} | Check an image with the AI.
*AICheckOperationsApi* | [**check_stream**](docs/AICheckOperationsApi.md#check_stream) | **POST** /v2/check-stream/{configId} | Check a stream with the AI.
*AICheckOperationsApi* | [**check_video**](docs/AICheckOperationsApi.md#check_video) | **POST** /v2/check-video/{configId} | Check a video with the AI.
*BalanceEndpointsApi* | [**get_cost**](docs/BalanceEndpointsApi.md#get_cost) | **GET** /v2/cost/{configId} | Get the cost of the configuration for a single image.
*BalanceEndpointsApi* | [**get_license_info**](docs/BalanceEndpointsApi.md#get_license_info) | **GET** /v2/info/ | Get information for the given license key.
*BalanceEndpointsApi* | [**get_video_cost**](docs/BalanceEndpointsApi.md#get_video_cost) | **GET** /v2/cost/{configId}/{frames} | Get the cost of the configuration for moving images.
*BalanceEndpointsApi* | [**get_video_cost1**](docs/BalanceEndpointsApi.md#get_video_cost1) | **GET** /v2/cost/{configId}/{fps}/{duration} | Get the cost of the configuration for moving images.
*ConfigurationManagementApi* | [**delete_config**](docs/ConfigurationManagementApi.md#delete_config) | **DELETE** /v2/config/{configId} | Delete an AI configuration.
*ConfigurationManagementApi* | [**get_all_configs**](docs/ConfigurationManagementApi.md#get_all_configs) | **GET** /v2/config/ | List all saved AI configurations.
*ConfigurationManagementApi* | [**get_config**](docs/ConfigurationManagementApi.md#get_config) | **GET** /v2/config/{configId} | Get a specific AI configuration.
*ConfigurationManagementApi* | [**set_config**](docs/ConfigurationManagementApi.md#set_config) | **POST** /v2/config/ | Create a new AI configuration.
*DetailedConfigurationParametersApi* | [**clear_parameters**](docs/DetailedConfigurationParametersApi.md#clear_parameters) | **DELETE** /v2/config/parameters/{configId} | Delete the parameters of the AI configuration.
*DetailedConfigurationParametersApi* | [**get_parameters**](docs/DetailedConfigurationParametersApi.md#get_parameters) | **GET** /v2/config/parameters/{configId} | Get the parameters of the AI configuration.
*DetailedConfigurationParametersApi* | [**set_parameters**](docs/DetailedConfigurationParametersApi.md#set_parameters) | **POST** /v2/config/parameters/{configId} | Set parameters to the given AI configuration.


## Documentation For Models

 - [ApiNotice](docs/ApiNotice.md)
 - [BaseAttribute](docs/BaseAttribute.md)
 - [BaseDetection](docs/BaseDetection.md)
 - [BreastDetection](docs/BreastDetection.md)
 - [BrokenRule](docs/BrokenRule.md)
 - [Callback](docs/Callback.md)
 - [CheckResult](docs/CheckResult.md)
 - [CheckResultDetectionsInner](docs/CheckResultDetectionsInner.md)
 - [Config](docs/Config.md)
 - [Data](docs/Data.md)
 - [Encoded](docs/Encoded.md)
 - [Event](docs/Event.md)
 - [FaceDetection](docs/FaceDetection.md)
 - [HairAttribute](docs/HairAttribute.md)
 - [HairDetection](docs/HairDetection.md)
 - [IdDocumentAttribute](docs/IdDocumentAttribute.md)
 - [IdDocumentDetection](docs/IdDocumentDetection.md)
 - [IdDocumentSubChecks](docs/IdDocumentSubChecks.md)
 - [LicenseInfo](docs/LicenseInfo.md)
 - [Param](docs/Param.md)
 - [ParamSet](docs/ParamSet.md)
 - [Pricing](docs/Pricing.md)
 - [Summary](docs/Summary.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="LICENSE-KEY"></a>
### LICENSE-KEY

- **Type**: API key
- **API key parameter name**: LICENSE-KEY
- **Location**: HTTP header


## Author

info@irisnet.de


