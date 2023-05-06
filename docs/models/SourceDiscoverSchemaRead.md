# airbyte_config_api_client.model.source_discover_schema_read.SourceDiscoverSchemaRead

Returns the results of a discover catalog job. If the job was not successful, the catalog field will not be present. jobInfo will aways be present and its status be used to determine if the job was successful or not.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Returns the results of a discover catalog job. If the job was not successful, the catalog field will not be present. jobInfo will aways be present and its status be used to determine if the job was successful or not. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**jobInfo** | [**SynchronousJobRead**](SynchronousJobRead.md) | [**SynchronousJobRead**](SynchronousJobRead.md) |  | 
**catalog** | [**AirbyteCatalog**](AirbyteCatalog.md) | [**AirbyteCatalog**](AirbyteCatalog.md) |  | [optional] 
**catalogId** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**catalogDiff** | [**CatalogDiff**](CatalogDiff.md) | [**CatalogDiff**](CatalogDiff.md) |  | [optional] 
**breakingChange** | bool,  | BoolClass,  |  | [optional] 
**connectionStatus** | [**ConnectionStatus**](ConnectionStatus.md) | [**ConnectionStatus**](ConnectionStatus.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

