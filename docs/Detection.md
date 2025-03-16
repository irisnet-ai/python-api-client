# Detection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Used as a type discriminator for json to object conversion. | [optional] 
**classification** | **str** | The classification of the recognized object. | [optional] 
**group** | **str** | The group of the classification. | [optional] 
**id** | **int** | The id of the detection object. | [optional] 
**probability** | **int** | The probability that the object found matches the classification. | [optional] 
**coordinates** | [**Coordinates**](Coordinates.md) |  | [optional] 
**attributes** | [**List[AgeVerificationAttribute]**](AgeVerificationAttribute.md) | Attributes of the _ageVerification_ detection. | [optional] 
**check_id** | **str** | The id of the check that lead to the detection | [optional] 
**has_official_document** | **bool** | Indicates whether the identified document is official | [optional] 
**comparable** | **bool** | Indicates whether the provided selfie-image is comparable to the document | [optional] 
**face_similarity** | **int** | Indicates the similarity-level of whether two faces belong to the same person | [optional] 
**face_liveness_check_score** | **int** | Indicates the liveness score of the selfie image | [optional] 
**document_front_liveness_score** | **int** | Indicates the liveness score of the front side image of the document | [optional] 
**document_back_liveness_score** | **int** | Indicates the liveness score of the back side image of the document | [optional] 
**processed_checks** | [**AgeVerificationSubChecks**](AgeVerificationSubChecks.md) |  | [optional] 
**document_holder_id** | **str** | The id of the documentHolder | [optional] 
**known_faces** | [**List[KnownFace]**](KnownFace.md) | A list of known faces, describing which other documentHolders match this documentHolder with a certain similarity | [optional] 
**sub_detections** | [**List[Detection]**](Detection.md) | A set of sub-detection that are particular to the _face_ detection. Mainly contains detections that were activated with the _attributesCheck_ prototype. | [optional] 

## Example

```python
from irisnet_client.models.detection import Detection

# TODO update the JSON string below
json = "{}"
# create an instance of Detection from a JSON string
detection_instance = Detection.from_json(json)
# print the JSON string representation of the object
print(Detection.to_json())

# convert the object into a dict
detection_dict = detection_instance.to_dict()
# create an instance of Detection from a dict
detection_from_dict = Detection.from_dict(detection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


