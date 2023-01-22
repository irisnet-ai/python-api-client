# irisnet-client
Artificial Intelligence (AI) for image- and video-processing in real-time. This is an interactive documentation where you can quickly look up the endpoints and their schemas, while having the opportunity to try things out for yourself.

In the list below, you can see the available endpoints of the API, which can be expanded by clicking on them. Each expanded endpoint lists the request parameters (if available) and the request body (if available). The request body can list some example bodies and the schema, explaining each model in detail.

Additionally you'll find a 'Try it out' button that allows you to enter your custom parameters and custom body and execute that against the API. <b>Be sure to enter your license key to authorize the requests before using this documentation interactively.</b>

The responses section in the expanded endpoint lists the possible responses with their corresponding status codes. If you've executed an API call it will also show you the response from the server.

Underneath the endpoints you'll find the model schemas. These are the models used for the requests and responses. If you click on the right arrow, you can expand the model and get a description of the model and the model parameters. For nested models, you can keep clicking the right arrow for further details.

Clicking the link below the title at the top of this page opens the [OpenAPI specification](https://swagger.io/specification/) (OAS3) in JSON format. The OAS3 Spec allows the generation of clients in many programming languages. There are several free client generators available that can be used to get started easily.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v2
- Package version: 3.0.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://irisnet.de/subscribe/](https://irisnet.de/subscribe/)

## Requirements.

Python &gt;&#x3D;3.7

## Migration from other generators like python and python-legacy

### Changes
1. This generator uses spec case for all (object) property names and parameter names.
    - So if the spec has a property name like camelCase, it will use camelCase rather than camel_case
    - So you will need to update how you input and read properties to use spec case
2. Endpoint parameters are stored in dictionaries to prevent collisions (explanation below)
    - So you will need to update how you pass data in to endpoints
3. Endpoint responses now include the original response, the deserialized response body, and (todo)the deserialized headers
    - So you will need to update your code to use response.body to access deserialized data
4. All validated data is instantiated in an instance that subclasses all validated Schema classes and Decimal/str/list/tuple/frozendict/NoneClass/BoolClass/bytes/io.FileIO
    - This means that you can use isinstance to check if a payload validated against a schema class
    - This means that no data will be of type None/True/False
        - ingested None will subclass NoneClass
        - ingested True will subclass BoolClass
        - ingested False will subclass BoolClass
        - So if you need to check is True/False/None, instead use instance.is_true_oapg()/.is_false_oapg()/.is_none_oapg()
5. All validated class instances are immutable except for ones based on io.File
    - This is because if properties were changed after validation, that validation would no longer apply
    - So no changing values or property values after a class has been instantiated
6. String + Number types with formats
    - String type data is stored as a string and if you need to access types based on its format like date,
    date-time, uuid, number etc then you will need to use accessor functions on the instance
    - type string + format: See .as_date_oapg, .as_datetime_oapg, .as_decimal_oapg, .as_uuid_oapg
    - type number + format: See .as_float_oapg, .as_int_oapg
    - this was done because openapi/json-schema defines constraints. string data may be type string with no format
    keyword in one schema, and include a format constraint in another schema
    - So if you need to access a string format based type, use as_date_oapg/as_datetime_oapg/as_decimal_oapg/as_uuid_oapg
    - So if you need to access a number format based type, use as_int_oapg/as_float_oapg
7. Property access on AnyType(type unset) or object(dict) schemas
    - Only required keys with valid python names are properties like .someProp and have type hints
    - All optional keys may not exist, so properties are not defined for them
    - One can access optional values with dict_instance['optionalProp'] and KeyError will be raised if it does not exist
    - Use get_item_oapg if you need a way to always get a value whether or not the key exists
        - If the key does not exist, schemas.unset is returned from calling dict_instance.get_item_oapg('optionalProp')
        - All required and optional keys have type hints for this method, and @typing.overload is used
        - A type hint is also generated for additionalProperties accessed using this method
    - So you will need to update you code to use some_instance['optionalProp'] to access optional property
    and additionalProperty values
8. The location of the api classes has changed
    - Api classes are located in your_package.apis.tags.some_api
    - This change was made to eliminate redundant code generation
    - Legacy generators generated the same endpoint twice if it had > 1 tag on it
    - This generator defines an endpoint in one class, then inherits that class to generate
      apis by tags and by paths
    - This change reduces code and allows quicker run time if you use the path apis
        - path apis are at your_package.apis.paths.some_path
    - Those apis will only load their needed models, which is less to load than all of the resources needed in a tag api
    - So you will need to update your import paths to the api classes

### Why are Oapg and _oapg used in class and method names?
Classes can have arbitrarily named properties set on them
Endpoints can have arbitrary operationId method names set
For those reasons, I use the prefix Oapg and _oapg to greatly reduce the likelihood of collisions
on protected + public classes/methods.
oapg stands for OpenApi Python Generator.

### Object property spec case
This was done because when payloads are ingested, they can be validated against N number of schemas.
If the input signature used a different property name then that has mutated the payload.
So SchemaA and SchemaB must both see the camelCase spec named variable.
Also it is possible to send in two properties, named camelCase and camel_case in the same payload.
That use case should be support so spec case is used.

### Parameter spec case
Parameters can be included in different locations including:
- query
- path
- header
- cookie

Any of those parameters could use the same parameter names, so if every parameter
was included as an endpoint parameter in a function signature, they would collide.
For that reason, each of those inputs have been separated out into separate typed dictionaries:
- query_params
- path_params
- header_params
- cookie_params

So when updating your code, you will need to pass endpoint parameters in using those
dictionaries.

### Endpoint responses
Endpoint responses have been enriched to now include more information.
Any response reom an endpoint will now include the following properties:
response: urllib3.HTTPResponse
body: typing.Union[Unset, Schema]
headers: typing.Union[Unset, TODO]
Note: response header deserialization has not yet been added


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

import time
import irisnet_client
from pprint import pprint
from irisnet_client.apis.tags import ai_check_operations_api
from irisnet_client.model.api_notice import ApiNotice
from irisnet_client.model.callback import Callback
from irisnet_client.model.check_result import CheckResult
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
configuration.api_key['LICENSE-KEY'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['LICENSE-KEY'] = 'Bearer'

# Enter a context with an instance of the API client
with irisnet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ai_check_operations_api.AICheckOperationsApi(api_client)
    config_id = "configId_example" # str | The configuration id from the Basic Configuration operations.
url = "url_example" # str | The url to the image that needs to be checked.
detail = 1 # int | Set the detail level of the response.  * _1_ - The response only contains the _Summary_ and possibly the _Encoded_ schemas for basic information's (better API performance). * _2_ - Additionally lists all broken rules (_BrokenRule_ schema) according to the configuration parameters that were requested. * _3_ - Also shows detections (e.g. _BaseDetection_ schema) that contains extended features to each found object. (optional) (default to CodegenParameter{isFormParam=false, isQueryParam=true, isPathParam=false, isHeaderParam=false, isCookieParam=false, isBodyParam=false, isContainer=false, isCollectionFormatMulti=false, isPrimitiveType=true, isModel=false, isExplode=true, baseName='detail', paramName='detail', dataType='int', datatypeWithEnum='null', dataFormat='int32', collectionFormat='null', description='Set the detail level of the response.  * _1_ - The response only contains the _Summary_ and possibly the _Encoded_ schemas for basic information's (better API performance). * _2_ - Additionally lists all broken rules (_BrokenRule_ schema) according to the configuration parameters that were requested. * _3_ - Also shows detections (e.g. _BaseDetection_ schema) that contains extended features to each found object.', unescapedDescription='Set the detail level of the response.
 * _1_ - The response only contains the _Summary_ and possibly the _Encoded_ schemas for basic information's (better API performance).
* _2_ - Additionally lists all broken rules (_BrokenRule_ schema) according to the configuration parameters that were requested.
* _3_ - Also shows detections (e.g. _BaseDetection_ schema) that contains extended features to each found object.', baseType='null', defaultValue='1', enumDefaultValue='null', enumName='null', style='FORM', deepObject='false', allowEmptyValue='false', example='1', jsonSchema='{
  "name" : "detail",
  "in" : "query",
  "description" : "Set the detail level of the response.\n * _1_ - The response only contains the _Summary_ and possibly the _Encoded_ schemas for basic information's (better API performance).\n* _2_ - Additionally lists all broken rules (_BrokenRule_ schema) according to the configuration parameters that were requested.\n* _3_ - Also shows detections (e.g. _BaseDetection_ schema) that contains extended features to each found object.",
  "required" : false,
  "style" : "form",
  "explode" : true,
  "schema" : {
    "maximum" : 3,
    "minimum" : 0,
    "type" : "integer",
    "format" : "int32",
    "default" : 1
  }
}', isString=false, isNumeric=false, isInteger=true, isShort=true, isLong=false, isUnboundedInteger=false, isNumber=false, isFloat=false, isDouble=false, isDecimal=false, isByteArray=false, isBinary=false, isBoolean=false, isDate=false, isDateTime=false, isUuid=false, isUri=false, isEmail=false, isFreeFormObject=false, isAnyType=false, isArray=false, isMap=false, isFile=false, isEnum=false, _enum=null, allowableValues=null, items=null, mostInnerItems=null, additionalProperties=null, vars=[], requiredVars=[], vendorExtensions={}, hasValidation=true, maxProperties=null, minProperties=null, isNullable=false, isDeprecated=false, required=false, maximum='3', exclusiveMaximum=false, minimum='0', exclusiveMinimum=false, maxLength=null, minLength=null, pattern='null', maxItems=null, minItems=null, uniqueItems=false, uniqueItemsBoolean=null, contentType=null, multipleOf=null, isNull=false, getAdditionalPropertiesIsAnyType=false, getHasVars=false, getHasRequired=false, getHasDiscriminatorWithNonEmptyMapping=false, composedSchemas=null, hasMultipleTypes=false, schema=CodegenProperty{openApiType='integer', baseName='DetailSchema', complexType='null', getter='getDetail', setter='setDetail', description='null', dataType='int', datatypeWithEnum='int', dataFormat='int32', name='detail', min='null', max='null', defaultValue='1', defaultValueWithParam=' = data.detail;', baseType='int', containerType='null', title='null', unescapedDescription='null', maxLength=null, minLength=null, pattern='null', example='1', jsonSchema='{
  "maximum" : 3,
  "minimum" : 0,
  "type" : "integer",
  "format" : "int32",
  "default" : 1
}', minimum='0', maximum='3', exclusiveMinimum=false, exclusiveMaximum=false, required=false, deprecated=false, hasMoreNonReadOnly=false, isPrimitiveType=true, isModel=false, isContainer=false, isString=false, isNumeric=false, isInteger=true, isShort=false, isLong=false, isUnboundedInteger=false, isNumber=false, isFloat=false, isDouble=false, isDecimal=false, isByteArray=false, isBinary=false, isFile=false, isBoolean=false, isDate=false, isDateTime=false, isUuid=false, isUri=false, isEmail=false, isFreeFormObject=false, isArray=false, isMap=false, isEnum=false, isInnerEnum=false, isAnyType=false, isReadOnly=false, isWriteOnly=false, isNullable=false, isSelfReference=false, isCircularReference=false, isDiscriminator=false, _enum=null, allowableValues=null, items=null, additionalProperties=null, vars=[], requiredVars=[], mostInnerItems=null, vendorExtensions={}, hasValidation=true, isInherited=false, discriminatorValue='null', nameInCamelCase='Detail', nameInSnakeCase='null', enumName='null', maxItems=null, minItems=null, maxProperties=null, minProperties=null, uniqueItems=false, uniqueItemsBoolean=null, multipleOf=null, isXmlAttribute=false, xmlPrefix='null', xmlName='null', xmlNamespace='null', isXmlWrapped=false, isNull=false, getAdditionalPropertiesIsAnyType=false, getHasVars=false, getHasRequired=false, getHasDiscriminatorWithNonEmptyMapping=false, composedSchemas=null, hasMultipleTypes=false, requiredVarsMap=null, ref=null, schemaIsFromAdditionalProperties=false, isBooleanSchemaTrue=false, isBooleanSchemaFalse=false, format=int32, dependentRequired=null, contains=null}, content=null, requiredVarsMap=null, ref=null, schemaIsFromAdditionalProperties=false})
image_encode = False # bool | Specifies whether or not to draw an output image that will be delivered in the response body as base64 encoded string. The _Encoded_ schema will be available in the response. (optional) (default to CodegenParameter{isFormParam=false, isQueryParam=true, isPathParam=false, isHeaderParam=false, isCookieParam=false, isBodyParam=false, isContainer=false, isCollectionFormatMulti=false, isPrimitiveType=true, isModel=false, isExplode=true, baseName='imageEncode', paramName='image_encode', dataType='bool', datatypeWithEnum='null', dataFormat='null', collectionFormat='null', description='Specifies whether or not to draw an output image that will be delivered in the response body as base64 encoded string. The _Encoded_ schema will be available in the response.', unescapedDescription='Specifies whether or not to draw an output image that will be delivered in the response body as base64 encoded string. The _Encoded_ schema will be available in the response.', baseType='null', defaultValue='False', enumDefaultValue='null', enumName='null', style='FORM', deepObject='false', allowEmptyValue='false', example='False', jsonSchema='{
  "name" : "imageEncode",
  "in" : "query",
  "description" : "Specifies whether or not to draw an output image that will be delivered in the response body as base64 encoded string. The _Encoded_ schema will be available in the response.",
  "required" : false,
  "style" : "form",
  "explode" : true,
  "schema" : {
    "type" : "boolean",
    "default" : false
  }
}', isString=false, isNumeric=false, isInteger=false, isShort=false, isLong=false, isUnboundedInteger=false, isNumber=false, isFloat=false, isDouble=false, isDecimal=false, isByteArray=false, isBinary=false, isBoolean=true, isDate=false, isDateTime=false, isUuid=false, isUri=false, isEmail=false, isFreeFormObject=false, isAnyType=false, isArray=false, isMap=false, isFile=false, isEnum=false, _enum=null, allowableValues=null, items=null, mostInnerItems=null, additionalProperties=null, vars=[], requiredVars=[], vendorExtensions={}, hasValidation=false, maxProperties=null, minProperties=null, isNullable=false, isDeprecated=false, required=false, maximum='null', exclusiveMaximum=false, minimum='null', exclusiveMinimum=false, maxLength=null, minLength=null, pattern='null', maxItems=null, minItems=null, uniqueItems=false, uniqueItemsBoolean=null, contentType=null, multipleOf=null, isNull=false, getAdditionalPropertiesIsAnyType=false, getHasVars=false, getHasRequired=false, getHasDiscriminatorWithNonEmptyMapping=false, composedSchemas=null, hasMultipleTypes=false, schema=CodegenProperty{openApiType='boolean', baseName='ImageEncodeSchema', complexType='null', getter='getImageEncode', setter='setImageEncode', description='null', dataType='bool', datatypeWithEnum='bool', dataFormat='null', name='image_encode', min='null', max='null', defaultValue='False', defaultValueWithParam=' = data.imageEncode;', baseType='bool', containerType='null', title='null', unescapedDescription='null', maxLength=null, minLength=null, pattern='null', example='False', jsonSchema='{
  "type" : "boolean",
  "default" : false
}', minimum='null', maximum='null', exclusiveMinimum=false, exclusiveMaximum=false, required=false, deprecated=false, hasMoreNonReadOnly=false, isPrimitiveType=true, isModel=false, isContainer=false, isString=false, isNumeric=false, isInteger=false, isShort=false, isLong=false, isUnboundedInteger=false, isNumber=false, isFloat=false, isDouble=false, isDecimal=false, isByteArray=false, isBinary=false, isFile=false, isBoolean=true, isDate=false, isDateTime=false, isUuid=false, isUri=false, isEmail=false, isFreeFormObject=false, isArray=false, isMap=false, isEnum=false, isInnerEnum=false, isAnyType=false, isReadOnly=false, isWriteOnly=false, isNullable=false, isSelfReference=false, isCircularReference=false, isDiscriminator=false, _enum=null, allowableValues=null, items=null, additionalProperties=null, vars=[], requiredVars=[], mostInnerItems=null, vendorExtensions={}, hasValidation=false, isInherited=false, discriminatorValue='null', nameInCamelCase='ImageEncode', nameInSnakeCase='null', enumName='null', maxItems=null, minItems=null, maxProperties=null, minProperties=null, uniqueItems=false, uniqueItemsBoolean=null, multipleOf=null, isXmlAttribute=false, xmlPrefix='null', xmlName='null', xmlNamespace='null', isXmlWrapped=false, isNull=false, getAdditionalPropertiesIsAnyType=false, getHasVars=false, getHasRequired=false, getHasDiscriminatorWithNonEmptyMapping=false, composedSchemas=null, hasMultipleTypes=false, requiredVarsMap=null, ref=null, schemaIsFromAdditionalProperties=false, isBooleanSchemaTrue=false, isBooleanSchemaFalse=false, format=null, dependentRequired=null, contains=null}, content=null, requiredVarsMap=null, ref=null, schemaIsFromAdditionalProperties=false})

    try:
        # Check an image with the AI.
        api_response = api_instance.check_image(config_idurldetail=detailimage_encode=image_encode)
        pprint(api_response)
    except irisnet_client.ApiException as e:
        print("Exception when calling AICheckOperationsApi->check_image: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.irisnet.de*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AICheckOperationsApi* | [**check_image**](docs/apis/tags/AICheckOperationsApi.md#check_image) | **post** /v2/check-image/{configId} | Check an image with the AI.
*AICheckOperationsApi* | [**check_stream**](docs/apis/tags/AICheckOperationsApi.md#check_stream) | **post** /v2/check-stream/{configId} | Check a stream with the AI.
*AICheckOperationsApi* | [**check_video**](docs/apis/tags/AICheckOperationsApi.md#check_video) | **post** /v2/check-video/{configId} | Check a video with the AI.
*BalanceEndpointsApi* | [**get_cost**](docs/apis/tags/BalanceEndpointsApi.md#get_cost) | **get** /v2/cost/{configId} | Get the cost of the configuration for a single image.
*BalanceEndpointsApi* | [**get_license_info**](docs/apis/tags/BalanceEndpointsApi.md#get_license_info) | **get** /v2/info/ | Get information for the given license key.
*BalanceEndpointsApi* | [**get_video_cost**](docs/apis/tags/BalanceEndpointsApi.md#get_video_cost) | **get** /v2/cost/{configId}/{frames} | Get the cost of the configuration for moving images.
*BalanceEndpointsApi* | [**get_video_cost1**](docs/apis/tags/BalanceEndpointsApi.md#get_video_cost1) | **get** /v2/cost/{configId}/{fps}/{duration} | Get the cost of the configuration for moving images.
*ConfigurationManagementApi* | [**delete_config**](docs/apis/tags/ConfigurationManagementApi.md#delete_config) | **delete** /v2/config/{configId} | Delete an AI configuration.
*ConfigurationManagementApi* | [**get_all_configs**](docs/apis/tags/ConfigurationManagementApi.md#get_all_configs) | **get** /v2/config/ | List all saved AI configurations.
*ConfigurationManagementApi* | [**get_config**](docs/apis/tags/ConfigurationManagementApi.md#get_config) | **get** /v2/config/{configId} | Get a specific AI configuration.
*ConfigurationManagementApi* | [**set_config**](docs/apis/tags/ConfigurationManagementApi.md#set_config) | **post** /v2/config/ | Create a new AI configuration.
*DetailedConfigurationParametersApi* | [**clear_parameters**](docs/apis/tags/DetailedConfigurationParametersApi.md#clear_parameters) | **delete** /v2/config/parameters/{configId} | Delete the parameters of the AI configuration.
*DetailedConfigurationParametersApi* | [**get_parameters**](docs/apis/tags/DetailedConfigurationParametersApi.md#get_parameters) | **get** /v2/config/parameters/{configId} | Get the parameters of the AI configuration.
*DetailedConfigurationParametersApi* | [**set_parameters**](docs/apis/tags/DetailedConfigurationParametersApi.md#set_parameters) | **post** /v2/config/parameters/{configId} | Set parameters to the given AI configuration.

## Documentation For Models

 - [ApiNotice](docs/models/ApiNotice.md)
 - [BaseAttribute](docs/models/BaseAttribute.md)
 - [BaseDetection](docs/models/BaseDetection.md)
 - [BreastDetection](docs/models/BreastDetection.md)
 - [BrokenRule](docs/models/BrokenRule.md)
 - [Callback](docs/models/Callback.md)
 - [CheckResult](docs/models/CheckResult.md)
 - [Config](docs/models/Config.md)
 - [Coordinates](docs/models/Coordinates.md)
 - [Encoded](docs/models/Encoded.md)
 - [Event](docs/models/Event.md)
 - [FaceDetection](docs/models/FaceDetection.md)
 - [HairAttribute](docs/models/HairAttribute.md)
 - [HairDetection](docs/models/HairDetection.md)
 - [LicenseInfo](docs/models/LicenseInfo.md)
 - [Param](docs/models/Param.md)
 - [ParamSet](docs/models/ParamSet.md)
 - [Pricing](docs/models/Pricing.md)
 - [Rectangle](docs/models/Rectangle.md)
 - [Summary](docs/models/Summary.md)

## Documentation For Authorization

 Authentication schemes defined for the API:
## LICENSE-KEY

- **Type**: API key
- **API key parameter name**: LICENSE-KEY
- **Location**: HTTP header


## Author

info@irisnet.de
info@irisnet.de
info@irisnet.de
info@irisnet.de

## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in irisnet_client.apis and irisnet_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from irisnet_client.apis.default_api import DefaultApi`
- `from irisnet_client.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import irisnet_client
from irisnet_client.apis import *
from irisnet_client.models import *
```
