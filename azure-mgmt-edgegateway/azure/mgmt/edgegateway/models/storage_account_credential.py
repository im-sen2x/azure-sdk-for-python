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

from .arm_base_model import ARMBaseModel


class StorageAccountCredential(ARMBaseModel):
    """The storage account credential.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The path ID that uniquely identifies the object.
    :vartype id: str
    :ivar name: The name of the object.
    :vartype name: str
    :ivar type: The hierarchical type of the object.
    :vartype type: str
    :param alias: Required. Alias for the storage account.
    :type alias: str
    :param user_name: UserName for the storage account.
    :type user_name: str
    :param account_key: Encrypted storage key.
    :type account_key:
     ~azure.mgmt.edgegateway.models.AsymmetricEncryptedSecret
    :param connection_string: ConnectionString for the storage account. This
     needs to be specified if UserName/AccountKey are not specified.
    :type connection_string: str
    :param ssl_status: Required. Signifies whether SSL needs to be enabled or
     not. Possible values include: 'Enabled', 'Disabled'
    :type ssl_status: str or ~azure.mgmt.edgegateway.models.SSLStatus
    :param blob_domain_name: Blob end point for private clouds.
    :type blob_domain_name: str
    :param account_type: Required. Type of storage accessed on the storage
     account. Possible values include: 'GeneralPurposeStorage', 'BlobStorage'
    :type account_type: str or ~azure.mgmt.edgegateway.models.AccountType
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'alias': {'required': True},
        'ssl_status': {'required': True},
        'account_type': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'alias': {'key': 'properties.alias', 'type': 'str'},
        'user_name': {'key': 'properties.userName', 'type': 'str'},
        'account_key': {'key': 'properties.accountKey', 'type': 'AsymmetricEncryptedSecret'},
        'connection_string': {'key': 'properties.connectionString', 'type': 'str'},
        'ssl_status': {'key': 'properties.sslStatus', 'type': 'str'},
        'blob_domain_name': {'key': 'properties.blobDomainName', 'type': 'str'},
        'account_type': {'key': 'properties.accountType', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(StorageAccountCredential, self).__init__(**kwargs)
        self.alias = kwargs.get('alias', None)
        self.user_name = kwargs.get('user_name', None)
        self.account_key = kwargs.get('account_key', None)
        self.connection_string = kwargs.get('connection_string', None)
        self.ssl_status = kwargs.get('ssl_status', None)
        self.blob_domain_name = kwargs.get('blob_domain_name', None)
        self.account_type = kwargs.get('account_type', None)
