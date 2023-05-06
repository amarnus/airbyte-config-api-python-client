<a name="__pageTop"></a>
# airbyte_config_api_client.apis.tags.source_oauth_api.SourceOauthApi

All URIs are relative to *http://localhost:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**complete_source_o_auth**](#complete_source_o_auth) | **post** /v1/source_oauths/complete_oauth | Given a source def ID generate an access/refresh token etc.
[**get_source_o_auth_consent**](#get_source_o_auth_consent) | **post** /v1/source_oauths/get_consent_url | Given a source connector definition ID, return the URL to the consent screen where to redirect the user to.
[**set_instancewide_source_oauth_params**](#set_instancewide_source_oauth_params) | **post** /v1/source_oauths/oauth_params/create | Sets instancewide variables to be used for the oauth flow when creating this source. When set, these variables will be injected into a connector&#x27;s configuration before any interaction with the connector image itself. This enables running oauth flows with consistent variables e.g: the company&#x27;s Google Ads developer_token, client_id, and client_secret without the user having to know about these variables. 

# **complete_source_o_auth**
<a name="complete_source_o_auth"></a>
> CompleteOAuthResponse complete_source_o_auth(complete_source_oauth_request)

Given a source def ID generate an access/refresh token etc.

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import source_oauth_api
from airbyte_config_api_client.model.complete_o_auth_response import CompleteOAuthResponse
from airbyte_config_api_client.model.complete_source_oauth_request import CompleteSourceOauthRequest
from airbyte_config_api_client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from airbyte_config_api_client.model.not_found_known_exception_info import NotFoundKnownExceptionInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = airbyte_config_api_client.Configuration(
    host = "http://localhost:8000/api"
)

# Enter a context with an instance of the API client
with airbyte_config_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source_oauth_api.SourceOauthApi(api_client)

    # example passing only required values which don't have defaults set
    body = CompleteSourceOauthRequest(
        source_definition_id="source_definition_id_example",
        workspace_id="workspace_id_example",
        redirect_url="redirect_url_example",
        _query_params=dict(),
        o_auth_input_configuration=None,
        source_id="source_id_example",
    )
    try:
        # Given a source def ID generate an access/refresh token etc.
        api_response = api_instance.complete_source_o_auth(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling SourceOauthApi->complete_source_o_auth: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CompleteSourceOauthRequest**](../../models/CompleteSourceOauthRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#complete_source_o_auth.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#complete_source_o_auth.ApiResponseFor404) | Object with given id was not found.
422 | [ApiResponseFor422](#complete_source_o_auth.ApiResponseFor422) | Input failed validation

#### complete_source_o_auth.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CompleteOAuthResponse**](../../models/CompleteOAuthResponse.md) |  | 


#### complete_source_o_auth.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundKnownExceptionInfo**](../../models/NotFoundKnownExceptionInfo.md) |  | 


#### complete_source_o_auth.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InvalidInputExceptionInfo**](../../models/InvalidInputExceptionInfo.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_source_o_auth_consent**
<a name="get_source_o_auth_consent"></a>
> OAuthConsentRead get_source_o_auth_consent(source_oauth_consent_request)

Given a source connector definition ID, return the URL to the consent screen where to redirect the user to.

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import source_oauth_api
from airbyte_config_api_client.model.o_auth_consent_read import OAuthConsentRead
from airbyte_config_api_client.model.source_oauth_consent_request import SourceOauthConsentRequest
from airbyte_config_api_client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from airbyte_config_api_client.model.not_found_known_exception_info import NotFoundKnownExceptionInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = airbyte_config_api_client.Configuration(
    host = "http://localhost:8000/api"
)

# Enter a context with an instance of the API client
with airbyte_config_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source_oauth_api.SourceOauthApi(api_client)

    # example passing only required values which don't have defaults set
    body = SourceOauthConsentRequest(
        source_definition_id="source_definition_id_example",
        workspace_id="workspace_id_example",
        redirect_url="redirect_url_example",
        o_auth_input_configuration=None,
        source_id="source_id_example",
    )
    try:
        # Given a source connector definition ID, return the URL to the consent screen where to redirect the user to.
        api_response = api_instance.get_source_o_auth_consent(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling SourceOauthApi->get_source_o_auth_consent: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SourceOauthConsentRequest**](../../models/SourceOauthConsentRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_source_o_auth_consent.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#get_source_o_auth_consent.ApiResponseFor404) | Object with given id was not found.
422 | [ApiResponseFor422](#get_source_o_auth_consent.ApiResponseFor422) | Input failed validation

#### get_source_o_auth_consent.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OAuthConsentRead**](../../models/OAuthConsentRead.md) |  | 


#### get_source_o_auth_consent.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundKnownExceptionInfo**](../../models/NotFoundKnownExceptionInfo.md) |  | 


#### get_source_o_auth_consent.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InvalidInputExceptionInfo**](../../models/InvalidInputExceptionInfo.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **set_instancewide_source_oauth_params**
<a name="set_instancewide_source_oauth_params"></a>
> set_instancewide_source_oauth_params(set_instancewide_source_oauth_params_request_body)

Sets instancewide variables to be used for the oauth flow when creating this source. When set, these variables will be injected into a connector's configuration before any interaction with the connector image itself. This enables running oauth flows with consistent variables e.g: the company's Google Ads developer_token, client_id, and client_secret without the user having to know about these variables. 

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import source_oauth_api
from airbyte_config_api_client.model.set_instancewide_source_oauth_params_request_body import SetInstancewideSourceOauthParamsRequestBody
from airbyte_config_api_client.model.known_exception_info import KnownExceptionInfo
from airbyte_config_api_client.model.not_found_known_exception_info import NotFoundKnownExceptionInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = airbyte_config_api_client.Configuration(
    host = "http://localhost:8000/api"
)

# Enter a context with an instance of the API client
with airbyte_config_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source_oauth_api.SourceOauthApi(api_client)

    # example passing only required values which don't have defaults set
    body = SetInstancewideSourceOauthParamsRequestBody(
        source_definition_id="source_definition_id_example",
        params=dict(),
    )
    try:
        # Sets instancewide variables to be used for the oauth flow when creating this source. When set, these variables will be injected into a connector's configuration before any interaction with the connector image itself. This enables running oauth flows with consistent variables e.g: the company's Google Ads developer_token, client_id, and client_secret without the user having to know about these variables. 
        api_response = api_instance.set_instancewide_source_oauth_params(
            body=body,
        )
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling SourceOauthApi->set_instancewide_source_oauth_params: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SetInstancewideSourceOauthParamsRequestBody**](../../models/SetInstancewideSourceOauthParamsRequestBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#set_instancewide_source_oauth_params.ApiResponseFor200) | Successful
400 | [ApiResponseFor400](#set_instancewide_source_oauth_params.ApiResponseFor400) | Exception occurred; see message for details.
404 | [ApiResponseFor404](#set_instancewide_source_oauth_params.ApiResponseFor404) | Object with given id was not found.

#### set_instancewide_source_oauth_params.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### set_instancewide_source_oauth_params.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**KnownExceptionInfo**](../../models/KnownExceptionInfo.md) |  | 


#### set_instancewide_source_oauth_params.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundKnownExceptionInfo**](../../models/NotFoundKnownExceptionInfo.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

