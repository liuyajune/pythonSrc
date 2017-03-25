#!usr/bin/env python
#-*-  coding: utf-8 -*-

import os

def countWord(fileName=None):
    lines =  0
    try:
        if fileName==None:
            raise("error open file")
        else:
            with open(fileName ,'r') as f:
                for i  in  f.readline():
                    lines += 1
    except  ZeroDivisionError as e:
        print(e)
    finally:
        #print('finally')
    return  lines

print(countWord('test.txt'))