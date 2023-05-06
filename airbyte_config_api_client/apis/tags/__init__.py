# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from airbyte_config_api_client.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    WORKSPACE = "workspace"
    SOURCE_DEFINITION = "source_definition"
    SOURCE_DEFINITION_SPECIFICATION = "source_definition_specification"
    SOURCE = "source"
    DESTINATION_DEFINITION = "destination_definition"
    DESTINATION_DEFINITION_SPECIFICATION = "destination_definition_specification"
    DESTINATION = "destination"
    CONNECTION = "connection"
    DESTINATION_OAUTH = "destination_oauth"
    SOURCE_OAUTH = "source_oauth"
    WEB_BACKEND = "web_backend"
    HEALTH = "health"
    DEPLOYMENT = "deployment"
    ATTEMPT = "attempt"
    STATE = "state"
    INTERNAL = "internal"
    JOBS = "jobs"
    LOGS = "logs"
    NOTIFICATIONS = "notifications"
    OPENAPI = "openapi"
    OPERATION = "operation"
    SCHEDULER = "scheduler"
