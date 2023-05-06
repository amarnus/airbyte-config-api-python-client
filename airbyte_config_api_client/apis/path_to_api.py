import typing_extensions

from airbyte_config_api_client.paths import PathValues
from airbyte_config_api_client.apis.paths.v1_workspaces_create import V1WorkspacesCreate
from airbyte_config_api_client.apis.paths.v1_workspaces_delete import V1WorkspacesDelete
from airbyte_config_api_client.apis.paths.v1_workspaces_list import V1WorkspacesList
from airbyte_config_api_client.apis.paths.v1_workspaces_get import V1WorkspacesGet
from airbyte_config_api_client.apis.paths.v1_workspaces_get_by_slug import V1WorkspacesGetBySlug
from airbyte_config_api_client.apis.paths.v1_workspaces_get_by_connection_id import V1WorkspacesGetByConnectionId
from airbyte_config_api_client.apis.paths.v1_workspaces_update import V1WorkspacesUpdate
from airbyte_config_api_client.apis.paths.v1_workspaces_update_name import V1WorkspacesUpdateName
from airbyte_config_api_client.apis.paths.v1_workspaces_tag_feedback_status_as_done import V1WorkspacesTagFeedbackStatusAsDone
from airbyte_config_api_client.apis.paths.v1_notifications_try import V1NotificationsTry
from airbyte_config_api_client.apis.paths.v1_source_definitions_update import V1SourceDefinitionsUpdate
from airbyte_config_api_client.apis.paths.v1_source_definitions_list import V1SourceDefinitionsList
from airbyte_config_api_client.apis.paths.v1_source_definitions_list_latest import V1SourceDefinitionsListLatest
from airbyte_config_api_client.apis.paths.v1_source_definitions_get import V1SourceDefinitionsGet
from airbyte_config_api_client.apis.paths.v1_source_definitions_delete import V1SourceDefinitionsDelete
from airbyte_config_api_client.apis.paths.v1_source_definitions_list_private import V1SourceDefinitionsListPrivate
from airbyte_config_api_client.apis.paths.v1_source_definitions_list_for_workspace import V1SourceDefinitionsListForWorkspace
from airbyte_config_api_client.apis.paths.v1_source_definitions_create_custom import V1SourceDefinitionsCreateCustom
from airbyte_config_api_client.apis.paths.v1_source_definitions_get_for_workspace import V1SourceDefinitionsGetForWorkspace
from airbyte_config_api_client.apis.paths.v1_source_definitions_grant_definition import V1SourceDefinitionsGrantDefinition
from airbyte_config_api_client.apis.paths.v1_source_definitions_revoke_definition import V1SourceDefinitionsRevokeDefinition
from airbyte_config_api_client.apis.paths.v1_source_definition_specifications_get import V1SourceDefinitionSpecificationsGet
from airbyte_config_api_client.apis.paths.v1_sources_create import V1SourcesCreate
from airbyte_config_api_client.apis.paths.v1_sources_update import V1SourcesUpdate
from airbyte_config_api_client.apis.paths.v1_sources_list import V1SourcesList
from airbyte_config_api_client.apis.paths.v1_sources_get import V1SourcesGet
from airbyte_config_api_client.apis.paths.v1_sources_most_recent_source_actor_catalog import V1SourcesMostRecentSourceActorCatalog
from airbyte_config_api_client.apis.paths.v1_sources_search import V1SourcesSearch
from airbyte_config_api_client.apis.paths.v1_sources_clone import V1SourcesClone
from airbyte_config_api_client.apis.paths.v1_sources_delete import V1SourcesDelete
from airbyte_config_api_client.apis.paths.v1_sources_check_connection import V1SourcesCheckConnection
from airbyte_config_api_client.apis.paths.v1_sources_check_connection_for_update import V1SourcesCheckConnectionForUpdate
from airbyte_config_api_client.apis.paths.v1_sources_discover_schema import V1SourcesDiscoverSchema
from airbyte_config_api_client.apis.paths.v1_sources_write_discover_catalog_result import V1SourcesWriteDiscoverCatalogResult
from airbyte_config_api_client.apis.paths.v1_destination_definitions_update import V1DestinationDefinitionsUpdate
from airbyte_config_api_client.apis.paths.v1_destination_definitions_list import V1DestinationDefinitionsList
from airbyte_config_api_client.apis.paths.v1_destination_definitions_list_latest import V1DestinationDefinitionsListLatest
from airbyte_config_api_client.apis.paths.v1_destination_definitions_get import V1DestinationDefinitionsGet
from airbyte_config_api_client.apis.paths.v1_destination_definitions_delete import V1DestinationDefinitionsDelete
from airbyte_config_api_client.apis.paths.v1_destination_definitions_list_private import V1DestinationDefinitionsListPrivate
from airbyte_config_api_client.apis.paths.v1_destination_definitions_list_for_workspace import V1DestinationDefinitionsListForWorkspace
from airbyte_config_api_client.apis.paths.v1_destination_definitions_create_custom import V1DestinationDefinitionsCreateCustom
from airbyte_config_api_client.apis.paths.v1_destination_definitions_get_for_workspace import V1DestinationDefinitionsGetForWorkspace
from airbyte_config_api_client.apis.paths.v1_destination_definitions_grant_definition import V1DestinationDefinitionsGrantDefinition
from airbyte_config_api_client.apis.paths.v1_destination_definitions_revoke_definition import V1DestinationDefinitionsRevokeDefinition
from airbyte_config_api_client.apis.paths.v1_destination_definition_specifications_get import V1DestinationDefinitionSpecificationsGet
from airbyte_config_api_client.apis.paths.v1_destinations_create import V1DestinationsCreate
from airbyte_config_api_client.apis.paths.v1_destinations_update import V1DestinationsUpdate
from airbyte_config_api_client.apis.paths.v1_destinations_list import V1DestinationsList
from airbyte_config_api_client.apis.paths.v1_destinations_get import V1DestinationsGet
from airbyte_config_api_client.apis.paths.v1_destinations_search import V1DestinationsSearch
from airbyte_config_api_client.apis.paths.v1_destinations_check_connection import V1DestinationsCheckConnection
from airbyte_config_api_client.apis.paths.v1_destinations_check_connection_for_update import V1DestinationsCheckConnectionForUpdate
from airbyte_config_api_client.apis.paths.v1_destinations_delete import V1DestinationsDelete
from airbyte_config_api_client.apis.paths.v1_destinations_clone import V1DestinationsClone
from airbyte_config_api_client.apis.paths.v1_connections_create import V1ConnectionsCreate
from airbyte_config_api_client.apis.paths.v1_connections_update import V1ConnectionsUpdate
from airbyte_config_api_client.apis.paths.v1_connections_list import V1ConnectionsList
from airbyte_config_api_client.apis.paths.v1_connections_list_all import V1ConnectionsListAll
from airbyte_config_api_client.apis.paths.v1_connections_get import V1ConnectionsGet
from airbyte_config_api_client.apis.paths.v1_state_get import V1StateGet
from airbyte_config_api_client.apis.paths.v1_state_create_or_update import V1StateCreateOrUpdate
from airbyte_config_api_client.apis.paths.v1_connections_search import V1ConnectionsSearch
from airbyte_config_api_client.apis.paths.v1_connections_delete import V1ConnectionsDelete
from airbyte_config_api_client.apis.paths.v1_connections_sync import V1ConnectionsSync
from airbyte_config_api_client.apis.paths.v1_connections_reset import V1ConnectionsReset
from airbyte_config_api_client.apis.paths.v1_operations_check import V1OperationsCheck
from airbyte_config_api_client.apis.paths.v1_operations_create import V1OperationsCreate
from airbyte_config_api_client.apis.paths.v1_operations_update import V1OperationsUpdate
from airbyte_config_api_client.apis.paths.v1_operations_list import V1OperationsList
from airbyte_config_api_client.apis.paths.v1_operations_get import V1OperationsGet
from airbyte_config_api_client.apis.paths.v1_operations_delete import V1OperationsDelete
from airbyte_config_api_client.apis.paths.v1_scheduler_sources_check_connection import V1SchedulerSourcesCheckConnection
from airbyte_config_api_client.apis.paths.v1_scheduler_sources_discover_schema import V1SchedulerSourcesDiscoverSchema
from airbyte_config_api_client.apis.paths.v1_scheduler_destinations_check_connection import V1SchedulerDestinationsCheckConnection
from airbyte_config_api_client.apis.paths.v1_source_oauths_oauth_params_create import V1SourceOauthsOauthParamsCreate
from airbyte_config_api_client.apis.paths.v1_source_oauths_get_consent_url import V1SourceOauthsGetConsentUrl
from airbyte_config_api_client.apis.paths.v1_source_oauths_complete_oauth import V1SourceOauthsCompleteOauth
from airbyte_config_api_client.apis.paths.v1_destination_oauths_get_consent_url import V1DestinationOauthsGetConsentUrl
from airbyte_config_api_client.apis.paths.v1_destination_oauths_complete_oauth import V1DestinationOauthsCompleteOauth
from airbyte_config_api_client.apis.paths.v1_destination_oauths_oauth_params_create import V1DestinationOauthsOauthParamsCreate
from airbyte_config_api_client.apis.paths.v1_web_backend_check_updates import V1WebBackendCheckUpdates
from airbyte_config_api_client.apis.paths.v1_web_backend_connections_list import V1WebBackendConnectionsList
from airbyte_config_api_client.apis.paths.v1_web_backend_connections_get import V1WebBackendConnectionsGet
from airbyte_config_api_client.apis.paths.v1_web_backend_connections_create import V1WebBackendConnectionsCreate
from airbyte_config_api_client.apis.paths.v1_web_backend_connections_update import V1WebBackendConnectionsUpdate
from airbyte_config_api_client.apis.paths.v1_web_backend_state_get_type import V1WebBackendStateGetType
from airbyte_config_api_client.apis.paths.v1_web_backend_workspace_state import V1WebBackendWorkspaceState
from airbyte_config_api_client.apis.paths.v1_web_backend_geographies_list import V1WebBackendGeographiesList
from airbyte_config_api_client.apis.paths.v1_jobs_list import V1JobsList
from airbyte_config_api_client.apis.paths.v1_jobs_get import V1JobsGet
from airbyte_config_api_client.apis.paths.v1_jobs_get_last_replication_job import V1JobsGetLastReplicationJob
from airbyte_config_api_client.apis.paths.v1_jobs_get_light import V1JobsGetLight
from airbyte_config_api_client.apis.paths.v1_jobs_cancel import V1JobsCancel
from airbyte_config_api_client.apis.paths.v1_jobs_get_debug_info import V1JobsGetDebugInfo
from airbyte_config_api_client.apis.paths.v1_jobs_get_normalization_status import V1JobsGetNormalizationStatus
from airbyte_config_api_client.apis.paths.v1_health import V1Health
from airbyte_config_api_client.apis.paths.v1_logs_get import V1LogsGet
from airbyte_config_api_client.apis.paths.v1_openapi import V1Openapi
from airbyte_config_api_client.apis.paths.v1_attempt_set_workflow_in_attempt import V1AttemptSetWorkflowInAttempt
from airbyte_config_api_client.apis.paths.v1_attempt_save_stats import V1AttemptSaveStats
from airbyte_config_api_client.apis.paths.v1_attempt_save_sync_config import V1AttemptSaveSyncConfig

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_WORKSPACES_CREATE: V1WorkspacesCreate,
        PathValues.V1_WORKSPACES_DELETE: V1WorkspacesDelete,
        PathValues.V1_WORKSPACES_LIST: V1WorkspacesList,
        PathValues.V1_WORKSPACES_GET: V1WorkspacesGet,
        PathValues.V1_WORKSPACES_GET_BY_SLUG: V1WorkspacesGetBySlug,
        PathValues.V1_WORKSPACES_GET_BY_CONNECTION_ID: V1WorkspacesGetByConnectionId,
        PathValues.V1_WORKSPACES_UPDATE: V1WorkspacesUpdate,
        PathValues.V1_WORKSPACES_UPDATE_NAME: V1WorkspacesUpdateName,
        PathValues.V1_WORKSPACES_TAG_FEEDBACK_STATUS_AS_DONE: V1WorkspacesTagFeedbackStatusAsDone,
        PathValues.V1_NOTIFICATIONS_TRY: V1NotificationsTry,
        PathValues.V1_SOURCE_DEFINITIONS_UPDATE: V1SourceDefinitionsUpdate,
        PathValues.V1_SOURCE_DEFINITIONS_LIST: V1SourceDefinitionsList,
        PathValues.V1_SOURCE_DEFINITIONS_LIST_LATEST: V1SourceDefinitionsListLatest,
        PathValues.V1_SOURCE_DEFINITIONS_GET: V1SourceDefinitionsGet,
        PathValues.V1_SOURCE_DEFINITIONS_DELETE: V1SourceDefinitionsDelete,
        PathValues.V1_SOURCE_DEFINITIONS_LIST_PRIVATE: V1SourceDefinitionsListPrivate,
        PathValues.V1_SOURCE_DEFINITIONS_LIST_FOR_WORKSPACE: V1SourceDefinitionsListForWorkspace,
        PathValues.V1_SOURCE_DEFINITIONS_CREATE_CUSTOM: V1SourceDefinitionsCreateCustom,
        PathValues.V1_SOURCE_DEFINITIONS_GET_FOR_WORKSPACE: V1SourceDefinitionsGetForWorkspace,
        PathValues.V1_SOURCE_DEFINITIONS_GRANT_DEFINITION: V1SourceDefinitionsGrantDefinition,
        PathValues.V1_SOURCE_DEFINITIONS_REVOKE_DEFINITION: V1SourceDefinitionsRevokeDefinition,
        PathValues.V1_SOURCE_DEFINITION_SPECIFICATIONS_GET: V1SourceDefinitionSpecificationsGet,
        PathValues.V1_SOURCES_CREATE: V1SourcesCreate,
        PathValues.V1_SOURCES_UPDATE: V1SourcesUpdate,
        PathValues.V1_SOURCES_LIST: V1SourcesList,
        PathValues.V1_SOURCES_GET: V1SourcesGet,
        PathValues.V1_SOURCES_MOST_RECENT_SOURCE_ACTOR_CATALOG: V1SourcesMostRecentSourceActorCatalog,
        PathValues.V1_SOURCES_SEARCH: V1SourcesSearch,
        PathValues.V1_SOURCES_CLONE: V1SourcesClone,
        PathValues.V1_SOURCES_DELETE: V1SourcesDelete,
        PathValues.V1_SOURCES_CHECK_CONNECTION: V1SourcesCheckConnection,
        PathValues.V1_SOURCES_CHECK_CONNECTION_FOR_UPDATE: V1SourcesCheckConnectionForUpdate,
        PathValues.V1_SOURCES_DISCOVER_SCHEMA: V1SourcesDiscoverSchema,
        PathValues.V1_SOURCES_WRITE_DISCOVER_CATALOG_RESULT: V1SourcesWriteDiscoverCatalogResult,
        PathValues.V1_DESTINATION_DEFINITIONS_UPDATE: V1DestinationDefinitionsUpdate,
        PathValues.V1_DESTINATION_DEFINITIONS_LIST: V1DestinationDefinitionsList,
        PathValues.V1_DESTINATION_DEFINITIONS_LIST_LATEST: V1DestinationDefinitionsListLatest,
        PathValues.V1_DESTINATION_DEFINITIONS_GET: V1DestinationDefinitionsGet,
        PathValues.V1_DESTINATION_DEFINITIONS_DELETE: V1DestinationDefinitionsDelete,
        PathValues.V1_DESTINATION_DEFINITIONS_LIST_PRIVATE: V1DestinationDefinitionsListPrivate,
        PathValues.V1_DESTINATION_DEFINITIONS_LIST_FOR_WORKSPACE: V1DestinationDefinitionsListForWorkspace,
        PathValues.V1_DESTINATION_DEFINITIONS_CREATE_CUSTOM: V1DestinationDefinitionsCreateCustom,
        PathValues.V1_DESTINATION_DEFINITIONS_GET_FOR_WORKSPACE: V1DestinationDefinitionsGetForWorkspace,
        PathValues.V1_DESTINATION_DEFINITIONS_GRANT_DEFINITION: V1DestinationDefinitionsGrantDefinition,
        PathValues.V1_DESTINATION_DEFINITIONS_REVOKE_DEFINITION: V1DestinationDefinitionsRevokeDefinition,
        PathValues.V1_DESTINATION_DEFINITION_SPECIFICATIONS_GET: V1DestinationDefinitionSpecificationsGet,
        PathValues.V1_DESTINATIONS_CREATE: V1DestinationsCreate,
        PathValues.V1_DESTINATIONS_UPDATE: V1DestinationsUpdate,
        PathValues.V1_DESTINATIONS_LIST: V1DestinationsList,
        PathValues.V1_DESTINATIONS_GET: V1DestinationsGet,
        PathValues.V1_DESTINATIONS_SEARCH: V1DestinationsSearch,
        PathValues.V1_DESTINATIONS_CHECK_CONNECTION: V1DestinationsCheckConnection,
        PathValues.V1_DESTINATIONS_CHECK_CONNECTION_FOR_UPDATE: V1DestinationsCheckConnectionForUpdate,
        PathValues.V1_DESTINATIONS_DELETE: V1DestinationsDelete,
        PathValues.V1_DESTINATIONS_CLONE: V1DestinationsClone,
        PathValues.V1_CONNECTIONS_CREATE: V1ConnectionsCreate,
        PathValues.V1_CONNECTIONS_UPDATE: V1ConnectionsUpdate,
        PathValues.V1_CONNECTIONS_LIST: V1ConnectionsList,
        PathValues.V1_CONNECTIONS_LIST_ALL: V1ConnectionsListAll,
        PathValues.V1_CONNECTIONS_GET: V1ConnectionsGet,
        PathValues.V1_STATE_GET: V1StateGet,
        PathValues.V1_STATE_CREATE_OR_UPDATE: V1StateCreateOrUpdate,
        PathValues.V1_CONNECTIONS_SEARCH: V1ConnectionsSearch,
        PathValues.V1_CONNECTIONS_DELETE: V1ConnectionsDelete,
        PathValues.V1_CONNECTIONS_SYNC: V1ConnectionsSync,
        PathValues.V1_CONNECTIONS_RESET: V1ConnectionsReset,
        PathValues.V1_OPERATIONS_CHECK: V1OperationsCheck,
        PathValues.V1_OPERATIONS_CREATE: V1OperationsCreate,
        PathValues.V1_OPERATIONS_UPDATE: V1OperationsUpdate,
        PathValues.V1_OPERATIONS_LIST: V1OperationsList,
        PathValues.V1_OPERATIONS_GET: V1OperationsGet,
        PathValues.V1_OPERATIONS_DELETE: V1OperationsDelete,
        PathValues.V1_SCHEDULER_SOURCES_CHECK_CONNECTION: V1SchedulerSourcesCheckConnection,
        PathValues.V1_SCHEDULER_SOURCES_DISCOVER_SCHEMA: V1SchedulerSourcesDiscoverSchema,
        PathValues.V1_SCHEDULER_DESTINATIONS_CHECK_CONNECTION: V1SchedulerDestinationsCheckConnection,
        PathValues.V1_SOURCE_OAUTHS_OAUTH_PARAMS_CREATE: V1SourceOauthsOauthParamsCreate,
        PathValues.V1_SOURCE_OAUTHS_GET_CONSENT_URL: V1SourceOauthsGetConsentUrl,
        PathValues.V1_SOURCE_OAUTHS_COMPLETE_OAUTH: V1SourceOauthsCompleteOauth,
        PathValues.V1_DESTINATION_OAUTHS_GET_CONSENT_URL: V1DestinationOauthsGetConsentUrl,
        PathValues.V1_DESTINATION_OAUTHS_COMPLETE_OAUTH: V1DestinationOauthsCompleteOauth,
        PathValues.V1_DESTINATION_OAUTHS_OAUTH_PARAMS_CREATE: V1DestinationOauthsOauthParamsCreate,
        PathValues.V1_WEB_BACKEND_CHECK_UPDATES: V1WebBackendCheckUpdates,
        PathValues.V1_WEB_BACKEND_CONNECTIONS_LIST: V1WebBackendConnectionsList,
        PathValues.V1_WEB_BACKEND_CONNECTIONS_GET: V1WebBackendConnectionsGet,
        PathValues.V1_WEB_BACKEND_CONNECTIONS_CREATE: V1WebBackendConnectionsCreate,
        PathValues.V1_WEB_BACKEND_CONNECTIONS_UPDATE: V1WebBackendConnectionsUpdate,
        PathValues.V1_WEB_BACKEND_STATE_GET_TYPE: V1WebBackendStateGetType,
        PathValues.V1_WEB_BACKEND_WORKSPACE_STATE: V1WebBackendWorkspaceState,
        PathValues.V1_WEB_BACKEND_GEOGRAPHIES_LIST: V1WebBackendGeographiesList,
        PathValues.V1_JOBS_LIST: V1JobsList,
        PathValues.V1_JOBS_GET: V1JobsGet,
        PathValues.V1_JOBS_GET_LAST_REPLICATION_JOB: V1JobsGetLastReplicationJob,
        PathValues.V1_JOBS_GET_LIGHT: V1JobsGetLight,
        PathValues.V1_JOBS_CANCEL: V1JobsCancel,
        PathValues.V1_JOBS_GET_DEBUG_INFO: V1JobsGetDebugInfo,
        PathValues.V1_JOBS_GET_NORMALIZATION_STATUS: V1JobsGetNormalizationStatus,
        PathValues.V1_HEALTH: V1Health,
        PathValues.V1_LOGS_GET: V1LogsGet,
        PathValues.V1_OPENAPI: V1Openapi,
        PathValues.V1_ATTEMPT_SET_WORKFLOW_IN_ATTEMPT: V1AttemptSetWorkflowInAttempt,
        PathValues.V1_ATTEMPT_SAVE_STATS: V1AttemptSaveStats,
        PathValues.V1_ATTEMPT_SAVE_SYNC_CONFIG: V1AttemptSaveSyncConfig,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_WORKSPACES_CREATE: V1WorkspacesCreate,
        PathValues.V1_WORKSPACES_DELETE: V1WorkspacesDelete,
        PathValues.V1_WORKSPACES_LIST: V1WorkspacesList,
        PathValues.V1_WORKSPACES_GET: V1WorkspacesGet,
        PathValues.V1_WORKSPACES_GET_BY_SLUG: V1WorkspacesGetBySlug,
        PathValues.V1_WORKSPACES_GET_BY_CONNECTION_ID: V1WorkspacesGetByConnectionId,
        PathValues.V1_WORKSPACES_UPDATE: V1WorkspacesUpdate,
        PathValues.V1_WORKSPACES_UPDATE_NAME: V1WorkspacesUpdateName,
        PathValues.V1_WORKSPACES_TAG_FEEDBACK_STATUS_AS_DONE: V1WorkspacesTagFeedbackStatusAsDone,
        PathValues.V1_NOTIFICATIONS_TRY: V1NotificationsTry,
        PathValues.V1_SOURCE_DEFINITIONS_UPDATE: V1SourceDefinitionsUpdate,
        PathValues.V1_SOURCE_DEFINITIONS_LIST: V1SourceDefinitionsList,
        PathValues.V1_SOURCE_DEFINITIONS_LIST_LATEST: V1SourceDefinitionsListLatest,
        PathValues.V1_SOURCE_DEFINITIONS_GET: V1SourceDefinitionsGet,
        PathValues.V1_SOURCE_DEFINITIONS_DELETE: V1SourceDefinitionsDelete,
        PathValues.V1_SOURCE_DEFINITIONS_LIST_PRIVATE: V1SourceDefinitionsListPrivate,
        PathValues.V1_SOURCE_DEFINITIONS_LIST_FOR_WORKSPACE: V1SourceDefinitionsListForWorkspace,
        PathValues.V1_SOURCE_DEFINITIONS_CREATE_CUSTOM: V1SourceDefinitionsCreateCustom,
        PathValues.V1_SOURCE_DEFINITIONS_GET_FOR_WORKSPACE: V1SourceDefinitionsGetForWorkspace,
        PathValues.V1_SOURCE_DEFINITIONS_GRANT_DEFINITION: V1SourceDefinitionsGrantDefinition,
        PathValues.V1_SOURCE_DEFINITIONS_REVOKE_DEFINITION: V1SourceDefinitionsRevokeDefinition,
        PathValues.V1_SOURCE_DEFINITION_SPECIFICATIONS_GET: V1SourceDefinitionSpecificationsGet,
        PathValues.V1_SOURCES_CREATE: V1SourcesCreate,
        PathValues.V1_SOURCES_UPDATE: V1SourcesUpdate,
        PathValues.V1_SOURCES_LIST: V1SourcesList,
        PathValues.V1_SOURCES_GET: V1SourcesGet,
        PathValues.V1_SOURCES_MOST_RECENT_SOURCE_ACTOR_CATALOG: V1SourcesMostRecentSourceActorCatalog,
        PathValues.V1_SOURCES_SEARCH: V1SourcesSearch,
        PathValues.V1_SOURCES_CLONE: V1SourcesClone,
        PathValues.V1_SOURCES_DELETE: V1SourcesDelete,
        PathValues.V1_SOURCES_CHECK_CONNECTION: V1SourcesCheckConnection,
        PathValues.V1_SOURCES_CHECK_CONNECTION_FOR_UPDATE: V1SourcesCheckConnectionForUpdate,
        PathValues.V1_SOURCES_DISCOVER_SCHEMA: V1SourcesDiscoverSchema,
        PathValues.V1_SOURCES_WRITE_DISCOVER_CATALOG_RESULT: V1SourcesWriteDiscoverCatalogResult,
        PathValues.V1_DESTINATION_DEFINITIONS_UPDATE: V1DestinationDefinitionsUpdate,
        PathValues.V1_DESTINATION_DEFINITIONS_LIST: V1DestinationDefinitionsList,
        PathValues.V1_DESTINATION_DEFINITIONS_LIST_LATEST: V1DestinationDefinitionsListLatest,
        PathValues.V1_DESTINATION_DEFINITIONS_GET: V1DestinationDefinitionsGet,
        PathValues.V1_DESTINATION_DEFINITIONS_DELETE: V1DestinationDefinitionsDelete,
        PathValues.V1_DESTINATION_DEFINITIONS_LIST_PRIVATE: V1DestinationDefinitionsListPrivate,
        PathValues.V1_DESTINATION_DEFINITIONS_LIST_FOR_WORKSPACE: V1DestinationDefinitionsListForWorkspace,
        PathValues.V1_DESTINATION_DEFINITIONS_CREATE_CUSTOM: V1DestinationDefinitionsCreateCustom,
        PathValues.V1_DESTINATION_DEFINITIONS_GET_FOR_WORKSPACE: V1DestinationDefinitionsGetForWorkspace,
        PathValues.V1_DESTINATION_DEFINITIONS_GRANT_DEFINITION: V1DestinationDefinitionsGrantDefinition,
        PathValues.V1_DESTINATION_DEFINITIONS_REVOKE_DEFINITION: V1DestinationDefinitionsRevokeDefinition,
        PathValues.V1_DESTINATION_DEFINITION_SPECIFICATIONS_GET: V1DestinationDefinitionSpecificationsGet,
        PathValues.V1_DESTINATIONS_CREATE: V1DestinationsCreate,
        PathValues.V1_DESTINATIONS_UPDATE: V1DestinationsUpdate,
        PathValues.V1_DESTINATIONS_LIST: V1DestinationsList,
        PathValues.V1_DESTINATIONS_GET: V1DestinationsGet,
        PathValues.V1_DESTINATIONS_SEARCH: V1DestinationsSearch,
        PathValues.V1_DESTINATIONS_CHECK_CONNECTION: V1DestinationsCheckConnection,
        PathValues.V1_DESTINATIONS_CHECK_CONNECTION_FOR_UPDATE: V1DestinationsCheckConnectionForUpdate,
        PathValues.V1_DESTINATIONS_DELETE: V1DestinationsDelete,
        PathValues.V1_DESTINATIONS_CLONE: V1DestinationsClone,
        PathValues.V1_CONNECTIONS_CREATE: V1ConnectionsCreate,
        PathValues.V1_CONNECTIONS_UPDATE: V1ConnectionsUpdate,
        PathValues.V1_CONNECTIONS_LIST: V1ConnectionsList,
        PathValues.V1_CONNECTIONS_LIST_ALL: V1ConnectionsListAll,
        PathValues.V1_CONNECTIONS_GET: V1ConnectionsGet,
        PathValues.V1_STATE_GET: V1StateGet,
        PathValues.V1_STATE_CREATE_OR_UPDATE: V1StateCreateOrUpdate,
        PathValues.V1_CONNECTIONS_SEARCH: V1ConnectionsSearch,
        PathValues.V1_CONNECTIONS_DELETE: V1ConnectionsDelete,
        PathValues.V1_CONNECTIONS_SYNC: V1ConnectionsSync,
        PathValues.V1_CONNECTIONS_RESET: V1ConnectionsReset,
        PathValues.V1_OPERATIONS_CHECK: V1OperationsCheck,
        PathValues.V1_OPERATIONS_CREATE: V1OperationsCreate,
        PathValues.V1_OPERATIONS_UPDATE: V1OperationsUpdate,
        PathValues.V1_OPERATIONS_LIST: V1OperationsList,
        PathValues.V1_OPERATIONS_GET: V1OperationsGet,
        PathValues.V1_OPERATIONS_DELETE: V1OperationsDelete,
        PathValues.V1_SCHEDULER_SOURCES_CHECK_CONNECTION: V1SchedulerSourcesCheckConnection,
        PathValues.V1_SCHEDULER_SOURCES_DISCOVER_SCHEMA: V1SchedulerSourcesDiscoverSchema,
        PathValues.V1_SCHEDULER_DESTINATIONS_CHECK_CONNECTION: V1SchedulerDestinationsCheckConnection,
        PathValues.V1_SOURCE_OAUTHS_OAUTH_PARAMS_CREATE: V1SourceOauthsOauthParamsCreate,
        PathValues.V1_SOURCE_OAUTHS_GET_CONSENT_URL: V1SourceOauthsGetConsentUrl,
        PathValues.V1_SOURCE_OAUTHS_COMPLETE_OAUTH: V1SourceOauthsCompleteOauth,
        PathValues.V1_DESTINATION_OAUTHS_GET_CONSENT_URL: V1DestinationOauthsGetConsentUrl,
        PathValues.V1_DESTINATION_OAUTHS_COMPLETE_OAUTH: V1DestinationOauthsCompleteOauth,
        PathValues.V1_DESTINATION_OAUTHS_OAUTH_PARAMS_CREATE: V1DestinationOauthsOauthParamsCreate,
        PathValues.V1_WEB_BACKEND_CHECK_UPDATES: V1WebBackendCheckUpdates,
        PathValues.V1_WEB_BACKEND_CONNECTIONS_LIST: V1WebBackendConnectionsList,
        PathValues.V1_WEB_BACKEND_CONNECTIONS_GET: V1WebBackendConnectionsGet,
        PathValues.V1_WEB_BACKEND_CONNECTIONS_CREATE: V1WebBackendConnectionsCreate,
        PathValues.V1_WEB_BACKEND_CONNECTIONS_UPDATE: V1WebBackendConnectionsUpdate,
        PathValues.V1_WEB_BACKEND_STATE_GET_TYPE: V1WebBackendStateGetType,
        PathValues.V1_WEB_BACKEND_WORKSPACE_STATE: V1WebBackendWorkspaceState,
        PathValues.V1_WEB_BACKEND_GEOGRAPHIES_LIST: V1WebBackendGeographiesList,
        PathValues.V1_JOBS_LIST: V1JobsList,
        PathValues.V1_JOBS_GET: V1JobsGet,
        PathValues.V1_JOBS_GET_LAST_REPLICATION_JOB: V1JobsGetLastReplicationJob,
        PathValues.V1_JOBS_GET_LIGHT: V1JobsGetLight,
        PathValues.V1_JOBS_CANCEL: V1JobsCancel,
        PathValues.V1_JOBS_GET_DEBUG_INFO: V1JobsGetDebugInfo,
        PathValues.V1_JOBS_GET_NORMALIZATION_STATUS: V1JobsGetNormalizationStatus,
        PathValues.V1_HEALTH: V1Health,
        PathValues.V1_LOGS_GET: V1LogsGet,
        PathValues.V1_OPENAPI: V1Openapi,
        PathValues.V1_ATTEMPT_SET_WORKFLOW_IN_ATTEMPT: V1AttemptSetWorkflowInAttempt,
        PathValues.V1_ATTEMPT_SAVE_STATS: V1AttemptSaveStats,
        PathValues.V1_ATTEMPT_SAVE_SYNC_CONFIG: V1AttemptSaveSyncConfig,
    }
)
