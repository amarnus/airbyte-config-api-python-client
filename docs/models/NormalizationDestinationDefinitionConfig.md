# airbyte_config_api_client.model.normalization_destination_definition_config.NormalizationDestinationDefinitionConfig

describes a normalization config for destination definition

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | describes a normalization config for destination definition | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**supported** | bool,  | BoolClass,  | whether the destination definition supports normalization. | if omitted the server will use the default value of False
**normalizationRepository** | str,  | str,  | a field indicating the name of the repository to be used for normalization. If the value of the flag is NULL - normalization is not used. | [optional] 
**normalizationTag** | str,  | str,  | a field indicating the tag of the docker repository to be used for normalization. | [optional] 
**normalizationIntegrationType** | str,  | str,  | a field indicating the type of integration dialect to use for normalization. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

