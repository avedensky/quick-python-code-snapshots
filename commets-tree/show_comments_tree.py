#!/usr/bin/env python
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
    {'id':1, 'parrent_id':0, 'path':'', 'level':0, 'message':'What is mean : green'}, 
    {'id':2, 'parrent_id':0, 'path':'', 'level':0, 'message':'Vasya here is'},
    {'id':3, 'parrent_id':0, 'path':'', 'level':0, 'message':'I am Third'},
    {'id':4, 'parrent_id':1, 'path':'', 'level':0, 'message':'Green is color'},
    {'id':5, 'parrent_id':1, 'path':'', 'level':0, 'message':'Green is color of apple'},
    {'id':6, 'parrent_id':4, 'path':'', 'level':0, 'message':'I don\'t think' },
    {'id':7, 'parrent_id':6, 'path':'', 'level':0, 'message':'Ist true'},
    {'id':8, 'parrent_id':2, 'path':'', 'level':0, 'message':'Vasya to kick'},
    {'id':9, 'parrent_id':8, 'path':'', 'level':0, 'message':'Ura!'},
    {'id':10, 'parrent_id':9, 'path':'', 'level':0, 'message':'Aha!'},
]

def show(lst):
    ''' Show to display '''
    for i in lst:              
        print(' '*(i['level']*5)+i['message'])
        

def get_parrent_id(lst, id):    
    for i in lst:
        if i['id'] == id:
            return i['parrent_id']

def main():
    for i in mlst:        
        if i['parrent_id'] == 0:
            i['path'] = str (i['id'])
            continue

        t_id = i['parrent_id']
        s = ''
        level = 0
        while t_id!=0:
            s += '.'+str(t_id)
            level +=1
            t_id = get_parrent_id(mlst, t_id)            

        i['level'] = level
        i['path'] = s[::-1]

    mlst.sort(key=itemgetter('path'))
    show(mlst)

if __name__=='__main__':    
    main()