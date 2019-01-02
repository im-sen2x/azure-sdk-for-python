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


class Operation(Model):
    """Operations.

    :param name: Name of the operation.
    :type name: str
    :param display: Properties to displayed for the operation.
    :type display: ~azure.mgmt.edgegateway.models.OperationDisplay
    :param origin: Origin of the operation.
    :type origin: str
    :param service_specification: Service specification.
    :type service_specification:
     ~azure.mgmt.edgegateway.models.ServiceSpecification
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
        'origin': {'key': 'origin', 'type': 'str'},
        'service_specification': {'key': 'properties.serviceSpecification', 'type': 'ServiceSpecification'},
    }

    def __init__(self, *, name: str=None, display=None, origin: str=None, service_specification=None, **kwargs) -> None:
        super(Operation, self).__init__(**kwargs)
        self.name = name
        self.display = display
        self.origin = origin
        self.service_specification = service_specification
