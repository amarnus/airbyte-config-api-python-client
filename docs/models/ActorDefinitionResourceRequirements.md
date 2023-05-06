# airbyte_config_api_client.model.actor_definition_resource_requirements.ActorDefinitionResourceRequirements

actor definition specific resource requirements. if default is set, these are the requirements that should be set for ALL jobs run for this actor definition. it is overriden by the job type specific configurations. if not set, the platform will use defaults. these values will be overriden by configuration at the connection level.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | actor definition specific resource requirements. if default is set, these are the requirements that should be set for ALL jobs run for this actor definition. it is overriden by the job type specific configurations. if not set, the platform will use defaults. these values will be overriden by configuration at the connection level. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**default** | [**ResourceRequirements**](ResourceRequirements.md) | [**ResourceRequirements**](ResourceRequirements.md) |  | [optional] 
**[jobSpecific](#jobSpecific)** | list, tuple,  | tuple,  |  | [optional] 

# jobSpecific

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**JobTypeResourceLimit**](JobTypeResourceLimit.md) | [**JobTypeResourceLimit**](JobTypeResourceLimit.md) | [**JobTypeResourceLimit**](JobTypeResourceLimit.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

