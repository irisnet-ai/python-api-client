# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import irisnet_client
from irisnet_client.paths.v2_check_video_config_id import post  # noqa: E501
from irisnet_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV2CheckVideoConfigId(ApiTestMixin, unittest.TestCase):
    """
    V2CheckVideoConfigId unit test stubs
        Check a video with the AI.  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 202
    response_body = ''




if __name__ == '__main__':
    unittest.main()
