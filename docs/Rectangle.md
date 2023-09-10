# Rectangle

Describes the bounds of a rectangle starting from the center.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x0** | **float** | The center of the rectangle in the horizontal (x) direction. | [optional] 
**y0** | **float** | The center of the rectangle in the vertical (y) direction. | [optional] 
**width** | **float** | The total width of the rectangle in the horizontal (x) direction. Use _x0 - width / 2_ and _x0 + width / 2_ to get the left and right edges of the rectangle. | [optional] 
**height** | **float** | The total height of the rectangle in the vertical (y) direction. Use _y0 - height / 2_ and _y0 + height / 2_ to get the top and bottom edges of the rectangle. | [optional] 

## Example

```python
from irisnet_client.models.rectangle import Rectangle

# TODO update the JSON string below
json = "{}"
# create an instance of Rectangle from a JSON string
rectangle_instance = Rectangle.from_json(json)
# print the JSON string representation of the object
print Rectangle.to_json()

# convert the object into a dict
rectangle_dict = rectangle_instance.to_dict()
# create an instance of Rectangle from a dict
rectangle_form_dict = rectangle.from_dict(rectangle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


