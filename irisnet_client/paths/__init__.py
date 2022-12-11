# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from irisnet_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V2_CONFIG_PARAMETERS_CONFIG_ID = "/v2/config/parameters/{configId}"
    V2_CONFIG_ = "/v2/config/"
    V2_CHECKVIDEO_CONFIG_ID = "/v2/check-video/{configId}"
    V2_CHECKSTREAM_CONFIG_ID = "/v2/check-stream/{configId}"
    V2_CHECKIMAGE_CONFIG_ID = "/v2/check-image/{configId}"
    V2_INFO_ = "/v2/info/"
    V2_COST_CONFIG_ID_FRAMES = "/v2/cost/{configId}/{frames}"
    V2_COST_CONFIG_ID_FPS_DURATION = "/v2/cost/{configId}/{fps}/{duration}"
    V2_COST_CONFIG_ID = "/v2/cost/{configId}"
    V2_CONFIG_CONFIG_ID = "/v2/config/{configId}"
