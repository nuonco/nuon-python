# coding: utf-8

"""
    Nuon

    API for managing nuon apps, components, and installs.

    The version of the OpenAPI document: 0.19.15
    Contact: support@nuon.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.service_update_install_request import ServiceUpdateInstallRequest

class TestServiceUpdateInstallRequest(unittest.TestCase):
    """ServiceUpdateInstallRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceUpdateInstallRequest:
        """Test ServiceUpdateInstallRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceUpdateInstallRequest`
        """
        model = ServiceUpdateInstallRequest()
        if include_optional:
            return ServiceUpdateInstallRequest(
                name = ''
            )
        else:
            return ServiceUpdateInstallRequest(
        )
        """

    def testServiceUpdateInstallRequest(self):
        """Test ServiceUpdateInstallRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
