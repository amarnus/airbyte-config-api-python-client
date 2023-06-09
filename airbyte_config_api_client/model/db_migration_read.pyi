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


class DbMigrationRead(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "migrationDescription",
            "migrationVersion",
            "migrationType",
        }
        
        class properties:
            migrationType = schemas.StrSchema
            migrationVersion = schemas.StrSchema
            migrationDescription = schemas.StrSchema
        
            @staticmethod
            def migrationState() -> typing.Type['DbMigrationState']:
                return DbMigrationState
            migratedBy = schemas.StrSchema
            migratedAt = schemas.Int64Schema
            migrationScript = schemas.StrSchema
            __annotations__ = {
                "migrationType": migrationType,
                "migrationVersion": migrationVersion,
                "migrationDescription": migrationDescription,
                "migrationState": migrationState,
                "migratedBy": migratedBy,
                "migratedAt": migratedAt,
                "migrationScript": migrationScript,
            }
    
    migrationDescription: MetaOapg.properties.migrationDescription
    migrationVersion: MetaOapg.properties.migrationVersion
    migrationType: MetaOapg.properties.migrationType
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["migrationType"]) -> MetaOapg.properties.migrationType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["migrationVersion"]) -> MetaOapg.properties.migrationVersion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["migrationDescription"]) -> MetaOapg.properties.migrationDescription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["migrationState"]) -> 'DbMigrationState': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["migratedBy"]) -> MetaOapg.properties.migratedBy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["migratedAt"]) -> MetaOapg.properties.migratedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["migrationScript"]) -> MetaOapg.properties.migrationScript: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["migrationType", "migrationVersion", "migrationDescription", "migrationState", "migratedBy", "migratedAt", "migrationScript", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["migrationType"]) -> MetaOapg.properties.migrationType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["migrationVersion"]) -> MetaOapg.properties.migrationVersion: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["migrationDescription"]) -> MetaOapg.properties.migrationDescription: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["migrationState"]) -> typing.Union['DbMigrationState', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["migratedBy"]) -> typing.Union[MetaOapg.properties.migratedBy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["migratedAt"]) -> typing.Union[MetaOapg.properties.migratedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["migrationScript"]) -> typing.Union[MetaOapg.properties.migrationScript, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["migrationType", "migrationVersion", "migrationDescription", "migrationState", "migratedBy", "migratedAt", "migrationScript", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        migrationDescription: typing.Union[MetaOapg.properties.migrationDescription, str, ],
        migrationVersion: typing.Union[MetaOapg.properties.migrationVersion, str, ],
        migrationType: typing.Union[MetaOapg.properties.migrationType, str, ],
        migrationState: typing.Union['DbMigrationState', schemas.Unset] = schemas.unset,
        migratedBy: typing.Union[MetaOapg.properties.migratedBy, str, schemas.Unset] = schemas.unset,
        migratedAt: typing.Union[MetaOapg.properties.migratedAt, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        migrationScript: typing.Union[MetaOapg.properties.migrationScript, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DbMigrationRead':
        return super().__new__(
            cls,
            *_args,
            migrationDescription=migrationDescription,
            migrationVersion=migrationVersion,
            migrationType=migrationType,
            migrationState=migrationState,
            migratedBy=migratedBy,
            migratedAt=migratedAt,
            migrationScript=migrationScript,
            _configuration=_configuration,
            **kwargs,
        )

from airbyte_config_api_client.model.db_migration_state import DbMigrationState
