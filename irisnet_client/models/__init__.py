# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from irisnet_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from irisnet_client.model.api_notice import ApiNotice
from irisnet_client.model.base_attribute import BaseAttribute
from irisnet_client.model.base_detection import BaseDetection
from irisnet_client.model.breast_detection import BreastDetection
from irisnet_client.model.broken_rule import BrokenRule
from irisnet_client.model.callback import Callback
from irisnet_client.model.check_result import CheckResult
from irisnet_client.model.config import Config
from irisnet_client.model.coordinates import Coordinates
from irisnet_client.model.encoded import Encoded
from irisnet_client.model.event import Event
from irisnet_client.model.face_detection import FaceDetection
from irisnet_client.model.hair_attribute import HairAttribute
from irisnet_client.model.hair_detection import HairDetection
from irisnet_client.model.license_info import LicenseInfo
from irisnet_client.model.param import Param
from irisnet_client.model.param_set import ParamSet
from irisnet_client.model.pricing import Pricing
from irisnet_client.model.rectangle import Rectangle
from irisnet_client.model.summary import Summary
