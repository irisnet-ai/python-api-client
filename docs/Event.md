# Event

Describes an event that lead to a broken rule.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification** | **str** | The classification of the recognized object. | [optional] 
**group** | **str** | The group of the classification. | [optional] 
**start** | **float** | The start in seconds where the classification object is found. | [optional] 
**duration** | **float** | The duration of the event in seconds until the classification object is no longer in frame. The current event is ongoing if the duration is not set. | [optional] 
**severity** | **int** | The severity of the classification object set while configuring the AI. | [optional] 

## Example

```python
from irisnet_client.models.event import Event

# TODO update the JSON string below
json = "{}"
# create an instance of Event from a JSON string
event_instance = Event.from_json(json)
# print the JSON string representation of the object
print Event.to_json()

# convert the object into a dict
event_dict = event_instance.to_dict()
# create an instance of Event from a dict
event_form_dict = event.from_dict(event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


