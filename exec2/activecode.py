#!/usr/bin/env  python
#-*-  coding:utf-8 -*-
import random
def genCode(len=4):
    activeCode = []
    for i in range(len):
        activeCode += chr(random.randint(ord('a'),ord('z')))
    activeCode = "".join(activeCode)
    return activeCode

def genCodeList(length=5 ,number =200):
    for i in range(number):
        print(i , genCode(length), end="\n")


print(genCodeList(5,200))