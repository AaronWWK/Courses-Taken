# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 12:59:05 2016

@author: ericgrimson
"""

def f( x ):
    x = x + 1
    print('in f(x): x =', x)
    return x
x = 3
z = f( x )
print(z)
print(x)
#
# x = 12
# def g(x):
#       x = x + 1
#       def h(y):
#           return x + y
#       return h(6)
# print(g(x))
