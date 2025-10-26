# BaseDetection

A detection describes the object found with all its details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Used as a type discriminator for json to object conversion. | [optional] 
**classification** | **str** | The classification of the recognized object. | [optional] 
**group** | **str** | The group of the classification. | [optional] 
**id** | **int** | The id of the detection object. | [optional] 
**probability** | **int** | The probability that the object found matches the classification. | [optional] 
**coordinates** | [**Coordinates**](Coordinates.md) |  | [optional] 
**attributes** | [**List[Attribute]**](Attribute.md) | Attributes characterizing the _base_ detection. | [optional] 

## Example

```python
from irisnet_client.models.base_detection import BaseDetection

# TODO update the JSON string below
json = "{}"
# create an instance of BaseDetection from a JSON string
base_detection_instance = BaseDetection.from_json(json)
# print the JSON string representation of the object
print(BaseDetection.to_json())

# convert the object into a dict
base_detection_dict = base_detection_instance.to_dict()
# create an instance of BaseDetection from a dict
base_detection_from_dict = BaseDetection.from_dict(base_detection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


