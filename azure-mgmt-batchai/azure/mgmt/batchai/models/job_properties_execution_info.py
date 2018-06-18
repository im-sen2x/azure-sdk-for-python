# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class JobPropertiesExecutionInfo(Model):
    """Information about the execution of a job.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar start_time: Start time. The time at which the job started running.
     'Running' corresponds to the running state. If the job has been restarted
     or retried, this is the most recent time at which the job started running.
     This property is present only for job that are in the running or completed
     state.
    :vartype start_time: datetime
    :ivar end_time: End time. The time at which the job completed. This
     property is only returned if the job is in completed state.
    :vartype end_time: datetime
    :ivar exit_code: Exit code. The exit code of the job. This property is
     only returned if the job is in completed state.
    :vartype exit_code: int
    :ivar errors: Errors. A collection of errors encountered by the service
     during job execution.
    :vartype errors: list[~azure.mgmt.batchai.models.BatchAIError]
    """

    _validation = {
        'start_time': {'readonly': True},
        'end_time': {'readonly': True},
        'exit_code': {'readonly': True},
        'errors': {'readonly': True},
    }

    _attribute_map = {
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'exit_code': {'key': 'exitCode', 'type': 'int'},
        'errors': {'key': 'errors', 'type': '[BatchAIError]'},
    }

    def __init__(self, **kwargs):
        super(JobPropertiesExecutionInfo, self).__init__(**kwargs)
        self.start_time = None
        self.end_time = None
        self.exit_code = None
        self.errors = None
