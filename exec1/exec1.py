'''
第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）？
'''
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