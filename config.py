#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "9e6d7d91-75c6-4e9a-b40a-83c36a18290b")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "X.D8Q~uYmvFJH0gedFt9QNVg9fQZxsNn0lKG5ck2")
