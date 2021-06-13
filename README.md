# irisnet-client
Artificial Intelligence (AI) for image- and video-processing in realtime. This is an interactive documentation meant to give a place were you can quickly look up the endpoints and their schemas, while also giving you the option to try things out yourself.

Listed below you'll see the available endpoints of the API that can be expanded by clicking on it. Each expanded endpoint lists the request parameter (if available) and the request body (if available). The request body can list some example bodies and the schema, explaining each model in detail. Additionally you'll find a 'Try it out' button where you can type in your custom parameters and custom body and execute that against the API.
The responses section in the expanded endpoint lists the possible responses with their corresponding status codes. If you've executed an API call it will also show you the response from the server.

Underneath the endpoints you'll find the model schemas. These are the models used for the requests and responses.By clicking on the right arrow you can expand the model and it will show you a description of the model and the model parameters. For nested models you can keep clicking the right arrow to reveal further details on it.



This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 2.2.3
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

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

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
with irisnet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = irisnet_client.EndpointsForAIChecksApi(api_client)
    license_key = 'license_key_example' # str | License obtained from irisnet.de shop.
file = '/path/to/file' # file | 
detail = 1 # int | Sets the response details.  * _1_ - The response body informs you if the image is ok or not ok (better API performance) * _2_ - In addition the response body lists all broken rules. * _3_ - In addition to the first two options, this will show all objects with positional information. (optional) (default to 1)

    try:
        # Upload and check image against previously chosen configuration.
        api_response = api_instance.check_image(license_key, file, detail=detail)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EndpointsForAIChecksApi->check_image: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *https://api.irisnet.de*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*EndpointsForAIChecksApi* | [**check_image**](docs/EndpointsForAIChecksApi.md#check_image) | **POST** /v1/check-image/{licenseKey} | Upload and check image against previously chosen configuration.
*EndpointsForAIChecksApi* | [**check_image_url**](docs/EndpointsForAIChecksApi.md#check_image_url) | **POST** /v1/check-url/{licenseKey} | Check image url against previously chosen configuration.
*EndpointsToSetupTheAIApi* | [**set_in_define**](docs/EndpointsToSetupTheAIApi.md#set_in_define) | **POST** /v1/set-definition | Set definitions via pre-defined prototypes.
*EndpointsToSetupTheAIApi* | [**set_in_params**](docs/EndpointsToSetupTheAIApi.md#set_in_params) | **POST** /v1/set-parameters | Set the behaviour parameters for one object class.
*MiscellaneousOperationsApi* | [**download_processed**](docs/MiscellaneousOperationsApi.md#download_processed) | **GET** /v1/download/{filename} | Get the resulting media file.
*MiscellaneousOperationsApi* | [**get_ai_cost**](docs/MiscellaneousOperationsApi.md#get_ai_cost) | **GET** /v1/cost | Get the cost per image check of the previously set parameters. The cost of the configuration is subtracted from the license key during each check.
*MiscellaneousOperationsApi* | [**get_license_info**](docs/MiscellaneousOperationsApi.md#get_license_info) | **GET** /v1/info/{licenseKey} | Get information from given license key.


## Documentation For Models

 - [INDefault](docs/INDefault.md)
 - [INDefineAI](docs/INDefineAI.md)
 - [INError](docs/INError.md)
 - [INImage](docs/INImage.md)
 - [INObject](docs/INObject.md)
 - [INParam](docs/INParam.md)
 - [INParams](docs/INParams.md)
 - [INRule](docs/INRule.md)
 - [InlineObject](docs/InlineObject.md)
 - [IrisNet](docs/IrisNet.md)
 - [LicenseInfo](docs/LicenseInfo.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




