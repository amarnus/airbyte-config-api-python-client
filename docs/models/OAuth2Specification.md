# airbyte_config_api_client.model.o_auth2_specification.OAuth2Specification

An object containing any metadata needed to describe this connector's Oauth flow

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object containing any metadata needed to describe this connector&#x27;s Oauth flow | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[oauthFlowOutputParameters](#oauthFlowOutputParameters)** | list, tuple,  | tuple,  | Pointers to the fields in the rootObject which can be populated from successfully completing the oauth flow using the init parameters. This is typically a refresh/access token. Each inner array represents the path in the rootObject of the referenced field. | 
**[rootObject](#rootObject)** | list, tuple,  | tuple,  | A list of strings representing a pointer to the root object which contains any oauth parameters in the ConnectorSpecification. Examples: if oauth parameters were contained inside the top level, rootObject&#x3D;[] If they were nested inside another object {&#x27;credentials&#x27;: {&#x27;app_id&#x27; etc...}, rootObject&#x3D;[&#x27;credentials&#x27;] If they were inside a oneOf {&#x27;switch&#x27;: {oneOf: [{client_id...}, {non_oauth_param]}},  rootObject&#x3D;[&#x27;switch&#x27;, 0]  | 
**[oauthFlowInitParameters](#oauthFlowInitParameters)** | list, tuple,  | tuple,  | Pointers to the fields in the rootObject needed to obtain the initial refresh/access tokens for the OAuth flow. Each inner array represents the path in the rootObject of the referenced field. For example. Assume the rootObject contains params &#x27;app_secret&#x27;, &#x27;app_id&#x27; which are needed to get the initial refresh token. If they are not nested in the rootObject, then the array would look like this [[&#x27;app_secret&#x27;], [&#x27;app_id&#x27;]] If they are nested inside an object called &#x27;auth_params&#x27; then this array would be [[&#x27;auth_params&#x27;, &#x27;app_secret&#x27;], [&#x27;auth_params&#x27;, &#x27;app_id&#x27;]] | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# rootObject

A list of strings representing a pointer to the root object which contains any oauth parameters in the ConnectorSpecification. Examples: if oauth parameters were contained inside the top level, rootObject=[] If they were nested inside another object {'credentials': {'app_id' etc...}, rootObject=['credentials'] If they were inside a oneOf {'switch': {oneOf: [{client_id...}, {non_oauth_param]}},  rootObject=['switch', 0] 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of strings representing a pointer to the root object which contains any oauth parameters in the ConnectorSpecification. Examples: if oauth parameters were contained inside the top level, rootObject&#x3D;[] If they were nested inside another object {&#x27;credentials&#x27;: {&#x27;app_id&#x27; etc...}, rootObject&#x3D;[&#x27;credentials&#x27;] If they were inside a oneOf {&#x27;switch&#x27;: {oneOf: [{client_id...}, {non_oauth_param]}},  rootObject&#x3D;[&#x27;switch&#x27;, 0]  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# oauthFlowInitParameters

Pointers to the fields in the rootObject needed to obtain the initial refresh/access tokens for the OAuth flow. Each inner array represents the path in the rootObject of the referenced field. For example. Assume the rootObject contains params 'app_secret', 'app_id' which are needed to get the initial refresh token. If they are not nested in the rootObject, then the array would look like this [['app_secret'], ['app_id']] If they are nested inside an object called 'auth_params' then this array would be [['auth_params', 'app_secret'], ['auth_params', 'app_id']]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Pointers to the fields in the rootObject needed to obtain the initial refresh/access tokens for the OAuth flow. Each inner array represents the path in the rootObject of the referenced field. For example. Assume the rootObject contains params &#x27;app_secret&#x27;, &#x27;app_id&#x27; which are needed to get the initial refresh token. If they are not nested in the rootObject, then the array would look like this [[&#x27;app_secret&#x27;], [&#x27;app_id&#x27;]] If they are nested inside an object called &#x27;auth_params&#x27; then this array would be [[&#x27;auth_params&#x27;, &#x27;app_secret&#x27;], [&#x27;auth_params&#x27;, &#x27;app_id&#x27;]] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | list, tuple,  | tuple,  | A list of strings denoting a pointer into the rootObject for where to find this property | 

# items

A list of strings denoting a pointer into the rootObject for where to find this property

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of strings denoting a pointer into the rootObject for where to find this property | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# oauthFlowOutputParameters

Pointers to the fields in the rootObject which can be populated from successfully completing the oauth flow using the init parameters. This is typically a refresh/access token. Each inner array represents the path in the rootObject of the referenced field.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Pointers to the fields in the rootObject which can be populated from successfully completing the oauth flow using the init parameters. This is typically a refresh/access token. Each inner array represents the path in the rootObject of the referenced field. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | list, tuple,  | tuple,  | A list of strings denoting a pointer into the rootObject for where to find this property | 

# items

A list of strings denoting a pointer into the rootObject for where to find this property

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of strings denoting a pointer into the rootObject for where to find this property | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

