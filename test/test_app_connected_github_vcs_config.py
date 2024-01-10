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

from nuon.models.app_connected_github_vcs_config import AppConnectedGithubVCSConfig

class TestAppConnectedGithubVCSConfig(unittest.TestCase):
    """AppConnectedGithubVCSConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppConnectedGithubVCSConfig:
        """Test AppConnectedGithubVCSConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppConnectedGithubVCSConfig`
        """
        model = AppConnectedGithubVCSConfig()
        if include_optional:
            return AppConnectedGithubVCSConfig(
                branch = '',
                component_config_id = '',
                component_config_type = '',
                created_at = '',
                created_by_id = '',
                directory = '',
                id = '',
                repo = '',
                repo_name = '',
                repo_owner = '',
                updated_at = '',
                vcs_connection = nuon.models.app/vcs_connection.app.VCSConnection(
                    created_at = '', 
                    created_by_id = '', 
                    github_install_id = '', 
                    id = '', 
                    updated_at = '', 
                    vcs_connection_commit = [
                        nuon.models.app/vcs_connection_commit.app.VCSConnectionCommit(
                            author_email = '', 
                            author_name = '', 
                            component_config_connection_id = '', 
                            created_at = '', 
                            created_by_id = '', 
                            id = '', 
                            message = '', 
                            sha = '', 
                            updated_at = '', )
                        ], ),
                vcs_connection_id = ''
            )
        else:
            return AppConnectedGithubVCSConfig(
        )
        """

    def testAppConnectedGithubVCSConfig(self):
        """Test AppConnectedGithubVCSConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
