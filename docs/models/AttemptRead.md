# airbyte_config_api_client.model.attempt_read.AttemptRead

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**createdAt** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**status** | [**AttemptStatus**](AttemptStatus.md) | [**AttemptStatus**](AttemptStatus.md) |  | 
**updatedAt** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**endedAt** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**bytesSynced** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**recordsSynced** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**totalStats** | [**AttemptStats**](AttemptStats.md) | [**AttemptStats**](AttemptStats.md) |  | [optional] 
**[streamStats](#streamStats)** | list, tuple,  | tuple,  |  | [optional] 
**failureSummary** | [**AttemptFailureSummary**](AttemptFailureSummary.md) | [**AttemptFailureSummary**](AttemptFailureSummary.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# streamStats

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AttemptStreamStats**](AttemptStreamStats.md) | [**AttemptStreamStats**](AttemptStreamStats.md) | [**AttemptStreamStats**](AttemptStreamStats.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

