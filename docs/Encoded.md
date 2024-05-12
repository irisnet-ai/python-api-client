# Encoded

Contains the resulting media as base64 encoded string or an URL to download that media.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | &lt;s&gt;The original filename of the image or video.&lt;/s&gt; Contains a randomly generated filename. &lt;b&gt;This property will be removed in future releases.&lt;/b&gt; | [optional] 
**data** | **bytearray** | The encoded image in base64 format. | [optional] 
**download_url** | **str** | A one time URL to download the resulting video. The URL is only valid for 24 hours. | [optional] 

## Example

```python
from irisnet_client.models.encoded import Encoded

# TODO update the JSON string below
json = "{}"
# create an instance of Encoded from a JSON string
encoded_instance = Encoded.from_json(json)
# print the JSON string representation of the object
print(Encoded.to_json())

# convert the object into a dict
encoded_dict = encoded_instance.to_dict()
# create an instance of Encoded from a dict
encoded_from_dict = Encoded.from_dict(encoded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


