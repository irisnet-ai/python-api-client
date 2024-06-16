# AgeEstimationSubChecks

Contains information on ageEstimation sub-checks

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**face_liveness_check** | **str** | Indicates if the selfie image is genuine and not a photo of an image or of a screen | [optional] 
**age_validation_check** | **str** | Indicates if the estimated age is greater than or equal to a predefined minimum accepted age | [optional] 

## Example

```python
from irisnet_client.models.age_estimation_sub_checks import AgeEstimationSubChecks

# TODO update the JSON string below
json = "{}"
# create an instance of AgeEstimationSubChecks from a JSON string
age_estimation_sub_checks_instance = AgeEstimationSubChecks.from_json(json)
# print the JSON string representation of the object
print(AgeEstimationSubChecks.to_json())

# convert the object into a dict
age_estimation_sub_checks_dict = age_estimation_sub_checks_instance.to_dict()
# create an instance of AgeEstimationSubChecks from a dict
age_estimation_sub_checks_from_dict = AgeEstimationSubChecks.from_dict(age_estimation_sub_checks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


