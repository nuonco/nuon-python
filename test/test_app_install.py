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

from openapi_client.models.app_install import AppInstall

class TestAppInstall(unittest.TestCase):
    """AppInstall unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppInstall:
        """Test AppInstall
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppInstall`
        """
        model = AppInstall()
        if include_optional:
            return AppInstall(
                app_id = '',
                app_runner_config = openapi_client.models.app/app_runner_config.app.AppRunnerConfig(
                    app_id = '', 
                    app_runner_type = 'aws-ecs', 
                    created_at = '', 
                    created_by_id = '', 
                    env_vars = {
                        'key' : ''
                        }, 
                    id = '', 
                    org_id = '', 
                    updated_at = '', ),
                app_sandbox_config = openapi_client.models.app/app_sandbox_config.app.AppSandboxConfig(
                    app_id = '', 
                    connected_github_vcs_config = openapi_client.models.app/connected_github_vcs_config.app.ConnectedGithubVCSConfig(
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
                        vcs_connection = openapi_client.models.app/vcs_connection.app.VCSConnection(
                            created_at = '', 
                            created_by_id = '', 
                            github_install_id = '', 
                            id = '', 
                            updated_at = '', 
                            vcs_connection_commit = [
                                openapi_client.models.app/vcs_connection_commit.app.VCSConnectionCommit(
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
                        vcs_connection_id = '', ), 
                    created_at = '', 
                    created_by_id = '', 
                    id = '', 
                    org_id = '', 
                    public_git_vcs_config = openapi_client.models.app/public_git_vcs_config.app.PublicGitVCSConfig(
                        branch = '', 
                        component_config_id = '', 
                        component_config_type = '', 
                        created_at = '', 
                        created_by_id = '', 
                        directory = '', 
                        id = '', 
                        repo = '', 
                        updated_at = '', ), 
                    sandbox_release = openapi_client.models.app/sandbox_release.app.SandboxRelease(
                        created_at = '', 
                        created_by_id = '', 
                        deprovision_policy_url = '', 
                        id = '', 
                        one_click_role_template_url = '', 
                        provision_policy_url = '', 
                        trust_policy_url = '', 
                        updated_at = '', 
                        version = '', ), 
                    sandbox_release_id = '', 
                    terraform_version = '', 
                    updated_at = '', 
                    variables = {
                        'key' : ''
                        }, ),
                aws_account = openapi_client.models.app/aws_account.app.AWSAccount(
                    created_at = '', 
                    created_by_id = '', 
                    iam_role_arn = '', 
                    id = '', 
                    region = '', 
                    updated_at = '', ),
                created_at = '',
                created_by_id = '',
                id = '',
                install_components = [
                    openapi_client.models.app/install_component.app.InstallComponent(
                        component = openapi_client.models.app/component.app.Component(
                            app_id = '', 
                            config_versions = 56, 
                            created_at = '', 
                            created_by_id = '', 
                            dependencies = [
                                ''
                                ], 
                            id = '', 
                            name = '', 
                            status = '', 
                            status_description = '', 
                            updated_at = '', ), 
                        component_id = '', 
                        created_at = '', 
                        created_by_id = '', 
                        id = '', 
                        install_deploys = [
                            openapi_client.models.app/install_deploy.app.InstallDeploy(
                                build_id = '', 
                                component_id = '', 
                                component_name = '', 
                                created_at = '', 
                                created_by_id = '', 
                                id = '', 
                                install_component_id = '', 
                                install_deploy_type = 'release', 
                                install_id = '', 
                                release_id = '', 
                                status = '', 
                                status_description = '', 
                                updated_at = '', )
                            ], 
                        install_id = '', 
                        updated_at = '', )
                    ],
                install_inputs = [
                    openapi_client.models.app/install_inputs.app.InstallInputs(
                        created_at = '', 
                        created_by_id = '', 
                        id = '', 
                        install_id = '', 
                        org_id = '', 
                        updated_at = '', 
                        values = {
                            'key' : ''
                            }, )
                    ],
                install_sandbox_runs = [
                    openapi_client.models.app/install_sandbox_run.app.InstallSandboxRun(
                        app_sandbox_config = openapi_client.models.app/app_sandbox_config.app.AppSandboxConfig(
                            app_id = '', 
                            connected_github_vcs_config = openapi_client.models.app/connected_github_vcs_config.app.ConnectedGithubVCSConfig(
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
                                vcs_connection = openapi_client.models.app/vcs_connection.app.VCSConnection(
                                    created_at = '', 
                                    created_by_id = '', 
                                    github_install_id = '', 
                                    id = '', 
                                    updated_at = '', 
                                    vcs_connection_commit = [
                                        openapi_client.models.app/vcs_connection_commit.app.VCSConnectionCommit(
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
                                vcs_connection_id = '', ), 
                            created_at = '', 
                            created_by_id = '', 
                            id = '', 
                            org_id = '', 
                            public_git_vcs_config = openapi_client.models.app/public_git_vcs_config.app.PublicGitVCSConfig(
                                branch = '', 
                                component_config_id = '', 
                                component_config_type = '', 
                                created_at = '', 
                                created_by_id = '', 
                                directory = '', 
                                id = '', 
                                repo = '', 
                                updated_at = '', ), 
                            sandbox_release = openapi_client.models.app/sandbox_release.app.SandboxRelease(
                                created_at = '', 
                                created_by_id = '', 
                                deprovision_policy_url = '', 
                                id = '', 
                                one_click_role_template_url = '', 
                                provision_policy_url = '', 
                                trust_policy_url = '', 
                                updated_at = '', 
                                version = '', ), 
                            sandbox_release_id = '', 
                            terraform_version = '', 
                            updated_at = '', 
                            variables = {
                                'key' : ''
                                }, ), 
                        created_at = '', 
                        created_by_id = '', 
                        id = '', 
                        install_id = '', 
                        run_type = 'provision', 
                        status = '', 
                        status_description = '', 
                        updated_at = '', )
                    ],
                name = '',
                status = '',
                status_description = '',
                updated_at = ''
            )
        else:
            return AppInstall(
        )
        """

    def testAppInstall(self):
        """Test AppInstall"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
