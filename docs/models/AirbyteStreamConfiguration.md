# airbyte_config_api_client.model.airbyte_stream_configuration.AirbyteStreamConfiguration

the mutable part of the stream to configure the destination

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | the mutable part of the stream to configure the destination | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**syncMode** | [**SyncMode**](SyncMode.md) | [**SyncMode**](SyncMode.md) |  | 
**destinationSyncMode** | [**DestinationSyncMode**](DestinationSyncMode.md) | [**DestinationSyncMode**](DestinationSyncMode.md) |  | 
**[cursorField](#cursorField)** | list, tuple,  | tuple,  | Path to the field that will be used to determine if a record is new or modified since the last sync. This field is REQUIRED if &#x60;sync_mode&#x60; is &#x60;incremental&#x60;. Otherwise it is ignored. | [optional] 
**[primaryKey](#primaryKey)** | list, tuple,  | tuple,  | Paths to the fields that will be used as primary key. This field is REQUIRED if &#x60;destination_sync_mode&#x60; is &#x60;*_dedup&#x60;. Otherwise it is ignored. | [optional] 
**aliasName** | str,  | str,  | Alias name to the stream to be used in the destination | [optional] 
**selected** | bool,  | BoolClass,  | If this is true, the stream is selected with all of its properties. For new connections, this considers if the stream is suggested or not | [optional] 
**suggested** | bool,  | BoolClass,  | Does the connector suggest that this stream be enabled by default? | [optional] 
**fieldSelectionEnabled** | bool,  | BoolClass,  | Whether field selection should be enabled. If this is true, only the properties in &#x60;selectedFields&#x60; will be included. | [optional] 
**[selectedFields](#selectedFields)** | list, tuple,  | tuple,  | Paths to the fields that will be included in the configured catalog. This must be set if &#x60;fieldSelectedEnabled&#x60; is set. An empty list indicates that no properties will be included. | [optional] 

# cursorField

Path to the field that will be used to determine if a record is new or modified since the last sync. This field is REQUIRED if `sync_mode` is `incremental`. Otherwise it is ignored.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Path to the field that will be used to determine if a record is new or modified since the last sync. This field is REQUIRED if &#x60;sync_mode&#x60; is &#x60;incremental&#x60;. Otherwise it is ignored. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# primaryKey

Paths to the fields that will be used as primary key. This field is REQUIRED if `destination_sync_mode` is `*_dedup`. Otherwise it is ignored.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Paths to the fields that will be used as primary key. This field is REQUIRED if &#x60;destination_sync_mode&#x60; is &#x60;*_dedup&#x60;. Otherwise it is ignored. | 

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

# selectedFields

Paths to the fields that will be included in the configured catalog. This must be set if `fieldSelectedEnabled` is set. An empty list indicates that no properties will be included.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Paths to the fields that will be included in the configured catalog. This must be set if &#x60;fieldSelectedEnabled&#x60; is set. An empty list indicates that no properties will be included. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SelectedFieldInfo**](SelectedFieldInfo.md) | [**SelectedFieldInfo**](SelectedFieldInfo.md) | [**SelectedFieldInfo**](SelectedFieldInfo.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

