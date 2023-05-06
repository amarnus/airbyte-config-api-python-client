<a name="__pageTop"></a>
# airbyte_config_api_client.apis.tags.attempt_api.AttemptApi

All URIs are relative to *http://localhost:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**save_stats**](#save_stats) | **post** /v1/attempt/save_stats | For worker to set sync stats of a running attempt.
[**save_sync_config**](#save_sync_config) | **post** /v1/attempt/save_sync_config | For worker to save the AttemptSyncConfig for an attempt.
[**set_workflow_in_attempt**](#set_workflow_in_attempt) | **post** /v1/attempt/set_workflow_in_attempt | For worker to register the workflow id in attempt.

# **save_stats**
<a name="save_stats"></a>
> InternalOperationResult save_stats(save_stats_request_body)

For worker to set sync stats of a running attempt.

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import attempt_api
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
    api_instance = attempt_api.AttemptApi(api_client)

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
        print("Exception when calling AttemptApi->save_stats: %s\n" % e)
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
from airbyte_config_api_client.apis.tags import attempt_api
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
    api_instance = attempt_api.AttemptApi(api_client)

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
        print("Exception when calling AttemptApi->save_sync_config: %s\n" % e)
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
from airbyte_config_api_client.apis.tags import attempt_api
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
    api_instance = attempt_api.AttemptApi(api_client)

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
        print("Exception when calling AttemptApi->set_workflow_in_attempt: %s\n" % e)
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

