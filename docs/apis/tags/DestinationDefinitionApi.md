<a name="__pageTop"></a>
# airbyte_config_api_client.apis.tags.destination_definition_api.DestinationDefinitionApi

All URIs are relative to *http://localhost:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_destination_definition**](#create_custom_destination_definition) | **post** /v1/destination_definitions/create_custom | Creates a custom destinationDefinition for the given workspace
[**delete_destination_definition**](#delete_destination_definition) | **post** /v1/destination_definitions/delete | Delete a destination definition
[**get_destination_definition**](#get_destination_definition) | **post** /v1/destination_definitions/get | Get destinationDefinition
[**get_destination_definition_for_workspace**](#get_destination_definition_for_workspace) | **post** /v1/destination_definitions/get_for_workspace | Get a destinationDefinition that is configured for the given workspace
[**grant_destination_definition_to_workspace**](#grant_destination_definition_to_workspace) | **post** /v1/destination_definitions/grant_definition | grant a private, non-custom destinationDefinition to a given workspace
[**list_destination_definitions**](#list_destination_definitions) | **post** /v1/destination_definitions/list | List all the destinationDefinitions the current Airbyte deployment is configured to use
[**list_destination_definitions_for_workspace**](#list_destination_definitions_for_workspace) | **post** /v1/destination_definitions/list_for_workspace | List all the destinationDefinitions the given workspace is configured to use
[**list_latest_destination_definitions**](#list_latest_destination_definitions) | **post** /v1/destination_definitions/list_latest | List the latest destinationDefinitions Airbyte supports
[**list_private_destination_definitions**](#list_private_destination_definitions) | **post** /v1/destination_definitions/list_private | List all private, non-custom destinationDefinitions, and for each indicate whether the given workspace has a grant for using the definition. Used by admins to view and modify a given workspace&#x27;s grants.
[**revoke_destination_definition_from_workspace**](#revoke_destination_definition_from_workspace) | **post** /v1/destination_definitions/revoke_definition | revoke a grant to a private, non-custom destinationDefinition from a given workspace
[**update_destination_definition**](#update_destination_definition) | **post** /v1/destination_definitions/update | Update destinationDefinition

# **create_custom_destination_definition**
<a name="create_custom_destination_definition"></a>
> DestinationDefinitionRead create_custom_destination_definition()

Creates a custom destinationDefinition for the given workspace

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import destination_definition_api
from airbyte_config_api_client.model.custom_destination_definition_create import CustomDestinationDefinitionCreate
from airbyte_config_api_client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from airbyte_config_api_client.model.destination_definition_read import DestinationDefinitionRead
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = airbyte_config_api_client.Configuration(
    host = "http://localhost:8000/api"
)

# Enter a context with an instance of the API client
with airbyte_config_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = destination_definition_api.DestinationDefinitionApi(api_client)

    # example passing only optional values
    body = CustomDestinationDefinitionCreate(
        workspace_id="workspace_id_example",
        destination_definition=DestinationDefinitionCreate(
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
        # Creates a custom destinationDefinition for the given workspace
        api_response = api_instance.create_custom_destination_definition(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling DestinationDefinitionApi->create_custom_destination_definition: %s\n" % e)
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
[**CustomDestinationDefinitionCreate**](../../models/CustomDestinationDefinitionCreate.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_custom_destination_definition.ApiResponseFor200) | Successful operation
422 | [ApiResponseFor422](#create_custom_destination_definition.ApiResponseFor422) | Input failed validation

#### create_custom_destination_definition.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DestinationDefinitionRead**](../../models/DestinationDefinitionRead.md) |  | 


#### create_custom_destination_definition.ApiResponseFor422
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

# **delete_destination_definition**
<a name="delete_destination_definition"></a>
> delete_destination_definition(destination_definition_id_request_body)

Delete a destination definition

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import destination_definition_api
from airbyte_config_api_client.model.destination_definition_id_request_body import DestinationDefinitionIdRequestBody
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
    api_instance = destination_definition_api.DestinationDefinitionApi(api_client)

    # example passing only required values which don't have defaults set
    body = DestinationDefinitionIdRequestBody(
        destination_definition_id="destination_definition_id_example",
    )
    try:
        # Delete a destination definition
        api_response = api_instance.delete_destination_definition(
            body=body,
        )
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling DestinationDefinitionApi->delete_destination_definition: %s\n" % e)
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
[**DestinationDefinitionIdRequestBody**](../../models/DestinationDefinitionIdRequestBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_destination_definition.ApiResponseFor204) | The resource was deleted successfully.
404 | [ApiResponseFor404](#delete_destination_definition.ApiResponseFor404) | Object with given id was not found.
422 | [ApiResponseFor422](#delete_destination_definition.ApiResponseFor422) | Input failed validation

#### delete_destination_definition.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_destination_definition.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundKnownExceptionInfo**](../../models/NotFoundKnownExceptionInfo.md) |  | 


#### delete_destination_definition.ApiResponseFor422
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

# **get_destination_definition**
<a name="get_destination_definition"></a>
> DestinationDefinitionRead get_destination_definition(destination_definition_id_request_body)

Get destinationDefinition

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import destination_definition_api
from airbyte_config_api_client.model.destination_definition_id_request_body import DestinationDefinitionIdRequestBody
from airbyte_config_api_client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from airbyte_config_api_client.model.destination_definition_read import DestinationDefinitionRead
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
    api_instance = destination_definition_api.DestinationDefinitionApi(api_client)

    # example passing only required values which don't have defaults set
    body = DestinationDefinitionIdRequestBody(
        destination_definition_id="destination_definition_id_example",
    )
    try:
        # Get destinationDefinition
        api_response = api_instance.get_destination_definition(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling DestinationDefinitionApi->get_destination_definition: %s\n" % e)
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
[**DestinationDefinitionIdRequestBody**](../../models/DestinationDefinitionIdRequestBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_destination_definition.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#get_destination_definition.ApiResponseFor404) | Object with given id was not found.
422 | [ApiResponseFor422](#get_destination_definition.ApiResponseFor422) | Input failed validation

#### get_destination_definition.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DestinationDefinitionRead**](../../models/DestinationDefinitionRead.md) |  | 


#### get_destination_definition.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundKnownExceptionInfo**](../../models/NotFoundKnownExceptionInfo.md) |  | 


#### get_destination_definition.ApiResponseFor422
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

# **get_destination_definition_for_workspace**
<a name="get_destination_definition_for_workspace"></a>
> DestinationDefinitionRead get_destination_definition_for_workspace(destination_definition_id_with_workspace_id)

Get a destinationDefinition that is configured for the given workspace

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import destination_definition_api
from airbyte_config_api_client.model.destination_definition_id_with_workspace_id import DestinationDefinitionIdWithWorkspaceId
from airbyte_config_api_client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from airbyte_config_api_client.model.destination_definition_read import DestinationDefinitionRead
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
    api_instance = destination_definition_api.DestinationDefinitionApi(api_client)

    # example passing only required values which don't have defaults set
    body = DestinationDefinitionIdWithWorkspaceId(
        destination_definition_id="destination_definition_id_example",
        workspace_id="workspace_id_example",
    )
    try:
        # Get a destinationDefinition that is configured for the given workspace
        api_response = api_instance.get_destination_definition_for_workspace(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling DestinationDefinitionApi->get_destination_definition_for_workspace: %s\n" % e)
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
[**DestinationDefinitionIdWithWorkspaceId**](../../models/DestinationDefinitionIdWithWorkspaceId.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_destination_definition_for_workspace.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#get_destination_definition_for_workspace.ApiResponseFor404) | Object with given id was not found.
422 | [ApiResponseFor422](#get_destination_definition_for_workspace.ApiResponseFor422) | Input failed validation

#### get_destination_definition_for_workspace.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DestinationDefinitionRead**](../../models/DestinationDefinitionRead.md) |  | 


#### get_destination_definition_for_workspace.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundKnownExceptionInfo**](../../models/NotFoundKnownExceptionInfo.md) |  | 


#### get_destination_definition_for_workspace.ApiResponseFor422
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

# **grant_destination_definition_to_workspace**
<a name="grant_destination_definition_to_workspace"></a>
> PrivateDestinationDefinitionRead grant_destination_definition_to_workspace(destination_definition_id_with_workspace_id)

grant a private, non-custom destinationDefinition to a given workspace

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import destination_definition_api
from airbyte_config_api_client.model.destination_definition_id_with_workspace_id import DestinationDefinitionIdWithWorkspaceId
from airbyte_config_api_client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from airbyte_config_api_client.model.private_destination_definition_read import PrivateDestinationDefinitionRead
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
    api_instance = destination_definition_api.DestinationDefinitionApi(api_client)

    # example passing only required values which don't have defaults set
    body = DestinationDefinitionIdWithWorkspaceId(
        destination_definition_id="destination_definition_id_example",
        workspace_id="workspace_id_example",
    )
    try:
        # grant a private, non-custom destinationDefinition to a given workspace
        api_response = api_instance.grant_destination_definition_to_workspace(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling DestinationDefinitionApi->grant_destination_definition_to_workspace: %s\n" % e)
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
[**DestinationDefinitionIdWithWorkspaceId**](../../models/DestinationDefinitionIdWithWorkspaceId.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#grant_destination_definition_to_workspace.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#grant_destination_definition_to_workspace.ApiResponseFor404) | Object with given id was not found.
422 | [ApiResponseFor422](#grant_destination_definition_to_workspace.ApiResponseFor422) | Input failed validation

#### grant_destination_definition_to_workspace.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PrivateDestinationDefinitionRead**](../../models/PrivateDestinationDefinitionRead.md) |  | 


#### grant_destination_definition_to_workspace.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundKnownExceptionInfo**](../../models/NotFoundKnownExceptionInfo.md) |  | 


#### grant_destination_definition_to_workspace.ApiResponseFor422
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

# **list_destination_definitions**
<a name="list_destination_definitions"></a>
> DestinationDefinitionReadList list_destination_definitions()

List all the destinationDefinitions the current Airbyte deployment is configured to use

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import destination_definition_api
from airbyte_config_api_client.model.destination_definition_read_list import DestinationDefinitionReadList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = airbyte_config_api_client.Configuration(
    host = "http://localhost:8000/api"
)

# Enter a context with an instance of the API client
with airbyte_config_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = destination_definition_api.DestinationDefinitionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List all the destinationDefinitions the current Airbyte deployment is configured to use
        api_response = api_instance.list_destination_definitions()
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling DestinationDefinitionApi->list_destination_definitions: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_destination_definitions.ApiResponseFor200) | Successful operation

#### list_destination_definitions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DestinationDefinitionReadList**](../../models/DestinationDefinitionReadList.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_destination_definitions_for_workspace**
<a name="list_destination_definitions_for_workspace"></a>
> DestinationDefinitionReadList list_destination_definitions_for_workspace()

List all the destinationDefinitions the given workspace is configured to use

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import destination_definition_api
from airbyte_config_api_client.model.workspace_id_request_body import WorkspaceIdRequestBody
from airbyte_config_api_client.model.destination_definition_read_list import DestinationDefinitionReadList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = airbyte_config_api_client.Configuration(
    host = "http://localhost:8000/api"
)

# Enter a context with an instance of the API client
with airbyte_config_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = destination_definition_api.DestinationDefinitionApi(api_client)

    # example passing only optional values
    body = WorkspaceIdRequestBody(
        workspace_id="workspace_id_example",
    )
    try:
        # List all the destinationDefinitions the given workspace is configured to use
        api_response = api_instance.list_destination_definitions_for_workspace(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling DestinationDefinitionApi->list_destination_definitions_for_workspace: %s\n" % e)
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
200 | [ApiResponseFor200](#list_destination_definitions_for_workspace.ApiResponseFor200) | Successful operation

#### list_destination_definitions_for_workspace.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DestinationDefinitionReadList**](../../models/DestinationDefinitionReadList.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_latest_destination_definitions**
<a name="list_latest_destination_definitions"></a>
> DestinationDefinitionReadList list_latest_destination_definitions()

List the latest destinationDefinitions Airbyte supports

Guaranteed to retrieve the latest information on supported destinations.

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import destination_definition_api
from airbyte_config_api_client.model.destination_definition_read_list import DestinationDefinitionReadList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = airbyte_config_api_client.Configuration(
    host = "http://localhost:8000/api"
)

# Enter a context with an instance of the API client
with airbyte_config_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = destination_definition_api.DestinationDefinitionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List the latest destinationDefinitions Airbyte supports
        api_response = api_instance.list_latest_destination_definitions()
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling DestinationDefinitionApi->list_latest_destination_definitions: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_latest_destination_definitions.ApiResponseFor200) | Successful operation

#### list_latest_destination_definitions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DestinationDefinitionReadList**](../../models/DestinationDefinitionReadList.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_private_destination_definitions**
<a name="list_private_destination_definitions"></a>
> PrivateDestinationDefinitionReadList list_private_destination_definitions()

List all private, non-custom destinationDefinitions, and for each indicate whether the given workspace has a grant for using the definition. Used by admins to view and modify a given workspace's grants.

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import destination_definition_api
from airbyte_config_api_client.model.private_destination_definition_read_list import PrivateDestinationDefinitionReadList
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
    api_instance = destination_definition_api.DestinationDefinitionApi(api_client)

    # example passing only optional values
    body = WorkspaceIdRequestBody(
        workspace_id="workspace_id_example",
    )
    try:
        # List all private, non-custom destinationDefinitions, and for each indicate whether the given workspace has a grant for using the definition. Used by admins to view and modify a given workspace's grants.
        api_response = api_instance.list_private_destination_definitions(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling DestinationDefinitionApi->list_private_destination_definitions: %s\n" % e)
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
200 | [ApiResponseFor200](#list_private_destination_definitions.ApiResponseFor200) | Successful operation

#### list_private_destination_definitions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PrivateDestinationDefinitionReadList**](../../models/PrivateDestinationDefinitionReadList.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **revoke_destination_definition_from_workspace**
<a name="revoke_destination_definition_from_workspace"></a>
> revoke_destination_definition_from_workspace(destination_definition_id_with_workspace_id)

revoke a grant to a private, non-custom destinationDefinition from a given workspace

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import destination_definition_api
from airbyte_config_api_client.model.destination_definition_id_with_workspace_id import DestinationDefinitionIdWithWorkspaceId
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
    api_instance = destination_definition_api.DestinationDefinitionApi(api_client)

    # example passing only required values which don't have defaults set
    body = DestinationDefinitionIdWithWorkspaceId(
        destination_definition_id="destination_definition_id_example",
        workspace_id="workspace_id_example",
    )
    try:
        # revoke a grant to a private, non-custom destinationDefinition from a given workspace
        api_response = api_instance.revoke_destination_definition_from_workspace(
            body=body,
        )
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling DestinationDefinitionApi->revoke_destination_definition_from_workspace: %s\n" % e)
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
[**DestinationDefinitionIdWithWorkspaceId**](../../models/DestinationDefinitionIdWithWorkspaceId.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#revoke_destination_definition_from_workspace.ApiResponseFor204) | The resource was deleted successfully.
404 | [ApiResponseFor404](#revoke_destination_definition_from_workspace.ApiResponseFor404) | Object with given id was not found.
422 | [ApiResponseFor422](#revoke_destination_definition_from_workspace.ApiResponseFor422) | Input failed validation

#### revoke_destination_definition_from_workspace.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### revoke_destination_definition_from_workspace.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundKnownExceptionInfo**](../../models/NotFoundKnownExceptionInfo.md) |  | 


#### revoke_destination_definition_from_workspace.ApiResponseFor422
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

# **update_destination_definition**
<a name="update_destination_definition"></a>
> DestinationDefinitionRead update_destination_definition(destination_definition_update)

Update destinationDefinition

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import destination_definition_api
from airbyte_config_api_client.model.destination_definition_update import DestinationDefinitionUpdate
from airbyte_config_api_client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from airbyte_config_api_client.model.destination_definition_read import DestinationDefinitionRead
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
    api_instance = destination_definition_api.DestinationDefinitionApi(api_client)

    # example passing only required values which don't have defaults set
    body = DestinationDefinitionUpdate(
        destination_definition_id="destination_definition_id_example",
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
        # Update destinationDefinition
        api_response = api_instance.update_destination_definition(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling DestinationDefinitionApi->update_destination_definition: %s\n" % e)
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
[**DestinationDefinitionUpdate**](../../models/DestinationDefinitionUpdate.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_destination_definition.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#update_destination_definition.ApiResponseFor404) | Object with given id was not found.
422 | [ApiResponseFor422](#update_destination_definition.ApiResponseFor422) | Input failed validation

#### update_destination_definition.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DestinationDefinitionRead**](../../models/DestinationDefinitionRead.md) |  | 


#### update_destination_definition.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundKnownExceptionInfo**](../../models/NotFoundKnownExceptionInfo.md) |  | 


#### update_destination_definition.ApiResponseFor422
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

