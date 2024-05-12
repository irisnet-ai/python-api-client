# BreastDetection

Contains further characteristics particular to _breast_ detection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**List[BaseAttribute]**](BaseAttribute.md) | Attributes characterizing the _breast_ detection. Mainly contains attributes that were activated with the _nippleCheck_ prototype. | [optional] 

## Example

```python
from irisnet_client.models.breast_detection import BreastDetection

# TODO update the JSON string below
json = "{}"
# create an instance of BreastDetection from a JSON string
breast_detection_instance = BreastDetection.from_json(json)
# print the JSON string representation of the object
print(BreastDetection.to_json())

# convert the object into a dict
breast_detection_dict = breast_detection_instance.to_dict()
# create an instance of BreastDetection from a dict
breast_detection_from_dict = BreastDetection.from_dict(breast_detection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


