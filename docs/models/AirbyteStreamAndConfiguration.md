# airbyte_config_api_client.model.airbyte_stream_and_configuration.AirbyteStreamAndConfiguration

each stream is split in two parts; the immutable schema from source and mutable configuration for destination

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | each stream is split in two parts; the immutable schema from source and mutable configuration for destination | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**stream** | [**AirbyteStream**](AirbyteStream.md) | [**AirbyteStream**](AirbyteStream.md) |  | [optional] 
**config** | [**AirbyteStreamConfiguration**](AirbyteStreamConfiguration.md) | [**AirbyteStreamConfiguration**](AirbyteStreamConfiguration.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

