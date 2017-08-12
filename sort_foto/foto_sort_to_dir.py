#!/usr/bin/env python2
# -*- coding: utf-8 -*-

'''

Sorted foto file by camera model to directory


- Read exif information from foto file (pyexiv2) in current directory
- Make directory by exif 'camera model' 
- Copy and past foto file

Requirement:

pyexiv2
python 2.x

'''

import pyexiv2
import os
import shutil

supported_fromat = ['.JPG','.jpg','.png','.PNG','.tif','.TIF','.tiff','.TIFF']

workdir = os.getcwd()
for filename in os.listdir(workdir):
    name, ext = os.path.splitext(filename)
    if ext in supported_fromat:
        metadata = pyexiv2.ImageMetadata(filename)
        metadata.read()
        metadata.iptc_charset = 'utf-8'
        model = str(metadata['Exif.Image.Model']).split ('=')[1][1:-1]
        path_new = os.path.join (workdir,model)
        if not os.path.exists (path_new):
            os.mkdir (path_new)
        shutil.copy2(os.path.join (workdir,filename), os.path.join (path_new,filename))
        print filename+' to '+model
