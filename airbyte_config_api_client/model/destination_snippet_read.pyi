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


class DestinationSnippetRead(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "destinationName",
            "name",
            "destinationDefinitionId",
            "destinationId",
        }
        
        class properties:
            destinationId = schemas.UUIDSchema
            name = schemas.StrSchema
            destinationDefinitionId = schemas.UUIDSchema
            destinationName = schemas.StrSchema
            icon = schemas.StrSchema
            __annotations__ = {
                "destinationId": destinationId,
                "name": name,
                "destinationDefinitionId": destinationDefinitionId,
                "destinationName": destinationName,
                "icon": icon,
            }
    
    destinationName: MetaOapg.properties.destinationName
    name: MetaOapg.properties.name
    destinationDefinitionId: MetaOapg.properties.destinationDefinitionId
    destinationId: MetaOapg.properties.destinationId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["destinationId"]) -> MetaOapg.properties.destinationId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["destinationDefinitionId"]) -> MetaOapg.properties.destinationDefinitionId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["destinationName"]) -> MetaOapg.properties.destinationName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["icon"]) -> MetaOapg.properties.icon: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["destinationId", "name", "destinationDefinitionId", "destinationName", "icon", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["destinationId"]) -> MetaOapg.properties.destinationId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["destinationDefinitionId"]) -> MetaOapg.properties.destinationDefinitionId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["destinationName"]) -> MetaOapg.properties.destinationName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["icon"]) -> typing.Union[MetaOapg.properties.icon, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["destinationId", "name", "destinationDefinitionId", "destinationName", "icon", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        destinationName: typing.Union[MetaOapg.properties.destinationName, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        destinationDefinitionId: typing.Union[MetaOapg.properties.destinationDefinitionId, str, uuid.UUID, ],
        destinationId: typing.Union[MetaOapg.properties.destinationId, str, uuid.UUID, ],
        icon: typing.Union[MetaOapg.properties.icon, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DestinationSnippetRead':
        return super().__new__(
            cls,
            *_args,
            destinationName=destinationName,
            name=name,
            destinationDefinitionId=destinationDefinitionId,
            destinationId=destinationId,
            icon=icon,
            _configuration=_configuration,
            **kwargs,
        )
