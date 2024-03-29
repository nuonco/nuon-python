# coding: utf-8

"""
    Nuon

    API for managing nuon apps, components, and installs.

    The version of the OpenAPI document: 0.19.26
    Contact: support@nuon.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from nuon.models.app_org_health_check import AppOrgHealthCheck

class TestAppOrgHealthCheck(unittest.TestCase):
    """AppOrgHealthCheck unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppOrgHealthCheck:
        """Test AppOrgHealthCheck
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppOrgHealthCheck`
        """
        model = AppOrgHealthCheck()
        if include_optional:
            return AppOrgHealthCheck(
                created_at = '',
                created_by_id = '',
                id = '',
                org_id = '',
                status = 'ok',
                status_description = '',
                updated_at = ''
            )
        else:
            return AppOrgHealthCheck(
        )
        """

    def testAppOrgHealthCheck(self):
        """Test AppOrgHealthCheck"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
