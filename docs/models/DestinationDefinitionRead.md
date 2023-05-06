# airbyte_config_api_client.model.destination_definition_read.DestinationDefinitionRead

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**documentationUrl** | str,  | str,  |  | 
**dockerImageTag** | str,  | str,  |  | 
**dockerRepository** | str,  | str,  |  | 
**supportsDbt** | bool,  | BoolClass,  | an optional flag indicating whether DBT is used in the normalization. If the flag value is NULL - DBT is not used. | 
**name** | str,  | str,  |  | 
**normalizationConfig** | [**NormalizationDestinationDefinitionConfig**](NormalizationDestinationDefinitionConfig.md) | [**NormalizationDestinationDefinitionConfig**](NormalizationDestinationDefinitionConfig.md) |  | 
**destinationDefinitionId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**icon** | str,  | str,  |  | [optional] 
**protocolVersion** | str,  | str,  | The Airbyte Protocol version supported by the connector | [optional] 
**releaseStage** | [**ReleaseStage**](ReleaseStage.md) | [**ReleaseStage**](ReleaseStage.md) |  | [optional] 
**releaseDate** | str, date,  | str,  | The date when this connector was first released, in yyyy-mm-dd format. | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**resourceRequirements** | [**ActorDefinitionResourceRequirements**](ActorDefinitionResourceRequirements.md) | [**ActorDefinitionResourceRequirements**](ActorDefinitionResourceRequirements.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

