<a name="__pageTop"></a>
# airbyte_config_api_client.apis.tags.state_api.StateApi

All URIs are relative to *http://localhost:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_update_state**](#create_or_update_state) | **post** /v1/state/create_or_update | Create or update the state for a connection.
[**get_state**](#get_state) | **post** /v1/state/get | Fetch the current state for a connection.

# **create_or_update_state**
<a name="create_or_update_state"></a>
> ConnectionState create_or_update_state(connection_state_create_or_update)

Create or update the state for a connection.

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import state_api
from airbyte_config_api_client.model.connection_state_create_or_update import ConnectionStateCreateOrUpdate
from airbyte_config_api_client.model.connection_state import ConnectionState
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
    api_instance = state_api.StateApi(api_client)

    # example passing only required values which don't have defaults set
    body = ConnectionStateCreateOrUpdate(
        connection_id="connection_id_example",
        connection_state=ConnectionState(
            state_type=ConnectionStateType("global"),
            connection_id="connection_id_example",
            state=dict(),
            stream_state=[
                StreamState(
                    stream_descriptor=StreamDescriptor(
                        name="name_example",
                        namespace="namespace_example",
                    ),
                    stream_state=dict(),
                )
            ],
            global_state=GlobalState(
                shared_state=dict(),
,
            ),
        ),
    )
    try:
        # Create or update the state for a connection.
        api_response = api_instance.create_or_update_state(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling StateApi->create_or_update_state: %s\n" % e)
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
[**ConnectionStateCreateOrUpdate**](../../models/ConnectionStateCreateOrUpdate.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_or_update_state.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#create_or_update_state.ApiResponseFor404) | Object with given id was not found.
422 | [ApiResponseFor422](#create_or_update_state.ApiResponseFor422) | Input failed validation

#### create_or_update_state.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConnectionState**](../../models/ConnectionState.md) |  | 


#### create_or_update_state.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundKnownExceptionInfo**](../../models/NotFoundKnownExceptionInfo.md) |  | 


#### create_or_update_state.ApiResponseFor422
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

# **get_state**
<a name="get_state"></a>
> ConnectionState get_state(connection_id_request_body)

Fetch the current state for a connection.

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import state_api
from airbyte_config_api_client.model.connection_state import ConnectionState
from airbyte_config_api_client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from airbyte_config_api_client.model.connection_id_request_body import ConnectionIdRequestBody
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
    api_instance = state_api.StateApi(api_client)

    # example passing only required values which don't have defaults set
    body = ConnectionIdRequestBody(
        connection_id="connection_id_example",
    )
    try:
        # Fetch the current state for a connection.
        api_response = api_instance.get_state(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling StateApi->get_state: %s\n" % e)
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
[**ConnectionIdRequestBody**](../../models/ConnectionIdRequestBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_state.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#get_state.ApiResponseFor404) | Object with given id was not found.
422 | [ApiResponseFor422](#get_state.ApiResponseFor422) | Input failed validation

#### get_state.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConnectionState**](../../models/ConnectionState.md) |  | 


#### get_state.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundKnownExceptionInfo**](../../models/NotFoundKnownExceptionInfo.md) |  | 


#### get_state.ApiResponseFor422
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

