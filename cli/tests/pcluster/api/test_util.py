#  Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance
#  with the License. A copy of the License is located at http://aws.amazon.com/apache2.0/
#  or in the "LICENSE.txt" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
#  OR CONDITIONS OF ANY KIND, express or implied. See the License for the specific language governing permissions and
#  limitations under the License.
import logging
import subprocess

import pytest
from assertpy import assert_that

from pcluster.api import util


class TestParallelClusterApiUtil:
    @pytest.mark.parametrize(
        "version, error, expected_message",
        [
            ("14.21.0", None, None),
            ("v18.12.0", None, None),
            ("10.1.0", Exception(), "requires Node.js version >="),
            (Exception(), Exception(), "Unable to check Node.js version"),
        ],
    )
    def test_assert_node_version(self, mocker, version, error, expected_message):
        if isinstance(version, Exception):
            check_output_mock = mocker.patch("pcluster.api.util.subprocess.check_output", side_effect=Exception)
            with pytest.raises(Exception) as exc:
                util._assert_node_version()
            check_output_mock.assert_has_calls(
                [
                    mocker.call((["node", "--version"]), stderr=subprocess.STDOUT, encoding="utf-8", shell=False),
                    mocker.call((["nvm", "current"]), stderr=subprocess.STDOUT, encoding="utf-8", shell=False),
                ]
            )
            assert_that(str(exc.value)).matches(expected_message)
        else:
            check_output_mock = mocker.patch("pcluster.api.util.subprocess.check_output", return_value=version)
            if isinstance(error, Exception):
                with pytest.raises(Exception) as exc:
                    util._assert_node_version()
                assert_that(str(exc.value)).matches(expected_message)
            else:
                util._assert_node_version()
            check_output_mock.assert_called_once_with(
                (["node", "--version"]), stderr=subprocess.STDOUT, encoding="utf-8", shell=False
            )

    @pytest.mark.parametrize(
        "version, expected_message",
        [
            ("v18.12.0", "Unable to invoke Node.js for the installed version v18.12.0."),
            ("v16.16.0", "Unable to invoke Node.js for the installed version v16.16.0."),
            ("none", "Node.js does not appear to be installed."),
        ],
    )
    def test_assert_node_version_fallback_to_nvm(self, mocker, caplog, version, expected_message):
        check_output_mock = mocker.patch("pcluster.api.util.subprocess.check_output")
        check_output_mock.side_effect = [Exception, version]
        with pytest.raises(Exception) as exc:
            util._assert_node_version()
        assert_that(str(exc.value)).starts_with(expected_message)
        check_output_mock.assert_has_calls(
            [
                mocker.call((["node", "--version"]), stderr=subprocess.STDOUT, encoding="utf-8", shell=False),
                mocker.call((["nvm", "current"]), stderr=subprocess.STDOUT, encoding="utf-8", shell=False),
            ]
        )
        warnings = [record for record in caplog.records if record.levelno == logging.CRITICAL]
        assert_that(warnings).is_length(1)
        assert_that(warnings[0].message).starts_with(expected_message)
