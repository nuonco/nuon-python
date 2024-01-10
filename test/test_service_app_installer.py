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

from nuon.models.service_app_installer import ServiceAppInstaller

class TestServiceAppInstaller(unittest.TestCase):
    """ServiceAppInstaller unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceAppInstaller:
        """Test ServiceAppInstaller
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceAppInstaller`
        """
        model = ServiceAppInstaller()
        if include_optional:
            return ServiceAppInstaller(
                app = nuon.models.app/app.app.App(
                    created_at = '', 
                    created_by_id = '', 
                    id = '', 
                    name = '', 
                    org_id = '', 
                    status = '', 
                    status_description = '', 
                    updated_at = '', ),
                metadata = nuon.models.app/app_installer_metadata.app.AppInstallerMetadata(
                    app_installer_id = '', 
                    community_url = '', 
                    created_at = '', 
                    created_by_id = '', 
                    demo_url = '', 
                    description = '', 
                    documentation_url = '', 
                    github_url = '', 
                    homepage_url = '', 
                    id = '', 
                    logo_url = '', 
                    name = '', 
                    updated_at = '', ),
                sandbox_mode = True
            )
        else:
            return ServiceAppInstaller(
        )
        """

    def testServiceAppInstaller(self):
        """Test ServiceAppInstaller"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()