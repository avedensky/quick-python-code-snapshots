#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlwt

"""
How work with Excel sheets from python.
Attention: This code depend from xlwt python library
"""


def xlsCreate (filename, lst):
    '''format raw data, lst has pair :code and description, this is you data, insert to cells on the finish'''
    wb = xlwt.Workbook()
    ws0 = wb.add_sheet('0')

    borders_bold_left = xlwt.Borders()
    borders_bold_left.left   = 2
    borders_bold_left.right  = 1
    borders_bold_left.top    = 2
    borders_bold_left.bottom = 2

    borders_bold_right = xlwt.Borders()
    borders_bold_right.left   = 1
    borders_bold_right.right  = 2
    borders_bold_right.top    = 2
    borders_bold_right.bottom = 2

    borders_normal = xlwt.Borders()
    borders_normal.left   = 1
    borders_normal.right  = 1
    borders_normal.top    = 1
    borders_normal.bottom = 1

    font_normal = xlwt.Font()
    font_normal.name = 'Times New Roman'
    font_normal.bold = False

    font_bold = xlwt.Font()
    font_bold.name = 'Times New Roman'
    font_bold.bold = True

    #Title borders left bold
    style_left_border_title = xlwt.XFStyle()
    style_left_border_title.font = font_bold
    style_left_border_title.borders = borders_bold_left

    #Title borders right bold
    style_rihgt_border_title = xlwt.XFStyle()
    style_rihgt_border_title.font = font_bold
    style_rihgt_border_title.borders = borders_bold_right

    #for sapcode and description
    style_nt = xlwt.XFStyle()
    style_nt.font = font_normal
    style_nt.borders = borders_normal
    i=1
    for item in lst:
        ws0.write(i, 0,item[0], style_nt) #code
        ws0.write(i, 1,item[1], style_nt) #description
        i+=1

    ws0.write(0, 0,'Material code', style_left_border_title)
    ws0.write(0, 1,'Description', style_rihgt_border_title)
    ws0.col(0).width = 3000
    ws0.col(1).width = 10000

    wb.save(filename)


	#******************************************************************************
def main ():
    lst = [('12345','Black'),('12345','White')] #This is you data, insert to cells on the finish
    xlsCreate ('result.xls', lst)


if __name__ == '__main__':
    main()