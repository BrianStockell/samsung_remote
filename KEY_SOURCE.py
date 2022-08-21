#!/usr/bin/env python3

import samsungctl
import time

config = {
    "name": "samsungctl",
    "description": "PC",
    "id": "",
    "host": "10.41.77.202",
    "port": 55000,
    "method": "legacy",
    "timeout": 0,
}

#with samsungctl.Remote(config) as remote:
#    for i in range(1):
#        remote.control("KEY_CONTENTS")
#        time.sleep(0.5)

# with samsungctl.Remote(config) as remote:
#    for i in range(1):
#        remote.control("KEY_POWEROFF")
#        time.sleep(0.5)

with samsungctl.Remote(config) as remote:
    for i in range(1):
        remote.control("KEY_SOURCE")
        time.sleep(0.5)