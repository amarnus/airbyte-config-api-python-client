# airbyte_config_api_client.model.destination_definition_specification_read.DestinationDefinitionSpecificationRead

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**destinationDefinitionId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**jobInfo** | [**SynchronousJobRead**](SynchronousJobRead.md) | [**SynchronousJobRead**](SynchronousJobRead.md) |  | 
**documentationUrl** | str,  | str,  |  | [optional] 
**connectionSpecification** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The specification for what values are required to configure the destinationDefinition. | [optional] 
**authSpecification** | [**AuthSpecification**](AuthSpecification.md) | [**AuthSpecification**](AuthSpecification.md) |  | [optional] 
**advancedAuth** | [**AdvancedAuth**](AdvancedAuth.md) | [**AdvancedAuth**](AdvancedAuth.md) |  | [optional] 
**[supportedDestinationSyncModes](#supportedDestinationSyncModes)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# supportedDestinationSyncModes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**DestinationSyncMode**](DestinationSyncMode.md) | [**DestinationSyncMode**](DestinationSyncMode.md) | [**DestinationSyncMode**](DestinationSyncMode.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

