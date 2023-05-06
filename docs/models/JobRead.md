# airbyte_config_api_client.model.job_read.JobRead

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**createdAt** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**configId** | str,  | str,  |  | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**configType** | [**JobConfigType**](JobConfigType.md) | [**JobConfigType**](JobConfigType.md) |  | 
**status** | [**JobStatus**](JobStatus.md) | [**JobStatus**](JobStatus.md) |  | 
**updatedAt** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**startedAt** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**resetConfig** | [**ResetConfig**](ResetConfig.md) | [**ResetConfig**](ResetConfig.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

