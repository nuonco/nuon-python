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

from nuon.models.app_app_runner_config import AppAppRunnerConfig

class TestAppAppRunnerConfig(unittest.TestCase):
    """AppAppRunnerConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppAppRunnerConfig:
        """Test AppAppRunnerConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppAppRunnerConfig`
        """
        model = AppAppRunnerConfig()
        if include_optional:
            return AppAppRunnerConfig(
                app_id = '',
                app_runner_type = 'aws-ecs',
                created_at = '',
                created_by_id = '',
                env_vars = {
                    'key' : ''
                    },
                id = '',
                org_id = '',
                updated_at = ''
            )
        else:
            return AppAppRunnerConfig(
        )
        """

    def testAppAppRunnerConfig(self):
        """Test AppAppRunnerConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
