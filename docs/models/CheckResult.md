# irisnet_client.model.check_result.CheckResult

The root object returned after a check operation.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The root object returned after a check operation. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**summary** | [**Summary**](Summary.md) | [**Summary**](Summary.md) |  | [optional] 
**[encodings](#encodings)** | list, tuple,  | tuple,  |  | [optional] 
**[brokenRules](#brokenRules)** | list, tuple,  | tuple,  |  | [optional] 
**[detections](#detections)** | list, tuple,  | tuple,  |  | [optional] 
**[events](#events)** | list, tuple,  | tuple,  |  | [optional] 
**[notifications](#notifications)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# encodings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Encoded**](Encoded.md) | [**Encoded**](Encoded.md) | [**Encoded**](Encoded.md) |  | 

# brokenRules

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BrokenRule**](BrokenRule.md) | [**BrokenRule**](BrokenRule.md) | [**BrokenRule**](BrokenRule.md) |  | 

# detections

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[BaseDetection](BaseDetection.md) | [**BaseDetection**](BaseDetection.md) | [**BaseDetection**](BaseDetection.md) |  | 
[BreastDetection](BreastDetection.md) | [**BreastDetection**](BreastDetection.md) | [**BreastDetection**](BreastDetection.md) |  | 
[FaceDetection](FaceDetection.md) | [**FaceDetection**](FaceDetection.md) | [**FaceDetection**](FaceDetection.md) |  | 
[HairDetection](HairDetection.md) | [**HairDetection**](HairDetection.md) | [**HairDetection**](HairDetection.md) |  | 

# events

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Event**](Event.md) | [**Event**](Event.md) | [**Event**](Event.md) |  | 

# notifications

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ApiNotice**](ApiNotice.md) | [**ApiNotice**](ApiNotice.md) | [**ApiNotice**](ApiNotice.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

