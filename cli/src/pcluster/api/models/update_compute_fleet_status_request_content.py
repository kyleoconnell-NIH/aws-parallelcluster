# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance
# with the License. A copy of the License is located at http://aws.amazon.com/apache2.0/
# or in the "LICENSE.txt" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
# OR CONDITIONS OF ANY KIND, express or implied. See the License for the specific language governing permissions and
# limitations under the License.

# pylint: disable=R0801


from pcluster.api import util
from pcluster.api.models.base_model_ import Model
from pcluster.api.models.requested_compute_fleet_status import RequestedComputeFleetStatus


class UpdateComputeFleetStatusRequestContent(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, status=None):
        """UpdateComputeFleetStatusRequestContent - a model defined in OpenAPI

        :param status: The status of this UpdateComputeFleetStatusRequestContent.
        :type status: RequestedComputeFleetStatus
        """
        self.openapi_types = {"status": RequestedComputeFleetStatus}

        self.attribute_map = {"status": "status"}

        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> "UpdateComputeFleetStatusRequestContent":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UpdateComputeFleetStatusRequestContent of this UpdateComputeFleetStatusRequestContent.
        :rtype: UpdateComputeFleetStatusRequestContent
        """
        return util.deserialize_model(dikt, cls)

    @property
    def status(self):
        """Gets the status of this UpdateComputeFleetStatusRequestContent.


        :return: The status of this UpdateComputeFleetStatusRequestContent.
        :rtype: RequestedComputeFleetStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateComputeFleetStatusRequestContent.


        :param status: The status of this UpdateComputeFleetStatusRequestContent.
        :type status: RequestedComputeFleetStatus
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")

        self._status = status
