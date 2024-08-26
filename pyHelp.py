# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 10:53:39 2024

@author: LuChen
"""

def calc_maxTable(table1):
    maximum=0
    product=1
    for k in table1:
        for l in range(len(k)-3):
            product = k[l]*k[l+1]*k[l+2]*k[l+3]
            #print(maximum)
            if product>maximum:
                maximum=product
    return maximum

def write_file (file, number, entry):
    open(str(file+str(number)+'.txt'), 'a').write(entry+'\n')
    open(str(file+str(number)+'.txt'), 'a').close()
def writers_notebook (number, entry):
    write_file('writers_notebook_list', number, entry)
def del_file(file):
    open(file, 'w')
    open(file, 'w').close()
def del_wn(number):
    del_file('writers_notebook_list'+str(number))