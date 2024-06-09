# IdDocumentSubChecks

Contains information on idDocument sub-checks

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mrz_checksum** | **str** | Indicates whether the MRZ checksum is correct | [optional] 
**mrz_format** | **str** | Indicates whether the MRZ format is correct | [optional] 
**mrz_consistency** | **str** | Indicates whether the MRZ is consistent with the document type | [optional] 
**expiration_date** | **str** | Indicates whether the expirationDate is valid | [optional] 
**security_elements** | **str** | Indicates whether the document&#39;s security elements are valid | [optional] 
**photo_location** | **str** | Indicates whether the photo is in the correct location for a given document type | [optional] 
**blacklist_check** | **str** | Indicates whether a competent authority deny-listed the ID document | [optional] 
**photocopy_check** | **str** | Indicates whether the document is a photocopy | [optional] 
**specimen_check** | **str** | Indicates whether the document has been copied from the Internet | [optional] 
**document_model_identification** | **str** | Indicates whether the document model has been identified | [optional] 
**document_liveness_check** | **str** | Indicates if the document image is genuine and not a photo of an image or of a screen | [optional] 
**spoofed_image_analysis** | **str** | Indicates whether the selfie image is spoofed, copied from the Internet, or is a known deny-listed image | [optional] 
**face_liveness_check** | **str** | Indicates if the selfie image is genuine and not a photo of an image or of a screen | [optional] 

## Example

```python
from irisnet_client.models.id_document_sub_checks import IdDocumentSubChecks

# TODO update the JSON string below
json = "{}"
# create an instance of IdDocumentSubChecks from a JSON string
id_document_sub_checks_instance = IdDocumentSubChecks.from_json(json)
# print the JSON string representation of the object
print(IdDocumentSubChecks.to_json())

# convert the object into a dict
id_document_sub_checks_dict = id_document_sub_checks_instance.to_dict()
# create an instance of IdDocumentSubChecks from a dict
id_document_sub_checks_from_dict = IdDocumentSubChecks.from_dict(id_document_sub_checks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


