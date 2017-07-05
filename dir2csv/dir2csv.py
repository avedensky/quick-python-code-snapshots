#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os.path
import os
import sys
import hashlib
import csv
import time

file_lst = []

"""

  The program recurse scan directory and write info about every file (size, datatime, md5) to csv file 
  
  The program expect two arguments in comand line
  The first argument:  path to dir
  The second argument: file name in csv format

"""


def md5sum(filename):
    """calculate hash by algoritm md5"""
    md5 = hashlib.md5()
    with open(filename,'rb') as f:
        for chunk in iter(lambda: f.read(128*md5.block_size), b''):
             md5.update(chunk)
    return md5.hexdigest()
	
	
def fileSortToDir (workdir, file_csv):    
    """ write file info to csv file, recursive walk dirs"""
    for root, dirs, files in os.walk(workdir):
        for filename in files:
            pth    = os.path.join (root,"",filename)
            if os.path.isfile (pth):
                try:
                    name, ext_ul = os.path.splitext(filename)            
                    dir_n  = os.path.dirname (pth)
                    ext    = ext_ul.lower()
                    sz     = os.path.getsize(pth) # узнать размер
                    cdt    = time.strftime ("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getctime(pth))) # время создания файла
                    mdt    = time.strftime ("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getmtime(pth))) # время изменения
                    md5    = md5sum (pth)
                    file_lst.append (["you_command",pth,dir_n,name,ext,str(sz),cdt,mdt,md5])
                except:
                    print ("Unexpected error:", sys.exc_info ()[0])
                 
	
    with open(file_csv, 'w', newline='') as csvfile:
        file_csv = csv.writer(csvfile, delimiter=',')
        for item in file_lst:
            file_csv.writerow(item)
		
		
def main():
#   workdir = "/home/"
#   filename_csv = "/home/dir.csv"
    workdir = None
    movedir = None    
    workdir      = sys.argv[1]
    filename_csv = sys.argv[2]    
    if workdir == None:
        return        
    if filename_csv == None:
        return
		
    fileSortToDir (workdir, filename_csv)
	
if __name__ == '__main__':
    main ()
