# INDefault

An element that defines some overall defaults if needed. These will be applied on every parameter set. Single parameters can be still overwritten by their respective attributes within the 'inParam' element.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thresh** | **float** | Threshold when an object can be recognized. Lowering the value will increase the probability of recognizing objects. A threshhold of 0.5 would mean, that 50% of an object like a face must be visible, to be detected.Setting the value too low however, can cause false positives. | [optional] [default to 0.5]
**grey** | **int** | A grey scale color to use for frame or masking. &#39;0&#39; will represent black, while the maximum &#39;255&#39; will be white. | [optional] [default to 127]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


