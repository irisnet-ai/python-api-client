# irisnet_client.model.rectangle.Rectangle

Describes the bounds of a rectangle starting from the center.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Describes the bounds of a rectangle starting from the center. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**x0** | decimal.Decimal, int, float,  | decimal.Decimal,  | The center of the rectangle in the horizontal (x) direction. | [optional] value must be a 32 bit float
**y0** | decimal.Decimal, int, float,  | decimal.Decimal,  | The center of the rectangle in the vertical (y) direction. | [optional] value must be a 32 bit float
**width** | decimal.Decimal, int, float,  | decimal.Decimal,  | The total width of the rectangle in the horizontal (x) direction. Use _x0 - width / 2_ and _x0 + width / 2_ to get the left and right edges of the rectangle. | [optional] value must be a 32 bit float
**height** | decimal.Decimal, int, float,  | decimal.Decimal,  | The total height of the rectangle in the vertical (y) direction. Use _y0 - height / 2_ and _y0 + height / 2_ to get the top and bottom edges of the rectangle. | [optional] value must be a 32 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

