<a name="__pageTop"></a>
# airbyte_config_api_client.apis.tags.destination_api.DestinationApi

All URIs are relative to *http://localhost:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_connection_to_destination**](#check_connection_to_destination) | **post** /v1/destinations/check_connection | Check connection to the destination
[**check_connection_to_destination_for_update**](#check_connection_to_destination_for_update) | **post** /v1/destinations/check_connection_for_update | Check connection for a proposed update to a destination
[**clone_destination**](#clone_destination) | **post** /v1/destinations/clone | Clone destination
[**create_destination**](#create_destination) | **post** /v1/destinations/create | Create a destination
[**delete_destination**](#delete_destination) | **post** /v1/destinations/delete | Delete the destination
[**get_destination**](#get_destination) | **post** /v1/destinations/get | Get configured destination
[**list_destinations_for_workspace**](#list_destinations_for_workspace) | **post** /v1/destinations/list | List configured destinations for a workspace
[**search_destinations**](#search_destinations) | **post** /v1/destinations/search | Search destinations
[**update_destination**](#update_destination) | **post** /v1/destinations/update | Update a destination

# **check_connection_to_destination**
<a name="check_connection_to_destination"></a>
> CheckConnectionRead check_connection_to_destination(destination_id_request_body)

Check connection to the destination

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import destination_api
from airbyte_config_api_client.model.destination_id_request_body import DestinationIdRequestBody
from airbyte_config_api_client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from airbyte_config_api_client.model.check_connection_read import CheckConnectionRead
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
    api_instance = destination_api.DestinationApi(api_client)

    # example passing only required values which don't have defaults set
    body = DestinationIdRequestBody(
        destination_id="destination_id_example",
    )
    try:
        # Check connection to the destination
        api_response = api_instance.check_connection_to_destination(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling DestinationApi->check_connection_to_destination: %s\n" % e)
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
[**DestinationIdRequestBody**](../../models/DestinationIdRequestBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#check_connection_to_destination.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#check_connection_to_destination.ApiResponseFor404) | Object with given id was not found.
422 | [ApiResponseFor422](#check_connection_to_destination.ApiResponseFor422) | Input failed validation

#### check_connection_to_destination.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CheckConnectionRead**](../../models/CheckConnectionRead.md) |  | 


#### check_connection_to_destination.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundKnownExceptionInfo**](../../models/NotFoundKnownExceptionInfo.md) |  | 


#### check_connection_to_destination.ApiResponseFor422
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

# **check_connection_to_destination_for_update**
<a name="check_connection_to_destination_for_update"></a>
> CheckConnectionRead check_connection_to_destination_for_update(destination_update)

Check connection for a proposed update to a destination

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import destination_api
from airbyte_config_api_client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from airbyte_config_api_client.model.check_connection_read import CheckConnectionRead
from airbyte_config_api_client.model.destination_update import DestinationUpdate
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
    api_instance = destination_api.DestinationApi(api_client)

    # example passing only required values which don't have defaults set
    body = DestinationUpdate(
        destination_id="destination_id_example",
        connection_configuration=None,
        name="name_example",
    )
    try:
        # Check connection for a proposed update to a destination
        api_response = api_instance.check_connection_to_destination_for_update(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling DestinationApi->check_connection_to_destination_for_update: %s\n" % e)
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
[**DestinationUpdate**](../../models/DestinationUpdate.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#check_connection_to_destination_for_update.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#check_connection_to_destination_for_update.ApiResponseFor404) | Object with given id was not found.
422 | [ApiResponseFor422](#check_connection_to_destination_for_update.ApiResponseFor422) | Input failed validation

#### check_connection_to_destination_for_update.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CheckConnectionRead**](../../models/CheckConnectionRead.md) |  | 


#### check_connection_to_destination_for_update.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundKnownExceptionInfo**](../../models/NotFoundKnownExceptionInfo.md) |  | 


#### check_connection_to_destination_for_update.ApiResponseFor422
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

# **clone_destination**
<a name="clone_destination"></a>
> DestinationRead clone_destination(destination_clone_request_body)

Clone destination

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import destination_api
from airbyte_config_api_client.model.destination_read import DestinationRead
from airbyte_config_api_client.model.destination_clone_request_body import DestinationCloneRequestBody
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
    api_instance = destination_api.DestinationApi(api_client)

    # example passing only required values which don't have defaults set
    body = DestinationCloneRequestBody(
        destination_clone_id="destination_clone_id_example",
        destination_configuration=DestinationCloneConfiguration(
            connection_configuration=None,
            name="name_example",
        ),
    )
    try:
        # Clone destination
        api_response = api_instance.clone_destination(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling DestinationApi->clone_destination: %s\n" % e)
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
[**DestinationCloneRequestBody**](../../models/DestinationCloneRequestBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#clone_destination.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#clone_destination.ApiResponseFor404) | Object with given id was not found.
422 | [ApiResponseFor422](#clone_destination.ApiResponseFor422) | Input failed validation

#### clone_destination.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DestinationRead**](../../models/DestinationRead.md) |  | 


#### clone_destination.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundKnownExceptionInfo**](../../models/NotFoundKnownExceptionInfo.md) |  | 


#### clone_destination.ApiResponseFor422
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

# **create_destination**
<a name="create_destination"></a>
> DestinationRead create_destination(destination_create)

Create a destination

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import destination_api
from airbyte_config_api_client.model.destination_read import DestinationRead
from airbyte_config_api_client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from airbyte_config_api_client.model.destination_create import DestinationCreate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = airbyte_config_api_client.Configuration(
    host = "http://localhost:8000/api"
)

# Enter a context with an instance of the API client
with airbyte_config_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = destination_api.DestinationApi(api_client)

    # example passing only required values which don't have defaults set
    body = DestinationCreate(
        workspace_id="workspace_id_example",
        name="name_example",
        destination_definition_id="destination_definition_id_example",
        connection_configuration=None,
    )
    try:
        # Create a destination
        api_response = api_instance.create_destination(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling DestinationApi->create_destination: %s\n" % e)
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
[**DestinationCreate**](../../models/DestinationCreate.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_destination.ApiResponseFor200) | Successful operation
422 | [ApiResponseFor422](#create_destination.ApiResponseFor422) | Input failed validation

#### create_destination.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DestinationRead**](../../models/DestinationRead.md) |  | 


#### create_destination.ApiResponseFor422
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

# **delete_destination**
<a name="delete_destination"></a>
> delete_destination(destination_id_request_body)

Delete the destination

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import destination_api
from airbyte_config_api_client.model.destination_id_request_body import DestinationIdRequestBody
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
    api_instance = destination_api.DestinationApi(api_client)

    # example passing only required values which don't have defaults set
    body = DestinationIdRequestBody(
        destination_id="destination_id_example",
    )
    try:
        # Delete the destination
        api_response = api_instance.delete_destination(
            body=body,
        )
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling DestinationApi->delete_destination: %s\n" % e)
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
[**DestinationIdRequestBody**](../../models/DestinationIdRequestBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_destination.ApiResponseFor204) | The resource was deleted successfully.
404 | [ApiResponseFor404](#delete_destination.ApiResponseFor404) | Object with given id was not found.
422 | [ApiResponseFor422](#delete_destination.ApiResponseFor422) | Input failed validation

#### delete_destination.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_destination.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundKnownExceptionInfo**](../../models/NotFoundKnownExceptionInfo.md) |  | 


#### delete_destination.ApiResponseFor422
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

# **get_destination**
<a name="get_destination"></a>
> DestinationRead get_destination(destination_id_request_body)

Get configured destination

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import destination_api
from airbyte_config_api_client.model.destination_read import DestinationRead
from airbyte_config_api_client.model.destination_id_request_body import DestinationIdRequestBody
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
    api_instance = destination_api.DestinationApi(api_client)

    # example passing only required values which don't have defaults set
    body = DestinationIdRequestBody(
        destination_id="destination_id_example",
    )
    try:
        # Get configured destination
        api_response = api_instance.get_destination(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling DestinationApi->get_destination: %s\n" % e)
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
[**DestinationIdRequestBody**](../../models/DestinationIdRequestBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_destination.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#get_destination.ApiResponseFor404) | Object with given id was not found.
422 | [ApiResponseFor422](#get_destination.ApiResponseFor422) | Input failed validation

#### get_destination.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DestinationRead**](../../models/DestinationRead.md) |  | 


#### get_destination.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundKnownExceptionInfo**](../../models/NotFoundKnownExceptionInfo.md) |  | 


#### get_destination.ApiResponseFor422
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

# **list_destinations_for_workspace**
<a name="list_destinations_for_workspace"></a>
> DestinationReadList list_destinations_for_workspace(workspace_id_request_body)

List configured destinations for a workspace

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import destination_api
from airbyte_config_api_client.model.destination_read_list import DestinationReadList
from airbyte_config_api_client.model.workspace_id_request_body import WorkspaceIdRequestBody
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
    api_instance = destination_api.DestinationApi(api_client)

    # example passing only required values which don't have defaults set
    body = WorkspaceIdRequestBody(
        workspace_id="workspace_id_example",
    )
    try:
        # List configured destinations for a workspace
        api_response = api_instance.list_destinations_for_workspace(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling DestinationApi->list_destinations_for_workspace: %s\n" % e)
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
[**WorkspaceIdRequestBody**](../../models/WorkspaceIdRequestBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_destinations_for_workspace.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#list_destinations_for_workspace.ApiResponseFor404) | Object with given id was not found.
422 | [ApiResponseFor422](#list_destinations_for_workspace.ApiResponseFor422) | Input failed validation

#### list_destinations_for_workspace.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DestinationReadList**](../../models/DestinationReadList.md) |  | 


#### list_destinations_for_workspace.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundKnownExceptionInfo**](../../models/NotFoundKnownExceptionInfo.md) |  | 


#### list_destinations_for_workspace.ApiResponseFor422
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

# **search_destinations**
<a name="search_destinations"></a>
> DestinationReadList search_destinations(destination_search)

Search destinations

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import destination_api
from airbyte_config_api_client.model.destination_search import DestinationSearch
from airbyte_config_api_client.model.destination_read_list import DestinationReadList
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
    api_instance = destination_api.DestinationApi(api_client)

    # example passing only required values which don't have defaults set
    body = DestinationSearch(
        destination_definition_id="destination_definition_id_example",
        destination_id="destination_id_example",
        workspace_id="workspace_id_example",
        connection_configuration=None,
        name="name_example",
        destination_name="destination_name_example",
    )
    try:
        # Search destinations
        api_response = api_instance.search_destinations(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling DestinationApi->search_destinations: %s\n" % e)
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
[**DestinationSearch**](../../models/DestinationSearch.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_destinations.ApiResponseFor200) | Successful operation
422 | [ApiResponseFor422](#search_destinations.ApiResponseFor422) | Input failed validation

#### search_destinations.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DestinationReadList**](../../models/DestinationReadList.md) |  | 


#### search_destinations.ApiResponseFor422
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

# **update_destination**
<a name="update_destination"></a>
> DestinationRead update_destination(destination_update)

Update a destination

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import destination_api
from airbyte_config_api_client.model.destination_read import DestinationRead
from airbyte_config_api_client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from airbyte_config_api_client.model.destination_update import DestinationUpdate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = airbyte_config_api_client.Configuration(
    host = "http://localhost:8000/api"
)

# Enter a context with an instance of the API client
with airbyte_config_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = destination_api.DestinationApi(api_client)

    # example passing only required values which don't have defaults set
    body = DestinationUpdate(
        destination_id="destination_id_example",
        connection_configuration=None,
        name="name_example",
    )
    try:
        # Update a destination
        api_response = api_instance.update_destination(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling DestinationApi->update_destination: %s\n" % e)
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
[**DestinationUpdate**](../../models/DestinationUpdate.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_destination.ApiResponseFor200) | Successful operation
422 | [ApiResponseFor422](#update_destination.ApiResponseFor422) | Input failed validation

#### update_destination.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DestinationRead**](../../models/DestinationRead.md) |  | 


#### update_destination.ApiResponseFor422
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

