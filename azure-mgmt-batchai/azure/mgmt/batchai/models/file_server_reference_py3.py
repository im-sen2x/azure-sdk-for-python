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


class FileServerReference(Model):
    """File Server mounting configuration.

    All required parameters must be populated in order to send to Azure.

    :param file_server: Required. File server. Resource ID of the existing
     File Server to be mounted.
    :type file_server: ~azure.mgmt.batchai.models.ResourceId
    :param source_directory: Source directory. File Server directory that
     needs to be mounted. If this property is not specified, the entire File
     Server will be mounted.
    :type source_directory: str
    :param relative_mount_path: Required. Relative mount path. The relative
     path on the compute node where the File Server will be mounted. Note that
     all cluster level file servers will be mounted under
     $AZ_BATCHAI_MOUNT_ROOT location and all job level file servers will be
     mounted under $AZ_BATCHAI_JOB_MOUNT_ROOT.
    :type relative_mount_path: str
    :param mount_options: Mount options. Mount options to be passed to mount
     command.
    :type mount_options: str
    """

    _validation = {
        'file_server': {'required': True},
        'relative_mount_path': {'required': True},
    }

    _attribute_map = {
        'file_server': {'key': 'fileServer', 'type': 'ResourceId'},
        'source_directory': {'key': 'sourceDirectory', 'type': 'str'},
        'relative_mount_path': {'key': 'relativeMountPath', 'type': 'str'},
        'mount_options': {'key': 'mountOptions', 'type': 'str'},
    }

    def __init__(self, *, file_server, relative_mount_path: str, source_directory: str=None, mount_options: str=None, **kwargs) -> None:
        super(FileServerReference, self).__init__(**kwargs)
        self.file_server = file_server
        self.source_directory = source_directory
        self.relative_mount_path = relative_mount_path
        self.mount_options = mount_options
