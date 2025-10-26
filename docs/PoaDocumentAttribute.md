# PoaDocumentAttribute

Attributes qualifying the _poaDocument_ classification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Used as a type discriminator for json to object conversion. | [optional] 
**name** | **str** | The document holder&#39;s name | [optional] 
**document_type** | **str** | The type of the document | [optional] 
**issuer** | **str** | The issuer of the document | [optional] 
**issuing_date** | **date** | The issuing date | [optional] 
**address** | **str** | The document holder&#39;s address | [optional] 
**address_country** | **str** | The document holders&#39;s address country in ISO 3166-1 alpha-2 format | [optional] 

## Example

```python
from irisnet_client.models.poa_document_attribute import PoaDocumentAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of PoaDocumentAttribute from a JSON string
poa_document_attribute_instance = PoaDocumentAttribute.from_json(json)
# print the JSON string representation of the object
print(PoaDocumentAttribute.to_json())

# convert the object into a dict
poa_document_attribute_dict = poa_document_attribute_instance.to_dict()
# create an instance of PoaDocumentAttribute from a dict
poa_document_attribute_from_dict = PoaDocumentAttribute.from_dict(poa_document_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


