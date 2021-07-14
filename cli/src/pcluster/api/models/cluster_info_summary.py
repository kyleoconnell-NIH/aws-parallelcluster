# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance
# with the License. A copy of the License is located at http://aws.amazon.com/apache2.0/
# or in the "LICENSE.txt" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
# OR CONDITIONS OF ANY KIND, express or implied. See the License for the specific language governing permissions and
# limitations under the License.

# pylint: disable=R0801


import re

from pcluster.api import util
from pcluster.api.models.base_model_ import Model
from pcluster.api.models.cloud_formation_status import CloudFormationStatus
from pcluster.api.models.cluster_status import ClusterStatus


class ClusterInfoSummary(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(
        self,
        cluster_name=None,
        cloudformation_stack_status=None,
        cloudformation_stack_arn=None,
        region=None,
        version=None,
        cluster_status=None,
    ):
        """ClusterInfoSummary - a model defined in OpenAPI

        :param cluster_name: The cluster_name of this ClusterInfoSummary.
        :type cluster_name: str
        :param cloudformation_stack_status: The cloudformation_stack_status of this ClusterInfoSummary.
        :type cloudformation_stack_status: CloudFormationStatus
        :param cloudformation_stack_arn: The cloudformation_stack_arn of this ClusterInfoSummary.
        :type cloudformation_stack_arn: str
        :param region: The region of this ClusterInfoSummary.
        :type region: str
        :param version: The version of this ClusterInfoSummary.
        :type version: str
        :param cluster_status: The cluster_status of this ClusterInfoSummary.
        :type cluster_status: ClusterStatus
        """
        self.openapi_types = {
            "cluster_name": str,
            "cloudformation_stack_status": CloudFormationStatus,
            "cloudformation_stack_arn": str,
            "region": str,
            "version": str,
            "cluster_status": ClusterStatus,
        }

        self.attribute_map = {
            "cluster_name": "clusterName",
            "cloudformation_stack_status": "cloudformationStackStatus",
            "cloudformation_stack_arn": "cloudformationStackArn",
            "region": "region",
            "version": "version",
            "cluster_status": "clusterStatus",
        }

        self._cluster_name = cluster_name
        self._cloudformation_stack_status = cloudformation_stack_status
        self._cloudformation_stack_arn = cloudformation_stack_arn
        self._region = region
        self._version = version
        self._cluster_status = cluster_status

    @classmethod
    def from_dict(cls, dikt) -> "ClusterInfoSummary":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ClusterInfoSummary of this ClusterInfoSummary.
        :rtype: ClusterInfoSummary
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cluster_name(self):
        """Gets the cluster_name of this ClusterInfoSummary.

        Name of the cluster

        :return: The cluster_name of this ClusterInfoSummary.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this ClusterInfoSummary.

        Name of the cluster

        :param cluster_name: The cluster_name of this ClusterInfoSummary.
        :type cluster_name: str
        """
        if cluster_name is None:
            raise ValueError("Invalid value for `cluster_name`, must not be `None`")
        if cluster_name is not None and len(cluster_name) > 60:
            raise ValueError("Invalid value for `cluster_name`, length must be less than or equal to `60`")
        if cluster_name is not None and len(cluster_name) < 5:
            raise ValueError("Invalid value for `cluster_name`, length must be greater than or equal to `5`")
        if cluster_name is not None and not re.search(r"^[a-zA-Z][a-zA-Z0-9-]+$", cluster_name):
            raise ValueError(
                "Invalid value for `cluster_name`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9-]+$/`"
            )

        self._cluster_name = cluster_name

    @property
    def cloudformation_stack_status(self):
        """Gets the cloudformation_stack_status of this ClusterInfoSummary.


        :return: The cloudformation_stack_status of this ClusterInfoSummary.
        :rtype: CloudFormationStatus
        """
        return self._cloudformation_stack_status

    @cloudformation_stack_status.setter
    def cloudformation_stack_status(self, cloudformation_stack_status):
        """Sets the cloudformation_stack_status of this ClusterInfoSummary.


        :param cloudformation_stack_status: The cloudformation_stack_status of this ClusterInfoSummary.
        :type cloudformation_stack_status: CloudFormationStatus
        """
        if cloudformation_stack_status is None:
            raise ValueError("Invalid value for `cloudformation_stack_status`, must not be `None`")

        self._cloudformation_stack_status = cloudformation_stack_status

    @property
    def cloudformation_stack_arn(self):
        """Gets the cloudformation_stack_arn of this ClusterInfoSummary.

        ARN of the main CloudFormation stack

        :return: The cloudformation_stack_arn of this ClusterInfoSummary.
        :rtype: str
        """
        return self._cloudformation_stack_arn

    @cloudformation_stack_arn.setter
    def cloudformation_stack_arn(self, cloudformation_stack_arn):
        """Sets the cloudformation_stack_arn of this ClusterInfoSummary.

        ARN of the main CloudFormation stack

        :param cloudformation_stack_arn: The cloudformation_stack_arn of this ClusterInfoSummary.
        :type cloudformation_stack_arn: str
        """
        if cloudformation_stack_arn is None:
            raise ValueError("Invalid value for `cloudformation_stack_arn`, must not be `None`")

        self._cloudformation_stack_arn = cloudformation_stack_arn

    @property
    def region(self):
        """Gets the region of this ClusterInfoSummary.

        AWS region where the cluster is created

        :return: The region of this ClusterInfoSummary.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ClusterInfoSummary.

        AWS region where the cluster is created

        :param region: The region of this ClusterInfoSummary.
        :type region: str
        """
        if region is None:
            raise ValueError("Invalid value for `region`, must not be `None`")

        self._region = region

    @property
    def version(self):
        """Gets the version of this ClusterInfoSummary.

        ParallelCluster version used to create the cluster

        :return: The version of this ClusterInfoSummary.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ClusterInfoSummary.

        ParallelCluster version used to create the cluster

        :param version: The version of this ClusterInfoSummary.
        :type version: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")

        self._version = version

    @property
    def cluster_status(self):
        """Gets the cluster_status of this ClusterInfoSummary.


        :return: The cluster_status of this ClusterInfoSummary.
        :rtype: ClusterStatus
        """
        return self._cluster_status

    @cluster_status.setter
    def cluster_status(self, cluster_status):
        """Sets the cluster_status of this ClusterInfoSummary.


        :param cluster_status: The cluster_status of this ClusterInfoSummary.
        :type cluster_status: ClusterStatus
        """
        if cluster_status is None:
            raise ValueError("Invalid value for `cluster_status`, must not be `None`")

        self._cluster_status = cluster_status
