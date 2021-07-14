# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance
# with the License. A copy of the License is located at http://aws.amazon.com/apache2.0/
# or in the "LICENSE.txt" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
# OR CONDITIONS OF ANY KIND, express or implied. See the License for the specific language governing permissions and
# limitations under the License.

# pylint: disable=R0801


from datetime import datetime

from pcluster.api import util
from pcluster.api.models.base_model_ import Model
from pcluster.api.models.compute_fleet_status import ComputeFleetStatus


class DescribeComputeFleetStatusResponseContent(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, last_updated_time=None, status=None):
        """DescribeComputeFleetStatusResponseContent - a model defined in OpenAPI

        :param last_updated_time: The last_updated_time of this DescribeComputeFleetStatusResponseContent.
        :type last_updated_time: datetime
        :param status: The status of this DescribeComputeFleetStatusResponseContent.
        :type status: ComputeFleetStatus
        """
        self.openapi_types = {"last_updated_time": datetime, "status": ComputeFleetStatus}

        self.attribute_map = {"last_updated_time": "lastUpdatedTime", "status": "status"}

        self._last_updated_time = last_updated_time
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> "DescribeComputeFleetStatusResponseContent":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DescribeComputeFleetStatusResponseContent of this DescribeComputeFleetStatusResponseContent.
        :rtype: DescribeComputeFleetStatusResponseContent
        """
        return util.deserialize_model(dikt, cls)

    @property
    def last_updated_time(self):
        """Gets the last_updated_time of this DescribeComputeFleetStatusResponseContent.

        Timestamp representing the last status update time

        :return: The last_updated_time of this DescribeComputeFleetStatusResponseContent.
        :rtype: datetime
        """
        return self._last_updated_time

    @last_updated_time.setter
    def last_updated_time(self, last_updated_time):
        """Sets the last_updated_time of this DescribeComputeFleetStatusResponseContent.

        Timestamp representing the last status update time

        :param last_updated_time: The last_updated_time of this DescribeComputeFleetStatusResponseContent.
        :type last_updated_time: datetime
        """
        if last_updated_time is None:
            raise ValueError("Invalid value for `last_updated_time`, must not be `None`")

        self._last_updated_time = last_updated_time

    @property
    def status(self):
        """Gets the status of this DescribeComputeFleetStatusResponseContent.


        :return: The status of this DescribeComputeFleetStatusResponseContent.
        :rtype: ComputeFleetStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DescribeComputeFleetStatusResponseContent.


        :param status: The status of this DescribeComputeFleetStatusResponseContent.
        :type status: ComputeFleetStatus
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")

        self._status = status
