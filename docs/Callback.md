# Callback

Callback options to send a response to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_url** | **str** | Define a URL where a response should be sent. | 
**headers** | **Dict[str, str]** | Define headers to send to the URL. | [optional] 

## Example

```python
from irisnet_client.models.callback import Callback

# TODO update the JSON string below
json = "{}"
# create an instance of Callback from a JSON string
callback_instance = Callback.from_json(json)
# print the JSON string representation of the object
print(Callback.to_json())

# convert the object into a dict
callback_dict = callback_instance.to_dict()
# create an instance of Callback from a dict
callback_from_dict = Callback.from_dict(callback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


