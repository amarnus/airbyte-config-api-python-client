<a name="__pageTop"></a>
# airbyte_config_api_client.apis.tags.scheduler_api.SchedulerApi

All URIs are relative to *http://localhost:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_destination_check_connection**](#execute_destination_check_connection) | **post** /v1/scheduler/destinations/check_connection | Run check connection for a given destination configuration
[**execute_source_check_connection**](#execute_source_check_connection) | **post** /v1/scheduler/sources/check_connection | Run check connection for a given source configuration
[**execute_source_discover_schema**](#execute_source_discover_schema) | **post** /v1/scheduler/sources/discover_schema | Run discover schema for a given source a source configuration

# **execute_destination_check_connection**
<a name="execute_destination_check_connection"></a>
> CheckConnectionRead execute_destination_check_connection(destination_core_config)

Run check connection for a given destination configuration

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import scheduler_api
from airbyte_config_api_client.model.destination_core_config import DestinationCoreConfig
from airbyte_config_api_client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from airbyte_config_api_client.model.check_connection_read import CheckConnectionRead
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = airbyte_config_api_client.Configuration(
    host = "http://localhost:8000/api"
)

# Enter a context with an instance of the API client
with airbyte_config_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scheduler_api.SchedulerApi(api_client)

    # example passing only required values which don't have defaults set
    body = DestinationCoreConfig(
        destination_id="destination_id_example",
        destination_definition_id="destination_definition_id_example",
        connection_configuration=None,
        workspace_id="workspace_id_example",
    )
    try:
        # Run check connection for a given destination configuration
        api_response = api_instance.execute_destination_check_connection(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling SchedulerApi->execute_destination_check_connection: %s\n" % e)
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
[**DestinationCoreConfig**](../../models/DestinationCoreConfig.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#execute_destination_check_connection.ApiResponseFor200) | Successful operation
422 | [ApiResponseFor422](#execute_destination_check_connection.ApiResponseFor422) | Input failed validation

#### execute_destination_check_connection.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CheckConnectionRead**](../../models/CheckConnectionRead.md) |  | 


#### execute_destination_check_connection.ApiResponseFor422
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

# **execute_source_check_connection**
<a name="execute_source_check_connection"></a>
> CheckConnectionRead execute_source_check_connection(source_core_config)

Run check connection for a given source configuration

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import scheduler_api
from airbyte_config_api_client.model.source_core_config import SourceCoreConfig
from airbyte_config_api_client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from airbyte_config_api_client.model.check_connection_read import CheckConnectionRead
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = airbyte_config_api_client.Configuration(
    host = "http://localhost:8000/api"
)

# Enter a context with an instance of the API client
with airbyte_config_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scheduler_api.SchedulerApi(api_client)

    # example passing only required values which don't have defaults set
    body = SourceCoreConfig(
        source_id="source_id_example",
        source_definition_id="source_definition_id_example",
        connection_configuration=None,
        workspace_id="workspace_id_example",
    )
    try:
        # Run check connection for a given source configuration
        api_response = api_instance.execute_source_check_connection(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling SchedulerApi->execute_source_check_connection: %s\n" % e)
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
[**SourceCoreConfig**](../../models/SourceCoreConfig.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#execute_source_check_connection.ApiResponseFor200) | Successful operation
422 | [ApiResponseFor422](#execute_source_check_connection.ApiResponseFor422) | Input failed validation

#### execute_source_check_connection.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CheckConnectionRead**](../../models/CheckConnectionRead.md) |  | 


#### execute_source_check_connection.ApiResponseFor422
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

# **execute_source_discover_schema**
<a name="execute_source_discover_schema"></a>
> SourceDiscoverSchemaRead execute_source_discover_schema(source_core_config)

Run discover schema for a given source a source configuration

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import scheduler_api
from airbyte_config_api_client.model.source_core_config import SourceCoreConfig
from airbyte_config_api_client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from airbyte_config_api_client.model.source_discover_schema_read import SourceDiscoverSchemaRead
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = airbyte_config_api_client.Configuration(
    host = "http://localhost:8000/api"
)

# Enter a context with an instance of the API client
with airbyte_config_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scheduler_api.SchedulerApi(api_client)

    # example passing only required values which don't have defaults set
    body = SourceCoreConfig(
        source_id="source_id_example",
        source_definition_id="source_definition_id_example",
        connection_configuration=None,
        workspace_id="workspace_id_example",
    )
    try:
        # Run discover schema for a given source a source configuration
        api_response = api_instance.execute_source_discover_schema(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling SchedulerApi->execute_source_discover_schema: %s\n" % e)
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
[**SourceCoreConfig**](../../models/SourceCoreConfig.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#execute_source_discover_schema.ApiResponseFor200) | Successful operation
422 | [ApiResponseFor422](#execute_source_discover_schema.ApiResponseFor422) | Input failed validation

#### execute_source_discover_schema.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SourceDiscoverSchemaRead**](../../models/SourceDiscoverSchemaRead.md) |  | 


#### execute_source_discover_schema.ApiResponseFor422
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

