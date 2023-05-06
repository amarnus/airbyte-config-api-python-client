# airbyte_config_api_client.model.source_read.SourceRead

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sourceId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**connectionConfiguration** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The values required to configure the source. The schema for this must match the schema return by source_definition_specifications/get for the source. | 
**name** | str,  | str,  |  | 
**sourceDefinitionId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**sourceName** | str,  | str,  |  | 
**workspaceId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**icon** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

