# LiveDocumentCheckResponseData

Response object containing necessary information to start the enduser live document check on the client side.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | unique id of this live document check | [optional] 
**ident_token** | **str** | token to secure the live document check, might be null since already incorporated into endUserIdentUrl | [optional] 
**end_user_ident_url** | **str** | URL to send the enduser to, to start the live document check | [optional] 

## Example

```python
from irisnet_client.models.live_document_check_response_data import LiveDocumentCheckResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of LiveDocumentCheckResponseData from a JSON string
live_document_check_response_data_instance = LiveDocumentCheckResponseData.from_json(json)
# print the JSON string representation of the object
print(LiveDocumentCheckResponseData.to_json())

# convert the object into a dict
live_document_check_response_data_dict = live_document_check_response_data_instance.to_dict()
# create an instance of LiveDocumentCheckResponseData from a dict
live_document_check_response_data_from_dict = LiveDocumentCheckResponseData.from_dict(live_document_check_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


