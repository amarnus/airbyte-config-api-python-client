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


class AttemptStats(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            recordsEmitted = schemas.Int64Schema
            bytesEmitted = schemas.Int64Schema
            stateMessagesEmitted = schemas.Int64Schema
            recordsCommitted = schemas.Int64Schema
            estimatedRecords = schemas.Int64Schema
            estimatedBytes = schemas.Int64Schema
            __annotations__ = {
                "recordsEmitted": recordsEmitted,
                "bytesEmitted": bytesEmitted,
                "stateMessagesEmitted": stateMessagesEmitted,
                "recordsCommitted": recordsCommitted,
                "estimatedRecords": estimatedRecords,
                "estimatedBytes": estimatedBytes,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recordsEmitted"]) -> MetaOapg.properties.recordsEmitted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bytesEmitted"]) -> MetaOapg.properties.bytesEmitted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stateMessagesEmitted"]) -> MetaOapg.properties.stateMessagesEmitted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recordsCommitted"]) -> MetaOapg.properties.recordsCommitted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["estimatedRecords"]) -> MetaOapg.properties.estimatedRecords: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["estimatedBytes"]) -> MetaOapg.properties.estimatedBytes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["recordsEmitted", "bytesEmitted", "stateMessagesEmitted", "recordsCommitted", "estimatedRecords", "estimatedBytes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recordsEmitted"]) -> typing.Union[MetaOapg.properties.recordsEmitted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bytesEmitted"]) -> typing.Union[MetaOapg.properties.bytesEmitted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stateMessagesEmitted"]) -> typing.Union[MetaOapg.properties.stateMessagesEmitted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recordsCommitted"]) -> typing.Union[MetaOapg.properties.recordsCommitted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["estimatedRecords"]) -> typing.Union[MetaOapg.properties.estimatedRecords, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["estimatedBytes"]) -> typing.Union[MetaOapg.properties.estimatedBytes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["recordsEmitted", "bytesEmitted", "stateMessagesEmitted", "recordsCommitted", "estimatedRecords", "estimatedBytes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        recordsEmitted: typing.Union[MetaOapg.properties.recordsEmitted, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        bytesEmitted: typing.Union[MetaOapg.properties.bytesEmitted, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        stateMessagesEmitted: typing.Union[MetaOapg.properties.stateMessagesEmitted, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        recordsCommitted: typing.Union[MetaOapg.properties.recordsCommitted, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        estimatedRecords: typing.Union[MetaOapg.properties.estimatedRecords, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        estimatedBytes: typing.Union[MetaOapg.properties.estimatedBytes, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AttemptStats':
        return super().__new__(
            cls,
            *_args,
            recordsEmitted=recordsEmitted,
            bytesEmitted=bytesEmitted,
            stateMessagesEmitted=stateMessagesEmitted,
            recordsCommitted=recordsCommitted,
            estimatedRecords=estimatedRecords,
            estimatedBytes=estimatedBytes,
            _configuration=_configuration,
            **kwargs,
        )
