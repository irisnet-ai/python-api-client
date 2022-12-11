import typing_extensions

from irisnet_client.apis.tags import TagValues
from irisnet_client.apis.tags.configuration_management_api import ConfigurationManagementApi
from irisnet_client.apis.tags.detailed_configuration_parameters_api import DetailedConfigurationParametersApi
from irisnet_client.apis.tags.ai_check_operations_api import AICheckOperationsApi
from irisnet_client.apis.tags.balance_endpoints_api import BalanceEndpointsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.CONFIGURATION_MANAGEMENT: ConfigurationManagementApi,
        TagValues.DETAILED_CONFIGURATION_PARAMETERS: DetailedConfigurationParametersApi,
        TagValues.AI_CHECK_OPERATIONS: AICheckOperationsApi,
        TagValues.BALANCE_ENDPOINTS: BalanceEndpointsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.CONFIGURATION_MANAGEMENT: ConfigurationManagementApi,
        TagValues.DETAILED_CONFIGURATION_PARAMETERS: DetailedConfigurationParametersApi,
        TagValues.AI_CHECK_OPERATIONS: AICheckOperationsApi,
        TagValues.BALANCE_ENDPOINTS: BalanceEndpointsApi,
    }
)
