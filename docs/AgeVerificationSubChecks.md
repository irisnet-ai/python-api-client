# AgeVerificationSubChecks

Contains information on ageVerification sub-checks

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**face_liveness_check** | **str** | Indicates if the selfie image is genuine and not a photo of an image or of a screen | [optional] 
**age_validation_check** | **str** | Indicates if the estimated age is greater than or equal to a predefined minimum accepted age | [optional] 

## Example

```python
from irisnet_client.models.age_verification_sub_checks import AgeVerificationSubChecks

# TODO update the JSON string below
json = "{}"
# create an instance of AgeVerificationSubChecks from a JSON string
age_verification_sub_checks_instance = AgeVerificationSubChecks.from_json(json)
# print the JSON string representation of the object
print(AgeVerificationSubChecks.to_json())

# convert the object into a dict
age_verification_sub_checks_dict = age_verification_sub_checks_instance.to_dict()
# create an instance of AgeVerificationSubChecks from a dict
age_verification_sub_checks_from_dict = AgeVerificationSubChecks.from_dict(age_verification_sub_checks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


