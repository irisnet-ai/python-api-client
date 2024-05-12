# IdDocumentAttribute

Attributes qualifying the _idDocument_ classification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Used as a type discriminator for json to object conversion. | [optional] 
**document_type** | **str** | The type of the document | [optional] 
**document_number** | **str** | The number of the document | [optional] 
**is_two_sided** | **bool** | Indicates whether the document is two-sided | [optional] 
**issuing_authority** | **str** | The issuing authority | [optional] 
**issuing_date** | **date** | The issuing date | [optional] 
**issuing_country** | **str** | The document&#39;s country in ISO 3166-1 alpha-2 format | [optional] 
**expiration_date** | **date** | The expiration date | [optional] 
**access_number** | **str** | The access number | [optional] 
**first_names** | **List[str]** | The document holder&#39;s first name(s) | [optional] 
**last_names** | **List[str]** | The document holder&#39;s last name(s) | [optional] 
**birth_name** | **str** | The document holder&#39;s birth name | [optional] 
**date_of_birth** | **date** | The document holder&#39;s date of birth | [optional] 
**place_of_birth** | **str** | The document holder&#39;s place of birth | [optional] 
**nationality** | **str** | The document holder&#39;s nationality in ISO 3166-1 alpha-2 format | [optional] 
**gender** | **str** | The document holder&#39;s gender | [optional] 
**height** | **str** | The document holder&#39;s height | [optional] 
**address** | **str** | The document holder&#39;s address | [optional] 
**machine_readable_zone** | **List[str]** | The document&#39;s machine readable zone (MRZ), at most 3 lines | [optional] 

## Example

```python
from irisnet_client.models.id_document_attribute import IdDocumentAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of IdDocumentAttribute from a JSON string
id_document_attribute_instance = IdDocumentAttribute.from_json(json)
# print the JSON string representation of the object
print(IdDocumentAttribute.to_json())

# convert the object into a dict
id_document_attribute_dict = id_document_attribute_instance.to_dict()
# create an instance of IdDocumentAttribute from a dict
id_document_attribute_from_dict = IdDocumentAttribute.from_dict(id_document_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


