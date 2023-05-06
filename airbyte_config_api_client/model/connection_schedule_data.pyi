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


class ConnectionScheduleData(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    schedule for when the the connection should run, per the schedule type
    """


    class MetaOapg:
        
        class properties:
            
            
            class basicSchedule(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "units",
                        "timeUnit",
                    }
                    
                    class properties:
                        
                        
                        class timeUnit(
                            schemas.EnumBase,
                            schemas.StrSchema
                        ):
                            
                            @schemas.classproperty
                            def MINUTES(cls):
                                return cls("minutes")
                            
                            @schemas.classproperty
                            def HOURS(cls):
                                return cls("hours")
                            
                            @schemas.classproperty
                            def DAYS(cls):
                                return cls("days")
                            
                            @schemas.classproperty
                            def WEEKS(cls):
                                return cls("weeks")
                            
                            @schemas.classproperty
                            def MONTHS(cls):
                                return cls("months")
                        units = schemas.Int64Schema
                        __annotations__ = {
                            "timeUnit": timeUnit,
                            "units": units,
                        }
                
                units: MetaOapg.properties.units
                timeUnit: MetaOapg.properties.timeUnit
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["timeUnit"]) -> MetaOapg.properties.timeUnit: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["units"]) -> MetaOapg.properties.units: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["timeUnit", "units", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["timeUnit"]) -> MetaOapg.properties.timeUnit: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["units"]) -> MetaOapg.properties.units: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["timeUnit", "units", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    units: typing.Union[MetaOapg.properties.units, decimal.Decimal, int, ],
                    timeUnit: typing.Union[MetaOapg.properties.timeUnit, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'basicSchedule':
                    return super().__new__(
                        cls,
                        *_args,
                        units=units,
                        timeUnit=timeUnit,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class cron(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "cronExpression",
                        "cronTimeZone",
                    }
                    
                    class properties:
                        cronExpression = schemas.StrSchema
                        cronTimeZone = schemas.StrSchema
                        __annotations__ = {
                            "cronExpression": cronExpression,
                            "cronTimeZone": cronTimeZone,
                        }
                
                cronExpression: MetaOapg.properties.cronExpression
                cronTimeZone: MetaOapg.properties.cronTimeZone
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["cronExpression"]) -> MetaOapg.properties.cronExpression: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["cronTimeZone"]) -> MetaOapg.properties.cronTimeZone: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["cronExpression", "cronTimeZone", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["cronExpression"]) -> MetaOapg.properties.cronExpression: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["cronTimeZone"]) -> MetaOapg.properties.cronTimeZone: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cronExpression", "cronTimeZone", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    cronExpression: typing.Union[MetaOapg.properties.cronExpression, str, ],
                    cronTimeZone: typing.Union[MetaOapg.properties.cronTimeZone, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'cron':
                    return super().__new__(
                        cls,
                        *_args,
                        cronExpression=cronExpression,
                        cronTimeZone=cronTimeZone,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "basicSchedule": basicSchedule,
                "cron": cron,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["basicSchedule"]) -> MetaOapg.properties.basicSchedule: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cron"]) -> MetaOapg.properties.cron: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["basicSchedule", "cron", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["basicSchedule"]) -> typing.Union[MetaOapg.properties.basicSchedule, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cron"]) -> typing.Union[MetaOapg.properties.cron, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["basicSchedule", "cron", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        basicSchedule: typing.Union[MetaOapg.properties.basicSchedule, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        cron: typing.Union[MetaOapg.properties.cron, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ConnectionScheduleData':
        return super().__new__(
            cls,
            *_args,
            basicSchedule=basicSchedule,
            cron=cron,
            _configuration=_configuration,
            **kwargs,
        )
