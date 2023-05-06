<a name="__pageTop"></a>
# airbyte_config_api_client.apis.tags.source_definition_api.SourceDefinitionApi

All URIs are relative to *http://localhost:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_source_definition**](#create_custom_source_definition) | **post** /v1/source_definitions/create_custom | Creates a custom sourceDefinition for the given workspace
[**delete_source_definition**](#delete_source_definition) | **post** /v1/source_definitions/delete | Delete a source definition
[**get_source_definition**](#get_source_definition) | **post** /v1/source_definitions/get | Get source
[**get_source_definition_for_workspace**](#get_source_definition_for_workspace) | **post** /v1/source_definitions/get_for_workspace | Get a sourceDefinition that is configured for the given workspace
[**grant_source_definition_to_workspace**](#grant_source_definition_to_workspace) | **post** /v1/source_definitions/grant_definition | grant a private, non-custom sourceDefinition to a given workspace
[**list_latest_source_definitions**](#list_latest_source_definitions) | **post** /v1/source_definitions/list_latest | List the latest sourceDefinitions Airbyte supports
[**list_private_source_definitions**](#list_private_source_definitions) | **post** /v1/source_definitions/list_private | List all private, non-custom sourceDefinitions, and for each indicate whether the given workspace has a grant for using the definition. Used by admins to view and modify a given workspace&#x27;s grants.
[**list_source_definitions**](#list_source_definitions) | **post** /v1/source_definitions/list | List all the sourceDefinitions the current Airbyte deployment is configured to use
[**list_source_definitions_for_workspace**](#list_source_definitions_for_workspace) | **post** /v1/source_definitions/list_for_workspace | List all the sourceDefinitions the given workspace is configured to use
[**revoke_source_definition_from_workspace**](#revoke_source_definition_from_workspace) | **post** /v1/source_definitions/revoke_definition | revoke a grant to a private, non-custom sourceDefinition from a given workspace
[**update_source_definition**](#update_source_definition) | **post** /v1/source_definitions/update | Update a sourceDefinition

# **create_custom_source_definition**
<a name="create_custom_source_definition"></a>
> SourceDefinitionRead create_custom_source_definition()

Creates a custom sourceDefinition for the given workspace

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import source_definition_api
from airbyte_config_api_client.model.source_definition_read import SourceDefinitionRead
from airbyte_config_api_client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from airbyte_config_api_client.model.custom_source_definition_create import CustomSourceDefinitionCreate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = airbyte_config_api_client.Configuration(
    host = "http://localhost:8000/api"
)

# Enter a context with an instance of the API client
with airbyte_config_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source_definition_api.SourceDefinitionApi(api_client)

    # example passing only optional values
    body = CustomSourceDefinitionCreate(
        workspace_id="workspace_id_example",
        source_definition=SourceDefinitionCreate(
            name="name_example",
            docker_repository="docker_repository_example",
            docker_image_tag="docker_image_tag_example",
            documentation_url="documentation_url_example",
            icon="icon_example",
            resource_requirements=ActorDefinitionResourceRequirements(
                default=ResourceRequirements(
                    cpu_request="cpu_request_example",
                    cpu_limit="cpu_limit_example",
                    memory_request="memory_request_example",
                    memory_limit="memory_limit_example",
                ),
                job_specific=[
                    JobTypeResourceLimit(
                        job_type=JobType("get_spec"),
                        resource_requirements=ResourceRequirements(),
                    )
                ],
            ),
        ),
    )
    try:
        # Creates a custom sourceDefinition for the given workspace
        api_response = api_instance.create_custom_source_definition(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling SourceDefinitionApi->create_custom_source_definition: %s\n" % e)
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
[**CustomSourceDefinitionCreate**](../../models/CustomSourceDefinitionCreate.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_custom_source_definition.ApiResponseFor200) | Successful operation
422 | [ApiResponseFor422](#create_custom_source_definition.ApiResponseFor422) | Input failed validation

#### create_custom_source_definition.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SourceDefinitionRead**](../../models/SourceDefinitionRead.md) |  | 


#### create_custom_source_definition.ApiResponseFor422
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

# **delete_source_definition**
<a name="delete_source_definition"></a>
> delete_source_definition(source_definition_id_request_body)

Delete a source definition

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import source_definition_api
from airbyte_config_api_client.model.source_definition_id_request_body import SourceDefinitionIdRequestBody
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
    api_instance = source_definition_api.SourceDefinitionApi(api_client)

    # example passing only required values which don't have defaults set
    body = SourceDefinitionIdRequestBody(
        source_definition_id="source_definition_id_example",
    )
    try:
        # Delete a source definition
        api_response = api_instance.delete_source_definition(
            body=body,
        )
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling SourceDefinitionApi->delete_source_definition: %s\n" % e)
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
[**SourceDefinitionIdRequestBody**](../../models/SourceDefinitionIdRequestBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_source_definition.ApiResponseFor204) | The resource was deleted successfully.
404 | [ApiResponseFor404](#delete_source_definition.ApiResponseFor404) | Object with given id was not found.
422 | [ApiResponseFor422](#delete_source_definition.ApiResponseFor422) | Input failed validation

#### delete_source_definition.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_source_definition.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundKnownExceptionInfo**](../../models/NotFoundKnownExceptionInfo.md) |  | 


#### delete_source_definition.ApiResponseFor422
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

# **get_source_definition**
<a name="get_source_definition"></a>
> SourceDefinitionRead get_source_definition(source_definition_id_request_body)

Get source

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import source_definition_api
from airbyte_config_api_client.model.source_definition_id_request_body import SourceDefinitionIdRequestBody
from airbyte_config_api_client.model.source_definition_read import SourceDefinitionRead
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
    api_instance = source_definition_api.SourceDefinitionApi(api_client)

    # example passing only required values which don't have defaults set
    body = SourceDefinitionIdRequestBody(
        source_definition_id="source_definition_id_example",
    )
    try:
        # Get source
        api_response = api_instance.get_source_definition(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling SourceDefinitionApi->get_source_definition: %s\n" % e)
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
[**SourceDefinitionIdRequestBody**](../../models/SourceDefinitionIdRequestBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_source_definition.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#get_source_definition.ApiResponseFor404) | Object with given id was not found.
422 | [ApiResponseFor422](#get_source_definition.ApiResponseFor422) | Input failed validation

#### get_source_definition.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SourceDefinitionRead**](../../models/SourceDefinitionRead.md) |  | 


#### get_source_definition.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundKnownExceptionInfo**](../../models/NotFoundKnownExceptionInfo.md) |  | 


#### get_source_definition.ApiResponseFor422
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

# **get_source_definition_for_workspace**
<a name="get_source_definition_for_workspace"></a>
> SourceDefinitionRead get_source_definition_for_workspace(source_definition_id_with_workspace_id)

Get a sourceDefinition that is configured for the given workspace

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import source_definition_api
from airbyte_config_api_client.model.source_definition_id_with_workspace_id import SourceDefinitionIdWithWorkspaceId
from airbyte_config_api_client.model.source_definition_read import SourceDefinitionRead
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
    api_instance = source_definition_api.SourceDefinitionApi(api_client)

    # example passing only required values which don't have defaults set
    body = SourceDefinitionIdWithWorkspaceId(
        source_definition_id="source_definition_id_example",
        workspace_id="workspace_id_example",
    )
    try:
        # Get a sourceDefinition that is configured for the given workspace
        api_response = api_instance.get_source_definition_for_workspace(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling SourceDefinitionApi->get_source_definition_for_workspace: %s\n" % e)
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
[**SourceDefinitionIdWithWorkspaceId**](../../models/SourceDefinitionIdWithWorkspaceId.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_source_definition_for_workspace.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#get_source_definition_for_workspace.ApiResponseFor404) | Object with given id was not found.
422 | [ApiResponseFor422](#get_source_definition_for_workspace.ApiResponseFor422) | Input failed validation

#### get_source_definition_for_workspace.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SourceDefinitionRead**](../../models/SourceDefinitionRead.md) |  | 


#### get_source_definition_for_workspace.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundKnownExceptionInfo**](../../models/NotFoundKnownExceptionInfo.md) |  | 


#### get_source_definition_for_workspace.ApiResponseFor422
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

# **grant_source_definition_to_workspace**
<a name="grant_source_definition_to_workspace"></a>
> PrivateSourceDefinitionRead grant_source_definition_to_workspace(source_definition_id_with_workspace_id)

grant a private, non-custom sourceDefinition to a given workspace

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import source_definition_api
from airbyte_config_api_client.model.source_definition_id_with_workspace_id import SourceDefinitionIdWithWorkspaceId
from airbyte_config_api_client.model.private_source_definition_read import PrivateSourceDefinitionRead
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
    api_instance = source_definition_api.SourceDefinitionApi(api_client)

    # example passing only required values which don't have defaults set
    body = SourceDefinitionIdWithWorkspaceId(
        source_definition_id="source_definition_id_example",
        workspace_id="workspace_id_example",
    )
    try:
        # grant a private, non-custom sourceDefinition to a given workspace
        api_response = api_instance.grant_source_definition_to_workspace(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling SourceDefinitionApi->grant_source_definition_to_workspace: %s\n" % e)
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
[**SourceDefinitionIdWithWorkspaceId**](../../models/SourceDefinitionIdWithWorkspaceId.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#grant_source_definition_to_workspace.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#grant_source_definition_to_workspace.ApiResponseFor404) | Object with given id was not found.
422 | [ApiResponseFor422](#grant_source_definition_to_workspace.ApiResponseFor422) | Input failed validation

#### grant_source_definition_to_workspace.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PrivateSourceDefinitionRead**](../../models/PrivateSourceDefinitionRead.md) |  | 


#### grant_source_definition_to_workspace.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundKnownExceptionInfo**](../../models/NotFoundKnownExceptionInfo.md) |  | 


#### grant_source_definition_to_workspace.ApiResponseFor422
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

# **list_latest_source_definitions**
<a name="list_latest_source_definitions"></a>
> SourceDefinitionReadList list_latest_source_definitions()

List the latest sourceDefinitions Airbyte supports

Guaranteed to retrieve the latest information on supported sources.

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import source_definition_api
from airbyte_config_api_client.model.source_definition_read_list import SourceDefinitionReadList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = airbyte_config_api_client.Configuration(
    host = "http://localhost:8000/api"
)

# Enter a context with an instance of the API client
with airbyte_config_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source_definition_api.SourceDefinitionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List the latest sourceDefinitions Airbyte supports
        api_response = api_instance.list_latest_source_definitions()
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling SourceDefinitionApi->list_latest_source_definitions: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_latest_source_definitions.ApiResponseFor200) | Successful operation

#### list_latest_source_definitions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SourceDefinitionReadList**](../../models/SourceDefinitionReadList.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_private_source_definitions**
<a name="list_private_source_definitions"></a>
> PrivateSourceDefinitionReadList list_private_source_definitions()

List all private, non-custom sourceDefinitions, and for each indicate whether the given workspace has a grant for using the definition. Used by admins to view and modify a given workspace's grants.

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import source_definition_api
from airbyte_config_api_client.model.private_source_definition_read_list import PrivateSourceDefinitionReadList
from airbyte_config_api_client.model.workspace_id_request_body import WorkspaceIdRequestBody
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = airbyte_config_api_client.Configuration(
    host = "http://localhost:8000/api"
)

# Enter a context with an instance of the API client
with airbyte_config_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source_definition_api.SourceDefinitionApi(api_client)

    # example passing only optional values
    body = WorkspaceIdRequestBody(
        workspace_id="workspace_id_example",
    )
    try:
        # List all private, non-custom sourceDefinitions, and for each indicate whether the given workspace has a grant for using the definition. Used by admins to view and modify a given workspace's grants.
        api_response = api_instance.list_private_source_definitions(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling SourceDefinitionApi->list_private_source_definitions: %s\n" % e)
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
[**WorkspaceIdRequestBody**](../../models/WorkspaceIdRequestBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_private_source_definitions.ApiResponseFor200) | Successful operation

#### list_private_source_definitions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PrivateSourceDefinitionReadList**](../../models/PrivateSourceDefinitionReadList.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_source_definitions**
<a name="list_source_definitions"></a>
> SourceDefinitionReadList list_source_definitions()

List all the sourceDefinitions the current Airbyte deployment is configured to use

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import source_definition_api
from airbyte_config_api_client.model.source_definition_read_list import SourceDefinitionReadList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = airbyte_config_api_client.Configuration(
    host = "http://localhost:8000/api"
)

# Enter a context with an instance of the API client
with airbyte_config_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source_definition_api.SourceDefinitionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List all the sourceDefinitions the current Airbyte deployment is configured to use
        api_response = api_instance.list_source_definitions()
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling SourceDefinitionApi->list_source_definitions: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_source_definitions.ApiResponseFor200) | Successful operation

#### list_source_definitions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SourceDefinitionReadList**](../../models/SourceDefinitionReadList.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_source_definitions_for_workspace**
<a name="list_source_definitions_for_workspace"></a>
> SourceDefinitionReadList list_source_definitions_for_workspace()

List all the sourceDefinitions the given workspace is configured to use

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import source_definition_api
from airbyte_config_api_client.model.source_definition_read_list import SourceDefinitionReadList
from airbyte_config_api_client.model.workspace_id_request_body import WorkspaceIdRequestBody
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = airbyte_config_api_client.Configuration(
    host = "http://localhost:8000/api"
)

# Enter a context with an instance of the API client
with airbyte_config_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = source_definition_api.SourceDefinitionApi(api_client)

    # example passing only optional values
    body = WorkspaceIdRequestBody(
        workspace_id="workspace_id_example",
    )
    try:
        # List all the sourceDefinitions the given workspace is configured to use
        api_response = api_instance.list_source_definitions_for_workspace(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling SourceDefinitionApi->list_source_definitions_for_workspace: %s\n" % e)
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
[**WorkspaceIdRequestBody**](../../models/WorkspaceIdRequestBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_source_definitions_for_workspace.ApiResponseFor200) | Successful operation

#### list_source_definitions_for_workspace.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SourceDefinitionReadList**](../../models/SourceDefinitionReadList.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **revoke_source_definition_from_workspace**
<a name="revoke_source_definition_from_workspace"></a>
> revoke_source_definition_from_workspace(source_definition_id_with_workspace_id)

revoke a grant to a private, non-custom sourceDefinition from a given workspace

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import source_definition_api
from airbyte_config_api_client.model.source_definition_id_with_workspace_id import SourceDefinitionIdWithWorkspaceId
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
    api_instance = source_definition_api.SourceDefinitionApi(api_client)

    # example passing only required values which don't have defaults set
    body = SourceDefinitionIdWithWorkspaceId(
        source_definition_id="source_definition_id_example",
        workspace_id="workspace_id_example",
    )
    try:
        # revoke a grant to a private, non-custom sourceDefinition from a given workspace
        api_response = api_instance.revoke_source_definition_from_workspace(
            body=body,
        )
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling SourceDefinitionApi->revoke_source_definition_from_workspace: %s\n" % e)
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
[**SourceDefinitionIdWithWorkspaceId**](../../models/SourceDefinitionIdWithWorkspaceId.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#revoke_source_definition_from_workspace.ApiResponseFor204) | The resource was deleted successfully.
404 | [ApiResponseFor404](#revoke_source_definition_from_workspace.ApiResponseFor404) | Object with given id was not found.
422 | [ApiResponseFor422](#revoke_source_definition_from_workspace.ApiResponseFor422) | Input failed validation

#### revoke_source_definition_from_workspace.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### revoke_source_definition_from_workspace.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundKnownExceptionInfo**](../../models/NotFoundKnownExceptionInfo.md) |  | 


#### revoke_source_definition_from_workspace.ApiResponseFor422
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

# **update_source_definition**
<a name="update_source_definition"></a>
> SourceDefinitionRead update_source_definition()

Update a sourceDefinition

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import source_definition_api
from airbyte_config_api_client.model.source_definition_update import SourceDefinitionUpdate
from airbyte_config_api_client.model.source_definition_read import SourceDefinitionRead
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
    api_instance = source_definition_api.SourceDefinitionApi(api_client)

    # example passing only optional values
    body = SourceDefinitionUpdate(
        source_definition_id="source_definition_id_example",
        docker_image_tag="docker_image_tag_example",
        resource_requirements=ActorDefinitionResourceRequirements(
            default=ResourceRequirements(
                cpu_request="cpu_request_example",
                cpu_limit="cpu_limit_example",
                memory_request="memory_request_example",
                memory_limit="memory_limit_example",
            ),
            job_specific=[
                JobTypeResourceLimit(
                    job_type=JobType("get_spec"),
                    resource_requirements=ResourceRequirements(),
                )
            ],
        ),
    )
    try:
        # Update a sourceDefinition
        api_response = api_instance.update_source_definition(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling SourceDefinitionApi->update_source_definition: %s\n" % e)
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
[**SourceDefinitionUpdate**](../../models/SourceDefinitionUpdate.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_source_definition.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#update_source_definition.ApiResponseFor404) | Object with given id was not found.
422 | [ApiResponseFor422](#update_source_definition.ApiResponseFor422) | Input failed validation

#### update_source_definition.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SourceDefinitionRead**](../../models/SourceDefinitionRead.md) |  | 


#### update_source_definition.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundKnownExceptionInfo**](../../models/NotFoundKnownExceptionInfo.md) |  | 


#### update_source_definition.ApiResponseFor422
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

