# coding: utf-8

"""
    Airbyte Configuration API

    Airbyte Configuration API [https://airbyte.io](https://airbyte.io).  This API is a collection of HTTP RPC-style methods. While it is not a REST API, those familiar with REST should find the conventions of this API recognizable.  Here are some conventions that this API follows: * All endpoints are http POST methods. * All endpoints accept data via `application/json` request bodies. The API does not accept any data via query params. * The naming convention for endpoints is: localhost:8000/{VERSION}/{METHOD_FAMILY}/{METHOD_NAME} e.g. `localhost:8000/v1/connections/create`. * For all `update` methods, the whole object must be passed in, even the fields that did not change.  Authentication (OSS): * When authenticating to the Configuration API, you must use Basic Authentication by setting the Authentication Header to Basic and base64 encoding the username and password (which are `airbyte` and `password` by default - so base64 encoding `airbyte:password` results in `YWlyYnl0ZTpwYXNzd29yZA==`). So the full header reads `'Authorization': \"Basic YWlyYnl0ZTpwYXNzd29yZA==\"`   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: contact@airbyte.io
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from airbyte_config_api_client import schemas  # noqa: F401


class SourceDiscoverSchemaRead(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Returns the results of a discover catalog job. If the job was not successful, the catalog field will not be present. jobInfo will aways be present and its status be used to determine if the job was successful or not.
    """


    class MetaOapg:
        required = {
            "jobInfo",
        }
        
        class properties:
        
            @staticmethod
            def jobInfo() -> typing.Type['SynchronousJobRead']:
                return SynchronousJobRead
        
            @staticmethod
            def catalog() -> typing.Type['AirbyteCatalog']:
                return AirbyteCatalog
            catalogId = schemas.UUIDSchema
        
            @staticmethod
            def catalogDiff() -> typing.Type['CatalogDiff']:
                return CatalogDiff
            breakingChange = schemas.BoolSchema
        
            @staticmethod
            def connectionStatus() -> typing.Type['ConnectionStatus']:
                return ConnectionStatus
            __annotations__ = {
                "jobInfo": jobInfo,
                "catalog": catalog,
                "catalogId": catalogId,
                "catalogDiff": catalogDiff,
                "breakingChange": breakingChange,
                "connectionStatus": connectionStatus,
            }
    
    jobInfo: 'SynchronousJobRead'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jobInfo"]) -> 'SynchronousJobRead': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["catalog"]) -> 'AirbyteCatalog': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["catalogId"]) -> MetaOapg.properties.catalogId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["catalogDiff"]) -> 'CatalogDiff': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["breakingChange"]) -> MetaOapg.properties.breakingChange: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["connectionStatus"]) -> 'ConnectionStatus': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["jobInfo", "catalog", "catalogId", "catalogDiff", "breakingChange", "connectionStatus", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jobInfo"]) -> 'SynchronousJobRead': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["catalog"]) -> typing.Union['AirbyteCatalog', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["catalogId"]) -> typing.Union[MetaOapg.properties.catalogId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["catalogDiff"]) -> typing.Union['CatalogDiff', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["breakingChange"]) -> typing.Union[MetaOapg.properties.breakingChange, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["connectionStatus"]) -> typing.Union['ConnectionStatus', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["jobInfo", "catalog", "catalogId", "catalogDiff", "breakingChange", "connectionStatus", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        jobInfo: 'SynchronousJobRead',
        catalog: typing.Union['AirbyteCatalog', schemas.Unset] = schemas.unset,
        catalogId: typing.Union[MetaOapg.properties.catalogId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        catalogDiff: typing.Union['CatalogDiff', schemas.Unset] = schemas.unset,
        breakingChange: typing.Union[MetaOapg.properties.breakingChange, bool, schemas.Unset] = schemas.unset,
        connectionStatus: typing.Union['ConnectionStatus', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SourceDiscoverSchemaRead':
        return super().__new__(
            cls,
            *_args,
            jobInfo=jobInfo,
            catalog=catalog,
            catalogId=catalogId,
            catalogDiff=catalogDiff,
            breakingChange=breakingChange,
            connectionStatus=connectionStatus,
            _configuration=_configuration,
            **kwargs,
        )

from airbyte_config_api_client.model.airbyte_catalog import AirbyteCatalog
from airbyte_config_api_client.model.catalog_diff import CatalogDiff
from airbyte_config_api_client.model.connection_status import ConnectionStatus
from airbyte_config_api_client.model.synchronous_job_read import SynchronousJobRead
