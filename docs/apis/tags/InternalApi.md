<a name="__pageTop"></a>
# airbyte_config_api_client.apis.tags.internal_api.InternalApi

All URIs are relative to *http://localhost:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_update_state**](#create_or_update_state) | **post** /v1/state/create_or_update | Create or update the state for a connection.
[**get_attempt_normalization_statuses_for_job**](#get_attempt_normalization_statuses_for_job) | **post** /v1/jobs/get_normalization_status | Get normalization status to determine if we can bypass normalization phase
[**save_stats**](#save_stats) | **post** /v1/attempt/save_stats | For worker to set sync stats of a running attempt.
[**save_sync_config**](#save_sync_config) | **post** /v1/attempt/save_sync_config | For worker to save the AttemptSyncConfig for an attempt.
[**set_workflow_in_attempt**](#set_workflow_in_attempt) | **post** /v1/attempt/set_workflow_in_attempt | For worker to register the workflow id in attempt.
[**write_discover_catalog_result**](#write_discover_catalog_result) | **post** /v1/sources/write_discover_catalog_result | Should only called from worker, to write result from discover activity back to DB.

# **create_or_update_state**
<a name="create_or_update_state"></a>
> ConnectionState create_or_update_state(connection_state_create_or_update)

Create or update the state for a connection.

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import internal_api
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
    api_instance = internal_api.InternalApi(api_client)

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
        print("Exception when calling InternalApi->create_or_update_state: %s\n" % e)
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

# **get_attempt_normalization_statuses_for_job**
<a name="get_attempt_normalization_statuses_for_job"></a>
> AttemptNormalizationStatusReadList get_attempt_normalization_statuses_for_job()

Get normalization status to determine if we can bypass normalization phase

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import internal_api
from airbyte_config_api_client.model.attempt_normalization_status_read_list import AttemptNormalizationStatusReadList
from airbyte_config_api_client.model.job_id_request_body import JobIdRequestBody
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = airbyte_config_api_client.Configuration(
    host = "http://localhost:8000/api"
)

# Enter a context with an instance of the API client
with airbyte_config_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = internal_api.InternalApi(api_client)

    # example passing only optional values
    body = JobIdRequestBody(
        id=1,
    )
    try:
        # Get normalization status to determine if we can bypass normalization phase
        api_response = api_instance.get_attempt_normalization_statuses_for_job(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling InternalApi->get_attempt_normalization_statuses_for_job: %s\n" % e)
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
[**JobIdRequestBody**](../../models/JobIdRequestBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_attempt_normalization_statuses_for_job.ApiResponseFor200) | Successful operation

#### get_attempt_normalization_statuses_for_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AttemptNormalizationStatusReadList**](../../models/AttemptNormalizationStatusReadList.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **save_stats**
<a name="save_stats"></a>
> InternalOperationResult save_stats(save_stats_request_body)

For worker to set sync stats of a running attempt.

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import internal_api
from airbyte_config_api_client.model.internal_operation_result import InternalOperationResult
from airbyte_config_api_client.model.save_stats_request_body import SaveStatsRequestBody
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = airbyte_config_api_client.Configuration(
    host = "http://localhost:8000/api"
)

# Enter a context with an instance of the API client
with airbyte_config_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = internal_api.InternalApi(api_client)

    # example passing only required values which don't have defaults set
    body = SaveStatsRequestBody(
        job_id=1,
        attempt_number=1,
        stats=AttemptStats(
            records_emitted=1,
            bytes_emitted=1,
            state_messages_emitted=1,
            records_committed=1,
            estimated_records=1,
            estimated_bytes=1,
        ),
        stream_stats=[
            AttemptStreamStats(
                stream_name="stream_name_example",
                stream_namespace="stream_namespace_example",
                stats=AttemptStats(),
            )
        ],
    )
    try:
        # For worker to set sync stats of a running attempt.
        api_response = api_instance.save_stats(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling InternalApi->save_stats: %s\n" % e)
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
[**SaveStatsRequestBody**](../../models/SaveStatsRequestBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#save_stats.ApiResponseFor200) | Successful Operation

#### save_stats.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalOperationResult**](../../models/InternalOperationResult.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **save_sync_config**
<a name="save_sync_config"></a>
> InternalOperationResult save_sync_config(save_attempt_sync_config_request_body)

For worker to save the AttemptSyncConfig for an attempt.

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import internal_api
from airbyte_config_api_client.model.internal_operation_result import InternalOperationResult
from airbyte_config_api_client.model.save_attempt_sync_config_request_body import SaveAttemptSyncConfigRequestBody
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = airbyte_config_api_client.Configuration(
    host = "http://localhost:8000/api"
)

# Enter a context with an instance of the API client
with airbyte_config_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = internal_api.InternalApi(api_client)

    # example passing only required values which don't have defaults set
    body = SaveAttemptSyncConfigRequestBody(
        job_id=1,
        attempt_number=1,
        sync_config=AttemptSyncConfig(
            source_configuration=None,
            destination_configuration=None,
            state=ConnectionState(
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
        ),
    )
    try:
        # For worker to save the AttemptSyncConfig for an attempt.
        api_response = api_instance.save_sync_config(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling InternalApi->save_sync_config: %s\n" % e)
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
[**SaveAttemptSyncConfigRequestBody**](../../models/SaveAttemptSyncConfigRequestBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#save_sync_config.ApiResponseFor200) | Successful Operation

#### save_sync_config.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalOperationResult**](../../models/InternalOperationResult.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **set_workflow_in_attempt**
<a name="set_workflow_in_attempt"></a>
> InternalOperationResult set_workflow_in_attempt(set_workflow_in_attempt_request_body)

For worker to register the workflow id in attempt.

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import internal_api
from airbyte_config_api_client.model.internal_operation_result import InternalOperationResult
from airbyte_config_api_client.model.set_workflow_in_attempt_request_body import SetWorkflowInAttemptRequestBody
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = airbyte_config_api_client.Configuration(
    host = "http://localhost:8000/api"
)

# Enter a context with an instance of the API client
with airbyte_config_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = internal_api.InternalApi(api_client)

    # example passing only required values which don't have defaults set
    body = SetWorkflowInAttemptRequestBody(
        job_id=1,
        attempt_number=1,
        workflow_id="workflow_id_example",
        processing_task_queue="",
    )
    try:
        # For worker to register the workflow id in attempt.
        api_response = api_instance.set_workflow_in_attempt(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling InternalApi->set_workflow_in_attempt: %s\n" % e)
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
[**SetWorkflowInAttemptRequestBody**](../../models/SetWorkflowInAttemptRequestBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#set_workflow_in_attempt.ApiResponseFor200) | Successful Operation

#### set_workflow_in_attempt.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalOperationResult**](../../models/InternalOperationResult.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **write_discover_catalog_result**
<a name="write_discover_catalog_result"></a>
> DiscoverCatalogResult write_discover_catalog_result(source_discover_schema_write_request_body)

Should only called from worker, to write result from discover activity back to DB.

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import internal_api
from airbyte_config_api_client.model.discover_catalog_result import DiscoverCatalogResult
from airbyte_config_api_client.model.source_discover_schema_write_request_body import SourceDiscoverSchemaWriteRequestBody
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = airbyte_config_api_client.Configuration(
    host = "http://localhost:8000/api"
)

# Enter a context with an instance of the API client
with airbyte_config_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = internal_api.InternalApi(api_client)

    # example passing only required values which don't have defaults set
    body = SourceDiscoverSchemaWriteRequestBody(
        catalog=AirbyteCatalog(
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
        source_id="source_id_example",
        connector_version="connector_version_example",
        configuration_hash="configuration_hash_example",
    )
    try:
        # Should only called from worker, to write result from discover activity back to DB.
        api_response = api_instance.write_discover_catalog_result(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling InternalApi->write_discover_catalog_result: %s\n" % e)
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
[**SourceDiscoverSchemaWriteRequestBody**](../../models/SourceDiscoverSchemaWriteRequestBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#write_discover_catalog_result.ApiResponseFor200) | Successful Operation

#### write_discover_catalog_result.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DiscoverCatalogResult**](../../models/DiscoverCatalogResult.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

