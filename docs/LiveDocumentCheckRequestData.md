# LiveDocumentCheckRequestData

Data containing neccessary information to handle the enduser live document check.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback** | [**Callback**](Callback.md) |  | 
**status_url** | **str** | The URL to send the intermediate status requests to. If not set, no intermediate status requests will be sent. | [optional] 
**end_user_redirect_url** | **str** | If set the enduser is being redirected to this URL after the check is finished. | [optional] 
**token_validity_in_seconds** | **int** | The validity duration of a started ident process in seconds. Defaults to 3600 seconds &#x3D; 60 minutes. | [optional] 

## Example

```python
from irisnet_client.models.live_document_check_request_data import LiveDocumentCheckRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of LiveDocumentCheckRequestData from a JSON string
live_document_check_request_data_instance = LiveDocumentCheckRequestData.from_json(json)
# print the JSON string representation of the object
print(LiveDocumentCheckRequestData.to_json())

# convert the object into a dict
live_document_check_request_data_dict = live_document_check_request_data_instance.to_dict()
# create an instance of LiveDocumentCheckRequestData from a dict
live_document_check_request_data_from_dict = LiveDocumentCheckRequestData.from_dict(live_document_check_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


