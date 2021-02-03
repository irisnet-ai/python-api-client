# coding: utf-8

"""
    Irisnet API

    Artificial Intelligence (AI) for image- and video-processing in realtime. This is an interactive documentation meant to give a place were you can quickly look up the endpoints and their schemas, while also giving you the option to try things out yourself.  Listed below you'll see the available endpoints of the API that can be expanded by clicking on it. Each expanded endpoint lists the request parameter (if available) and the request body (if available). The request body can list some example bodies and the schema, explaining each model in detail. Additionally you'll find a 'Try it out' button where you can type in your custom parameters and custom body and execute that against the API. The responses section in the expanded endpoint lists the possible responses with their corresponding status codes. If you've executed an API call it will also show you the response from the server.  Underneath the endpoints you'll find the model schemas. These are the models used for the requests and responses.By clicking on the right arrow you can expand the model and it will show you a description of the model and the model parameters. For nested models you can keep clicking the right arrow to reveal further details on it.    # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import irisnet_client
from irisnet_client.models.iris_net import IrisNet  # noqa: E501
from irisnet_client.rest import ApiException

class TestIrisNet(unittest.TestCase):
    """IrisNet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IrisNet
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = irisnet_client.models.iris_net.IrisNet()  # noqa: E501
        if include_optional :
            return IrisNet(
                rules_broken = 0, 
                help_suggested = 0, 
                getn_classes = 8, 
                getn_objects = 1, 
                in_rule = [
                    irisnet_client.models.in_rule.INRule(
                        in_class = 'face', 
                        found = 1, 
                        min = 1, 
                        max = 1, )
                    ], 
                in_object = [
                    irisnet_client.models.in_object.INObject(
                        in_class = 'face', 
                        x0 = 0.1, 
                        y0 = 0.1, 
                        width = 0.1, 
                        height = 0.1, 
                        probability = 94, )
                    ]
            )
        else :
            return IrisNet(
        )

    def testIrisNet(self):
        """Test IrisNet"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
