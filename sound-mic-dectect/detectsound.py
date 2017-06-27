#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
The module can detected sound in mic-in
This is simple example how this do it
Attention! This module depend from pyaudio
"""

import pyaudio
import wave
import audioop
import time

chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()

# open stream
stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                output = True,
                frames_per_buffer = chunk)

# read data
while True:    
    data = stream.read(chunk)
    #Return the maximum of the absolute value of all samples in a fragment.
    a=audioop.max(data, 2)
    #Return the maximum peak-peak value in the sound fragment.
    b=audioop.maxpp(data, 2)
    #if a>5000:
    #    print 'a=',a
    if b>5000:
        print 'Sound Detected'
    time.sleep(0.01)

stream.close()
p.terminate()
