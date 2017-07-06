#-------------------------------------------------------------------------------
# Name:        voc_ini
# Purpose:     initovoc and back
#
# Author:      avedensky
#-------------------------------------------------------------------------------

"""

	The program save pair data from map to ini file

"""


import ConfigParser


def SaveVocToINI (filename, voc, section = ''):
    '''Dictionary iteration and save to config file (ini)'''
    try:
        ini = ConfigParser.ConfigParser()
        ini.read(filename)
        if not ini.has_section (section):
            ini.add_section(section)

        for key, value in voc.items():
            ini.set (section, key, value)

        with open(filename, 'wb') as f1:
            ini.write(f1)
    except:
        sys.stderr.write ('* SaveVocToINI Error!\n')
        sys.stderr.write ('* Err Info :'+ str(sys.exc_info () [0])+'\n')
        sys.stderr.write ('* Err Info :'+ str(sys.exc_info () [1])+'\n')
        return -1
    return 0


def LoadINItoVoc (filename, voc, section = ''):
    '''Load config file (ini) and store to dictionary'''
    try:
        ini = ConfigParser.ConfigParser()
        ini.read(filename)

        if not ini.has_section (section):
            return -1
        itemsInSection  = ini.items(section)

        for item in itemsInSection:
            voc[item[0]] = ini.set (section, item[0], item[1])
    except:
        sys.stderr.write ('* LoadINItoVoc Error!\n')
        sys.stderr.write ('* Err Info :'+ str(sys.exc_info () [0])+'\n')
        sys.stderr.write ('* Err Info :'+ str(sys.exc_info () [1])+'\n')
        return -1
    return 0


def test1 ():
    voc = {}
    voc['file_name']='test.jpg'
    voc['size']=1234
    voc['path']='c:\\'
    voc['crc']=8911198
    SaveVocToINI ('test.ini',voc,'Options')
    

def test2 ():
    LoadINItoVoc ('test.ini',voc,'Options')
    print voc
    
def main():
    test1 ()
    test2 ()

if __name__ == '__main__':
    main()
