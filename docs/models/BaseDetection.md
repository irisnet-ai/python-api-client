# irisnet_client.model.base_detection.BaseDetection

A detection describes the object found with all its details.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A detection describes the object found with all its details. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**classification** | str,  | str,  | The classification of the recognized object. | [optional] 
**group** | str,  | str,  | The group of the classification. | [optional] 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The id of the detection object. | [optional] value must be a 32 bit integer
**probability** | decimal.Decimal, int,  | decimal.Decimal,  | The probability that the object found matches the classification. | [optional] value must be a 32 bit integer
**coordinates** | [**Coordinates**](Coordinates.md) | [**Coordinates**](Coordinates.md) |  | [optional] 
**type** | str,  | str,  | Used as a type discriminator for json to object conversion. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

