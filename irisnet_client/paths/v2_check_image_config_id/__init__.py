# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from irisnet_client.paths.v2_check_image_config_id import Api

from irisnet_client.paths import PathValues

path = PathValues.V2_CHECKIMAGE_CONFIG_ID