# airbyte_config_api_client.model.field_transform.FieldTransform

Describes the difference between two Streams.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Describes the difference between two Streams. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**fieldName** | [**FieldName**](FieldName.md) | [**FieldName**](FieldName.md) |  | 
**transformType** | str,  | str,  |  | must be one of ["add_field", "remove_field", "update_field_schema", ] 
**breaking** | bool,  | BoolClass,  |  | 
**addField** | [**FieldAdd**](FieldAdd.md) | [**FieldAdd**](FieldAdd.md) |  | [optional] 
**removeField** | [**FieldRemove**](FieldRemove.md) | [**FieldRemove**](FieldRemove.md) |  | [optional] 
**updateFieldSchema** | [**FieldSchemaUpdate**](FieldSchemaUpdate.md) | [**FieldSchemaUpdate**](FieldSchemaUpdate.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

