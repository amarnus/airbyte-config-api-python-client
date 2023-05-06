# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from airbyte_config_api_client.paths.v1_source_oauths_complete_oauth import Api

from airbyte_config_api_client.paths import PathValues

path = PathValues.V1_SOURCE_OAUTHS_COMPLETE_OAUTH