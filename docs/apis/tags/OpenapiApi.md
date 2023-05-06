<a name="__pageTop"></a>
# airbyte_config_api_client.apis.tags.openapi_api.OpenapiApi

All URIs are relative to *http://localhost:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_open_api_spec**](#get_open_api_spec) | **get** /v1/openapi | Returns the openapi specification

# **get_open_api_spec**
<a name="get_open_api_spec"></a>
> file_type get_open_api_spec()

Returns the openapi specification

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import openapi_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = airbyte_config_api_client.Configuration(
    host = "http://localhost:8000/api"
)

# Enter a context with an instance of the API client
with airbyte_config_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_api.OpenapiApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns the openapi specification
        api_response = api_instance.get_open_api_spec()
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling OpenapiApi->get_open_api_spec: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_open_api_spec.ApiResponseFor200) | Returns the openapi specification file

#### get_open_api_spec.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

