# AgeEstimationDetection

Contains further characteristics particular to _ageEstimation_ detection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_id** | **str** | The id of the check that lead to the detection | [optional] 
**face_similarity** | **int** | Indicates the similarity-level of whether two faces belong to the same person | [optional] 
**face_liveness_check_score** | **int** | Indicates the liveness score of the selfie image | [optional] 
**processed_checks** | [**AgeEstimationSubChecks**](AgeEstimationSubChecks.md) |  | [optional] 
**attributes** | [**List[AgeEstimationAttribute]**](AgeEstimationAttribute.md) | Attributes of the _idDocument_ detection. | [optional] 

## Example

```python
from irisnet_client.models.age_estimation_detection import AgeEstimationDetection

# TODO update the JSON string below
json = "{}"
# create an instance of AgeEstimationDetection from a JSON string
age_estimation_detection_instance = AgeEstimationDetection.from_json(json)
# print the JSON string representation of the object
print(AgeEstimationDetection.to_json())

# convert the object into a dict
age_estimation_detection_dict = age_estimation_detection_instance.to_dict()
# create an instance of AgeEstimationDetection from a dict
age_estimation_detection_from_dict = AgeEstimationDetection.from_dict(age_estimation_detection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


