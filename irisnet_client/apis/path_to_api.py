import typing_extensions

from irisnet_client.paths import PathValues
from irisnet_client.apis.paths.v2_config_parameters_config_id import V2ConfigParametersConfigId
from irisnet_client.apis.paths.v2_config_ import V2Config
from irisnet_client.apis.paths.v2_check_video_config_id import V2CheckVideoConfigId
from irisnet_client.apis.paths.v2_check_stream_config_id import V2CheckStreamConfigId
from irisnet_client.apis.paths.v2_check_image_config_id import V2CheckImageConfigId
from irisnet_client.apis.paths.v2_info_ import V2Info
from irisnet_client.apis.paths.v2_cost_config_id_frames import V2CostConfigIdFrames
from irisnet_client.apis.paths.v2_cost_config_id_fps_duration import V2CostConfigIdFpsDuration
from irisnet_client.apis.paths.v2_cost_config_id import V2CostConfigId
from irisnet_client.apis.paths.v2_config_config_id import V2ConfigConfigId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V2_CONFIG_PARAMETERS_CONFIG_ID: V2ConfigParametersConfigId,
        PathValues.V2_CONFIG_: V2Config,
        PathValues.V2_CHECKVIDEO_CONFIG_ID: V2CheckVideoConfigId,
        PathValues.V2_CHECKSTREAM_CONFIG_ID: V2CheckStreamConfigId,
        PathValues.V2_CHECKIMAGE_CONFIG_ID: V2CheckImageConfigId,
        PathValues.V2_INFO_: V2Info,
        PathValues.V2_COST_CONFIG_ID_FRAMES: V2CostConfigIdFrames,
        PathValues.V2_COST_CONFIG_ID_FPS_DURATION: V2CostConfigIdFpsDuration,
        PathValues.V2_COST_CONFIG_ID: V2CostConfigId,
        PathValues.V2_CONFIG_CONFIG_ID: V2ConfigConfigId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V2_CONFIG_PARAMETERS_CONFIG_ID: V2ConfigParametersConfigId,
        PathValues.V2_CONFIG_: V2Config,
        PathValues.V2_CHECKVIDEO_CONFIG_ID: V2CheckVideoConfigId,
        PathValues.V2_CHECKSTREAM_CONFIG_ID: V2CheckStreamConfigId,
        PathValues.V2_CHECKIMAGE_CONFIG_ID: V2CheckImageConfigId,
        PathValues.V2_INFO_: V2Info,
        PathValues.V2_COST_CONFIG_ID_FRAMES: V2CostConfigIdFrames,
        PathValues.V2_COST_CONFIG_ID_FPS_DURATION: V2CostConfigIdFpsDuration,
        PathValues.V2_COST_CONFIG_ID: V2CostConfigId,
        PathValues.V2_CONFIG_CONFIG_ID: V2ConfigConfigId,
    }
)
