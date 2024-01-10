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

from nuon.models.service_create_org_request import ServiceCreateOrgRequest

class TestServiceCreateOrgRequest(unittest.TestCase):
    """ServiceCreateOrgRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceCreateOrgRequest:
        """Test ServiceCreateOrgRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceCreateOrgRequest`
        """
        model = ServiceCreateOrgRequest()
        if include_optional:
            return ServiceCreateOrgRequest(
                name = '',
                use_custom_cert = True,
                use_sandbox_mode = True
            )
        else:
            return ServiceCreateOrgRequest(
                name = '',
        )
        """

    def testServiceCreateOrgRequest(self):
        """Test ServiceCreateOrgRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
