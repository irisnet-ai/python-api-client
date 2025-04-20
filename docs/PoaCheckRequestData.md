# PoaCheckRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback** | [**Callback**](Callback.md) |  | 
**front_image** | **str** | The base64-encoded front image of the document to be checked in either jpg or png file format. | [optional] 
**document_type** | **str** | The type of the document | 
**document_holder_id** | **str** | The documentHolderId from a previous successful check. | [optional] 

## Example

```python
from irisnet_client.models.poa_check_request_data import PoaCheckRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of PoaCheckRequestData from a JSON string
poa_check_request_data_instance = PoaCheckRequestData.from_json(json)
# print the JSON string representation of the object
print(PoaCheckRequestData.to_json())

# convert the object into a dict
poa_check_request_data_dict = poa_check_request_data_instance.to_dict()
# create an instance of PoaCheckRequestData from a dict
poa_check_request_data_from_dict = PoaCheckRequestData.from_dict(poa_check_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


