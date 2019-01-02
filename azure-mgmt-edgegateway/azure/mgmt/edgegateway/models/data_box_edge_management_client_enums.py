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

from enum import Enum


class AlertSeverity(str, Enum):

    informational = "Informational"
    warning = "Warning"
    critical = "Critical"


class EncryptionAlgorithm(str, Enum):

    none = "None"
    aes256 = "AES256"
    rsaes_pkcs1_v_1_5 = "RSAES_PKCS1_v_1_5"


class AzureContainerDataFormat(str, Enum):

    block_blob = "BlockBlob"
    page_blob = "PageBlob"
    azure_file = "AzureFile"


class DayOfWeek(str, Enum):

    sunday = "Sunday"
    monday = "Monday"
    tuesday = "Tuesday"
    wednesday = "Wednesday"
    thursday = "Thursday"
    friday = "Friday"
    saturday = "Saturday"


class ClientPermissionType(str, Enum):

    no_access = "NoAccess"
    read_only = "ReadOnly"
    read_write = "ReadWrite"


class SkuName(str, Enum):

    gateway = "Gateway"
    edge = "Edge"


class SkuTier(str, Enum):

    standard = "Standard"


class DataBoxEdgeDeviceStatus(str, Enum):

    ready_to_setup = "ReadyToSetup"
    online = "Online"
    offline = "Offline"
    needs_attention = "NeedsAttention"
    disconnected = "Disconnected"
    partially_disconnected = "PartiallyDisconnected"


class DeviceType(str, Enum):

    data_box_edge_device = "DataBoxEdgeDevice"


class RoleTypes(str, Enum):

    iot = "IOT"
    asa = "ASA"
    functions = "Functions"
    cognitive = "Cognitive"


class PlatformType(str, Enum):

    windows = "Windows"
    linux = "Linux"


class RoleStatus(str, Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class JobStatus(str, Enum):

    invalid = "Invalid"
    running = "Running"
    succeeded = "Succeeded"
    failed = "Failed"
    canceled = "Canceled"
    paused = "Paused"
    scheduled = "Scheduled"


class JobType(str, Enum):

    invalid = "Invalid"
    scan_for_updates = "ScanForUpdates"
    download_updates = "DownloadUpdates"
    install_updates = "InstallUpdates"
    refresh_share = "RefreshShare"


class UpdateOperationStage(str, Enum):

    unknown = "Unknown"
    initial = "Initial"
    scan_started = "ScanStarted"
    scan_complete = "ScanComplete"
    scan_failed = "ScanFailed"
    download_started = "DownloadStarted"
    download_complete = "DownloadComplete"
    download_failed = "DownloadFailed"
    install_started = "InstallStarted"
    install_complete = "InstallComplete"
    install_failed = "InstallFailed"
    reboot_initiated = "RebootInitiated"
    success = "Success"
    failure = "Failure"
    rescan_started = "RescanStarted"
    rescan_complete = "RescanComplete"
    rescan_failed = "RescanFailed"


class DownloadPhase(str, Enum):

    unknown = "Unknown"
    initializing = "Initializing"
    downloading = "Downloading"
    verifying = "Verifying"


class MetricUnit(str, Enum):

    not_specified = "NotSpecified"
    percent = "Percent"
    count = "Count"
    seconds = "Seconds"
    milliseconds = "Milliseconds"
    bytes = "Bytes"
    bytes_per_second = "BytesPerSecond"
    count_per_second = "CountPerSecond"


class MetricAggregationType(str, Enum):

    not_specified = "NotSpecified"
    none = "None"
    average = "Average"
    minimum = "Minimum"
    maximum = "Maximum"
    total = "Total"
    count = "Count"


class MetricCategory(str, Enum):

    capacity = "Capacity"
    transaction = "Transaction"


class TimeGrain(str, Enum):

    pt1_m = "PT1M"
    pt5_m = "PT5M"
    pt15_m = "PT15M"
    pt30_m = "PT30M"
    pt1_h = "PT1H"
    pt6_h = "PT6H"
    pt12_h = "PT12H"
    pt1_d = "PT1D"


class NetworkGroup(str, Enum):

    none = "None"
    non_rdma = "NonRDMA"
    rdma = "RDMA"


class NetworkAdapterStatus(str, Enum):

    inactive = "Inactive"
    active = "Active"


class NetworkAdapterRDMAStatus(str, Enum):

    incapable = "Incapable"
    capable = "Capable"


class NetworkAdapterDHCPStatus(str, Enum):

    disabled = "Disabled"
    enabled = "Enabled"


class StatusTypes(str, Enum):

    untracked = "Untracked"
    awaiting_fulfilment = "AwaitingFulfilment"
    awaiting_preparation = "AwaitingPreparation"
    awaiting_shipment = "AwaitingShipment"
    shipped = "Shipped"
    arriving = "Arriving"
    delivered = "Delivered"
    replacement_requested = "ReplacementRequested"
    lost_device = "LostDevice"
    declined = "Declined"
    return_initiated = "ReturnInitiated"
    awaiting_return_shipment = "AwaitingReturnShipment"
    shipped_back = "ShippedBack"
    collected_at_microsoft = "CollectedAtMicrosoft"


class AuthenticationType(str, Enum):

    invalid = "Invalid"
    azure_active_directory = "AzureActiveDirectory"


class ShareStatus(str, Enum):

    online = "Online"
    offline = "Offline"


class MonitoringStatus(str, Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class ShareAccessProtocol(str, Enum):

    smb = "SMB"
    nfs = "NFS"


class ShareAccessType(str, Enum):

    change = "Change"
    read = "Read"
    custom = "Custom"


class DataPolicy(str, Enum):

    cloud = "Cloud"
    local = "Local"


class SSLStatus(str, Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class AccountType(str, Enum):

    general_purpose_storage = "GeneralPurposeStorage"
    blob_storage = "BlobStorage"


class InstallRebootBehavior(str, Enum):

    never_reboots = "NeverReboots"
    requires_reboot = "RequiresReboot"
    request_reboot = "RequestReboot"


class UpdateOperation(str, Enum):

    none = "None"
    scan = "Scan"
    download = "Download"
    install = "Install"
