#!/usr/bin/env python3
#coding: utf-8

"""
Comments cultivator 2
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
    {'id':1, 'parrent_id':0, 'message':'What is mean word - green'}, 
    {'id':2, 'parrent_id':0, 'message':'Vasya is here.'},
    {'id':3, 'parrent_id':0, 'message':'I am Third'},
    {'id':4, 'parrent_id':1, 'message':'Green is color'},
    {'id':5, 'parrent_id':1, 'message':'Green is color of apple'},
    {'id':6, 'parrent_id':4, 'message':'I don\'t think' },
    {'id':7, 'parrent_id':6, 'message':'Ist true'},
    {'id':8, 'parrent_id':2, 'message':'Vasya to kick by admin'},
    {'id':9, 'parrent_id':8, 'message':'Ura!'},
    {'id':10, 'parrent_id':9, 'message':'Aha!'},
]


mlst2 = [ #Table 'comments' in Data Base
    {'id':1, 'parrent_id':None, 'message':'What is mean word - green'}, 
    {'id':2, 'parrent_id':None, 'message':'Vasya is here.'},
    {'id':3, 'parrent_id':None, 'message':'I am Third'},
    {'id':4, 'parrent_id':1, 'message':'Green is color'},
    {'id':5, 'parrent_id':1, 'message':'Green is color of apple'},
    {'id':6, 'parrent_id':4, 'message':'I don\'t think' },
    {'id':7, 'parrent_id':6, 'message':'Ist true'},
    {'id':8, 'parrent_id':2, 'message':'Vasya to kick by admin'},
    {'id':9, 'parrent_id':8, 'message':'Ura!'},
    {'id':10, 'parrent_id':9, 'message':'Aha!'},
]

#--------------------------------------------------------
def get_lst_id(id):
    res = []
    for i in mlst:
        if i['parrent_id'] == id:
            res.append(i['id'])            
            next_lst =  get_lst_id (i['id'])            
            if next_lst:
                res.append(next_lst)
    return res

def get_lst_id2(id, lst):
    res = []
    for i in range(0, len(mlst)):
        if 

        if lst[i]['parrent_id'] == id:
            res.append(lst[i]['id'])            
            next_lst =  get_lst_id (lst[i]['id'])            
            if next_lst:
                res.append(next_lst)
    return res



def show_id (lst, m):
    for i in lst:
        if type(i) == list:
            show_id (i, m+5)
        else:
            print(' '*m, i)

#--------------------------------------------------------
def get_lst_all(id):
    res = []
    for i in mlst:
        if i['parrent_id'] == id:
            res.append(i)            
            next_lst =  get_lst_all (i['id'])            
            if next_lst:
                res.append(next_lst)
    return res


def show_message (lst, m):
    for i in lst:
        if type(i) == list:
            show_message (i, m+5)
        else:
            print(' '*m, i['message'])    

#------------------------------------------
def show_html (lst):
    print(r'<ul>')    
    for i in lst:
        if type(i) == list:            
            show_html (i)            
        else:
            print(r'<li>')                   
            print(i)
            print(r'</li>')
    print(r'</ul>') 

#-------------------------------------------------------
def get_lst_message(id):
    res = []
    for i in mlst:
        if i['parrent_id'] == id:
            res.append(i['message'])            
            next_lst =  get_lst_message (i['id'])            
            if next_lst:
                res.append(next_lst)
    return res


def main():
    #Test 1
    print('-------- Show only ID ----------')
    lst = get_lst_id(0) 
    print(lst) 
    print()
    lst = get_lst_id2(0, mlst2) 
    print(lst) 
    print()
    print('-------- Show only ID with indent ----------')
    show_id(lst, 0) #recursive
    print()

    # #Test 2
    # print('-------- Show messages ----------')
    # lst = get_lst_all(0)    
    # show_message(lst, 0) #recursive
    # print()

    # #Test 3
    # print("-------- Prepare to Django for 'unordered_list' ----------")    
    # lst = get_lst_message(0)
    # print(lst) #start prepare to unordered_list in django !!!
    # print()

    # #Test 4    
    # print("-------- HTML ul li block ----------") 
    # show_html(lst)


if __name__=='__main__':
    main()
