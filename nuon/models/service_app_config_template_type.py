# coding: utf-8

"""
    Nuon

    API for managing nuon apps, components, and installs.

    The version of the OpenAPI document: 0.19.208
    Contact: support@nuon.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ServiceAppConfigTemplateType(str, Enum):
    """
    ServiceAppConfigTemplateType
    """

    """
    allowed enum values
    """
    AWS_MINUS_ECS = 'aws-ecs'
    AWS_MINUS_ECS_MINUS_BYOVPC = 'aws-ecs-byovpc'
    AWS_MINUS_EKS = 'aws-eks'
    AWS_MINUS_EKS_MINUS_BYOVPC = 'aws-eks-byovpc'
    AZURE_MINUS_AKS = 'azure-aks'
    FLAT = 'flat'
    TOP_MINUS_LEVEL = 'top-level'
    INSTALLER = 'installer'
    RUNNER = 'runner'
    SANDBOX = 'sandbox'
    INPUTS = 'inputs'
    TERRAFORM = 'terraform'
    TERRAFORMINFRA = 'terraformInfra'
    HELM = 'helm'
    DOCKER_MINUS_BUILD = 'docker-build'
    JOB = 'job'
    CONTAINER_MINUS_IMAGE = 'container-image'
    ECR_MINUS_CONTAINER_MINUS_IMAGE = 'ecr-container-image'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ServiceAppConfigTemplateType from a JSON string"""
        return cls(json.loads(json_str))


