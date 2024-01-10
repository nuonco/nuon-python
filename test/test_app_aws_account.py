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

from nuon.models.app_aws_account import AppAWSAccount

class TestAppAWSAccount(unittest.TestCase):
    """AppAWSAccount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppAWSAccount:
        """Test AppAWSAccount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppAWSAccount`
        """
        model = AppAWSAccount()
        if include_optional:
            return AppAWSAccount(
                created_at = '',
                created_by_id = '',
                iam_role_arn = '',
                id = '',
                region = '',
                updated_at = ''
            )
        else:
            return AppAWSAccount(
        )
        """

    def testAppAWSAccount(self):
        """Test AppAWSAccount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
