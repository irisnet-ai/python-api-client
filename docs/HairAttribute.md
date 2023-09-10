# HairAttribute

Attributes qualifying the _hair_ classification.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Used as a type discriminator for json to object conversion. | [optional] 
**color** | **str** | The color of the hair. | [optional] 
**style** | **str** | The hair style. | [optional] 

## Example

```python
from irisnet_client.models.hair_attribute import HairAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of HairAttribute from a JSON string
hair_attribute_instance = HairAttribute.from_json(json)
# print the JSON string representation of the object
print HairAttribute.to_json()

# convert the object into a dict
hair_attribute_dict = hair_attribute_instance.to_dict()
# create an instance of HairAttribute from a dict
hair_attribute_form_dict = hair_attribute.from_dict(hair_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


