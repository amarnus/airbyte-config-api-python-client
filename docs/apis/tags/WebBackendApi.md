<a name="__pageTop"></a>
# airbyte_config_api_client.apis.tags.web_backend_api.WebBackendApi

All URIs are relative to *http://localhost:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_state_type**](#get_state_type) | **post** /v1/web_backend/state/get_type | Fetch the current state type for a connection.
[**web_backend_check_updates**](#web_backend_check_updates) | **post** /v1/web_backend/check_updates | Returns a summary of source and destination definitions that could be updated.
[**web_backend_create_connection**](#web_backend_create_connection) | **post** /v1/web_backend/connections/create | Create a connection
[**web_backend_get_connection**](#web_backend_get_connection) | **post** /v1/web_backend/connections/get | Get a connection
[**web_backend_get_workspace_state**](#web_backend_get_workspace_state) | **post** /v1/web_backend/workspace/state | Returns the current state of a workspace
[**web_backend_list_connections_for_workspace**](#web_backend_list_connections_for_workspace) | **post** /v1/web_backend/connections/list | Returns all non-deleted connections for a workspace.
[**web_backend_list_geographies**](#web_backend_list_geographies) | **post** /v1/web_backend/geographies/list | Returns available geographies can be selected to run data syncs in a particular geography. The &#x27;auto&#x27; entry indicates that the sync will be automatically assigned to a geography according to the platform default behavior. Entries other than &#x27;auto&#x27; are two-letter country codes that follow the ISO 3166-1 alpha-2 standard. 
[**web_backend_update_connection**](#web_backend_update_connection) | **post** /v1/web_backend/connections/update | Update a connection

# **get_state_type**
<a name="get_state_type"></a>
> ConnectionStateType get_state_type(connection_id_request_body)

Fetch the current state type for a connection.

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import web_backend_api
from airbyte_config_api_client.model.connection_state_type import ConnectionStateType
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
    api_instance = web_backend_api.WebBackendApi(api_client)

    # example passing only required values which don't have defaults set
    body = ConnectionIdRequestBody(
        connection_id="connection_id_example",
    )
    try:
        # Fetch the current state type for a connection.
        api_response = api_instance.get_state_type(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling WebBackendApi->get_state_type: %s\n" % e)
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
200 | [ApiResponseFor200](#get_state_type.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#get_state_type.ApiResponseFor404) | Object with given id was not found.
422 | [ApiResponseFor422](#get_state_type.ApiResponseFor422) | Input failed validation

#### get_state_type.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConnectionStateType**](../../models/ConnectionStateType.md) |  | 


#### get_state_type.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundKnownExceptionInfo**](../../models/NotFoundKnownExceptionInfo.md) |  | 


#### get_state_type.ApiResponseFor422
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

# **web_backend_check_updates**
<a name="web_backend_check_updates"></a>
> WebBackendCheckUpdatesRead web_backend_check_updates()

Returns a summary of source and destination definitions that could be updated.

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import web_backend_api
from airbyte_config_api_client.model.web_backend_check_updates_read import WebBackendCheckUpdatesRead
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = airbyte_config_api_client.Configuration(
    host = "http://localhost:8000/api"
)

# Enter a context with an instance of the API client
with airbyte_config_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = web_backend_api.WebBackendApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns a summary of source and destination definitions that could be updated.
        api_response = api_instance.web_backend_check_updates()
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling WebBackendApi->web_backend_check_updates: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#web_backend_check_updates.ApiResponseFor200) | Successful operation

#### web_backend_check_updates.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**WebBackendCheckUpdatesRead**](../../models/WebBackendCheckUpdatesRead.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **web_backend_create_connection**
<a name="web_backend_create_connection"></a>
> WebBackendConnectionRead web_backend_create_connection(web_backend_connection_create)

Create a connection

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import web_backend_api
from airbyte_config_api_client.model.web_backend_connection_read import WebBackendConnectionRead
from airbyte_config_api_client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from airbyte_config_api_client.model.web_backend_connection_create import WebBackendConnectionCreate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = airbyte_config_api_client.Configuration(
    host = "http://localhost:8000/api"
)

# Enter a context with an instance of the API client
with airbyte_config_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = web_backend_api.WebBackendApi(api_client)

    # example passing only required values which don't have defaults set
    body = WebBackendConnectionCreate(
        name="name_example",
        namespace_definition=NamespaceDefinitionType("source"),
        namespace_format="${SOURCE_NAMESPACE}",
        prefix="prefix_example",
        source_id="source_id_example",
        destination_id="destination_id_example",
        operation_ids=[
            "operation_ids_example"
        ],
        sync_catalog=AirbyteCatalog(
            streams=[
                AirbyteStreamAndConfiguration(
                    stream=AirbyteStream(
                        name="name_example",
                        json_schema=dict(),
                        supported_sync_modes=[
                            SyncMode("full_refresh")
                        ],
                        source_defined_cursor=True,
                        default_cursor_field=[
                            "default_cursor_field_example"
                        ],
                        source_defined_primary_key=[
                            [
                                "string_example"
                            ]
                        ],
                        namespace="namespace_example",
                    ),
                    config=AirbyteStreamConfiguration(
                        sync_mode=SyncMode("full_refresh"),
                        cursor_field=[
                            "cursor_field_example"
                        ],
                        destination_sync_mode=DestinationSyncMode("append"),
                        primary_key=[],
                        alias_name="alias_name_example",
                        selected=True,
                        suggested=True,
                        field_selection_enabled=True,
                        selected_fields=[
                            SelectedFieldInfo(
,
                            )
                        ],
                    ),
                )
            ],
        ),
        schedule=ConnectionSchedule(
            units=1,
            time_unit="minutes",
        ),
        schedule_type=ConnectionScheduleType("manual"),
        schedule_data=ConnectionScheduleData(
            basic_schedule=dict(
                time_unit="minutes",
                units=1,
            ),
            cron=dict(
                cron_expression="cron_expression_example",
                cron_time_zone="cron_time_zone_example",
            ),
        ),
        status=ConnectionStatus("active"),
        resource_requirements=ResourceRequirements(
            cpu_request="cpu_request_example",
            cpu_limit="cpu_limit_example",
            memory_request="memory_request_example",
            memory_limit="memory_limit_example",
        ),
        operations=[
            OperationCreate(
                workspace_id="workspace_id_example",
                name="name_example",
                operator_configuration=OperatorConfiguration(
                    operator_type=OperatorType("normalization"),
                    normalization=OperatorNormalization(
                        option="basic",
                    ),
                    dbt=OperatorDbt(
                        git_repo_url="git_repo_url_example",
                        git_repo_branch="git_repo_branch_example",
                        docker_image="docker_image_example",
                        dbt_arguments="dbt_arguments_example",
                    ),
                    webhook=OperatorWebhook(
                        webhook_config_id="webhook_config_id_example",
                        webhook_type="dbtCloud",
                        dbt_cloud=dict(
                            account_id=1,
                            job_id=1,
                        ),
                        execution_url="execution_url_example",
                        execution_body="execution_body_example",
                    ),
                ),
            )
        ],
        source_catalog_id="source_catalog_id_example",
        geography=Geography("auto"),
        non_breaking_changes_preference=NonBreakingChangesPreference("ignore"),
    )
    try:
        # Create a connection
        api_response = api_instance.web_backend_create_connection(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling WebBackendApi->web_backend_create_connection: %s\n" % e)
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
[**WebBackendConnectionCreate**](../../models/WebBackendConnectionCreate.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#web_backend_create_connection.ApiResponseFor200) | Successful operation
422 | [ApiResponseFor422](#web_backend_create_connection.ApiResponseFor422) | Input failed validation

#### web_backend_create_connection.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**WebBackendConnectionRead**](../../models/WebBackendConnectionRead.md) |  | 


#### web_backend_create_connection.ApiResponseFor422
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

# **web_backend_get_connection**
<a name="web_backend_get_connection"></a>
> WebBackendConnectionRead web_backend_get_connection(web_backend_connection_request_body)

Get a connection

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import web_backend_api
from airbyte_config_api_client.model.web_backend_connection_read import WebBackendConnectionRead
from airbyte_config_api_client.model.web_backend_connection_request_body import WebBackendConnectionRequestBody
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
    api_instance = web_backend_api.WebBackendApi(api_client)

    # example passing only required values which don't have defaults set
    body = WebBackendConnectionRequestBody(
        with_refreshed_catalog=True,
        connection_id="connection_id_example",
    )
    try:
        # Get a connection
        api_response = api_instance.web_backend_get_connection(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling WebBackendApi->web_backend_get_connection: %s\n" % e)
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
[**WebBackendConnectionRequestBody**](../../models/WebBackendConnectionRequestBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#web_backend_get_connection.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#web_backend_get_connection.ApiResponseFor404) | Object with given id was not found.
422 | [ApiResponseFor422](#web_backend_get_connection.ApiResponseFor422) | Input failed validation

#### web_backend_get_connection.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**WebBackendConnectionRead**](../../models/WebBackendConnectionRead.md) |  | 


#### web_backend_get_connection.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundKnownExceptionInfo**](../../models/NotFoundKnownExceptionInfo.md) |  | 


#### web_backend_get_connection.ApiResponseFor422
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

# **web_backend_get_workspace_state**
<a name="web_backend_get_workspace_state"></a>
> WebBackendWorkspaceStateResult web_backend_get_workspace_state()

Returns the current state of a workspace

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import web_backend_api
from airbyte_config_api_client.model.web_backend_workspace_state_result import WebBackendWorkspaceStateResult
from airbyte_config_api_client.model.web_backend_workspace_state import WebBackendWorkspaceState
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
    api_instance = web_backend_api.WebBackendApi(api_client)

    # example passing only optional values
    body = WebBackendWorkspaceState(
        workspace_id="workspace_id_example",
    )
    try:
        # Returns the current state of a workspace
        api_response = api_instance.web_backend_get_workspace_state(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling WebBackendApi->web_backend_get_workspace_state: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**WebBackendWorkspaceState**](../../models/WebBackendWorkspaceState.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#web_backend_get_workspace_state.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#web_backend_get_workspace_state.ApiResponseFor404) | Object with given id was not found.
422 | [ApiResponseFor422](#web_backend_get_workspace_state.ApiResponseFor422) | Input failed validation

#### web_backend_get_workspace_state.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**WebBackendWorkspaceStateResult**](../../models/WebBackendWorkspaceStateResult.md) |  | 


#### web_backend_get_workspace_state.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundKnownExceptionInfo**](../../models/NotFoundKnownExceptionInfo.md) |  | 


#### web_backend_get_workspace_state.ApiResponseFor422
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

# **web_backend_list_connections_for_workspace**
<a name="web_backend_list_connections_for_workspace"></a>
> WebBackendConnectionReadList web_backend_list_connections_for_workspace(web_backend_connection_list_request_body)

Returns all non-deleted connections for a workspace.

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import web_backend_api
from airbyte_config_api_client.model.web_backend_connection_list_request_body import WebBackendConnectionListRequestBody
from airbyte_config_api_client.model.web_backend_connection_read_list import WebBackendConnectionReadList
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
    api_instance = web_backend_api.WebBackendApi(api_client)

    # example passing only required values which don't have defaults set
    body = WebBackendConnectionListRequestBody(
        workspace_id="workspace_id_example",
        source_id=[
            "source_id_example"
        ],
        destination_id=[
            "destination_id_example"
        ],
    )
    try:
        # Returns all non-deleted connections for a workspace.
        api_response = api_instance.web_backend_list_connections_for_workspace(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling WebBackendApi->web_backend_list_connections_for_workspace: %s\n" % e)
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
[**WebBackendConnectionListRequestBody**](../../models/WebBackendConnectionListRequestBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#web_backend_list_connections_for_workspace.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#web_backend_list_connections_for_workspace.ApiResponseFor404) | Object with given id was not found.
422 | [ApiResponseFor422](#web_backend_list_connections_for_workspace.ApiResponseFor422) | Input failed validation

#### web_backend_list_connections_for_workspace.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**WebBackendConnectionReadList**](../../models/WebBackendConnectionReadList.md) |  | 


#### web_backend_list_connections_for_workspace.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundKnownExceptionInfo**](../../models/NotFoundKnownExceptionInfo.md) |  | 


#### web_backend_list_connections_for_workspace.ApiResponseFor422
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

# **web_backend_list_geographies**
<a name="web_backend_list_geographies"></a>
> WebBackendGeographiesListResult web_backend_list_geographies()

Returns available geographies can be selected to run data syncs in a particular geography. The 'auto' entry indicates that the sync will be automatically assigned to a geography according to the platform default behavior. Entries other than 'auto' are two-letter country codes that follow the ISO 3166-1 alpha-2 standard. 

Returns all available geographies in which a data sync can run.

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import web_backend_api
from airbyte_config_api_client.model.web_backend_geographies_list_result import WebBackendGeographiesListResult
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = airbyte_config_api_client.Configuration(
    host = "http://localhost:8000/api"
)

# Enter a context with an instance of the API client
with airbyte_config_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = web_backend_api.WebBackendApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns available geographies can be selected to run data syncs in a particular geography. The 'auto' entry indicates that the sync will be automatically assigned to a geography according to the platform default behavior. Entries other than 'auto' are two-letter country codes that follow the ISO 3166-1 alpha-2 standard. 
        api_response = api_instance.web_backend_list_geographies()
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling WebBackendApi->web_backend_list_geographies: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#web_backend_list_geographies.ApiResponseFor200) | Successful operation

#### web_backend_list_geographies.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**WebBackendGeographiesListResult**](../../models/WebBackendGeographiesListResult.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **web_backend_update_connection**
<a name="web_backend_update_connection"></a>
> WebBackendConnectionRead web_backend_update_connection(web_backend_connection_update)

Update a connection

Apply a patch-style update to a connection. Only fields present on the update request body will be updated. Any operations that lack an ID will be created. Then, the newly created operationId will be applied to the connection along with the rest of the operationIds in the request body. Apply a patch-style update to a connection. Only fields present on the update request body will be updated. Note that if a catalog is present in the request body, the connection's entire catalog will be replaced with the catalog from the request. This means that to modify a single stream, the entire new catalog containing the updated stream needs to be sent. 

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import web_backend_api
from airbyte_config_api_client.model.web_backend_connection_update import WebBackendConnectionUpdate
from airbyte_config_api_client.model.web_backend_connection_read import WebBackendConnectionRead
from airbyte_config_api_client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = airbyte_config_api_client.Configuration(
    host = "http://localhost:8000/api"
)

# Enter a context with an instance of the API client
with airbyte_config_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = web_backend_api.WebBackendApi(api_client)

    # example passing only required values which don't have defaults set
    body = WebBackendConnectionUpdate(
        name="name_example",
        connection_id="connection_id_example",
        namespace_definition=NamespaceDefinitionType("source"),
        namespace_format="${SOURCE_NAMESPACE}",
        prefix="prefix_example",
        sync_catalog=AirbyteCatalog(
            streams=[
                AirbyteStreamAndConfiguration(
                    stream=AirbyteStream(
                        name="name_example",
                        json_schema=dict(),
                        supported_sync_modes=[
                            SyncMode("full_refresh")
                        ],
                        source_defined_cursor=True,
                        default_cursor_field=[
                            "default_cursor_field_example"
                        ],
                        source_defined_primary_key=[
                            [
                                "string_example"
                            ]
                        ],
                        namespace="namespace_example",
                    ),
                    config=AirbyteStreamConfiguration(
                        sync_mode=SyncMode("full_refresh"),
                        cursor_field=[
                            "cursor_field_example"
                        ],
                        destination_sync_mode=DestinationSyncMode("append"),
                        primary_key=[],
                        alias_name="alias_name_example",
                        selected=True,
                        suggested=True,
                        field_selection_enabled=True,
                        selected_fields=[
                            SelectedFieldInfo(
,
                            )
                        ],
                    ),
                )
            ],
        ),
        schedule=ConnectionSchedule(
            units=1,
            time_unit="minutes",
        ),
        schedule_type=ConnectionScheduleType("manual"),
        schedule_data=ConnectionScheduleData(
            basic_schedule=dict(
                time_unit="minutes",
                units=1,
            ),
            cron=dict(
                cron_expression="cron_expression_example",
                cron_time_zone="cron_time_zone_example",
            ),
        ),
        status=ConnectionStatus("active"),
        resource_requirements=ResourceRequirements(
            cpu_request="cpu_request_example",
            cpu_limit="cpu_limit_example",
            memory_request="memory_request_example",
            memory_limit="memory_limit_example",
        ),
        skip_reset=True,
        operations=[
            WebBackendOperationCreateOrUpdate(
                operation_id="operation_id_example",
                workspace_id="workspace_id_example",
                name="name_example",
                operator_configuration=OperatorConfiguration(
                    operator_type=OperatorType("normalization"),
                    normalization=OperatorNormalization(
                        option="basic",
                    ),
                    dbt=OperatorDbt(
                        git_repo_url="git_repo_url_example",
                        git_repo_branch="git_repo_branch_example",
                        docker_image="docker_image_example",
                        dbt_arguments="dbt_arguments_example",
                    ),
                    webhook=OperatorWebhook(
                        webhook_config_id="webhook_config_id_example",
                        webhook_type="dbtCloud",
                        dbt_cloud=dict(
                            account_id=1,
                            job_id=1,
                        ),
                        execution_url="execution_url_example",
                        execution_body="execution_body_example",
                    ),
                ),
            )
        ],
        source_catalog_id="source_catalog_id_example",
        geography=Geography("auto"),
        notify_schema_changes=True,
        non_breaking_changes_preference=NonBreakingChangesPreference("ignore"),
    )
    try:
        # Update a connection
        api_response = api_instance.web_backend_update_connection(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling WebBackendApi->web_backend_update_connection: %s\n" % e)
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
[**WebBackendConnectionUpdate**](../../models/WebBackendConnectionUpdate.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#web_backend_update_connection.ApiResponseFor200) | Successful operation
422 | [ApiResponseFor422](#web_backend_update_connection.ApiResponseFor422) | Input failed validation

#### web_backend_update_connection.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**WebBackendConnectionRead**](../../models/WebBackendConnectionRead.md) |  | 


#### web_backend_update_connection.ApiResponseFor422
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

