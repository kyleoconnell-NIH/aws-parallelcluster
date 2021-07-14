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


class CloudFormationStatus(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    CREATE_COMPLETE = "CREATE_COMPLETE"
    ROLLBACK_IN_PROGRESS = "ROLLBACK_IN_PROGRESS"
    ROLLBACK_FAILED = "ROLLBACK_FAILED"
    ROLLBACK_COMPLETE = "ROLLBACK_COMPLETE"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    DELETE_FAILED = "DELETE_FAILED"
    DELETE_COMPLETE = "DELETE_COMPLETE"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    UPDATE_COMPLETE_CLEANUP_IN_PROGRESS = "UPDATE_COMPLETE_CLEANUP_IN_PROGRESS"
    UPDATE_COMPLETE = "UPDATE_COMPLETE"
    UPDATE_ROLLBACK_IN_PROGRESS = "UPDATE_ROLLBACK_IN_PROGRESS"
    UPDATE_ROLLBACK_FAILED = "UPDATE_ROLLBACK_FAILED"
    UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS = "UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS"
    UPDATE_ROLLBACK_COMPLETE = "UPDATE_ROLLBACK_COMPLETE"

    def __init__(self):
        """CloudFormationStatus - a model defined in OpenAPI"""
        self.openapi_types = {}

        self.attribute_map = {}

    @classmethod
    def from_dict(cls, dikt) -> "CloudFormationStatus":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CloudFormationStatus of this CloudFormationStatus.
        :rtype: CloudFormationStatus
        """
        return util.deserialize_model(dikt, cls)
