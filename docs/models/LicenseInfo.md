# irisnet_client.model.license_info.LicenseInfo

Describes the current balance of the given license key. A key has a certain amount of credits that can be used for any kind of AI recognition. The license key is invalid, when all of the credits have been used, the license was disabled or expired.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Describes the current balance of the given license key. A key has a certain amount of credits that can be used for any kind of AI recognition. The license key is invalid, when all of the credits have been used, the license was disabled or expired. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**creditsUsed** | decimal.Decimal, int,  | decimal.Decimal,  | Credits used for the license key. | [optional] value must be a 32 bit integer
**creditsRemaining** | decimal.Decimal, int,  | decimal.Decimal,  | Credits remaining for the license key. | [optional] value must be a 32 bit integer
**totalCredits** | decimal.Decimal, int,  | decimal.Decimal,  | Total credits contained within the license key. | [optional] value must be a 32 bit integer
**licenseKey** | str,  | str,  | The license key | [optional] 
**[privileges](#privileges)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | A map of privileges | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# privileges

A map of privileges

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A map of privileges | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type A map of privileges | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

