#!/usr/bin/env python
#coding: utf-8

"""

	Calculate md5 for file

"""

import hashlib

def md5sum(filename):
    md5 = hashlib.md5()
    with open(filename,'rb') as f:
        for chunk in iter(lambda: f.read(128*md5.block_size), b''):
             md5.update(chunk)
    return md5.hexdigest()

def main():
    pass

if __name__ == '__main__':
    main()
