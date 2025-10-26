# TextDetection

Contains further characteristics regarding the moderation of text.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification** | **str** | The classification of the recognized object. | [optional] 
**group** | **str** | The group of the classification. | [optional] 
**id** | **int** | The id of the detection object. | [optional] 
**probability** | **int** | The probability that the object found matches the classification. | [optional] 
**coordinates** | [**Coordinates**](Coordinates.md) |  | [optional] 
**content** | **str** | The text that was detected | [optional] 
**attributes** | [**List[Attribute]**](Attribute.md) | Attributes characterizing the text. | [optional] 
**sub_detections** | [**List[BaseDetection]**](BaseDetection.md) | A set of sub-detection for text moderation. | [optional] 

## Example

```python
from irisnet_client.models.text_detection import TextDetection

# TODO update the JSON string below
json = "{}"
# create an instance of TextDetection from a JSON string
text_detection_instance = TextDetection.from_json(json)
# print the JSON string representation of the object
print(TextDetection.to_json())

# convert the object into a dict
text_detection_dict = text_detection_instance.to_dict()
# create an instance of TextDetection from a dict
text_detection_from_dict = TextDetection.from_dict(text_detection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


