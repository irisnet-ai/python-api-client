# ParamSet

A set of parameters/rules that describe how the AI should behave.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thresh** | **float** | Threshold when an object can be recognized. Lowering the value will increase the probability of recognizing objects. A threshold of 0.5 would mean, that 50% of an object like a face must be visible, to be detected.Setting the value too low however, can cause false positives. | [optional] [default to 0.5]
**grey** | **int** | A grey scale color to use for frame or masking. &#39;0&#39; will represent black, while the maximum &#39;255&#39; will be white. | [optional] [default to 127]
**min_duration** | **int** | Set the overall minimum duration in milliseconds for a rule to be broken in moving images. | [optional] [default to 100]
**abort_on_severity** | **int** | Set a severity on which to automatically stop the check operation. Works with moving images.Use &#39;-1&#39; to ignore this option. | [optional] [default to -1]
**params** | [**List[Param]**](Param.md) | A list of parameter sets that describe the rules of the objects. | [optional] 
**kyc_ui_parameters** | [**KycUiParameter**](KycUiParameter.md) |  | [optional] 
**kyc_document_country_deny_list** | **str** | A comma separated list of country codes (ISO 3166-1 alpha-2) for which id-documents should be rejected. | [optional] 

## Example

```python
from irisnet_client.models.param_set import ParamSet

# TODO update the JSON string below
json = "{}"
# create an instance of ParamSet from a JSON string
param_set_instance = ParamSet.from_json(json)
# print the JSON string representation of the object
print(ParamSet.to_json())

# convert the object into a dict
param_set_dict = param_set_instance.to_dict()
# create an instance of ParamSet from a dict
param_set_from_dict = ParamSet.from_dict(param_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


