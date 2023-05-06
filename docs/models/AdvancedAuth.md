# airbyte_config_api_client.model.advanced_auth.AdvancedAuth

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**authFlowType** | str,  | str,  |  | [optional] must be one of ["oauth2.0", "oauth1.0", ] 
**[predicateKey](#predicateKey)** | list, tuple,  | tuple,  | Json Path to a field in the connectorSpecification that should exist for the advanced auth to be applicable. | [optional] 
**predicateValue** | str,  | str,  | Value of the predicate_key fields for the advanced auth to be applicable. | [optional] 
**oauthConfigSpecification** | [**OAuthConfigSpecification**](OAuthConfigSpecification.md) | [**OAuthConfigSpecification**](OAuthConfigSpecification.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# predicateKey

Json Path to a field in the connectorSpecification that should exist for the advanced auth to be applicable.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Json Path to a field in the connectorSpecification that should exist for the advanced auth to be applicable. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

