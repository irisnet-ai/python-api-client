# Config

Can be used to set a multitude of pre-defined commonly used rules without the need of specifying each parameter set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the AI configuration. Use this for any check operation to tell the AI how to behave. | [optional] 
**prototypes** | **List[str]** | Configures your detection. As there are literally hundreds of parameters, prototypes can be used to get useful behaviour. This includes a default setting for parameters and rules that should be applied to the check operations. You can use multiple prototypes for a single check operation. | [optional] 

## Example

```python
from irisnet_client.models.config import Config

# TODO update the JSON string below
json = "{}"
# create an instance of Config from a JSON string
config_instance = Config.from_json(json)
# print the JSON string representation of the object
print(Config.to_json())

# convert the object into a dict
config_dict = config_instance.to_dict()
# create an instance of Config from a dict
config_from_dict = Config.from_dict(config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


