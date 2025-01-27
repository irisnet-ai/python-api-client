# KycUiParameter

A collection of parameters that determine the appearance and behaviour of the user interface (UI).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_color** | **str** | The primary color of the UI in hex format (rrggbb). | [optional] [default to '57a632']
**background_color** | **str** | The background color of the UI in hex format (rrggbb). | [optional] [default to '000000']
**text_color** | **str** | The text color of the UI in hex format (rrggbb). | [optional] [default to 'ffffff']
**logo** | **str** | The company logo for the UI in PNG fileformat (512 px * 512 px) as a base64 encoded string. | [optional] 

## Example

```python
from irisnet_client.models.kyc_ui_parameter import KycUiParameter

# TODO update the JSON string below
json = "{}"
# create an instance of KycUiParameter from a JSON string
kyc_ui_parameter_instance = KycUiParameter.from_json(json)
# print the JSON string representation of the object
print(KycUiParameter.to_json())

# convert the object into a dict
kyc_ui_parameter_dict = kyc_ui_parameter_instance.to_dict()
# create an instance of KycUiParameter from a dict
kyc_ui_parameter_from_dict = KycUiParameter.from_dict(kyc_ui_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


