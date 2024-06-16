# AgeEstimationAttribute

Attributes qualifying the _ageEstimation_ classification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Used as a type discriminator for json to object conversion. | [optional] 
**age** | **int** | The estimated age of the person in the selfie in years. | [optional] 
**age_min** | **int** | The estimated minimum age of the person in the selfie in years. | [optional] 
**age_max** | **int** | The estimated maximum age of the person in the selfie in years. | [optional] 

## Example

```python
from irisnet_client.models.age_estimation_attribute import AgeEstimationAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of AgeEstimationAttribute from a JSON string
age_estimation_attribute_instance = AgeEstimationAttribute.from_json(json)
# print the JSON string representation of the object
print(AgeEstimationAttribute.to_json())

# convert the object into a dict
age_estimation_attribute_dict = age_estimation_attribute_instance.to_dict()
# create an instance of AgeEstimationAttribute from a dict
age_estimation_attribute_from_dict = AgeEstimationAttribute.from_dict(age_estimation_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


