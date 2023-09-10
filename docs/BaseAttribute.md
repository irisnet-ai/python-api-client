# BaseAttribute

An attribute describes a quality or characteristic that a detection object has.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification** | **str** | The classification of the recognized attribute. | [optional] 
**probability** | **int** | The probability that the attribute found matches the classification. | [optional] 
**type** | **str** | Used as a type discriminator for json to object conversion. | [optional] 

## Example

```python
from irisnet_client.models.base_attribute import BaseAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of BaseAttribute from a JSON string
base_attribute_instance = BaseAttribute.from_json(json)
# print the JSON string representation of the object
print BaseAttribute.to_json()

# convert the object into a dict
base_attribute_dict = base_attribute_instance.to_dict()
# create an instance of BaseAttribute from a dict
base_attribute_form_dict = base_attribute.from_dict(base_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


