# coding: utf-8

"""
    Nuon

    API for managing nuon apps, components, and installs.

    The version of the OpenAPI document: 0.19.35
    Contact: support@nuon.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from nuon.models.service_update_installer_request_links import ServiceUpdateInstallerRequestLinks

class TestServiceUpdateInstallerRequestLinks(unittest.TestCase):
    """ServiceUpdateInstallerRequestLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceUpdateInstallerRequestLinks:
        """Test ServiceUpdateInstallerRequestLinks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceUpdateInstallerRequestLinks`
        """
        model = ServiceUpdateInstallerRequestLinks()
        if include_optional:
            return ServiceUpdateInstallerRequestLinks(
                community = '',
                demo = '',
                documentation = '',
                github = '',
                homepage = '',
                logo = ''
            )
        else:
            return ServiceUpdateInstallerRequestLinks(
                community = '',
                demo = '',
                documentation = '',
                github = '',
                homepage = '',
                logo = '',
        )
        """

    def testServiceUpdateInstallerRequestLinks(self):
        """Test ServiceUpdateInstallerRequestLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
