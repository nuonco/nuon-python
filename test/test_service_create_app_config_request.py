# coding: utf-8

"""
    Nuon

    API for managing nuon apps, components, and installs.

    The version of the OpenAPI document: 0.19.76
    Contact: support@nuon.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from nuon.models.service_create_app_config_request import ServiceCreateAppConfigRequest

class TestServiceCreateAppConfigRequest(unittest.TestCase):
    """ServiceCreateAppConfigRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceCreateAppConfigRequest:
        """Test ServiceCreateAppConfigRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceCreateAppConfigRequest`
        """
        model = ServiceCreateAppConfigRequest()
        if include_optional:
            return ServiceCreateAppConfigRequest(
                content = '0',
                format = 'json'
            )
        else:
            return ServiceCreateAppConfigRequest(
                content = '0',
                format = 'json',
        )
        """

    def testServiceCreateAppConfigRequest(self):
        """Test ServiceCreateAppConfigRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
