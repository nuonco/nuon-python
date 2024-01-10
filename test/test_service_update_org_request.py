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

from nuon.models.service_update_org_request import ServiceUpdateOrgRequest

class TestServiceUpdateOrgRequest(unittest.TestCase):
    """ServiceUpdateOrgRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceUpdateOrgRequest:
        """Test ServiceUpdateOrgRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceUpdateOrgRequest`
        """
        model = ServiceUpdateOrgRequest()
        if include_optional:
            return ServiceUpdateOrgRequest(
                name = ''
            )
        else:
            return ServiceUpdateOrgRequest(
                name = '',
        )
        """

    def testServiceUpdateOrgRequest(self):
        """Test ServiceUpdateOrgRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()