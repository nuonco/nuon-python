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

from nuon.models.service_public_git_vcs_sandbox_config_request import ServicePublicGitVCSSandboxConfigRequest

class TestServicePublicGitVCSSandboxConfigRequest(unittest.TestCase):
    """ServicePublicGitVCSSandboxConfigRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServicePublicGitVCSSandboxConfigRequest:
        """Test ServicePublicGitVCSSandboxConfigRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServicePublicGitVCSSandboxConfigRequest`
        """
        model = ServicePublicGitVCSSandboxConfigRequest()
        if include_optional:
            return ServicePublicGitVCSSandboxConfigRequest(
                branch = '',
                directory = '',
                repo = ''
            )
        else:
            return ServicePublicGitVCSSandboxConfigRequest(
                branch = '',
                directory = '',
                repo = '',
        )
        """

    def testServicePublicGitVCSSandboxConfigRequest(self):
        """Test ServicePublicGitVCSSandboxConfigRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
