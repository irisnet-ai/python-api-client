# INImage

Configures your detection. As there are literally hundreds of parameters, INDefine uses prototypes to get usefull behaviour. This includes a default setting for parameters and rules that should be applied to images. You can combine multiple detections by using more than 1 prototype

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**proto** | **str** | Name of commonly used rule sets (prototypes). That can be used to speed up the setup process. * _nudityCheck_ - Commonly used prototype to check for nudity. * _ageVerification_ - Deprecated see &#39;ageEstimation&#39;. * _ageEstimation_ - Checks if there are children, adults or seniors recognizable. This is intended to be a suggestion to help you implement further steps. * _illegalSymbols_ - Checks for symbols that are not permitted in Germany. * _textRecognition_ - Checks for text occurrences. * _attributesCheck_ - Checks for attributes of a person (e.g. female, male, glasses, hair, etc). * _nippleCheck_ - Check for determining if the object recognized as breast has a nipple.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


