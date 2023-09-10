# Summary

Summarizing the result of the AI.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | A simple status string that can be either _accept_ or _reject_. | [optional] 
**broken_rules_count** | **int** | The amount of broken rules that are contained in the source media. | [optional] 
**help_suggested** | **int** | In cases where the AI is uncertain, this attribute is set (1), indication that it could be useful to double check the source media by a human. | [optional] 
**severity** | **int** | The highest severity value found amongst the broken rules. | [optional] 
**credits_consumed** | **int** | The amount of credits that was consumed for the check. | [optional] 
**tags** | **List[str]** | A list of classification names that were found. | [optional] 
**reject_tags** | **List[str]** | A list of classification names that caused a rule to be broken. | [optional] 
**reject_reasons** | **List[str]** | The names of the classification groups that caused a rule to be broken. | [optional] 

## Example

```python
from irisnet_client.models.summary import Summary

# TODO update the JSON string below
json = "{}"
# create an instance of Summary from a JSON string
summary_instance = Summary.from_json(json)
# print the JSON string representation of the object
print Summary.to_json()

# convert the object into a dict
summary_dict = summary_instance.to_dict()
# create an instance of Summary from a dict
summary_form_dict = summary.from_dict(summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


