#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 15:20:52 2017

@author: Weikang_Wan
"""


##MY own code
a=1
def cllatz(n):
    global a
    if n == 1:
        return a
    elif n%2 != 0:
        n = 3*n + 1
        a +=1
        print(int(n))

        cllatz(n)
    else:
        n = n/2
        a += 1
        print(int(n))

        cllatz(n)
    return(a)

print(cllatz)


### A more nice and simple version of the code
def cllatz2(n):

    if n == 1:
        return 1
    elif n%2 != 0:
        return 1 + cllatz2(3*n+1)
    else:
        return 1 + cllatz2(n/2)


print('a =',cllatz(3))
print(cllatz2(3))
