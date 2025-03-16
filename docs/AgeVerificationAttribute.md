# AgeVerificationAttribute

Attributes qualifying the _ageVerification_ classification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Used as a type discriminator for json to object conversion. | [optional] 
**age** | **int** | The estimated age of the person in the selfie in years. | [optional] 
**age_min** | **int** | The estimated minimum age of the person in the selfie in years. | [optional] 
**age_max** | **int** | The estimated maximum age of the person in the selfie in years. | [optional] 

## Example

```python
from irisnet_client.models.age_verification_attribute import AgeVerificationAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of AgeVerificationAttribute from a JSON string
age_verification_attribute_instance = AgeVerificationAttribute.from_json(json)
# print the JSON string representation of the object
print(AgeVerificationAttribute.to_json())

# convert the object into a dict
age_verification_attribute_dict = age_verification_attribute_instance.to_dict()
# create an instance of AgeVerificationAttribute from a dict
age_verification_attribute_from_dict = AgeVerificationAttribute.from_dict(age_verification_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


