# DocumentCheckRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback** | [**Callback**](Callback.md) |  | 
**front_image** | **str** | The base64 encoded front image of the document to be checked in either jpg or png file format | 
**back_image** | **str** | The base64 encoded back image of the document to be checked in either jpg or png file format | [optional] 
**selfie_image** | **str** | The base64 encoded selfie image to be checked in either jpg or png file format | [optional] 
**minimum_accepted_age** | **int** | The minimum accepted age in years for a DocumentCheck. Defaults to 18 if not provided | [optional] 
**document_type** | **str** | The type of the document | [optional] 
**document_country** | **str** | The document&#39;s country in ISO 3166-1 alpha-2 format | [optional] 

## Example

```python
from irisnet_client.models.document_check_request_data import DocumentCheckRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCheckRequestData from a JSON string
document_check_request_data_instance = DocumentCheckRequestData.from_json(json)
# print the JSON string representation of the object
print(DocumentCheckRequestData.to_json())

# convert the object into a dict
document_check_request_data_dict = document_check_request_data_instance.to_dict()
# create an instance of DocumentCheckRequestData from a dict
document_check_request_data_from_dict = DocumentCheckRequestData.from_dict(document_check_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


