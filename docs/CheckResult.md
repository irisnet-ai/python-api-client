# CheckResult

The root object returned after a check operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | [**Summary**](Summary.md) |  | [optional] 
**encodings** | [**List[Encoded]**](Encoded.md) |  | [optional] 
**broken_rules** | [**List[BrokenRule]**](BrokenRule.md) |  | [optional] 
**detections** | [**List[BaseDetection]**](BaseDetection.md) |  | [optional] 
**events** | [**List[Event]**](Event.md) |  | [optional] 
**notifications** | [**List[ApiNotice]**](ApiNotice.md) |  | [optional] 
**check_id** | **str** | The id of the async running check | [optional] 

## Example

```python
from irisnet_client.models.check_result import CheckResult

# TODO update the JSON string below
json = "{}"
# create an instance of CheckResult from a JSON string
check_result_instance = CheckResult.from_json(json)
# print the JSON string representation of the object
print(CheckResult.to_json())

# convert the object into a dict
check_result_dict = check_result_instance.to_dict()
# create an instance of CheckResult from a dict
check_result_from_dict = CheckResult.from_dict(check_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


