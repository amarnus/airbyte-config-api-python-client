# airbyte_config_api_client.model.web_backend_connection_read.WebBackendConnectionRead

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sourceId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**notifySchemaChanges** | bool,  | BoolClass,  |  | 
**destination** | [**DestinationRead**](DestinationRead.md) | [**DestinationRead**](DestinationRead.md) |  | 
**name** | str,  | str,  |  | 
**syncCatalog** | [**AirbyteCatalog**](AirbyteCatalog.md) | [**AirbyteCatalog**](AirbyteCatalog.md) |  | 
**connectionId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**isSyncing** | bool,  | BoolClass,  |  | 
**source** | [**SourceRead**](SourceRead.md) | [**SourceRead**](SourceRead.md) |  | 
**destinationId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**nonBreakingChangesPreference** | [**NonBreakingChangesPreference**](NonBreakingChangesPreference.md) | [**NonBreakingChangesPreference**](NonBreakingChangesPreference.md) |  | 
**schemaChange** | [**SchemaChange**](SchemaChange.md) | [**SchemaChange**](SchemaChange.md) |  | 
**status** | [**ConnectionStatus**](ConnectionStatus.md) | [**ConnectionStatus**](ConnectionStatus.md) |  | 
**namespaceDefinition** | [**NamespaceDefinitionType**](NamespaceDefinitionType.md) | [**NamespaceDefinitionType**](NamespaceDefinitionType.md) |  | [optional] 
**namespaceFormat** | str,  | str,  | Used when namespaceDefinition is &#x27;customformat&#x27;. If blank then behaves like namespaceDefinition &#x3D; &#x27;destination&#x27;. If \&quot;${SOURCE_NAMESPACE}\&quot; then behaves like namespaceDefinition &#x3D; &#x27;source&#x27;. | [optional] 
**prefix** | str,  | str,  | Prefix that will be prepended to the name of each stream when it is written to the destination. | [optional] 
**schedule** | [**ConnectionSchedule**](ConnectionSchedule.md) | [**ConnectionSchedule**](ConnectionSchedule.md) |  | [optional] 
**scheduleType** | [**ConnectionScheduleType**](ConnectionScheduleType.md) | [**ConnectionScheduleType**](ConnectionScheduleType.md) |  | [optional] 
**scheduleData** | [**ConnectionScheduleData**](ConnectionScheduleData.md) | [**ConnectionScheduleData**](ConnectionScheduleData.md) |  | [optional] 
**[operationIds](#operationIds)** | list, tuple,  | tuple,  |  | [optional] 
**[operations](#operations)** | list, tuple,  | tuple,  |  | [optional] 
**latestSyncJobCreatedAt** | decimal.Decimal, int,  | decimal.Decimal,  | epoch time of the latest sync job. null if no sync job has taken place. | [optional] value must be a 64 bit integer
**latestSyncJobStatus** | [**JobStatus**](JobStatus.md) | [**JobStatus**](JobStatus.md) |  | [optional] 
**resourceRequirements** | [**ResourceRequirements**](ResourceRequirements.md) | [**ResourceRequirements**](ResourceRequirements.md) |  | [optional] 
**catalogId** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**catalogDiff** | [**CatalogDiff**](CatalogDiff.md) | [**CatalogDiff**](CatalogDiff.md) |  | [optional] 
**geography** | [**Geography**](Geography.md) | [**Geography**](Geography.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# operationIds

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, uuid.UUID,  | str,  |  | value must be a uuid

# operations

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OperationRead**](OperationRead.md) | [**OperationRead**](OperationRead.md) | [**OperationRead**](OperationRead.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

