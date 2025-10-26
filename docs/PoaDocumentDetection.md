# PoaDocumentDetection

Contains further characteristics particular to _poaDocument_ detection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification** | **str** | The classification of the recognized object. | [optional] 
**group** | **str** | The group of the classification. | [optional] 
**id** | **int** | The id of the detection object. | [optional] 
**probability** | **int** | The probability that the object found matches the classification. | [optional] 
**coordinates** | [**Coordinates**](Coordinates.md) |  | [optional] 
**check_id** | **str** | The id of the check that lead to the detection | [optional] 
**processed_checks** | [**PoaDocumentSubChecks**](PoaDocumentSubChecks.md) | The sub-checks that were processed | [optional] 
**attributes** | [**List[PoaDocumentAttribute]**](PoaDocumentAttribute.md) | Attributes of the _poaDocument_ detection. | [optional] 
**document_holder_id** | **str** | The id of the documentHolder | [optional] 

## Example

```python
from irisnet_client.models.poa_document_detection import PoaDocumentDetection

# TODO update the JSON string below
json = "{}"
# create an instance of PoaDocumentDetection from a JSON string
poa_document_detection_instance = PoaDocumentDetection.from_json(json)
# print the JSON string representation of the object
print(PoaDocumentDetection.to_json())

# convert the object into a dict
poa_document_detection_dict = poa_document_detection_instance.to_dict()
# create an instance of PoaDocumentDetection from a dict
poa_document_detection_from_dict = PoaDocumentDetection.from_dict(poa_document_detection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


