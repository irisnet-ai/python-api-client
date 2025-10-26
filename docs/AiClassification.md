# AiClassification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**min** | **int** |  | [optional] 
**max** | **int** |  | [optional] 
**draw_mode** | **int** |  | [optional] 
**grouped** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**cascaded_from** | **str** |  | [optional] 

## Example

```python
from irisnet_client.models.ai_classification import AiClassification

# TODO update the JSON string below
json = "{}"
# create an instance of AiClassification from a JSON string
ai_classification_instance = AiClassification.from_json(json)
# print the JSON string representation of the object
print(AiClassification.to_json())

# convert the object into a dict
ai_classification_dict = ai_classification_instance.to_dict()
# create an instance of AiClassification from a dict
ai_classification_from_dict = AiClassification.from_dict(ai_classification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


