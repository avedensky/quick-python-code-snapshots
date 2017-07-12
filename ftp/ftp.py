#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import ftplib

"""
   
Script check selected files by mask in directory and if files exists send file to FTP server

"""

def check_and_send(pth, ip_address, username, passw, supported_fromat):
    '''Check files in dir and send to ftp'''
    isConnected = False;
    
    for filename in os.listdir(pth): 
        name, ext = os.path.splitext(filename)
        if ext in supported_fromat:            
            full_filename = os.path.join (pth,'',filename)            
            try:
                if isConnected == False :
                    ftp = ftplib.FTP(ip_address, username, passw,'', 3)                

                isConnected = True    
                ftp.storbinary("STOR " + filename, open(full_filename, "rb"), 1024)                
            except :
                sys.stderr.write ('* FTP Error!\n')
                sys.stderr.write ('* Err Info :'+ str(sys.exc_info () [0])+'\n')
                sys.stderr.write ('* Err Info :'+ str(sys.exc_info () [1])+'\n')
                break
    if isConnected == True :
        ftp.quit()
                
if __name__ == "__main__":
    supported_fromat = [".txt"]    # Mask of files
    path             = "C://tmp//" # Path of files
    ftp_ip_address   = ""          # URL or IP of FTP server
    ftp_username     = ""          # User login
    ftp_passw        = ""          # User password

    check_and_send(path, ftp_ip_address, ftp_username, ftp_passw, supported_fromat)
