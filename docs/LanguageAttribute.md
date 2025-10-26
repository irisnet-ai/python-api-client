# LanguageAttribute

Attribute that contains the language of a text or spoken words.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iso_language** | **str** | The ISO 639-1 language code. | [optional] 
**probability** | **int** | The probability that the text matches the language. | [optional] 

## Example

```python
from irisnet_client.models.language_attribute import LanguageAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of LanguageAttribute from a JSON string
language_attribute_instance = LanguageAttribute.from_json(json)
# print the JSON string representation of the object
print(LanguageAttribute.to_json())

# convert the object into a dict
language_attribute_dict = language_attribute_instance.to_dict()
# create an instance of LanguageAttribute from a dict
language_attribute_from_dict = LanguageAttribute.from_dict(language_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


