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


class ConnectionState(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Contains the state for a connection. The stateType field identifies what type of state it is. Only the field corresponding to that type will be set, the rest will be null. If stateType=not_set, then none of the fields will be set.
    """


    class MetaOapg:
        required = {
            "stateType",
            "connectionId",
        }
        
        class properties:
        
            @staticmethod
            def stateType() -> typing.Type['ConnectionStateType']:
                return ConnectionStateType
            connectionId = schemas.UUIDSchema
            state = schemas.DictSchema
            
            
            class streamState(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['StreamState']:
                        return StreamState
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['StreamState'], typing.List['StreamState']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'streamState':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'StreamState':
                    return super().__getitem__(i)
        
            @staticmethod
            def globalState() -> typing.Type['GlobalState']:
                return GlobalState
            __annotations__ = {
                "stateType": stateType,
                "connectionId": connectionId,
                "state": state,
                "streamState": streamState,
                "globalState": globalState,
            }
    
    stateType: 'ConnectionStateType'
    connectionId: MetaOapg.properties.connectionId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stateType"]) -> 'ConnectionStateType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["connectionId"]) -> MetaOapg.properties.connectionId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["streamState"]) -> MetaOapg.properties.streamState: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["globalState"]) -> 'GlobalState': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["stateType", "connectionId", "state", "streamState", "globalState", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stateType"]) -> 'ConnectionStateType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["connectionId"]) -> MetaOapg.properties.connectionId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["streamState"]) -> typing.Union[MetaOapg.properties.streamState, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["globalState"]) -> typing.Union['GlobalState', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["stateType", "connectionId", "state", "streamState", "globalState", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        stateType: 'ConnectionStateType',
        connectionId: typing.Union[MetaOapg.properties.connectionId, str, uuid.UUID, ],
        state: typing.Union[MetaOapg.properties.state, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        streamState: typing.Union[MetaOapg.properties.streamState, list, tuple, schemas.Unset] = schemas.unset,
        globalState: typing.Union['GlobalState', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ConnectionState':
        return super().__new__(
            cls,
            *_args,
            stateType=stateType,
            connectionId=connectionId,
            state=state,
            streamState=streamState,
            globalState=globalState,
            _configuration=_configuration,
            **kwargs,
        )

from airbyte_config_api_client.model.connection_state_type import ConnectionStateType
from airbyte_config_api_client.model.global_state import GlobalState
from airbyte_config_api_client.model.stream_state import StreamState