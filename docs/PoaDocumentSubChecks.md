# PoaDocumentSubChecks

Contains information on poaDocument sub-checks

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | Indicates whether the first name is valid | [optional] 
**last_name** | **str** | Indicates whether the last name is valid | [optional] 
**document_age** | **str** | Indicates whether the age of the document is valid (not older than 3 months) | [optional] 
**ip_originates_in_address_country** | **str** | Indicates whether the client IP originates in the country of the address | [optional] 
**ip_nearby_address** | **str** | Indicates whether the client IP is in reasonable distance from the address | [optional] 

## Example

```python
from irisnet_client.models.poa_document_sub_checks import PoaDocumentSubChecks

# TODO update the JSON string below
json = "{}"
# create an instance of PoaDocumentSubChecks from a JSON string
poa_document_sub_checks_instance = PoaDocumentSubChecks.from_json(json)
# print the JSON string representation of the object
print(PoaDocumentSubChecks.to_json())

# convert the object into a dict
poa_document_sub_checks_dict = poa_document_sub_checks_instance.to_dict()
# create an instance of PoaDocumentSubChecks from a dict
poa_document_sub_checks_from_dict = PoaDocumentSubChecks.from_dict(poa_document_sub_checks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


