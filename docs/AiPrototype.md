# AiPrototype


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**classifications** | [**List[AiClassification]**](AiClassification.md) |  | [optional] 
**summary** | **str** |  | [optional] 
**aliases** | **List[str]** |  | [optional] 
**modes** | **List[str]** |  | [optional] 
**route** | **str** |  | [optional] 
**router_method** | **str** |  | [optional] 
**depends_on** | **List[str]** |  | [optional] 
**hidden** | **bool** |  | [optional] 

## Example

```python
from irisnet_client.models.ai_prototype import AiPrototype

# TODO update the JSON string below
json = "{}"
# create an instance of AiPrototype from a JSON string
ai_prototype_instance = AiPrototype.from_json(json)
# print the JSON string representation of the object
print(AiPrototype.to_json())

# convert the object into a dict
ai_prototype_dict = ai_prototype_instance.to_dict()
# create an instance of AiPrototype from a dict
ai_prototype_from_dict = AiPrototype.from_dict(ai_prototype_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


