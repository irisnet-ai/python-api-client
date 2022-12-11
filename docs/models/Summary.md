# irisnet_client.model.summary.Summary

Summarizing the result of the AI.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Summarizing the result of the AI. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**status** | str,  | str,  | A simple status string that can be either _accept_ or _reject_. | [optional] 
**brokenRulesCount** | decimal.Decimal, int,  | decimal.Decimal,  | The amount of broken rules that are contained in the source media. | [optional] value must be a 32 bit integer
**helpSuggested** | decimal.Decimal, int,  | decimal.Decimal,  | In cases where the AI is uncertain, this attribute is set (1), indication that it could be useful to double check the source media by a human. | [optional] value must be a 32 bit integer
**severity** | decimal.Decimal, int,  | decimal.Decimal,  | The highest severity value found amongst the broken rules. | [optional] value must be a 32 bit integer
**creditsConsumed** | decimal.Decimal, int,  | decimal.Decimal,  | The amount of credits that was consumed for the check. | [optional] value must be a 32 bit integer
**[tags](#tags)** | list, tuple,  | tuple,  | A list of classification names that were found. | [optional] 
**[rejectTags](#rejectTags)** | list, tuple,  | tuple,  | A list of classification names that caused a rule to be broken. | [optional] 
**[rejectReasons](#rejectReasons)** | list, tuple,  | tuple,  | The names of the classification groups that caused a rule to be broken. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tags

A list of classification names that were found.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of classification names that were found. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | A list of classification names that were found. | 

# rejectTags

A list of classification names that caused a rule to be broken.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of classification names that caused a rule to be broken. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | A list of classification names that caused a rule to be broken. | 

# rejectReasons

The names of the classification groups that caused a rule to be broken.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The names of the classification groups that caused a rule to be broken. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The names of the classification groups that caused a rule to be broken. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

