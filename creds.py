#!/usr/bin/env python3


'''Credentials'''

import os

bot_token = os.environ["5911160230:AAFk86M5NjtvPxqFUd9mXv_W4YlGHIGO8k8"]

api_id = os.environ["11480401"]

api_hash = os.environ["e151e5dc145d2b42accde41a37207201"]

pdisk_api = os.environ["https://pdisk.pro/api/account/info?key=1714c294o4yd68xtvw22"]

try:
    connection_string = os.environ["MONGO_CON_STRING"]
except KeyError:
    connection_string = None

