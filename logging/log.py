#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging

LOG_FILENAME = 'example.log'
myLog = logging.getLogger ()

#Our Config
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler = logging.FileHandler(LOG_FILENAME)
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)

#Set settings
myLog.addHandler (handler)

#Do it
myLog.warning ('This is warning') #You can see file example.log in current dir

