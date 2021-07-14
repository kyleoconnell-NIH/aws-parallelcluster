# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance
# with the License. A copy of the License is located at http://aws.amazon.com/apache2.0/
# or in the "LICENSE.txt" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
# OR CONDITIONS OF ANY KIND, express or implied. See the License for the specific language governing permissions and
# limitations under the License.

# pylint: disable=R0801


import re
from datetime import datetime
from typing import List

from pcluster.api import util
from pcluster.api.models.base_model_ import Model
from pcluster.api.models.cloud_formation_status import CloudFormationStatus
from pcluster.api.models.cluster_configuration_structure import ClusterConfigurationStructure
from pcluster.api.models.cluster_status import ClusterStatus
from pcluster.api.models.compute_fleet_status import ComputeFleetStatus
from pcluster.api.models.ec2_instance import EC2Instance
from pcluster.api.models.tag import Tag


class DescribeClusterResponseContent(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(
        self,
        creation_time=None,
        headnode=None,
        version=None,
        cluster_configuration=None,
        tags=None,
        cloud_formation_status=None,
        cluster_name=None,
        compute_fleet_status=None,
        failure_reason=None,
        cloudformation_stack_arn=None,
        last_updated_time=None,
        region=None,
        cluster_status=None,
    ):
        """DescribeClusterResponseContent - a model defined in OpenAPI

        :param creation_time: The creation_time of this DescribeClusterResponseContent.
        :type creation_time: datetime
        :param headnode: The headnode of this DescribeClusterResponseContent.
        :type headnode: EC2Instance
        :param version: The version of this DescribeClusterResponseContent.
        :type version: str
        :param cluster_configuration: The cluster_configuration of this DescribeClusterResponseContent.
        :type cluster_configuration: ClusterConfigurationStructure
        :param tags: The tags of this DescribeClusterResponseContent.
        :type tags: List[Tag]
        :param cloud_formation_status: The cloud_formation_status of this DescribeClusterResponseContent.
        :type cloud_formation_status: CloudFormationStatus
        :param cluster_name: The cluster_name of this DescribeClusterResponseContent.
        :type cluster_name: str
        :param compute_fleet_status: The compute_fleet_status of this DescribeClusterResponseContent.
        :type compute_fleet_status: ComputeFleetStatus
        :param failure_reason: The failure_reason of this DescribeClusterResponseContent.
        :type failure_reason: str
        :param cloudformation_stack_arn: The cloudformation_stack_arn of this DescribeClusterResponseContent.
        :type cloudformation_stack_arn: str
        :param last_updated_time: The last_updated_time of this DescribeClusterResponseContent.
        :type last_updated_time: datetime
        :param region: The region of this DescribeClusterResponseContent.
        :type region: str
        :param cluster_status: The cluster_status of this DescribeClusterResponseContent.
        :type cluster_status: ClusterStatus
        """
        self.openapi_types = {
            "creation_time": datetime,
            "headnode": EC2Instance,
            "version": str,
            "cluster_configuration": ClusterConfigurationStructure,
            "tags": List[Tag],
            "cloud_formation_status": CloudFormationStatus,
            "cluster_name": str,
            "compute_fleet_status": ComputeFleetStatus,
            "failure_reason": str,
            "cloudformation_stack_arn": str,
            "last_updated_time": datetime,
            "region": str,
            "cluster_status": ClusterStatus,
        }

        self.attribute_map = {
            "creation_time": "creationTime",
            "headnode": "headnode",
            "version": "version",
            "cluster_configuration": "clusterConfiguration",
            "tags": "tags",
            "cloud_formation_status": "cloudFormationStatus",
            "cluster_name": "clusterName",
            "compute_fleet_status": "computeFleetStatus",
            "failure_reason": "failureReason",
            "cloudformation_stack_arn": "cloudformationStackArn",
            "last_updated_time": "lastUpdatedTime",
            "region": "region",
            "cluster_status": "clusterStatus",
        }

        self._creation_time = creation_time
        self._headnode = headnode
        self._version = version
        self._cluster_configuration = cluster_configuration
        self._tags = tags
        self._cloud_formation_status = cloud_formation_status
        self._cluster_name = cluster_name
        self._compute_fleet_status = compute_fleet_status
        self._failure_reason = failure_reason
        self._cloudformation_stack_arn = cloudformation_stack_arn
        self._last_updated_time = last_updated_time
        self._region = region
        self._cluster_status = cluster_status

    @classmethod
    def from_dict(cls, dikt) -> "DescribeClusterResponseContent":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DescribeClusterResponseContent of this DescribeClusterResponseContent.
        :rtype: DescribeClusterResponseContent
        """
        return util.deserialize_model(dikt, cls)

    @property
    def creation_time(self):
        """Gets the creation_time of this DescribeClusterResponseContent.

        Timestamp representing the cluster creation time

        :return: The creation_time of this DescribeClusterResponseContent.
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this DescribeClusterResponseContent.

        Timestamp representing the cluster creation time

        :param creation_time: The creation_time of this DescribeClusterResponseContent.
        :type creation_time: datetime
        """
        if creation_time is None:
            raise ValueError("Invalid value for `creation_time`, must not be `None`")

        self._creation_time = creation_time

    @property
    def headnode(self):
        """Gets the headnode of this DescribeClusterResponseContent.


        :return: The headnode of this DescribeClusterResponseContent.
        :rtype: EC2Instance
        """
        return self._headnode

    @headnode.setter
    def headnode(self, headnode):
        """Sets the headnode of this DescribeClusterResponseContent.


        :param headnode: The headnode of this DescribeClusterResponseContent.
        :type headnode: EC2Instance
        """

        self._headnode = headnode

    @property
    def version(self):
        """Gets the version of this DescribeClusterResponseContent.

        ParallelCluster version used to create the cluster

        :return: The version of this DescribeClusterResponseContent.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DescribeClusterResponseContent.

        ParallelCluster version used to create the cluster

        :param version: The version of this DescribeClusterResponseContent.
        :type version: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")

        self._version = version

    @property
    def cluster_configuration(self):
        """Gets the cluster_configuration of this DescribeClusterResponseContent.


        :return: The cluster_configuration of this DescribeClusterResponseContent.
        :rtype: ClusterConfigurationStructure
        """
        return self._cluster_configuration

    @cluster_configuration.setter
    def cluster_configuration(self, cluster_configuration):
        """Sets the cluster_configuration of this DescribeClusterResponseContent.


        :param cluster_configuration: The cluster_configuration of this DescribeClusterResponseContent.
        :type cluster_configuration: ClusterConfigurationStructure
        """
        if cluster_configuration is None:
            raise ValueError("Invalid value for `cluster_configuration`, must not be `None`")

        self._cluster_configuration = cluster_configuration

    @property
    def tags(self):
        """Gets the tags of this DescribeClusterResponseContent.

        Tags associated with the cluster

        :return: The tags of this DescribeClusterResponseContent.
        :rtype: List[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DescribeClusterResponseContent.

        Tags associated with the cluster

        :param tags: The tags of this DescribeClusterResponseContent.
        :type tags: List[Tag]
        """
        if tags is None:
            raise ValueError("Invalid value for `tags`, must not be `None`")

        self._tags = tags

    @property
    def cloud_formation_status(self):
        """Gets the cloud_formation_status of this DescribeClusterResponseContent.


        :return: The cloud_formation_status of this DescribeClusterResponseContent.
        :rtype: CloudFormationStatus
        """
        return self._cloud_formation_status

    @cloud_formation_status.setter
    def cloud_formation_status(self, cloud_formation_status):
        """Sets the cloud_formation_status of this DescribeClusterResponseContent.


        :param cloud_formation_status: The cloud_formation_status of this DescribeClusterResponseContent.
        :type cloud_formation_status: CloudFormationStatus
        """
        if cloud_formation_status is None:
            raise ValueError("Invalid value for `cloud_formation_status`, must not be `None`")

        self._cloud_formation_status = cloud_formation_status

    @property
    def cluster_name(self):
        """Gets the cluster_name of this DescribeClusterResponseContent.

        Name of the cluster

        :return: The cluster_name of this DescribeClusterResponseContent.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this DescribeClusterResponseContent.

        Name of the cluster

        :param cluster_name: The cluster_name of this DescribeClusterResponseContent.
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
    def compute_fleet_status(self):
        """Gets the compute_fleet_status of this DescribeClusterResponseContent.


        :return: The compute_fleet_status of this DescribeClusterResponseContent.
        :rtype: ComputeFleetStatus
        """
        return self._compute_fleet_status

    @compute_fleet_status.setter
    def compute_fleet_status(self, compute_fleet_status):
        """Sets the compute_fleet_status of this DescribeClusterResponseContent.


        :param compute_fleet_status: The compute_fleet_status of this DescribeClusterResponseContent.
        :type compute_fleet_status: ComputeFleetStatus
        """
        if compute_fleet_status is None:
            raise ValueError("Invalid value for `compute_fleet_status`, must not be `None`")

        self._compute_fleet_status = compute_fleet_status

    @property
    def failure_reason(self):
        """Gets the failure_reason of this DescribeClusterResponseContent.

        Describe the reason of the failure when the stack is in CREATE_FAILED, UPDATE_FAILED or DELETE_FAILED status

        :return: The failure_reason of this DescribeClusterResponseContent.
        :rtype: str
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """Sets the failure_reason of this DescribeClusterResponseContent.

        Describe the reason of the failure when the stack is in CREATE_FAILED, UPDATE_FAILED or DELETE_FAILED status

        :param failure_reason: The failure_reason of this DescribeClusterResponseContent.
        :type failure_reason: str
        """

        self._failure_reason = failure_reason

    @property
    def cloudformation_stack_arn(self):
        """Gets the cloudformation_stack_arn of this DescribeClusterResponseContent.

        ARN of the main CloudFormation stack

        :return: The cloudformation_stack_arn of this DescribeClusterResponseContent.
        :rtype: str
        """
        return self._cloudformation_stack_arn

    @cloudformation_stack_arn.setter
    def cloudformation_stack_arn(self, cloudformation_stack_arn):
        """Sets the cloudformation_stack_arn of this DescribeClusterResponseContent.

        ARN of the main CloudFormation stack

        :param cloudformation_stack_arn: The cloudformation_stack_arn of this DescribeClusterResponseContent.
        :type cloudformation_stack_arn: str
        """
        if cloudformation_stack_arn is None:
            raise ValueError("Invalid value for `cloudformation_stack_arn`, must not be `None`")

        self._cloudformation_stack_arn = cloudformation_stack_arn

    @property
    def last_updated_time(self):
        """Gets the last_updated_time of this DescribeClusterResponseContent.

        Timestamp representing the last cluster update time

        :return: The last_updated_time of this DescribeClusterResponseContent.
        :rtype: datetime
        """
        return self._last_updated_time

    @last_updated_time.setter
    def last_updated_time(self, last_updated_time):
        """Sets the last_updated_time of this DescribeClusterResponseContent.

        Timestamp representing the last cluster update time

        :param last_updated_time: The last_updated_time of this DescribeClusterResponseContent.
        :type last_updated_time: datetime
        """
        if last_updated_time is None:
            raise ValueError("Invalid value for `last_updated_time`, must not be `None`")

        self._last_updated_time = last_updated_time

    @property
    def region(self):
        """Gets the region of this DescribeClusterResponseContent.

        AWS region where the cluster is created

        :return: The region of this DescribeClusterResponseContent.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this DescribeClusterResponseContent.

        AWS region where the cluster is created

        :param region: The region of this DescribeClusterResponseContent.
        :type region: str
        """
        if region is None:
            raise ValueError("Invalid value for `region`, must not be `None`")

        self._region = region

    @property
    def cluster_status(self):
        """Gets the cluster_status of this DescribeClusterResponseContent.


        :return: The cluster_status of this DescribeClusterResponseContent.
        :rtype: ClusterStatus
        """
        return self._cluster_status

    @cluster_status.setter
    def cluster_status(self, cluster_status):
        """Sets the cluster_status of this DescribeClusterResponseContent.


        :param cluster_status: The cluster_status of this DescribeClusterResponseContent.
        :type cluster_status: ClusterStatus
        """
        if cluster_status is None:
            raise ValueError("Invalid value for `cluster_status`, must not be `None`")

        self._cluster_status = cluster_status
