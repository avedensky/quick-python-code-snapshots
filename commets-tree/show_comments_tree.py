#!/usr/bin/env python3
#coding: utf-8

"""
Comments cultivator
-------------------

Read table comments from DB (here - from list), build path, sort and show:

What is mean : green
     Green is color
     Green is color of apple
          I don't think
               Ist true
Vasya here is
     Vasya to kick
          Ura!
               Aha!
I am Third
"""

from operator import itemgetter

mlst = [ #Table 'comments' in Data Base
    {'id':1, 'parrent_id':0, 'path':'', 'level':0, 'message':'What is mean word - green'}, 
    {'id':2, 'parrent_id':0, 'path':'', 'level':0, 'message':'Vasya is here.'},
    {'id':3, 'parrent_id':0, 'path':'', 'level':0, 'message':'I am Third'},
    {'id':4, 'parrent_id':1, 'path':'', 'level':0, 'message':'Green is color'},
    {'id':5, 'parrent_id':1, 'path':'', 'level':0, 'message':'Green is color of apple'},
    {'id':6, 'parrent_id':4, 'path':'', 'level':0, 'message':'I don\'t think' },
    {'id':7, 'parrent_id':6, 'path':'', 'level':0, 'message':'Ist true'},
    {'id':8, 'parrent_id':2, 'path':'', 'level':0, 'message':'Vasya to kick by admin'},
    {'id':9, 'parrent_id':8, 'path':'', 'level':0, 'message':'Ura!'},
    {'id':10, 'parrent_id':9, 'path':'', 'level':0, 'message':'Aha!'},
]

def show(lst):
    ''' Show to display '''
    for i in lst:              
        print(' ' * (i['level'] * 5) + i['message'])
        

def get_parrent_id(lst, id):    
    for i in lst:
        if i['id'] == id:
            return i['parrent_id']


def build_paths(lst):
    ''' 
    For every comment, calculate path to first of discuss comment
    path is a string type and format as: <id>.<id>.<id> ...
    3.12.  or 1.10.5. or 5.13.99.11.33. ...
    For easy sorting after
    '''
    for i in lst:        
        if i['parrent_id'] == 0: # 0 is a root comment
            i['path'] = str (i['id'])
            continue

        tmp_id = i['parrent_id']
        tmp_path = ''
        tmp_level = 0
        while tmp_id != 0:
            tmp_path += '.' + str(tmp_id)
            tmp_level += 1
            tmp_id = get_parrent_id(lst, tmp_id)            

        i['level'] = tmp_level
        i['path'] = tmp_path[::-1] #reverse string: .5.4.1 to 1.4.5.



def main():
    build_paths(mlst)
    mlst.sort(key=itemgetter('path'))
    show(mlst)

if __name__=='__main__':    
    main()