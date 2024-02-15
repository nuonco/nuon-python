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

from nuon.models.service_update_installer_request import ServiceUpdateInstallerRequest

class TestServiceUpdateInstallerRequest(unittest.TestCase):
    """ServiceUpdateInstallerRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceUpdateInstallerRequest:
        """Test ServiceUpdateInstallerRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceUpdateInstallerRequest`
        """
        model = ServiceUpdateInstallerRequest()
        if include_optional:
            return ServiceUpdateInstallerRequest(
                description = '',
                links = nuon.models.service_update_installer_request_links.service_UpdateInstallerRequest_links(
                    community = '', 
                    demo = '', 
                    documentation = '', 
                    github = '', 
                    homepage = '', 
                    logo = '', ),
                name = '',
                post_install_markdown = ''
            )
        else:
            return ServiceUpdateInstallerRequest(
                description = '',
                name = '',
        )
        """

    def testServiceUpdateInstallerRequest(self):
        """Test ServiceUpdateInstallerRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
