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

from nuon.models.app_public_git_vcs_config import AppPublicGitVCSConfig

class TestAppPublicGitVCSConfig(unittest.TestCase):
    """AppPublicGitVCSConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppPublicGitVCSConfig:
        """Test AppPublicGitVCSConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppPublicGitVCSConfig`
        """
        model = AppPublicGitVCSConfig()
        if include_optional:
            return AppPublicGitVCSConfig(
                branch = '',
                component_config_id = '',
                component_config_type = '',
                created_at = '',
                created_by_id = '',
                directory = '',
                id = '',
                repo = '',
                updated_at = ''
            )
        else:
            return AppPublicGitVCSConfig(
        )
        """

    def testAppPublicGitVCSConfig(self):
        """Test AppPublicGitVCSConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
