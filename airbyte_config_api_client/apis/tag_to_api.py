import typing_extensions

from airbyte_config_api_client.apis.tags import TagValues
from airbyte_config_api_client.apis.tags.workspace_api import WorkspaceApi
from airbyte_config_api_client.apis.tags.source_definition_api import SourceDefinitionApi
from airbyte_config_api_client.apis.tags.source_definition_specification_api import SourceDefinitionSpecificationApi
from airbyte_config_api_client.apis.tags.source_api import SourceApi
from airbyte_config_api_client.apis.tags.destination_definition_api import DestinationDefinitionApi
from airbyte_config_api_client.apis.tags.destination_definition_specification_api import DestinationDefinitionSpecificationApi
from airbyte_config_api_client.apis.tags.destination_api import DestinationApi
from airbyte_config_api_client.apis.tags.connection_api import ConnectionApi
from airbyte_config_api_client.apis.tags.destination_oauth_api import DestinationOauthApi
from airbyte_config_api_client.apis.tags.source_oauth_api import SourceOauthApi
from airbyte_config_api_client.apis.tags.web_backend_api import WebBackendApi
from airbyte_config_api_client.apis.tags.health_api import HealthApi
from airbyte_config_api_client.apis.tags.deployment_api import DeploymentApi
from airbyte_config_api_client.apis.tags.attempt_api import AttemptApi
from airbyte_config_api_client.apis.tags.state_api import StateApi
from airbyte_config_api_client.apis.tags.internal_api import InternalApi
from airbyte_config_api_client.apis.tags.jobs_api import JobsApi
from airbyte_config_api_client.apis.tags.logs_api import LogsApi
from airbyte_config_api_client.apis.tags.notifications_api import NotificationsApi
from airbyte_config_api_client.apis.tags.openapi_api import OpenapiApi
from airbyte_config_api_client.apis.tags.operation_api import OperationApi
from airbyte_config_api_client.apis.tags.scheduler_api import SchedulerApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.WORKSPACE: WorkspaceApi,
        TagValues.SOURCE_DEFINITION: SourceDefinitionApi,
        TagValues.SOURCE_DEFINITION_SPECIFICATION: SourceDefinitionSpecificationApi,
        TagValues.SOURCE: SourceApi,
        TagValues.DESTINATION_DEFINITION: DestinationDefinitionApi,
        TagValues.DESTINATION_DEFINITION_SPECIFICATION: DestinationDefinitionSpecificationApi,
        TagValues.DESTINATION: DestinationApi,
        TagValues.CONNECTION: ConnectionApi,
        TagValues.DESTINATION_OAUTH: DestinationOauthApi,
        TagValues.SOURCE_OAUTH: SourceOauthApi,
        TagValues.WEB_BACKEND: WebBackendApi,
        TagValues.HEALTH: HealthApi,
        TagValues.DEPLOYMENT: DeploymentApi,
        TagValues.ATTEMPT: AttemptApi,
        TagValues.STATE: StateApi,
        TagValues.INTERNAL: InternalApi,
        TagValues.JOBS: JobsApi,
        TagValues.LOGS: LogsApi,
        TagValues.NOTIFICATIONS: NotificationsApi,
        TagValues.OPENAPI: OpenapiApi,
        TagValues.OPERATION: OperationApi,
        TagValues.SCHEDULER: SchedulerApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.WORKSPACE: WorkspaceApi,
        TagValues.SOURCE_DEFINITION: SourceDefinitionApi,
        TagValues.SOURCE_DEFINITION_SPECIFICATION: SourceDefinitionSpecificationApi,
        TagValues.SOURCE: SourceApi,
        TagValues.DESTINATION_DEFINITION: DestinationDefinitionApi,
        TagValues.DESTINATION_DEFINITION_SPECIFICATION: DestinationDefinitionSpecificationApi,
        TagValues.DESTINATION: DestinationApi,
        TagValues.CONNECTION: ConnectionApi,
        TagValues.DESTINATION_OAUTH: DestinationOauthApi,
        TagValues.SOURCE_OAUTH: SourceOauthApi,
        TagValues.WEB_BACKEND: WebBackendApi,
        TagValues.HEALTH: HealthApi,
        TagValues.DEPLOYMENT: DeploymentApi,
        TagValues.ATTEMPT: AttemptApi,
        TagValues.STATE: StateApi,
        TagValues.INTERNAL: InternalApi,
        TagValues.JOBS: JobsApi,
        TagValues.LOGS: LogsApi,
        TagValues.NOTIFICATIONS: NotificationsApi,
        TagValues.OPENAPI: OpenapiApi,
        TagValues.OPERATION: OperationApi,
        TagValues.SCHEDULER: SchedulerApi,
    }
)
