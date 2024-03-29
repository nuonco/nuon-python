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

from nuon.models.service_create_app_sandbox_config_request import ServiceCreateAppSandboxConfigRequest

class TestServiceCreateAppSandboxConfigRequest(unittest.TestCase):
    """ServiceCreateAppSandboxConfigRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceCreateAppSandboxConfigRequest:
        """Test ServiceCreateAppSandboxConfigRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceCreateAppSandboxConfigRequest`
        """
        model = ServiceCreateAppSandboxConfigRequest()
        if include_optional:
            return ServiceCreateAppSandboxConfigRequest(
                connected_github_vcs_config = nuon.models.service/connected_github_vcs_sandbox_config_request.service.ConnectedGithubVCSSandboxConfigRequest(
                    branch = '', 
                    directory = '', 
                    git_ref = '', 
                    repo = '', ),
                public_git_vcs_config = nuon.models.service/public_git_vcs_sandbox_config_request.service.PublicGitVCSSandboxConfigRequest(
                    branch = '', 
                    directory = '', 
                    repo = '', ),
                sandbox_inputs = {
                    'key' : ''
                    },
                sandbox_release_id = '',
                terraform_version = ''
            )
        else:
            return ServiceCreateAppSandboxConfigRequest(
                sandbox_inputs = {
                    'key' : ''
                    },
                terraform_version = '',
        )
        """

    def testServiceCreateAppSandboxConfigRequest(self):
        """Test ServiceCreateAppSandboxConfigRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
