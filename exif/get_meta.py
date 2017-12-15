#!/usr/bin/env python3
#coding: utf-8
"""
Return Meta (IPTC, EXIF, XMP) info from graphical file format as dictionary

depends from exiftool utility
https://www.sno.phy.queensu.ca/~phil/exiftool/
"""
import subprocess
import json

def get_meta(filename):
    """Функция принимает имя файла и возвращает мета информацию
    """
    cmd = ["exiftool","-G", "-j", "-charset", "IPTC=cp1251", filename]
    p = subprocess.Popen(cmd,stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    return json.loads(p.stdout.read().decode('utf-8', 'ignore'))[0];

def test():
    #filename = './FotoForTest/IMG_7760.jpg'
    #filename = './FotoForTest/IMG_0613.jpg' # - coding cp1251
    #filename = './FotoForTest/IMG_0918.jpg'
    voc = getMeta(filename)
    for k, v in voc.items():
        print('{} = {}'.format(k, v))

if __name__ == '__main__':
    test()
