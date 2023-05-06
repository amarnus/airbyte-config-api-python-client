# airbyte_config_api_client.model.workspace_create.WorkspaceCreate

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | 
**email** | str,  | str,  |  | [optional] 
**anonymousDataCollection** | bool,  | BoolClass,  |  | [optional] 
**news** | bool,  | BoolClass,  |  | [optional] 
**securityUpdates** | bool,  | BoolClass,  |  | [optional] 
**[notifications](#notifications)** | list, tuple,  | tuple,  |  | [optional] 
**displaySetupWizard** | bool,  | BoolClass,  |  | [optional] 
**defaultGeography** | [**Geography**](Geography.md) | [**Geography**](Geography.md) |  | [optional] 
**[webhookConfigs](#webhookConfigs)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# notifications

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Notification**](Notification.md) | [**Notification**](Notification.md) | [**Notification**](Notification.md) |  | 

# webhookConfigs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**WebhookConfigWrite**](WebhookConfigWrite.md) | [**WebhookConfigWrite**](WebhookConfigWrite.md) | [**WebhookConfigWrite**](WebhookConfigWrite.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

