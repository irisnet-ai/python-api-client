# KnownFace

A list of known faces, describing which other documentHolders match this documentHolder with a certain similarity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_holder_id** | **str** | The id of the documentHolder | [optional] 
**face_similarity** | **int** | Indicates the similarity-level between the known face and the documentHolder&#39;s selfie | [optional] 

## Example

```python
from irisnet_client.models.known_face import KnownFace

# TODO update the JSON string below
json = "{}"
# create an instance of KnownFace from a JSON string
known_face_instance = KnownFace.from_json(json)
# print the JSON string representation of the object
print(KnownFace.to_json())

# convert the object into a dict
known_face_dict = known_face_instance.to_dict()
# create an instance of KnownFace from a dict
known_face_from_dict = KnownFace.from_dict(known_face_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


