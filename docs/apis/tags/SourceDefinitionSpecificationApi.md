<a name="__pageTop"></a>
# airbyte_config_api_client.apis.tags.source_definition_specification_api.SourceDefinitionSpecificationApi

All URIs are relative to *http://localhost:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_source_definition_specification**](#get_source_definition_specification) | **post** /v1/source_definition_specifications/get | Get specification for a SourceDefinition.

# **get_source_definition_specification**
<a name="get_source_definition_specification"></a>
> SourceDefinitionSpecificationRead get_source_definition_specification(source_definition_id_with_workspace_id)

Get specification for a SourceDefinition.

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import source_definition_specification_api
from airbyte_config_api_client.model.source_definition_id_with_workspace_id import SourceDefinitionIdWithWorkspaceId
from airbyte_config_api_client.model.invalid_input_exception_info import InvalidInputExceptionInfo
from airbyte_config_api_client.model.source_definition_specification_read import SourceDefinitionSpecificationRead
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
    api_instance = source_definition_specification_api.SourceDefinitionSpecificationApi(api_client)

    # example passing only required values which don't have defaults set
    body = SourceDefinitionIdWithWorkspaceId(
        source_definition_id="source_definition_id_example",
        workspace_id="workspace_id_example",
    )
    try:
        # Get specification for a SourceDefinition.
        api_response = api_instance.get_source_definition_specification(
            body=body,
        )
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling SourceDefinitionSpecificationApi->get_source_definition_specification: %s\n" % e)
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
200 | [ApiResponseFor200](#get_source_definition_specification.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#get_source_definition_specification.ApiResponseFor404) | Object with given id was not found.
422 | [ApiResponseFor422](#get_source_definition_specification.ApiResponseFor422) | Input failed validation

#### get_source_definition_specification.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SourceDefinitionSpecificationRead**](../../models/SourceDefinitionSpecificationRead.md) |  | 


#### get_source_definition_specification.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundKnownExceptionInfo**](../../models/NotFoundKnownExceptionInfo.md) |  | 


#### get_source_definition_specification.ApiResponseFor422
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

