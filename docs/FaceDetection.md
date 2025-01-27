# FaceDetection

Contains further characteristics particular to _face_ detection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification** | **str** | The classification of the recognized object. | [optional] 
**group** | **str** | The group of the classification. | [optional] 
**id** | **int** | The id of the detection object. | [optional] 
**probability** | **int** | The probability that the object found matches the classification. | [optional] 
**coordinates** | [**Coordinates**](Coordinates.md) |  | [optional] 
**attributes** | [**List[BaseAttribute]**](BaseAttribute.md) | Attributes characterizing the _face_ detection. Mainly contains attributes that were activated with the _ageEstimation_ prototype. | [optional] 
**sub_detections** | [**List[Detection]**](Detection.md) | A set of sub-detection that are particular to the _face_ detection. Mainly contains detections that were activated with the _attributesCheck_ prototype. | [optional] 

## Example

```python
from irisnet_client.models.face_detection import FaceDetection

# TODO update the JSON string below
json = "{}"
# create an instance of FaceDetection from a JSON string
face_detection_instance = FaceDetection.from_json(json)
# print the JSON string representation of the object
print(FaceDetection.to_json())

# convert the object into a dict
face_detection_dict = face_detection_instance.to_dict()
# create an instance of FaceDetection from a dict
face_detection_from_dict = FaceDetection.from_dict(face_detection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


