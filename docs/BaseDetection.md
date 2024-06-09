# BaseDetection

A detection describes the object found with all its details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**attributes** | [**List[IdDocumentAttribute]**](IdDocumentAttribute.md) | Attributes of the _idDocument_ detection. | [optional] 
**check_id** | **str** | The id of the check that lead to the detection | [optional] 
**has_official_document** | **bool** | Indicates whether the identified document is official | [optional] 
**comparable** | **bool** | Indicates whether the provided selfie-image is comparable to the document | [optional] 
**face_similarity** | **int** | Indicates the similarity-level of whether two faces belong to the same person | [optional] 
**face_liveness_check_score** | **int** | Indicates the liveness score of the selfie image | [optional] 
**document_front_liveness_score** | **int** | Indicates the liveness score of the front side image of the document | [optional] 
**document_back_liveness_score** | **int** | Indicates the liveness score of the back side image of the document | [optional] 
**processed_checks** | [**IdDocumentSubChecks**](IdDocumentSubChecks.md) |  | [optional] 
**document_holder_id** | **str** | The id of the documentHolder | [optional] 
**sub_detections** | [**List[BaseDetection]**](BaseDetection.md) | A set of sub-detection that are particular to the _face_ detection. Mainly contains detections that were activated with the _attributesCheck_ prototype. | [optional] 

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


