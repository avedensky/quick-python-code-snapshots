#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The program test time of adler32 and crc32 algoritms.
# adler32 and crc32 is calculate control sum. (for file or some binary data)

#Your config here
FILE_NAME_FOR_TEST_TIME_CRC = "you_file.big";
#----------------

import zlib
import time


def calc_crc32 (filename):
    try:
        input = open(filename, 'rb')
        crc32 = 0
        while True:
            data = input.read (1024)
            if data == "":
                break
            crc32 = zlib.crc32(data, crc32)
        
        input.close()
    except:
        sys.stderr.write (str+'\n')
        sys.stderr.write ('* Err Info :'+ str(sys.exc_info () [0])+'\n')
        sys.stderr.write ('* Err Info :'+ str(sys.exc_info () [1])+'\n')
        return -1
    
    return crc32


def calc_adler32 (filename):
    try:
        input = open(filename, 'rb')
        adler32 = 0
        while True:
            data = input.read (1024)
            if data == "":
                break
            adler32 = zlib.adler32(data, adler32)
        
        input.close()
    except:
        sys.stderr.write (str+'\n')
        sys.stderr.write ('* Err Info :'+ str(sys.exc_info () [0])+'\n')
        sys.stderr.write ('* Err Info :'+ str(sys.exc_info () [1])+'\n')
        return -1
    
    return adler32


print "FIGHT: CRC32 VS ADLER32"
print "----------------"
print ""

start_time = time.time()
print "crc32 : "+str(calc_crc32(FILE_NAME_FOR_TEST_TIME_CRC))
end_time = time.time()
print "time : "+str(end_time-start_time)
print "----------------------------------"

start_time = time.time()
print "adler32 : "+str(calc_adler32(FILE_NAME_FOR_TEST_TIME_CRC))
end_time = time.time()
print "time : "+str(end_time-start_time)
print "----------------------------------"
