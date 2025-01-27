# HairDetection

Contains further characteristics particular to _hair_ detection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification** | **str** | The classification of the recognized object. | [optional] 
**group** | **str** | The group of the classification. | [optional] 
**id** | **int** | The id of the detection object. | [optional] 
**probability** | **int** | The probability that the object found matches the classification. | [optional] 
**coordinates** | [**Coordinates**](Coordinates.md) |  | [optional] 
**attributes** | [**List[HairAttribute]**](HairAttribute.md) | Contains attributes for the _hair_ classification. | [optional] 

## Example

```python
from irisnet_client.models.hair_detection import HairDetection

# TODO update the JSON string below
json = "{}"
# create an instance of HairDetection from a JSON string
hair_detection_instance = HairDetection.from_json(json)
# print the JSON string representation of the object
print(HairDetection.to_json())

# convert the object into a dict
hair_detection_dict = hair_detection_instance.to_dict()
# create an instance of HairDetection from a dict
hair_detection_from_dict = HairDetection.from_dict(hair_detection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


