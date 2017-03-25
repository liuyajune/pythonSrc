#!usr/bin/env python
#-*-  coding: utf-8 -*-

import os

def countWord(fileName=None):
    words =  0
    list1 = []
    try:
        if fileName==None:
            raise("error open file")
        else:
            with open(fileName ,'r') as f:
                for line  in  f.readlines():
                    words  += len(line.strip('\n').split(' '))
                    list1.append(line.split(' '))
                print(list1)
    except  ZeroDivisionError as e:
        print(e)
    finally:
        print('finally')
    return  words

print(countWord('test.txt'))