# irisnet_client.model.config.Config

Can be used to set a multitude of pre-defined commonly used rules without the need of specifying each parameter set.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Can be used to set a multitude of pre-defined commonly used rules without the need of specifying each parameter set. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str, uuid.UUID,  | str,  | The unique identifier for the AI configuration. Use this for any check operation to tell the AI how to behave. | [optional] value must be a uuid
**[prototypes](#prototypes)** | list, tuple,  | tuple,  | Configures your detection. As there are literally hundreds of parameters, prototypes can be used to get useful behaviour. This includes a default setting for parameters and rules that should be applied to the check operations. You can use multiple prototypes for a single check operation. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# prototypes

Configures your detection. As there are literally hundreds of parameters, prototypes can be used to get useful behaviour. This includes a default setting for parameters and rules that should be applied to the check operations. You can use multiple prototypes for a single check operation.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Configures your detection. As there are literally hundreds of parameters, prototypes can be used to get useful behaviour. This includes a default setting for parameters and rules that should be applied to the check operations. You can use multiple prototypes for a single check operation. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Name of commonly used rule sets (prototypes). That can be used to speed up the setup process. * _nudityCheck_ - Commonly used prototype to check for nudity. * _ageEstimation_ - Checks if there are children, adults or seniors recognizable. This is intended to be a suggestion to help you implement further steps. * _illegalSymbols_ - Checks for symbols that are not permitted in Germany. * _textRecognition_ - Checks for text occurrences. * _attributesCheck_ - Checks for attributes of a person (e.g. female, male, glasses, hair, etc). * _bodyAttributes_ - Checks for attributes of the persons body. * _nippleCheck_ - Check for determining if the object recognized as breast has a nipple. * _unwantedSubstances_ - Check for undesired or unwanted substances. * _violenceCheck_ - Checks for recognizing weapons, camouflage, etc.  | must be one of ["nudityCheck", "ageVerification", "ageEstimation", "illegalSymbols", "textRecognition", "attributesCheck", "bodyAttributes", "nippleCheck", "unwantedSubstances", "violenceCheck", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

