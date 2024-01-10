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

from nuon.api.general_api import GeneralApi


class TestGeneralApi(unittest.TestCase):
    """GeneralApi unit test stubs"""

    def setUp(self) -> None:
        self.api = GeneralApi()

    def tearDown(self) -> None:
        pass

    def test_get_cli_config(self) -> None:
        """Test case for get_cli_config

        Get config for cli
        """
        pass

    def test_get_current_user(self) -> None:
        """Test case for get_current_user

        Get current user
        """
        pass

    def test_publish_metrics(self) -> None:
        """Test case for publish_metrics

        Publish a metric from different Nuon clients for telemetry purposes.
        """
        pass


if __name__ == '__main__':
    unittest.main()
