# CheckResultDetectionsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification** | **str** | The classification of the recognized object. | [optional] 
**group** | **str** | The group of the classification. | [optional] 
**id** | **int** | The id of the detection object. | [optional] 
**probability** | **int** | The probability that the object found matches the classification. | [optional] 
**coordinates** | [**Coordinates**](Coordinates.md) |  | [optional] 
**type** | **str** | Used as a type discriminator for json to object conversion. | [optional] 
**attributes** | [**List[HairAttribute]**](HairAttribute.md) | Contains attributes for the _hair_ classification. | [optional] 
**sub_detections** | [**List[BaseDetection]**](BaseDetection.md) | A set of sub-detection that are particular to the _face_ detection. Mainly contains detections that were activated with the _attributesCheck_ prototype. | [optional] 

## Example

```python
from irisnet_client.models.check_result_detections_inner import CheckResultDetectionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CheckResultDetectionsInner from a JSON string
check_result_detections_inner_instance = CheckResultDetectionsInner.from_json(json)
# print the JSON string representation of the object
print CheckResultDetectionsInner.to_json()

# convert the object into a dict
check_result_detections_inner_dict = check_result_detections_inner_instance.to_dict()
# create an instance of CheckResultDetectionsInner from a dict
check_result_detections_inner_form_dict = check_result_detections_inner.from_dict(check_result_detections_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


