# irisnet_client.model.broken_rule.BrokenRule

Describes what and why a rule was broken according the the applied during the configuration.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Describes what and why a rule was broken according the the applied during the configuration. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**classification** | str,  | str,  | The classification of the recognized object. | [optional] 
**group** | str,  | str,  | The group of the classification. | [optional] 
**found** | decimal.Decimal, int,  | decimal.Decimal,  | The count of how many instances of the classification object were found. | [optional] value must be a 32 bit integer
**min** | decimal.Decimal, int,  | decimal.Decimal,  | The minimum allowed instances of the classification object. | [optional] value must be a 32 bit integer
**max** | decimal.Decimal, int,  | decimal.Decimal,  | The maximum allowed instances of the classification object. | [optional] value must be a 32 bit integer
**severity** | decimal.Decimal, int,  | decimal.Decimal,  | The severity of the classification object set while configuring the AI. | [optional] value must be a 32 bit integer
**duration** | decimal.Decimal, int, float,  | decimal.Decimal,  | The overall duration of the found classification. Not available for still images. | [optional] value must be a 32 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

