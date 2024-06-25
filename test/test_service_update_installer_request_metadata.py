# coding: utf-8

"""
    Nuon

    API for managing nuon apps, components, and installs.

    The version of the OpenAPI document: 0.19.176
    Contact: support@nuon.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from nuon.models.service_update_installer_request_metadata import ServiceUpdateInstallerRequestMetadata

class TestServiceUpdateInstallerRequestMetadata(unittest.TestCase):
    """ServiceUpdateInstallerRequestMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceUpdateInstallerRequestMetadata:
        """Test ServiceUpdateInstallerRequestMetadata
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceUpdateInstallerRequestMetadata`
        """
        model = ServiceUpdateInstallerRequestMetadata()
        if include_optional:
            return ServiceUpdateInstallerRequestMetadata(
                community_url = '',
                copyright_markdown = '',
                demo_url = '',
                description = '',
                documentation_url = '',
                favicon_url = '',
                footer_markdown = '',
                github_url = '',
                homepage_url = '',
                logo_url = '',
                post_install_markdown = ''
            )
        else:
            return ServiceUpdateInstallerRequestMetadata(
                community_url = '',
                description = '',
                documentation_url = '',
                github_url = '',
                homepage_url = '',
                logo_url = '',
        )
        """

    def testServiceUpdateInstallerRequestMetadata(self):
        """Test ServiceUpdateInstallerRequestMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
