# ValueAttribute

An attribute describes a quality or characteristic that a detection object has.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification** | **str** | The classification of the recognized attribute. | [optional] 
**value** | **object** |  | [optional] 
**probability** | **int** | The probability that the value matches the classification. | [optional] 

## Example

```python
from irisnet_client.models.value_attribute import ValueAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of ValueAttribute from a JSON string
value_attribute_instance = ValueAttribute.from_json(json)
# print the JSON string representation of the object
print(ValueAttribute.to_json())

# convert the object into a dict
value_attribute_dict = value_attribute_instance.to_dict()
# create an instance of ValueAttribute from a dict
value_attribute_from_dict = ValueAttribute.from_dict(value_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


