# irisnet_client.model.event.Event

Describes an event that lead to a broken rule.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Describes an event that lead to a broken rule. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**classification** | str,  | str,  | The classification of the recognized object. | [optional] 
**group** | str,  | str,  | The group of the classification. | [optional] 
**start** | decimal.Decimal, int, float,  | decimal.Decimal,  | The start in seconds where the classification object is found. | [optional] value must be a 32 bit float
**duration** | decimal.Decimal, int, float,  | decimal.Decimal,  | The duration of the event in seconds until the classification object is no longer in frame. The current event is ongoing if the duration is not set. | [optional] value must be a 32 bit float
**severity** | decimal.Decimal, int,  | decimal.Decimal,  | The severity of the classification object set while configuring the AI. | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

