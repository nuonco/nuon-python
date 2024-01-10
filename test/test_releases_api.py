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

from openapi_client.api.releases_api import ReleasesApi


class TestReleasesApi(unittest.TestCase):
    """ReleasesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ReleasesApi()

    def tearDown(self) -> None:
        pass

    def test_create_component_release(self) -> None:
        """Test case for create_component_release

        create a release
        """
        pass

    def test_get_app_releases(self) -> None:
        """Test case for get_app_releases

        get all releases for an app
        """
        pass

    def test_get_component_releases(self) -> None:
        """Test case for get_component_releases

        get all releases for a component
        """
        pass

    def test_get_release(self) -> None:
        """Test case for get_release

        get a release
        """
        pass

    def test_get_release_steps(self) -> None:
        """Test case for get_release_steps

        get a release
        """
        pass


if __name__ == '__main__':
    unittest.main()
