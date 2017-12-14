#!/usr/bin/env python3
#coding: utf-8

import string
import random

LENGHT = 10
s = ''
for i in range(0, LENGHT):
    s += random.choice(string.ascii_lowercase+string.digits)

print(s)    