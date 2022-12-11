# irisnet_client.model.base_attribute.BaseAttribute

An attribute describes a quality or characteristic that a detection object has.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An attribute describes a quality or characteristic that a detection object has. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**classification** | str,  | str,  | The classification of the recognized attribute. | [optional] 
**probability** | decimal.Decimal, int,  | decimal.Decimal,  | The probability that the attribute found matches the classification. | [optional] value must be a 32 bit integer
**type** | str,  | str,  | Used as a type discriminator for json to object conversion. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

