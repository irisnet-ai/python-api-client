# Pricing

Contains information about the credit cost of a check operation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost** | **int** |  | [optional] 

## Example

```python
from irisnet_client.models.pricing import Pricing

# TODO update the JSON string below
json = "{}"
# create an instance of Pricing from a JSON string
pricing_instance = Pricing.from_json(json)
# print the JSON string representation of the object
print Pricing.to_json()

# convert the object into a dict
pricing_dict = pricing_instance.to_dict()
# create an instance of Pricing from a dict
pricing_form_dict = pricing.from_dict(pricing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


