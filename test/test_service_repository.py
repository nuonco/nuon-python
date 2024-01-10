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

from openapi_client.models.service_repository import ServiceRepository

class TestServiceRepository(unittest.TestCase):
    """ServiceRepository unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceRepository:
        """Test ServiceRepository
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceRepository`
        """
        model = ServiceRepository()
        if include_optional:
            return ServiceRepository(
                clone_url = '',
                default_branch = '',
                full_name = '',
                git_url = '',
                github_install_id = '',
                name = '',
                user_name = ''
            )
        else:
            return ServiceRepository(
                clone_url = '',
                default_branch = '',
                full_name = '',
                git_url = '',
                github_install_id = '',
                name = '',
                user_name = '',
        )
        """

    def testServiceRepository(self):
        """Test ServiceRepository"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
