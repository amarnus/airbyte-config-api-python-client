# airbyte_config_api_client.model.web_backend_connection_list_item.WebBackendConnectionListItem

Information about a connection that shows up in the connection list view.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Information about a connection that shows up in the connection list view. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**destination** | [**DestinationSnippetRead**](DestinationSnippetRead.md) | [**DestinationSnippetRead**](DestinationSnippetRead.md) |  | 
**name** | str,  | str,  |  | 
**connectionId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**isSyncing** | bool,  | BoolClass,  |  | 
**source** | [**SourceSnippetRead**](SourceSnippetRead.md) | [**SourceSnippetRead**](SourceSnippetRead.md) |  | 
**schemaChange** | [**SchemaChange**](SchemaChange.md) | [**SchemaChange**](SchemaChange.md) |  | 
**status** | [**ConnectionStatus**](ConnectionStatus.md) | [**ConnectionStatus**](ConnectionStatus.md) |  | 
**scheduleType** | [**ConnectionScheduleType**](ConnectionScheduleType.md) | [**ConnectionScheduleType**](ConnectionScheduleType.md) |  | [optional] 
**scheduleData** | [**ConnectionScheduleData**](ConnectionScheduleData.md) | [**ConnectionScheduleData**](ConnectionScheduleData.md) |  | [optional] 
**latestSyncJobCreatedAt** | decimal.Decimal, int,  | decimal.Decimal,  | epoch time of the latest sync job. null if no sync job has taken place. | [optional] value must be a 64 bit integer
**latestSyncJobStatus** | [**JobStatus**](JobStatus.md) | [**JobStatus**](JobStatus.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

