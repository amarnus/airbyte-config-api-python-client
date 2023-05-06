# airbyte_config_api_client.model.stream_transform.StreamTransform

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**streamDescriptor** | [**StreamDescriptor**](StreamDescriptor.md) | [**StreamDescriptor**](StreamDescriptor.md) |  | 
**transformType** | str,  | str,  |  | must be one of ["add_stream", "remove_stream", "update_stream", ] 
**[updateStream](#updateStream)** | list, tuple,  | tuple,  | list of field transformations. order does not matter. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# updateStream

list of field transformations. order does not matter.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | list of field transformations. order does not matter. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FieldTransform**](FieldTransform.md) | [**FieldTransform**](FieldTransform.md) | [**FieldTransform**](FieldTransform.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

