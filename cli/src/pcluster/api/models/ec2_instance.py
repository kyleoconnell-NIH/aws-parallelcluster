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
from pcluster.api.models.instance_state import InstanceState


class EC2Instance(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(
        self,
        launch_time=None,
        instance_id=None,
        public_ip_address=None,
        instance_type=None,
        state=None,
        private_ip_address=None,
    ):
        """EC2Instance - a model defined in OpenAPI

        :param launch_time: The launch_time of this EC2Instance.
        :type launch_time: datetime
        :param instance_id: The instance_id of this EC2Instance.
        :type instance_id: str
        :param public_ip_address: The public_ip_address of this EC2Instance.
        :type public_ip_address: str
        :param instance_type: The instance_type of this EC2Instance.
        :type instance_type: str
        :param state: The state of this EC2Instance.
        :type state: InstanceState
        :param private_ip_address: The private_ip_address of this EC2Instance.
        :type private_ip_address: str
        """
        self.openapi_types = {
            "launch_time": datetime,
            "instance_id": str,
            "public_ip_address": str,
            "instance_type": str,
            "state": InstanceState,
            "private_ip_address": str,
        }

        self.attribute_map = {
            "launch_time": "launchTime",
            "instance_id": "instanceId",
            "public_ip_address": "publicIpAddress",
            "instance_type": "instanceType",
            "state": "state",
            "private_ip_address": "privateIpAddress",
        }

        self._launch_time = launch_time
        self._instance_id = instance_id
        self._public_ip_address = public_ip_address
        self._instance_type = instance_type
        self._state = state
        self._private_ip_address = private_ip_address

    @classmethod
    def from_dict(cls, dikt) -> "EC2Instance":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EC2Instance of this EC2Instance.
        :rtype: EC2Instance
        """
        return util.deserialize_model(dikt, cls)

    @property
    def launch_time(self):
        """Gets the launch_time of this EC2Instance.


        :return: The launch_time of this EC2Instance.
        :rtype: datetime
        """
        return self._launch_time

    @launch_time.setter
    def launch_time(self, launch_time):
        """Sets the launch_time of this EC2Instance.


        :param launch_time: The launch_time of this EC2Instance.
        :type launch_time: datetime
        """
        if launch_time is None:
            raise ValueError("Invalid value for `launch_time`, must not be `None`")

        self._launch_time = launch_time

    @property
    def instance_id(self):
        """Gets the instance_id of this EC2Instance.


        :return: The instance_id of this EC2Instance.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this EC2Instance.


        :param instance_id: The instance_id of this EC2Instance.
        :type instance_id: str
        """
        if instance_id is None:
            raise ValueError("Invalid value for `instance_id`, must not be `None`")

        self._instance_id = instance_id

    @property
    def public_ip_address(self):
        """Gets the public_ip_address of this EC2Instance.


        :return: The public_ip_address of this EC2Instance.
        :rtype: str
        """
        return self._public_ip_address

    @public_ip_address.setter
    def public_ip_address(self, public_ip_address):
        """Sets the public_ip_address of this EC2Instance.


        :param public_ip_address: The public_ip_address of this EC2Instance.
        :type public_ip_address: str
        """

        self._public_ip_address = public_ip_address

    @property
    def instance_type(self):
        """Gets the instance_type of this EC2Instance.


        :return: The instance_type of this EC2Instance.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this EC2Instance.


        :param instance_type: The instance_type of this EC2Instance.
        :type instance_type: str
        """
        if instance_type is None:
            raise ValueError("Invalid value for `instance_type`, must not be `None`")

        self._instance_type = instance_type

    @property
    def state(self):
        """Gets the state of this EC2Instance.


        :return: The state of this EC2Instance.
        :rtype: InstanceState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this EC2Instance.


        :param state: The state of this EC2Instance.
        :type state: InstanceState
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")

        self._state = state

    @property
    def private_ip_address(self):
        """Gets the private_ip_address of this EC2Instance.


        :return: The private_ip_address of this EC2Instance.
        :rtype: str
        """
        return self._private_ip_address

    @private_ip_address.setter
    def private_ip_address(self, private_ip_address):
        """Sets the private_ip_address of this EC2Instance.


        :param private_ip_address: The private_ip_address of this EC2Instance.
        :type private_ip_address: str
        """
        if private_ip_address is None:
            raise ValueError("Invalid value for `private_ip_address`, must not be `None`")

        self._private_ip_address = private_ip_address
