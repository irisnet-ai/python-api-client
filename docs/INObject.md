# INObject

Describes a rectangle that stretches around the recognized object. This is useful when redacting or blurring certain recognized objects. Each object contains the name of the classification and coordinates for a rectangle around the recognized object. The origin point (y = 0.0, x = 0.0) of the coordinate system is on the top left of the of the source material. The bottom right of the source is always y = 1 and x = 1.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**in_class** | **str** | The classification of the recognized object. | [optional] 
**in_group** | **str** | The group of the classification. | [optional] 
**in_id** | **str** | The group of the classification. | [optional] 
**color** | **str** | The color of the object, e.g. the color of the hair. Is only available for certain classification objects. See list below:  * _hair_ - black, brown, blonde, grey, red, other | [optional] 
**style** | **str** | The style attribute of the object, e.g. the style of the hair. Is only available for certain classification objects. See list below:  * _hair_ - longHaired, shortHaired | [optional] 
**x0** | **float** | The center of the rectangle in the horizontal (x) direction. | [optional] 
**y0** | **float** | The center of the rectangle in the vertical (y) direction. | [optional] 
**width** | **float** | The total width of the rectangle in the horizontal (x) direction. Use _x0 - width / 2_ and _x0 + width / 2_ to get the left and right edges of the rectangle. | [optional] 
**height** | **float** | The total height of the rectangle in the vertical (y) direction. Use _y0 - height / 2_ and _y0 + height / 2_ to get the top and bottom edges of the rectangle. | [optional] 
**probability** | **int** | The probability that the object found matches the classification. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


