# INObject

Describes a rectangle that stretches around the recognized object. This is useful when redacting or blurring certain recognized objects. Each object contains the name of the classification and coordinates for a rectangle around the recognized object. The origin point (y = 0.0, x = 0.0) of the coordinate system is on the top left of the of the source material. The bottom right of the source is always y = 1 and x = 1.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**in_class** | **str** | The classification of the recognized object. | [optional] 
**in_group** | **str** | The group of the classification. | [optional] 
**in_id** | **str** | The group of the classification. | [optional] 
**x0** | **float** | The starting point of the rectangle in the vertical (x) direction. | [optional] 
**y0** | **float** | The starting point of the rectangle in the horizontal (y) direction. | [optional] 
**width** | **float** | The distance from the starting point (y0) to end the rectangle in the horizontal direction. | [optional] 
**height** | **float** | The distance from the starting point (x0) to end the rectangle in the vertical direction. | [optional] 
**probability** | **int** | The probability that the object found matches the classification. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


