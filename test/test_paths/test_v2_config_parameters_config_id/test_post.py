# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import irisnet_client
from irisnet_client.paths.v2_config_parameters_config_id import post  # noqa: E501
from irisnet_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV2ConfigParametersConfigId(ApiTestMixin, unittest.TestCase):
    """
    V2ConfigParametersConfigId unit test stubs
        Set parameters to the given AI configuration.  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 400






if __name__ == '__main__':
    unittest.main()
