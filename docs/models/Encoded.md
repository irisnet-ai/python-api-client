# irisnet_client.model.encoded.Encoded

Contains the resulting media as base64 encoded string or an URL to download that media.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Contains the resulting media as base64 encoded string or an URL to download that media. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The original filename of the image or video. | [optional] 
**data** | bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  | The encoded media in base64 format. | [optional] 
**downloadUrl** | str,  | str,  | A one time URL to download the resulting media. The URL is only valid for 24 hours. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

