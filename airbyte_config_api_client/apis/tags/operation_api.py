# coding: utf-8

"""
    Airbyte Configuration API

    Airbyte Configuration API [https://airbyte.io](https://airbyte.io).  This API is a collection of HTTP RPC-style methods. While it is not a REST API, those familiar with REST should find the conventions of this API recognizable.  Here are some conventions that this API follows: * All endpoints are http POST methods. * All endpoints accept data via `application/json` request bodies. The API does not accept any data via query params. * The naming convention for endpoints is: localhost:8000/{VERSION}/{METHOD_FAMILY}/{METHOD_NAME} e.g. `localhost:8000/v1/connections/create`. * For all `update` methods, the whole object must be passed in, even the fields that did not change.  Authentication (OSS): * When authenticating to the Configuration API, you must use Basic Authentication by setting the Authentication Header to Basic and base64 encoding the username and password (which are `airbyte` and `password` by default - so base64 encoding `airbyte:password` results in `YWlyYnl0ZTpwYXNzd29yZA==`). So the full header reads `'Authorization': \"Basic YWlyYnl0ZTpwYXNzd29yZA==\"`   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: contact@airbyte.io
    Generated by: https://openapi-generator.tech
"""

from airbyte_config_api_client.paths.v1_operations_check.post import CheckOperation
from airbyte_config_api_client.paths.v1_operations_create.post import CreateOperation
from airbyte_config_api_client.paths.v1_operations_delete.post import DeleteOperation
from airbyte_config_api_client.paths.v1_operations_get.post import GetOperation
from airbyte_config_api_client.paths.v1_operations_list.post import ListOperationsForConnection
from airbyte_config_api_client.paths.v1_operations_update.post import UpdateOperation


class OperationApi(
    CheckOperation,
    CreateOperation,
    DeleteOperation,
    GetOperation,
    ListOperationsForConnection,
    UpdateOperation,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
