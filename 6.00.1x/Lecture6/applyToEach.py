# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 19:24:14 2016

@author: ericgrimson
"""

def applyToEach(L, f):
    """assumes L is a list, f a function
       mutates L by replacing each element,
       e, of L by f(e)"""
    for i in range(len(L)):
        L[i] = f(L[i])


def applyFuns(L, x):
    for f in L:
         print(f(x))


def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
def abslist(a):
    return(abs(a))
def multilist(a):
    return(a**2)
testList = [1, -4, 8, -9]

applyToEach(testList,multilist)
print(testList)
