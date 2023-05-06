# airbyte_config_api_client.model.destination_oauth_consent_request.DestinationOauthConsentRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**redirectUrl** | str,  | str,  | The url to redirect to after getting the user consent | 
**destinationDefinitionId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**workspaceId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**oAuthInputConfiguration** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The values required to configure OAuth flows. The schema for this must match the &#x60;OAuthConfigSpecification.oauthUserInputFromConnectorConfigSpecification&#x60; schema. | [optional] 
**destinationId** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

