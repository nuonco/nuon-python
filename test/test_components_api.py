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

from nuon.api.components_api import ComponentsApi


class TestComponentsApi(unittest.TestCase):
    """ComponentsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ComponentsApi()

    def tearDown(self) -> None:
        pass

    def test_create_component(self) -> None:
        """Test case for create_component

        create a component
        """
        pass

    def test_create_component_build(self) -> None:
        """Test case for create_component_build

        create component build
        """
        pass

    def test_create_docker_build_component_config(self) -> None:
        """Test case for create_docker_build_component_config

        create a docker build component config
        """
        pass

    def test_create_external_image_component_config(self) -> None:
        """Test case for create_external_image_component_config

        create an external image component config
        """
        pass

    def test_create_helm_component_config(self) -> None:
        """Test case for create_helm_component_config

        create a helm component config
        """
        pass

    def test_create_job_component_config(self) -> None:
        """Test case for create_job_component_config

        create a job component config
        """
        pass

    def test_create_terraform_module_component_config(self) -> None:
        """Test case for create_terraform_module_component_config

        create a terraform component config
        """
        pass

    def test_delete_component(self) -> None:
        """Test case for delete_component

        delete a component
        """
        pass

    def test_get_app_components(self) -> None:
        """Test case for get_app_components

        get all components for an app
        """
        pass

    def test_get_build(self) -> None:
        """Test case for get_build

        get a build
        """
        pass

    def test_get_component(self) -> None:
        """Test case for get_component

        get a component
        """
        pass

    def test_get_component_build(self) -> None:
        """Test case for get_component_build

        get a build for a component
        """
        pass

    def test_get_component_build_logs(self) -> None:
        """Test case for get_component_build_logs

        get component build logs
        """
        pass

    def test_get_component_build_plan(self) -> None:
        """Test case for get_component_build_plan

        get component build plan
        """
        pass

    def test_get_component_builds(self) -> None:
        """Test case for get_component_builds

        get all builds for a component
        """
        pass

    def test_get_component_configs(self) -> None:
        """Test case for get_component_configs

        get all configs for a component
        """
        pass

    def test_get_component_latest_build(self) -> None:
        """Test case for get_component_latest_build

        get latest build for a component
        """
        pass

    def test_get_component_latest_config(self) -> None:
        """Test case for get_component_latest_config

        get latest config for a component
        """
        pass

    def test_get_org_components(self) -> None:
        """Test case for get_org_components

        get all components for an org
        """
        pass

    def test_update_component(self) -> None:
        """Test case for update_component

        update a component
        """
        pass


if __name__ == '__main__':
    unittest.main()
