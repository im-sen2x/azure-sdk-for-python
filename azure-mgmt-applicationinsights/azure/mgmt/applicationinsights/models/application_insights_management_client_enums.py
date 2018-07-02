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


class ApplicationType(Enum):

    web = "web"
    other = "other"


class FlowType(Enum):

    bluefield = "Bluefield"


class RequestSource(Enum):

    rest = "rest"


class PurgeState(Enum):

    pending = "pending"
    completed = "completed"


class FavoriteType(Enum):

    shared = "shared"
    user = "user"


class WebTestKind(Enum):

    ping = "ping"
    multistep = "multistep"


class ItemScope(Enum):

    shared = "shared"
    user = "user"


class ItemType(Enum):

    query = "query"
    function = "function"
    folder = "folder"
    recent = "recent"


class SharedTypeKind(Enum):

    user = "user"
    shared = "shared"


class FavoriteSourceType(Enum):

    retention = "retention"
    notebook = "notebook"
    sessions = "sessions"
    events = "events"
    userflows = "userflows"
    funnel = "funnel"
    impact = "impact"
    segmentation = "segmentation"


class ItemScopePath(Enum):

    analytics_items = "analyticsItems"
    myanalytics_items = "myanalyticsItems"


class ItemTypeParameter(Enum):

    none = "none"
    query = "query"
    function = "function"
    folder = "folder"
    recent = "recent"


class CategoryType(Enum):

    workbook = "workbook"
    tsg = "TSG"
    performance = "performance"
    retention = "retention"
