# airbyte_config_api_client.model.source_definition_specification_read.SourceDefinitionSpecificationRead

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sourceDefinitionId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**jobInfo** | [**SynchronousJobRead**](SynchronousJobRead.md) | [**SynchronousJobRead**](SynchronousJobRead.md) |  | 
**documentationUrl** | str,  | str,  |  | [optional] 
**[connectionSpecification](#connectionSpecification)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The specification for what values are required to configure the sourceDefinition. | [optional] 
**authSpecification** | [**AuthSpecification**](AuthSpecification.md) | [**AuthSpecification**](AuthSpecification.md) |  | [optional] 
**advancedAuth** | [**AdvancedAuth**](AdvancedAuth.md) | [**AdvancedAuth**](AdvancedAuth.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# connectionSpecification

The specification for what values are required to configure the sourceDefinition.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The specification for what values are required to configure the sourceDefinition. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

