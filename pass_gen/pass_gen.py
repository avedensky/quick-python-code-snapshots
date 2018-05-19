#!/usr/bin/env python3
#coding: utf-8

#Generating random pasword

import string
import random

pass_len = 12
password = ''.join([random.choice(string.ascii_lowercase+string.digits) for i in range(0, pass_len)])

print(password)
