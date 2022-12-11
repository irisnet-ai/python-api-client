# irisnet_client.model.hair_attribute.HairAttribute

Attributes qualifying the _hair_ classification.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Attributes qualifying the _hair_ classification. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | Used as a type discriminator for json to object conversion. | [optional] 
**color** | str,  | str,  | The color of the hair. | [optional] must be one of ["black", "brown", "blonde", "grey", "red", "other", ] 
**style** | str,  | str,  | The hair style. | [optional] must be one of ["longHaired", "shortHaired", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

