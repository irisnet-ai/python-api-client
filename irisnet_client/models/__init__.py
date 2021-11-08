# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from irisnet_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from irisnet_client.model.in_default import INDefault
from irisnet_client.model.in_define_ai import INDefineAI
from irisnet_client.model.in_error import INError
from irisnet_client.model.in_image import INImage
from irisnet_client.model.in_object import INObject
from irisnet_client.model.in_param import INParam
from irisnet_client.model.in_params import INParams
from irisnet_client.model.in_rule import INRule
from irisnet_client.model.iris_net import IrisNet
from irisnet_client.model.license_info import LicenseInfo
