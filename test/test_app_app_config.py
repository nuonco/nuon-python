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

from nuon.models.app_app_config import AppAppConfig

class TestAppAppConfig(unittest.TestCase):
    """AppAppConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppAppConfig:
        """Test AppAppConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppAppConfig`
        """
        model = AppAppConfig()
        if include_optional:
            return AppAppConfig(
                app_id = '',
                content = '',
                created_at = '',
                created_by = nuon.models.app/user_token.app.UserToken(
                    created_at = '', 
                    created_by_id = '', 
                    email = '', 
                    expires_at = '', 
                    id = '', 
                    issued_at = '', 
                    issuer = '', 
                    subject = '', 
                    token_type = 'auth0', 
                    updated_at = '', ),
                created_by_id = '',
                format = 'json',
                generated_terraform = '',
                id = '',
                org_id = '',
                status = 'active',
                status_description = '',
                updated_at = ''
            )
        else:
            return AppAppConfig(
        )
        """

    def testAppAppConfig(self):
        """Test AppAppConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()