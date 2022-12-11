# irisnet_client.model.param_set.ParamSet

A set of parameters/rules that describe how the AI should behave.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A set of parameters/rules that describe how the AI should behave. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**thresh** | decimal.Decimal, int, float,  | decimal.Decimal,  | Threshold when an object can be recognized. Lowering the value will increase the probability of recognizing objects. A threshold of 0.5 would mean, that 50% of an object like a face must be visible, to be detected.Setting the value too low however, can cause false positives. | [optional] if omitted the server will use the default value of 0.5value must be a 32 bit float
**grey** | decimal.Decimal, int,  | decimal.Decimal,  | A grey scale color to use for frame or masking. &#x27;0&#x27; will represent black, while the maximum &#x27;255&#x27; will be white. | [optional] if omitted the server will use the default value of 127value must be a 32 bit integer
**minDuration** | decimal.Decimal, int,  | decimal.Decimal,  | Set the overall minimum duration in milliseconds for a rule to be broken in moving images. | [optional] if omitted the server will use the default value of 100value must be a 32 bit integer
**abortOnSeverity** | decimal.Decimal, int,  | decimal.Decimal,  | Set a severity on which to automatically stop the check operation. Works with moving images.Use &#x27;-1&#x27; to ignore this option. | [optional] if omitted the server will use the default value of -1value must be a 32 bit integer
**[params](#params)** | list, tuple,  | tuple,  | A list of parameter sets that describe the rules of the objects. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# params

A list of parameter sets that describe the rules of the objects.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of parameter sets that describe the rules of the objects. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Param**](Param.md) | [**Param**](Param.md) | [**Param**](Param.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

