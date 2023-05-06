# airbyte_config_api_client.model.connection_state.ConnectionState

Contains the state for a connection. The stateType field identifies what type of state it is. Only the field corresponding to that type will be set, the rest will be null. If stateType=not_set, then none of the fields will be set.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Contains the state for a connection. The stateType field identifies what type of state it is. Only the field corresponding to that type will be set, the rest will be null. If stateType&#x3D;not_set, then none of the fields will be set. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**stateType** | [**ConnectionStateType**](ConnectionStateType.md) | [**ConnectionStateType**](ConnectionStateType.md) |  | 
**connectionId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**[state](#state)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[streamState](#streamState)** | list, tuple,  | tuple,  |  | [optional] 
**globalState** | [**GlobalState**](GlobalState.md) | [**GlobalState**](GlobalState.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# state

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# streamState

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**StreamState**](StreamState.md) | [**StreamState**](StreamState.md) | [**StreamState**](StreamState.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

