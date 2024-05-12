# IdDocumentDetection

Contains further characteristics particular to _idDocument_ detection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_id** | **str** | The id of the check that lead to the detection | [optional] 
**has_official_document** | **bool** | Indicates whether the identified document is official | [optional] 
**comparable** | **bool** | Indicates whether the provided selfie-image is comparable to the document | [optional] 
**face_similarity** | **int** | Indicates the similarity-level of whether two faces belong to the same person | [optional] 
**face_liveness_check_score** | **int** | Indicates the liveness score of the selfie image | [optional] 
**document_front_liveness_score** | **int** | Indicates the liveness score of the front side image of the document | [optional] 
**document_back_liveness_score** | **int** | Indicates the liveness score of the back side image of the document | [optional] 
**processed_checks** | [**IdDocumentSubChecks**](IdDocumentSubChecks.md) |  | [optional] 
**attributes** | [**List[IdDocumentAttribute]**](IdDocumentAttribute.md) | Attributes of the _idDocument_ detection. | [optional] 

## Example

```python
from irisnet_client.models.id_document_detection import IdDocumentDetection

# TODO update the JSON string below
json = "{}"
# create an instance of IdDocumentDetection from a JSON string
id_document_detection_instance = IdDocumentDetection.from_json(json)
# print the JSON string representation of the object
print(IdDocumentDetection.to_json())

# convert the object into a dict
id_document_detection_dict = id_document_detection_instance.to_dict()
# create an instance of IdDocumentDetection from a dict
id_document_detection_from_dict = IdDocumentDetection.from_dict(id_document_detection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


