# airbyte_config_api_client.model.synchronous_job_read.SynchronousJobRead

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**createdAt** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**endedAt** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**id** | str, uuid.UUID,  | str,  |  | value must be a uuid
**configType** | [**JobConfigType**](JobConfigType.md) | [**JobConfigType**](JobConfigType.md) |  | 
**succeeded** | bool,  | BoolClass,  |  | 
**configId** | str,  | str,  | only present if a config id was provided. | [optional] 
**connectorConfigurationUpdated** | bool,  | BoolClass,  |  | [optional] if omitted the server will use the default value of False
**logs** | [**LogRead**](LogRead.md) | [**LogRead**](LogRead.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

