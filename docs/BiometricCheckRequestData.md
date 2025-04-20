# BiometricCheckRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback** | [**Callback**](Callback.md) |  | 
**front_image** | **str** | The base64-encoded front image of the document to be checked in either jpg or png file format. | [optional] 
**selfie_image** | **str** | The base64-encoded selfie image to be checked in either jpg or png file format. | 
**minimum_accepted_age** | **int** | The minimum age in years accepted for a DocumentCheck, if applicable. Defaults to 18 if not specified. | [optional] 
**document_holder_id** | **str** | The documentHolderId from a previous successful DocumentCheck. | [optional] 

## Example

```python
from irisnet_client.models.biometric_check_request_data import BiometricCheckRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of BiometricCheckRequestData from a JSON string
biometric_check_request_data_instance = BiometricCheckRequestData.from_json(json)
# print the JSON string representation of the object
print(BiometricCheckRequestData.to_json())

# convert the object into a dict
biometric_check_request_data_dict = biometric_check_request_data_instance.to_dict()
# create an instance of BiometricCheckRequestData from a dict
biometric_check_request_data_from_dict = BiometricCheckRequestData.from_dict(biometric_check_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


