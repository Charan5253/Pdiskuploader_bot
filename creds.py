#!/usr/bin/env python3


'''Credentials'''

import os

bot_token = os.environ["2089129150:AAEE3oNNcd3NANRiIeVXJmDmQ0w2EuQxL1g"]

api_id = os.environ["8971105"]

api_hash = os.environ["b68b85bd69e423c421984a551b83e959"]

pdisk_api = os.environ["15ad1b496285541feb5d0e3334219f9b"]

try:
    connection_string = os.environ["MONGO_CON_STRING"]
except KeyError:
    connection_string = None

