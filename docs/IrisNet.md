# IrisNet

Contains information on the AI result from the source media check.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules_broken** | **int** | The amount of broken rules that are contained in the source media. | [optional] 
**help_suggested** | **int** | In cases where the AI is uncertain, this attribute is set (1), indication that it could be useful to double check the source media by a human. | [optional] 
**severity** | **int** | The highest severity value found amongst the broken rules. | [optional] 
**getn_classes** | **int** | The amount of classification objects that were checked against on the source media. This does not mean that all of the classifications were found. | [optional] 
**getn_objects** | **int** | The amount of objects that were recognized on the source image. | [optional] 
**in_rule** | [**[INRule]**](INRule.md) | This list contains one rule per classification. Rules for classification objects that were not found, are omitted. | [optional] 
**in_object** | [**[INObject]**](INObject.md) | A list of all instances of the classification objects found on the source image. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


