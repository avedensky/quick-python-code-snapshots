#!/usr/bin/python3.3
# -*- coding: utf-8 -*-

import os
import os.path
import datetime

"""

Script remove files in the selected directory by last modification time

argument 1: workdir
argument 2: file exctension (format example:.txt or * for all
argument 3: time of life file

"""        


def removeTemporyFiles (work_dir, file_extension, file_time_life_sec):
    for file_name in os.listdir(work_dir):
        name, ext = os.path.splitext(filename)            
            if ext.lower() in file_extension or ext.find('*')>-1:
                dt_mod_file = datetime.datitime.fromtimestamp(os.path.getmtime (filename))
                dt_now      = datetime.datetime.now ()
                delta       = dt_now-dt_mod_file
                if  delta.seconds>=file_time_life_sec:
                    os.remove (filename)


def main ():
    if len(sys.argv)<3:
        print ("This program deletes files by extension in the workdir\n")
        print ("after time since the last modification of the file.\n")        
        print ("argument 1: workdir\n")
        print ("argument 2: file exctension (format example:.txt or * for all) \n")
        print ("argument 3: time of life file\n")
        
    wkdir     = sys.argv[1]
    file_ext  = sys.argv[2]
    time_life = sys.argv[3]
    
    removeTemporyFiles (wkdir, [file_ext], time_life)
    
    
    
if __name__ == '__main__':
    main ()
    

                
