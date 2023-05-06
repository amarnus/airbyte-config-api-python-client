# airbyte_config_api_client.model.attempt_failure_reason.AttemptFailureReason

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**timestamp** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**failureOrigin** | [**AttemptFailureOrigin**](AttemptFailureOrigin.md) | [**AttemptFailureOrigin**](AttemptFailureOrigin.md) |  | [optional] 
**failureType** | [**AttemptFailureType**](AttemptFailureType.md) | [**AttemptFailureType**](AttemptFailureType.md) |  | [optional] 
**externalMessage** | str,  | str,  |  | [optional] 
**internalMessage** | str,  | str,  |  | [optional] 
**stacktrace** | str,  | str,  |  | [optional] 
**retryable** | bool,  | BoolClass,  | True if it is known that retrying may succeed, e.g. for a transient failure. False if it is known that a retry will not succeed, e.g. for a configuration issue. If not set, retryable status is not well known. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

