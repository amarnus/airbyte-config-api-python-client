# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from airbyte_config_api_client.paths.v1_sources_most_recent_source_actor_catalog import Api

from airbyte_config_api_client.paths import PathValues

path = PathValues.V1_SOURCES_MOST_RECENT_SOURCE_ACTOR_CATALOG