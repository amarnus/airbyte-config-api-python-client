<a name="__pageTop"></a>
# airbyte_config_api_client.apis.tags.operation_api.OperationApi

All URIs are relative to *http://localhost:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_operation**](#check_operation) | **post** /v1/operations/check | Check if an operation to be created is valid
[**create_operation**](#create_operation) | **post** /v1/operations/create | Create an operation to be applied as part of a connection pipeline
[**delete_operation**](#delete_operation) | **post** /v1/operations/delete | Delete an operation
[**get_operation**](#get_operation) | **post** /v1/operations/get | Returns an operation
[**list_operations_for_connection**](#list_operations_for_connection) | **post** /v1/operations/list | Returns all operations for a connection.
[**update_operation**](#update_operation) | **post** /v1/operations/update | Update an operation

# **check_operation**
<a name="check_operation"></a>
> CheckOperationRead check_operation(operator_configuration)

Check if an operation to be created is valid

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import operation_api
from airbyte_config_api_client.model.check_operation_read import CheckOperationRead
from airbyte_config_api_client.model.operator_configuration import OperatorConfiguration
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
    api_instance = operation_api.OperationApi(api_client)

    # example passing only required values which don't have defaults set
    body = OperatorConfiguration(
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
    )
    try:
        # Check if an operation to be created is valid
        api_response = api_instance.check_operation(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling OperationApi->check_operation: %s\n" % e)
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
[**OperatorConfiguration**](../../models/OperatorConfiguration.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#check_operation.ApiResponseFor200) | Successful operation
422 | [ApiResponseFor422](#check_operation.ApiResponseFor422) | Input failed validation

#### check_operation.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CheckOperationRead**](../../models/CheckOperationRead.md) |  | 


#### check_operation.ApiResponseFor422
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

# **create_operation**
<a name="create_operation"></a>
> OperationRead create_operation(operation_create)

Create an operation to be applied as part of a connection pipeline

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import operation_api
from airbyte_config_api_client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from airbyte_config_api_client.model.operation_read import OperationRead
from airbyte_config_api_client.model.operation_create import OperationCreate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = airbyte_config_api_client.Configuration(
    host = "http://localhost:8000/api"
)

# Enter a context with an instance of the API client
with airbyte_config_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = operation_api.OperationApi(api_client)

    # example passing only required values which don't have defaults set
    body = OperationCreate(
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
    try:
        # Create an operation to be applied as part of a connection pipeline
        api_response = api_instance.create_operation(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling OperationApi->create_operation: %s\n" % e)
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
[**OperationCreate**](../../models/OperationCreate.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_operation.ApiResponseFor200) | Successful operation
422 | [ApiResponseFor422](#create_operation.ApiResponseFor422) | Input failed validation

#### create_operation.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OperationRead**](../../models/OperationRead.md) |  | 


#### create_operation.ApiResponseFor422
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

# **delete_operation**
<a name="delete_operation"></a>
> delete_operation(operation_id_request_body)

Delete an operation

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import operation_api
from airbyte_config_api_client.model.operation_id_request_body import OperationIdRequestBody
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
    api_instance = operation_api.OperationApi(api_client)

    # example passing only required values which don't have defaults set
    body = OperationIdRequestBody(
        operation_id="operation_id_example",
    )
    try:
        # Delete an operation
        api_response = api_instance.delete_operation(
            body=body,
        )
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling OperationApi->delete_operation: %s\n" % e)
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
[**OperationIdRequestBody**](../../models/OperationIdRequestBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_operation.ApiResponseFor204) | The resource was deleted successfully.
404 | [ApiResponseFor404](#delete_operation.ApiResponseFor404) | Object with given id was not found.
422 | [ApiResponseFor422](#delete_operation.ApiResponseFor422) | Input failed validation

#### delete_operation.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_operation.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundKnownExceptionInfo**](../../models/NotFoundKnownExceptionInfo.md) |  | 


#### delete_operation.ApiResponseFor422
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

# **get_operation**
<a name="get_operation"></a>
> OperationRead get_operation(operation_id_request_body)

Returns an operation

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import operation_api
from airbyte_config_api_client.model.operation_id_request_body import OperationIdRequestBody
from airbyte_config_api_client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from airbyte_config_api_client.model.operation_read import OperationRead
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
    api_instance = operation_api.OperationApi(api_client)

    # example passing only required values which don't have defaults set
    body = OperationIdRequestBody(
        operation_id="operation_id_example",
    )
    try:
        # Returns an operation
        api_response = api_instance.get_operation(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling OperationApi->get_operation: %s\n" % e)
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
[**OperationIdRequestBody**](../../models/OperationIdRequestBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_operation.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#get_operation.ApiResponseFor404) | Object with given id was not found.
422 | [ApiResponseFor422](#get_operation.ApiResponseFor422) | Input failed validation

#### get_operation.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OperationRead**](../../models/OperationRead.md) |  | 


#### get_operation.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundKnownExceptionInfo**](../../models/NotFoundKnownExceptionInfo.md) |  | 


#### get_operation.ApiResponseFor422
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

# **list_operations_for_connection**
<a name="list_operations_for_connection"></a>
> OperationReadList list_operations_for_connection(connection_id_request_body)

Returns all operations for a connection.

List operations for connection.

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import operation_api
from airbyte_config_api_client.model.operation_read_list import OperationReadList
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
    api_instance = operation_api.OperationApi(api_client)

    # example passing only required values which don't have defaults set
    body = ConnectionIdRequestBody(
        connection_id="connection_id_example",
    )
    try:
        # Returns all operations for a connection.
        api_response = api_instance.list_operations_for_connection(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling OperationApi->list_operations_for_connection: %s\n" % e)
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
200 | [ApiResponseFor200](#list_operations_for_connection.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#list_operations_for_connection.ApiResponseFor404) | Object with given id was not found.
422 | [ApiResponseFor422](#list_operations_for_connection.ApiResponseFor422) | Input failed validation

#### list_operations_for_connection.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OperationReadList**](../../models/OperationReadList.md) |  | 


#### list_operations_for_connection.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundKnownExceptionInfo**](../../models/NotFoundKnownExceptionInfo.md) |  | 


#### list_operations_for_connection.ApiResponseFor422
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

# **update_operation**
<a name="update_operation"></a>
> OperationRead update_operation(operation_update)

Update an operation

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import operation_api
from airbyte_config_api_client.model.operation_update import OperationUpdate
from airbyte_config_api_client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from airbyte_config_api_client.model.operation_read import OperationRead
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = airbyte_config_api_client.Configuration(
    host = "http://localhost:8000/api"
)

# Enter a context with an instance of the API client
with airbyte_config_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = operation_api.OperationApi(api_client)

    # example passing only required values which don't have defaults set
    body = OperationUpdate(
        operation_id="operation_id_example",
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
    try:
        # Update an operation
        api_response = api_instance.update_operation(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling OperationApi->update_operation: %s\n" % e)
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
[**OperationUpdate**](../../models/OperationUpdate.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_operation.ApiResponseFor200) | Successful operation
422 | [ApiResponseFor422](#update_operation.ApiResponseFor422) | Input failed validation

#### update_operation.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OperationRead**](../../models/OperationRead.md) |  | 


#### update_operation.ApiResponseFor422
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

