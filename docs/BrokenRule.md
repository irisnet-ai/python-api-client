# BrokenRule

Describes what and why a rule was broken according the the applied during the configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification** | **str** | The classification of the recognized object. | [optional] 
**group** | **str** | The group of the classification. | [optional] 
**found** | **int** | The count of how many instances of the classification object were found. | [optional] 
**min** | **int** | The minimum allowed instances of the classification object. | [optional] 
**max** | **int** | The maximum allowed instances of the classification object. | [optional] 
**severity** | **int** | The severity of the classification object set while configuring the AI. | [optional] 
**duration** | **float** | The overall duration of the found classification. Not available for still images. | [optional] 

## Example

```python
from irisnet_client.models.broken_rule import BrokenRule

# TODO update the JSON string below
json = "{}"
# create an instance of BrokenRule from a JSON string
broken_rule_instance = BrokenRule.from_json(json)
# print the JSON string representation of the object
print BrokenRule.to_json()

# convert the object into a dict
broken_rule_dict = broken_rule_instance.to_dict()
# create an instance of BrokenRule from a dict
broken_rule_form_dict = broken_rule.from_dict(broken_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


