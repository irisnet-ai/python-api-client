# ImageAnalysisDetection

Contains further characteristics of the image itself.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification** | **str** | The classification of the recognized object. | [optional] 
**group** | **str** | The group of the classification. | [optional] 
**id** | **int** | The id of the detection object. | [optional] 
**probability** | **int** | The probability that the object found matches the classification. | [optional] 
**coordinates** | [**Coordinates**](Coordinates.md) |  | [optional] 
**attributes** | [**List[Attribute]**](Attribute.md) | Attributes characterizing the _image_ detection. | [optional] 

## Example

```python
from irisnet_client.models.image_analysis_detection import ImageAnalysisDetection

# TODO update the JSON string below
json = "{}"
# create an instance of ImageAnalysisDetection from a JSON string
image_analysis_detection_instance = ImageAnalysisDetection.from_json(json)
# print the JSON string representation of the object
print(ImageAnalysisDetection.to_json())

# convert the object into a dict
image_analysis_detection_dict = image_analysis_detection_instance.to_dict()
# create an instance of ImageAnalysisDetection from a dict
image_analysis_detection_from_dict = ImageAnalysisDetection.from_dict(image_analysis_detection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


