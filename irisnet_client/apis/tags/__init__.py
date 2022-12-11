# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from irisnet_client.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    CONFIGURATION_MANAGEMENT = "Configuration Management"
    DETAILED_CONFIGURATION_PARAMETERS = "Detailed configuration parameters"
    AI_CHECK_OPERATIONS = "AI check operations"
    BALANCE_ENDPOINTS = "Balance endpoints"
