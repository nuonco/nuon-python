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

from openapi_client.models.app_install_inputs import AppInstallInputs

class TestAppInstallInputs(unittest.TestCase):
    """AppInstallInputs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppInstallInputs:
        """Test AppInstallInputs
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppInstallInputs`
        """
        model = AppInstallInputs()
        if include_optional:
            return AppInstallInputs(
                created_at = '',
                created_by_id = '',
                id = '',
                install_id = '',
                org_id = '',
                updated_at = '',
                values = {
                    'key' : ''
                    }
            )
        else:
            return AppInstallInputs(
        )
        """

    def testAppInstallInputs(self):
        """Test AppInstallInputs"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
