# airbyte_config_api_client.model.operator_configuration.OperatorConfiguration

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**operatorType** | [**OperatorType**](OperatorType.md) | [**OperatorType**](OperatorType.md) |  | 
**normalization** | [**OperatorNormalization**](OperatorNormalization.md) | [**OperatorNormalization**](OperatorNormalization.md) |  | [optional] 
**dbt** | [**OperatorDbt**](OperatorDbt.md) | [**OperatorDbt**](OperatorDbt.md) |  | [optional] 
**webhook** | [**OperatorWebhook**](OperatorWebhook.md) | [**OperatorWebhook**](OperatorWebhook.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

