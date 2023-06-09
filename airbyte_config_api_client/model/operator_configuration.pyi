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


class OperatorConfiguration(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "operatorType",
        }
        
        class properties:
        
            @staticmethod
            def operatorType() -> typing.Type['OperatorType']:
                return OperatorType
        
            @staticmethod
            def normalization() -> typing.Type['OperatorNormalization']:
                return OperatorNormalization
        
            @staticmethod
            def dbt() -> typing.Type['OperatorDbt']:
                return OperatorDbt
        
            @staticmethod
            def webhook() -> typing.Type['OperatorWebhook']:
                return OperatorWebhook
            __annotations__ = {
                "operatorType": operatorType,
                "normalization": normalization,
                "dbt": dbt,
                "webhook": webhook,
            }
    
    operatorType: 'OperatorType'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operatorType"]) -> 'OperatorType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normalization"]) -> 'OperatorNormalization': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dbt"]) -> 'OperatorDbt': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhook"]) -> 'OperatorWebhook': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["operatorType", "normalization", "dbt", "webhook", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["operatorType"]) -> 'OperatorType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normalization"]) -> typing.Union['OperatorNormalization', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dbt"]) -> typing.Union['OperatorDbt', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhook"]) -> typing.Union['OperatorWebhook', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["operatorType", "normalization", "dbt", "webhook", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        operatorType: 'OperatorType',
        normalization: typing.Union['OperatorNormalization', schemas.Unset] = schemas.unset,
        dbt: typing.Union['OperatorDbt', schemas.Unset] = schemas.unset,
        webhook: typing.Union['OperatorWebhook', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OperatorConfiguration':
        return super().__new__(
            cls,
            *_args,
            operatorType=operatorType,
            normalization=normalization,
            dbt=dbt,
            webhook=webhook,
            _configuration=_configuration,
            **kwargs,
        )

from airbyte_config_api_client.model.operator_dbt import OperatorDbt
from airbyte_config_api_client.model.operator_normalization import OperatorNormalization
from airbyte_config_api_client.model.operator_type import OperatorType
from airbyte_config_api_client.model.operator_webhook import OperatorWebhook
