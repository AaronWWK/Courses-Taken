#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 13:53:45 2017

@author: Weikang_Wan
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    
    return  base*recurPower(base,exp-1)
 
        
    
print(recurPower(54,5))

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    else:
        base = base*recurPower(base,exp-1)
        exp -=1
       
        return base