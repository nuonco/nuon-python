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

from nuon.models.app_sandbox import AppSandbox

class TestAppSandbox(unittest.TestCase):
    """AppSandbox unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppSandbox:
        """Test AppSandbox
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppSandbox`
        """
        model = AppSandbox()
        if include_optional:
            return AppSandbox(
                created_at = '',
                created_by_id = '',
                description = '',
                id = '',
                name = '',
                releases = [
                    nuon.models.app/sandbox_release.app.SandboxRelease(
                        created_at = '', 
                        created_by_id = '', 
                        deprovision_policy_url = '', 
                        id = '', 
                        one_click_role_template_url = '', 
                        provision_policy_url = '', 
                        trust_policy_url = '', 
                        updated_at = '', 
                        version = '', )
                    ],
                updated_at = ''
            )
        else:
            return AppSandbox(
        )
        """

    def testAppSandbox(self):
        """Test AppSandbox"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
