# airbyte_config_api_client.model.web_backend_connection_create.WebBackendConnectionCreate

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sourceId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**destinationId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**status** | [**ConnectionStatus**](ConnectionStatus.md) | [**ConnectionStatus**](ConnectionStatus.md) |  | 
**name** | str,  | str,  | Optional name of the connection | [optional] 
**namespaceDefinition** | [**NamespaceDefinitionType**](NamespaceDefinitionType.md) | [**NamespaceDefinitionType**](NamespaceDefinitionType.md) |  | [optional] 
**namespaceFormat** | str,  | str,  | Used when namespaceDefinition is &#x27;customformat&#x27;. If blank then behaves like namespaceDefinition &#x3D; &#x27;destination&#x27;. If \&quot;${SOURCE_NAMESPACE}\&quot; then behaves like namespaceDefinition &#x3D; &#x27;source&#x27;. | [optional] 
**prefix** | str,  | str,  | Prefix that will be prepended to the name of each stream when it is written to the destination. | [optional] 
**[operationIds](#operationIds)** | list, tuple,  | tuple,  |  | [optional] 
**syncCatalog** | [**AirbyteCatalog**](AirbyteCatalog.md) | [**AirbyteCatalog**](AirbyteCatalog.md) |  | [optional] 
**schedule** | [**ConnectionSchedule**](ConnectionSchedule.md) | [**ConnectionSchedule**](ConnectionSchedule.md) |  | [optional] 
**scheduleType** | [**ConnectionScheduleType**](ConnectionScheduleType.md) | [**ConnectionScheduleType**](ConnectionScheduleType.md) |  | [optional] 
**scheduleData** | [**ConnectionScheduleData**](ConnectionScheduleData.md) | [**ConnectionScheduleData**](ConnectionScheduleData.md) |  | [optional] 
**resourceRequirements** | [**ResourceRequirements**](ResourceRequirements.md) | [**ResourceRequirements**](ResourceRequirements.md) |  | [optional] 
**[operations](#operations)** | list, tuple,  | tuple,  |  | [optional] 
**sourceCatalogId** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**geography** | [**Geography**](Geography.md) | [**Geography**](Geography.md) |  | [optional] 
**nonBreakingChangesPreference** | [**NonBreakingChangesPreference**](NonBreakingChangesPreference.md) | [**NonBreakingChangesPreference**](NonBreakingChangesPreference.md) |  | [optional] 
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
[**OperationCreate**](OperationCreate.md) | [**OperationCreate**](OperationCreate.md) | [**OperationCreate**](OperationCreate.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

