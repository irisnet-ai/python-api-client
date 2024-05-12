# ApiNotice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | The status code of the response. | [optional] 
**level** | **str** | The severity level of the notice. | [optional] 
**message** | **str** | A hopefully detailed message describing what went wrong. | [optional] 

## Example

```python
from irisnet_client.models.api_notice import ApiNotice

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNotice from a JSON string
api_notice_instance = ApiNotice.from_json(json)
# print the JSON string representation of the object
print(ApiNotice.to_json())

# convert the object into a dict
api_notice_dict = api_notice_instance.to_dict()
# create an instance of ApiNotice from a dict
api_notice_from_dict = ApiNotice.from_dict(api_notice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


