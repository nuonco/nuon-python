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

from nuon.models.service_aws_ecr_image_config_request import ServiceAwsECRImageConfigRequest

class TestServiceAwsECRImageConfigRequest(unittest.TestCase):
    """ServiceAwsECRImageConfigRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceAwsECRImageConfigRequest:
        """Test ServiceAwsECRImageConfigRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceAwsECRImageConfigRequest`
        """
        model = ServiceAwsECRImageConfigRequest()
        if include_optional:
            return ServiceAwsECRImageConfigRequest(
                aws_region = '',
                iam_role_arn = ''
            )
        else:
            return ServiceAwsECRImageConfigRequest(
        )
        """

    def testServiceAwsECRImageConfigRequest(self):
        """Test ServiceAwsECRImageConfigRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
