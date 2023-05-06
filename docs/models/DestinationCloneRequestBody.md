# airbyte_config_api_client.model.destination_clone_request_body.DestinationCloneRequestBody

The values required to configure the destination. The schema for this should have an id of the existing destination along with the configuration you want to change in case.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The values required to configure the destination. The schema for this should have an id of the existing destination along with the configuration you want to change in case. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**destinationCloneId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**destinationConfiguration** | [**DestinationCloneConfiguration**](DestinationCloneConfiguration.md) | [**DestinationCloneConfiguration**](DestinationCloneConfiguration.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

