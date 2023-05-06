# airbyte_config_api_client.model.airbyte_stream.AirbyteStream

the immutable schema defined by the source

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | the immutable schema defined by the source | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**json_schema** | 
**name** | str,  | str,  | Stream&#x27;s name. | 
**[jsonSchema](#jsonSchema)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Stream schema using Json Schema specs. | [optional] 
**[supportedSyncModes](#supportedSyncModes)** | list, tuple,  | tuple,  |  | [optional] 
**sourceDefinedCursor** | bool,  | BoolClass,  | If the source defines the cursor field, then any other cursor field inputs will be ignored. If it does not, either the user_provided one is used, or the default one is used as a backup. | [optional] 
**[defaultCursorField](#defaultCursorField)** | list, tuple,  | tuple,  | Path to the field that will be used to determine if a record is new or modified since the last sync. If not provided by the source, the end user will have to specify the comparable themselves. | [optional] 
**[sourceDefinedPrimaryKey](#sourceDefinedPrimaryKey)** | list, tuple,  | tuple,  | If the source defines the primary key, paths to the fields that will be used as a primary key. If not provided by the source, the end user will have to specify the primary key themselves. | [optional] 
**namespace** | str,  | str,  | Optional Source-defined namespace. Airbyte streams from the same sources should have the same namespace. Currently only used by JDBC destinations to determine what schema to write to. | [optional] 

# jsonSchema

Stream schema using Json Schema specs.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Stream schema using Json Schema specs. | 

# supportedSyncModes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SyncMode**](SyncMode.md) | [**SyncMode**](SyncMode.md) | [**SyncMode**](SyncMode.md) |  | 

# defaultCursorField

Path to the field that will be used to determine if a record is new or modified since the last sync. If not provided by the source, the end user will have to specify the comparable themselves.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Path to the field that will be used to determine if a record is new or modified since the last sync. If not provided by the source, the end user will have to specify the comparable themselves. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# sourceDefinedPrimaryKey

If the source defines the primary key, paths to the fields that will be used as a primary key. If not provided by the source, the end user will have to specify the primary key themselves.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | If the source defines the primary key, paths to the fields that will be used as a primary key. If not provided by the source, the end user will have to specify the primary key themselves. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | list, tuple,  | tuple,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

