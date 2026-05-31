# AgeAttribute

Attributes qualifying the _numericAgeEstimation_ classification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age** | **int** | The estimated age of the person in years. | [optional] 
**age_min** | **int** | The estimated minimum age of the person in years. | [optional] 
**age_max** | **int** | The estimated maximum age of the person in years. | [optional] 
**probability** | **int** | The probability of the estimated age. | [optional] 

## Example

```python
from irisnet_client.models.age_attribute import AgeAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of AgeAttribute from a JSON string
age_attribute_instance = AgeAttribute.from_json(json)
# print the JSON string representation of the object
print(AgeAttribute.to_json())

# convert the object into a dict
age_attribute_dict = age_attribute_instance.to_dict()
# create an instance of AgeAttribute from a dict
age_attribute_from_dict = AgeAttribute.from_dict(age_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


