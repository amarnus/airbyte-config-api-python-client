# airbyte_config_api_client.model.db_migration_read.DbMigrationRead

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**migrationDescription** | str,  | str,  |  | 
**migrationVersion** | str,  | str,  |  | 
**migrationType** | str,  | str,  |  | 
**migrationState** | [**DbMigrationState**](DbMigrationState.md) | [**DbMigrationState**](DbMigrationState.md) |  | [optional] 
**migratedBy** | str,  | str,  |  | [optional] 
**migratedAt** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**migrationScript** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

