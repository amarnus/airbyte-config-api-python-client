# airbyte_config_api_client.model.operator_webhook.OperatorWebhook

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**webhookConfigId** | str, uuid.UUID,  | str,  | The id of the webhook configs to use from the workspace. | [optional] value must be a uuid
**webhookType** | str,  | str,  |  | [optional] must be one of ["dbtCloud", ] 
**[dbtCloud](#dbtCloud)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**executionUrl** | str,  | str,  | DEPRECATED. Populate dbtCloud instead. | [optional] 
**executionBody** | str,  | str,  | DEPRECATED. Populate dbtCloud instead. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# dbtCloud

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**accountId** | decimal.Decimal, int,  | decimal.Decimal,  | The account id associated with the job | 
**jobId** | decimal.Decimal, int,  | decimal.Decimal,  | The job id associated with the job | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

