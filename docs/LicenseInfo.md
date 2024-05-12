# LicenseInfo

Describes the current balance of the given license key. A key has a certain amount of credits that can be used for any kind of AI recognition. The license key is invalid, when all of the credits have been used, the license was disabled or expired.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credits_used** | **int** | Credits used for the license key. | [optional] 
**credits_remaining** | **int** | Credits remaining for the license key. | [optional] 
**total_credits** | **int** | Total credits contained within the license key. | [optional] 
**license_key** | **str** | The license key | [optional] 
**privileges** | **Dict[str, str]** | A map of privileges | [optional] 

## Example

```python
from irisnet_client.models.license_info import LicenseInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseInfo from a JSON string
license_info_instance = LicenseInfo.from_json(json)
# print the JSON string representation of the object
print(LicenseInfo.to_json())

# convert the object into a dict
license_info_dict = license_info_instance.to_dict()
# create an instance of LicenseInfo from a dict
license_info_from_dict = LicenseInfo.from_dict(license_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


