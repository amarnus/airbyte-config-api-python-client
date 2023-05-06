<a name="__pageTop"></a>
# airbyte_config_api_client.apis.tags.health_api.HealthApi

All URIs are relative to *http://localhost:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_health_check**](#get_health_check) | **get** /v1/health | Health Check

# **get_health_check**
<a name="get_health_check"></a>
> HealthCheckRead get_health_check()

Health Check

### Example

```python
import airbyte_config_api_client
from airbyte_config_api_client.apis.tags import health_api
from airbyte_config_api_client.model.health_check_read import HealthCheckRead
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = airbyte_config_api_client.Configuration(
    host = "http://localhost:8000/api"
)

# Enter a context with an instance of the API client
with airbyte_config_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = health_api.HealthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Health Check
        api_response = api_instance.get_health_check()
        pprint(api_response)
    except airbyte_config_api_client.ApiException as e:
        print("Exception when calling HealthApi->get_health_check: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_health_check.ApiResponseFor200) | Successful operation

#### get_health_check.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HealthCheckRead**](../../models/HealthCheckRead.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

