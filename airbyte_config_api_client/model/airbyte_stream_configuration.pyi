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


class AirbyteStreamConfiguration(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    the mutable part of the stream to configure the destination
    """


    class MetaOapg:
        required = {
            "syncMode",
            "destinationSyncMode",
        }
        
        class properties:
        
            @staticmethod
            def syncMode() -> typing.Type['SyncMode']:
                return SyncMode
        
            @staticmethod
            def destinationSyncMode() -> typing.Type['DestinationSyncMode']:
                return DestinationSyncMode
            
            
            class cursorField(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'cursorField':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class primaryKey(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            items = schemas.StrSchema
                    
                        def __new__(
                            cls,
                            _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                _arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, list, tuple, ]], typing.List[typing.Union[MetaOapg.items, list, tuple, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'primaryKey':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            aliasName = schemas.StrSchema
            selected = schemas.BoolSchema
            suggested = schemas.BoolSchema
            fieldSelectionEnabled = schemas.BoolSchema
            
            
            class selectedFields(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SelectedFieldInfo']:
                        return SelectedFieldInfo
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['SelectedFieldInfo'], typing.List['SelectedFieldInfo']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'selectedFields':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'SelectedFieldInfo':
                    return super().__getitem__(i)
            __annotations__ = {
                "syncMode": syncMode,
                "destinationSyncMode": destinationSyncMode,
                "cursorField": cursorField,
                "primaryKey": primaryKey,
                "aliasName": aliasName,
                "selected": selected,
                "suggested": suggested,
                "fieldSelectionEnabled": fieldSelectionEnabled,
                "selectedFields": selectedFields,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    syncMode: 'SyncMode'
    destinationSyncMode: 'DestinationSyncMode'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["syncMode"]) -> 'SyncMode': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["destinationSyncMode"]) -> 'DestinationSyncMode': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cursorField"]) -> MetaOapg.properties.cursorField: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["primaryKey"]) -> MetaOapg.properties.primaryKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["aliasName"]) -> MetaOapg.properties.aliasName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["selected"]) -> MetaOapg.properties.selected: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["suggested"]) -> MetaOapg.properties.suggested: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fieldSelectionEnabled"]) -> MetaOapg.properties.fieldSelectionEnabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["selectedFields"]) -> MetaOapg.properties.selectedFields: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["syncMode"], typing_extensions.Literal["destinationSyncMode"], typing_extensions.Literal["cursorField"], typing_extensions.Literal["primaryKey"], typing_extensions.Literal["aliasName"], typing_extensions.Literal["selected"], typing_extensions.Literal["suggested"], typing_extensions.Literal["fieldSelectionEnabled"], typing_extensions.Literal["selectedFields"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["syncMode"]) -> 'SyncMode': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["destinationSyncMode"]) -> 'DestinationSyncMode': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cursorField"]) -> typing.Union[MetaOapg.properties.cursorField, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["primaryKey"]) -> typing.Union[MetaOapg.properties.primaryKey, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["aliasName"]) -> typing.Union[MetaOapg.properties.aliasName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["selected"]) -> typing.Union[MetaOapg.properties.selected, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["suggested"]) -> typing.Union[MetaOapg.properties.suggested, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fieldSelectionEnabled"]) -> typing.Union[MetaOapg.properties.fieldSelectionEnabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["selectedFields"]) -> typing.Union[MetaOapg.properties.selectedFields, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["syncMode"], typing_extensions.Literal["destinationSyncMode"], typing_extensions.Literal["cursorField"], typing_extensions.Literal["primaryKey"], typing_extensions.Literal["aliasName"], typing_extensions.Literal["selected"], typing_extensions.Literal["suggested"], typing_extensions.Literal["fieldSelectionEnabled"], typing_extensions.Literal["selectedFields"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        syncMode: 'SyncMode',
        destinationSyncMode: 'DestinationSyncMode',
        cursorField: typing.Union[MetaOapg.properties.cursorField, list, tuple, schemas.Unset] = schemas.unset,
        primaryKey: typing.Union[MetaOapg.properties.primaryKey, list, tuple, schemas.Unset] = schemas.unset,
        aliasName: typing.Union[MetaOapg.properties.aliasName, str, schemas.Unset] = schemas.unset,
        selected: typing.Union[MetaOapg.properties.selected, bool, schemas.Unset] = schemas.unset,
        suggested: typing.Union[MetaOapg.properties.suggested, bool, schemas.Unset] = schemas.unset,
        fieldSelectionEnabled: typing.Union[MetaOapg.properties.fieldSelectionEnabled, bool, schemas.Unset] = schemas.unset,
        selectedFields: typing.Union[MetaOapg.properties.selectedFields, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'AirbyteStreamConfiguration':
        return super().__new__(
            cls,
            *_args,
            syncMode=syncMode,
            destinationSyncMode=destinationSyncMode,
            cursorField=cursorField,
            primaryKey=primaryKey,
            aliasName=aliasName,
            selected=selected,
            suggested=suggested,
            fieldSelectionEnabled=fieldSelectionEnabled,
            selectedFields=selectedFields,
            _configuration=_configuration,
        )

from airbyte_config_api_client.model.destination_sync_mode import DestinationSyncMode
from airbyte_config_api_client.model.selected_field_info import SelectedFieldInfo
from airbyte_config_api_client.model.sync_mode import SyncMode