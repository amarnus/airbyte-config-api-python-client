# airbyte_config_api_client.model.workspace_read.WorkspaceRead

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**initialSetupComplete** | bool,  | BoolClass,  |  | 
**customerId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**name** | str,  | str,  |  | 
**slug** | str,  | str,  |  | 
**workspaceId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**email** | str,  | str,  |  | [optional] 
**displaySetupWizard** | bool,  | BoolClass,  |  | [optional] 
**anonymousDataCollection** | bool,  | BoolClass,  |  | [optional] 
**news** | bool,  | BoolClass,  |  | [optional] 
**securityUpdates** | bool,  | BoolClass,  |  | [optional] 
**[notifications](#notifications)** | list, tuple,  | tuple,  |  | [optional] 
**firstCompletedSync** | bool,  | BoolClass,  |  | [optional] 
**feedbackDone** | bool,  | BoolClass,  |  | [optional] 
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
[**WebhookConfigRead**](WebhookConfigRead.md) | [**WebhookConfigRead**](WebhookConfigRead.md) | [**WebhookConfigRead**](WebhookConfigRead.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

