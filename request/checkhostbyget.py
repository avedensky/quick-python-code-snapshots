#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Send GET query to HOST and print status
#
# The module depend from request lib
# You can install request lib: pip3 install request

import requests

HOST = 'http://yandex.ru'
r = requests.get(HOST)
print (r.status_code)